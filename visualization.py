import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv("custom_books_dataset.csv")
    print("Dataset successfully loaded for Visualization!\n")
except FileNotFoundError:
    print("Error: 'custom_books_dataset.csv' file-ah kandupudika mudiyala.\n")
    exit()

df['Price_Cleaned'] = df['Price'].str.replace('£', '').str.replace('Â', '').astype(float)

plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

top_expensive = df.nlargest(10, 'Price_Cleaned')

plt.subplot(1, 2, 1) # Left side chart
sns.barplot(x='Price_Cleaned', y='Book Title', data=top_expensive, palette='flare')
plt.title('Top 10 Most Expensive Books (£)', fontsize=14, fontweight='bold')
plt.xlabel('Price (£)', fontsize=12)
plt.ylabel('Book Title', fontsize=12)

plt.subplot(1, 2, 2) # Right side chart
sns.histplot(df['Price_Cleaned'], kde=True, color='teal', bins=8)
plt.title('Book Price Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Price (£)', fontsize=12)
plt.ylabel('Frequency (Count)', fontsize=12)

plt.tight_layout()

plt.savefig('books_data_visualization.png', dpi=300)
print("Task 3 Done! Charts have been successfully generated and saved as 'books_data_visualization.png'.")

plt.show()