import pandas as pd
from dataLoad import file_path
# Load the dataset
df = pd.read_csv(file_path)

# Display initial dataset info
print("Initial Dataset Info:")
print(df.info())

# Step 1: Remove rows with null values
df = df.dropna()
print("\nNull values removed. Current dataset shape:", df.shape)

# Step 2: Remove duplicate rows
df = df.drop_duplicates()
print("\nDuplicates removed. Current dataset shape:", df.shape)

# Step 3: Format data types
# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

# Convert amount to a numeric type
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# Check for any remaining nulls after conversion
df = df.dropna()  # Drop rows with nulls caused by invalid conversions
print("\nDataset after type formatting and cleanup:")
print(df.info())

# Step 4: Handle inconsistencies (example for category and status)
df['category'] = df['category'].str.strip().str.lower()
df['status'] = df['status'].str.strip().str.lower()

# Display cleaned data sample
print("\nCleaned Data Sample:")
reduced_file_path = "cleaned_reduce_data.csv"
df.to_csv(reduced_file_path, index=False)
print(df.head())
