import logging

from data_loader import load_spotify_data

logging.basicConfig(level=logging.INFO)

df = load_spotify_data()

# 1. Dataset dimensions
print("\nDataset shape:")
print(df.shape)

# 2. Column names and data types
print("\nDataset information:")
df.info()

# 3. Missing values
print("\nMissing values:")
print(df.isnull().sum())

# 4. Duplicate records
print("\nDuplicate rows:")
print(df.duplicated().sum())

# 5. Statistical summary
print("\nStatistical summary:")
print(df.describe())

print("\n--- CLEANING VALIDATION ---")

missing_rows = df[["track_id", "track_name", "artists"]].isnull().any(axis=1).sum()

duplicate_pairs = df.duplicated(
    subset=["track_id", "track_genre"]
).sum()

print("Rows with missing essential values:", missing_rows)
print("Duplicate track-genre pairs:", duplicate_pairs)