import pandas as pd

# 1. Dataset loading
try:
    df = pd.read_csv("custom_books_dataset.csv")
    print("Dataset successfully loaded for Sentiment Analysis!\n")
except FileNotFoundError:
    print("Error: 'custom_books_dataset.csv' file missing.\n")
    exit()

# 2. Price Cleaning
df['Price_Cleaned'] = df['Price'].str.replace('£', '').str.replace('Â', '').astype(float)

# 3. Sentiment Logic
def analyze_sentiment(row):
    title = str(row['Book Title']).lower()
    price = row['Price_Cleaned']
    
    positive_words = ['light', 'history', 'bright', 'love', 'science', 'art', 'life']
    negative_words = ['dirty', 'dark', 'secret', 'alone', 'lost', 'scary']
    
    if any(word in title for word in positive_words):
        return 'Positive'
    elif any(word in title for word in negative_words):
        return 'Negative'
    elif price < 30.0:
        return 'Positive'
    else:
        return 'Neutral'

df['Sentiment'] = df.apply(analyze_sentiment, axis=1)

# 4. Results Display
print("--- TASK 4: SENTIMENT ANALYSIS RESULTS ---")
print(df[['Book Title', 'Price', 'Sentiment']].head(10))
print("-" * 50)

print("\nSentiment Distribution Summary:")
print(df['Sentiment'].value_counts())
print("-" * 50)

df.to_csv("books_sentiment_analysis_results.csv", index=False)
print("\nTask 4 Done! Saved as 'books_sentiment_analysis_results.csv'.")