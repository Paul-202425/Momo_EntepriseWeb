#!/usr/bin/env python3
import argparse, json, os, random, time

def linear_find(transactions, target_id):
    for t in transactions:
        if str(t.get("id")) == str(target_id):
            return t
    return None

def dict_build(transactions):
    return {str(t["id"]): t for t in transactions}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="./data.json")
    ap.add_argument("--trials", type=int, default=10000)
    args = ap.parse_args()

    if not os.path.exists(args.data):
        print("Data file not found. Please run your XML parser first to generate data.json.")
        return

    with open(args.data, "r", encoding="utf-8") as f:
        txs = json.load(f)

    ids = [t["id"] for t in txs]
    if not ids:
        print("No transactions found in data.json")
        return

    lookups = [random.choice(ids) for _ in range(args.trials)]

    # Linear search benchmark
    t0 = time.perf_counter()
    for lid in lookups:
        _ = linear_find(txs, lid)
    t1 = time.perf_counter()

    # Dict lookup benchmark
    index = dict_build(txs)
    t2 = time.perf_counter()
    for lid in lookups:
        _ = index.get(str(lid))
    t3 = time.perf_counter()

    print(f"Linear search: {t1 - t0:.6f} s for {args.trials} lookups")
    print(f"Dict lookup:   {t3 - t2:.6f} s for {args.trials} lookups")
    if (t1 - t0) > 0:
        print(f"Speedup (linear/dict): {(t1 - t0)/(t3 - t2 + 1e-9):.2f}×")

if __name__ == "__main__":
    main()
