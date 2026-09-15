import pandas as pd
import time

file_path = "data/large_sales.csv"
chunk_size = 100_000

total_records = 0
total_sales = 0
start_time = time.time()

print("Processing 5 million records in chunks...\n")

for chunk_number, chunk in enumerate(
    pd.read_csv(file_path, chunksize=chunk_size),
    start=1
):
    # Clean the chunk
    chunk = chunk.drop_duplicates()
    chunk = chunk.dropna()

    # Calculate sales for this chunk
    total_records += len(chunk)
    total_sales += chunk["sales_amount"].sum()

    print(
        f"Chunk {chunk_number} processed | "
        f"Records: {len(chunk):,}"
    )

end_time = time.time()

print("\n🎉 LARGE DATA PROCESSING COMPLETED!")
print(f"Total records processed: {total_records:,}")
print(f"Total sales amount: {total_sales:,}")
print(f"Chunk size used: {chunk_size:,}")
print(f"Processing time: {end_time - start_time:.2f} seconds")