import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "http://books.toscrape.com/"

headers = {"User-Agent": "Mozilla/5.0"}  
response = requests.get(URL, headers=headers)

if response.status_code == 200:
    print("Website connect aiyidichi!")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    scraped_data = []
    
    books = soup.find_all('article', class_='product_pod')
    
    for book in books:
        title = book.h3.a['title']
        
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        
        scraped_data.append({
            "Book Title": title,
            "Price": price,
            "Availability": availability
        })
        
    df = pd.DataFrame(scraped_data)
    
    df.to_csv("custom_books_dataset.csv", index=False, encoding="utf-8-sig")
    print("Task 1 Done! Data saved as 'custom_books_dataset.csv'")
    
    print(df.head())

else:
    print(f"Error! Connection status: {response.status_code}")