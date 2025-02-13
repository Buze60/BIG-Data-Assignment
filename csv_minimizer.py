import pandas as pd

# Load the full dataset
file_path = "ecommerce1.csv"  # Replace with your actual file path
df = pd.read_csv(file_path)

# Reduce the dataset to 1 million rows by random sampling
reduced_df = df.sample(n=1_000_000, random_state=42)  

# Save the reduced dataset to a new file
reduced_file_path = "reduced_dataset.csv"
reduced_df.to_csv(reduced_file_path, index=False)

print(f"Reduced dataset saved to {reduced_file_path}, with {len(reduced_df)} rows.")
