import json, os, timeit, random

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data.json")

def load_data():
    # Handle UTF-8 BOM from PowerShell Set-Content
    with open(DATA_PATH, "r", encoding="utf-8-sig") as f:
        return json.load(f)

def linear_find(transactions, target_id):
    for t in transactions:
        if t.get("id") == target_id:
            return t
    return None

def dict_index(transactions):
    # Build id -> transaction map once
    return { int(t["id"]): t for t in transactions }

def main():
    print("Loading data...")
    data = load_data()
    print(f"Loaded {len(data)} records.")

    if len(data) < 20:
        print("Need ≥20 records in data.json for the benchmark.")
        return

    # Pick 20 random IDs to query repeatedly
    ids = [int(t["id"]) for t in data]
    keys = random.sample(ids, min(20, len(ids)))

    # Warm-up single examples
    example_id = keys[0]
    print("\nExample lookups:")
    print("  Linear:", linear_find(data, example_id))

    index = dict_index(data)
    print("  Dict  :", index.get(example_id))

    # Benchmark: run each batch of 20 lookups 1000 times
    linear_time = timeit.timeit(lambda: [linear_find(data, k) for k in keys], number=1000)
    dict_time   = timeit.timeit(lambda: [index.get(k) for k in keys],       number=1000)

    print("\nResults")
    print(f"  Records: {len(data)}")
    print(f"  Linear search total time (1000x over {len(keys)} keys): {linear_time:.6f}s")
    print(f"  Dict lookup total time   (1000x over {len(keys)} keys): {dict_time:.6f}s")
    if dict_time > 0:
        print(f"  Approx speedup (linear/dict): {linear_time/dict_time:.2f}x")

    print("\nWhy dict is faster?")
    print("- Linear search scans each element O(n).")
    print("- Dict uses a hash table; average O(1) lookup.")

if __name__ == "__main__":
    main()
