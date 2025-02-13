import pandas as pd

# Load the dataset
file_path = "reduced_dataset.csv" 
df = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Info:")
print(df.info())

print("\nSample Data:")
print(df.head())

print("\nDescriptive Statistics:")
print(df.describe(include='all'))
