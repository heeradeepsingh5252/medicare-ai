
import pandas as pd

# Load the dataset
df = pd.read_csv("Cleaned_Dataset.csv")

print("Dataset shape:", df.shape)

# Remove exact duplicate rows for this initial baseline
df = df.drop_duplicates().copy()

print("Shape after removing exact duplicates:", df.shape)

# Check the target
target = "outcome_variable"

print("\nTarget distribution:")
print(df[target].value_counts())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Save a cleaned copy for inspection
df.to_csv("data/cleaned_training_data.csv", index=False)

print("\nCleaned dataset saved to data/cleaned_training_data.csv")


print("\nDataset columns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head().to_string())

print("\nTarget distribution:")
print(df["outcome_variable"].value_counts())
