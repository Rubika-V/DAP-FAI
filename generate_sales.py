import pandas as pd
import random

# Fixed seed for reproducibility
random.seed(113025148082)

total_records = 5_000_000
chunk_size = 100_000

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

print("Generating 5 million sales records...")

first_chunk = True

for start in range(0, total_records, chunk_size):

    size = min(chunk_size, total_records - start)

    data = {
        "sale_id": [f"S{start + i + 1:07d}" for i in range(size)],
        "employee_id": [
            random.choice(["E101", "E102", "E103", "E104"])
            for _ in range(size)
        ],
        "date": [
            random.choice([
                "2026-09-15",
                "2026-09-16",
                "2026-09-17"
            ])
            for _ in range(size)
        ],
        "product": [
            random.choice(products)
            for _ in range(size)
        ],
        "quantity": [
            random.randint(1, 5)
            for _ in range(size)
        ],
        "sales_amount": [
            random.randint(1000, 120000)
            for _ in range(size)
        ]
    }

    df = pd.DataFrame(data)

    df.to_csv(
        "data/large_sales.csv",
        mode="w" if first_chunk else "a",
        header=first_chunk,
        index=False
    )

    first_chunk = False

    print(f"{start + size:,} records generated")

print("\n✅ 5 million sales records generated!")
print("File: data/large_sales.csv")