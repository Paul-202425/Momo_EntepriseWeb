# dsa/parse_xml.py
import xml.etree.ElementTree as ET
import re, json, datetime, sys
from pathlib import Path

AMOUNT_RE = re.compile(r'([0-9]{1,3}(?:,[0-9]{3})*|[0-9]+)\s*RWF', re.IGNORECASE)
TXID_RE = re.compile(r'(?:TxId|Financial Transaction Id)[:\s]*([0-9]+)', re.IGNORECASE)
NEWBAL_RE = re.compile(r'(?:new balance|NEW BALANCE)\s*[:\s]*([0-9,]+)\s*RWF', re.IGNORECASE)
FEE_RE = re.compile(r'Fee was[:\s]*([0-9,]+)', re.IGNORECASE)
FROM_RE = re.compile(r'from\s+([A-Za-z .]+?)(?:\s*\(|\s+on|\s+at|\s+has|\.)', re.IGNORECASE)
TO_RE = re.compile(r'to\s+([A-Za-z0-9 \-]+?)(?:\s+\d+|\s*\(|\s+has|\s+at|\.|,)', re.IGNORECASE)
PHONE_PAREN_RE = re.compile(r'\((\+?\d{6,})\)')

def ms_to_iso(ms):
    try:
        return datetime.datetime.utcfromtimestamp(int(ms)/1000.0).isoformat() + "Z"
    except:
        return None

def extract_amount(s):
    m = AMOUNT_RE.search(s)
    return int(m.group(1).replace(',','')) if m else None

def extract_txid(s):
    m = TXID_RE.search(s)
    return m.group(1) if m else None

def extract_new_balance(s):
    m = NEWBAL_RE.search(s)
    if m:
        return int(m.group(1).replace(',',''))
    m2 = re.search(r'new balance[:\s]*([0-9,]+)', s, re.IGNORECASE)
    return int(m2.group(1).replace(',','')) if m2 else None

def extract_fee(s):
    m = FEE_RE.search(s)
    return int(m.group(1).replace(',','')) if m else None

def extract_sender(s):
    m = FROM_RE.search(s)
    if m:
        phone_m = PHONE_PAREN_RE.search(s)
        return m.group(1).strip(), (phone_m.group(1) if phone_m else None)
    phone_m = PHONE_PAREN_RE.search(s)
    return (None, phone_m.group(1) if phone_m else None)

def extract_receiver(s):
    m = TO_RE.search(s)
    if m:
        phone_m = PHONE_PAREN_RE.search(s)
        return m.group(1).strip(), (phone_m.group(1) if phone_m else None)
    return None, None

def parse_body(body):
    b = (body or "").strip()
    info = {}
    info['raw_body'] = b
    info['txid'] = extract_txid(b)
    info['amount'] = extract_amount(b)
    info['new_balance'] = extract_new_balance(b)
    info['fee'] = extract_fee(b)
    snd_name, snd_phone = extract_sender(b)
    rcv_name, rcv_phone = extract_receiver(b)
    info['sender_name'] = snd_name
    info['sender_phone'] = snd_phone
    info['receiver_name'] = rcv_name
    info['receiver_phone'] = rcv_phone
    if 'received' in b.lower() or re.search(r'\byou have received\b', b, re.I):
        info['action'] = 'received'
    elif 'your payment' in b.lower():
        info['action'] = 'payment'
    elif 'transferred to' in b.lower():
        info['action'] = 'transfer'
    elif 'deposit' in b.lower():
        info['action'] = 'deposit'
    else:
        info['action'] = 'unknown'
    tm = re.search(r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})', b)
    info['body_timestamp'] = tm.group(1) if tm else None
    return info

def parse_file(xml_path, out_json_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    parsed = []
    for i, node in enumerate(root.findall('sms')):
        rec = dict(node.attrib)
        if 'date' in rec:
            rec['date_iso'] = ms_to_iso(rec['date'])
        if 'date_sent' in rec:
            rec['date_sent_iso'] = ms_to_iso(rec['date_sent'])
        parsed_body = parse_body(rec.get('body',''))
        rec.update(parsed_body)
        rec['id'] = parsed_body.get('txid') or rec.get('date') or str(i+1)
        parsed.append(rec)
    Path(out_json_path).write_text(json.dumps(parsed, indent=2, ensure_ascii=False))
    print(f"Wrote {len(parsed)} records to {out_json_path}")

if __name__ == "__main__":
    xml_in = sys.argv[1] if len(sys.argv)>1 else 'dsa/modified_sms_v2.xml'
    out = sys.argv[2] if len(sys.argv)>2 else 'dsa/data.json'
    parse_file(xml_in, out)


