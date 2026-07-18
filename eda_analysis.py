import pandas as pd

try:
    df = pd.read_csv("custom_books_dataset.csv")
    print("Dataset successfully loaded for EDA!\n")
except FileNotFoundError:
    print("Error: 'custom_books_dataset.csv' file-ah kandupudika mudiyala. Task 1 folder-la check pannunga.\n")
    exit()

print("--- 1. DATA STRUCTURE & INFO ---")
print(f"Dataset Shape (Rows, Columns): {df.shape}")
print("\nColumns and Data Types:")
print(df.dtypes)
print("\nDataset Preview (First 5 Rows):")
print(df.head())
print("-" * 40 + "\n")

print("--- 2. MISSING VALUES CHECK ---")
missing_data = df.isnull().sum()
print("Missing values count per column:")
print(missing_data)
print("-" * 40 + "\n")

print("--- 3. DATA CLEANING & STATISTICAL ANALYSIS ---")
df['Price_Cleaned'] = df['Price'].str.replace('£', '').str.replace('Â', '').astype(float)

print("Price Column Statistical Summary:")
print(df['Price_Cleaned'].describe())
print("-" * 40 + "\n")

print("--- 4. PATTERNS & ANOMALIES ---")

print("Stock Availability Pattern:")
print(df['Availability'].value_counts())
print("-" * 40 + "\n")

print("Task 2: EDA Phase Complete! Dataset structures analyzed successfully.")