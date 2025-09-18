# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the Dataset
df = pd.read_csv("books_scraped_data.csv", encoding="latin1")

# Clean the Price column
df['Price'] = df['Price'].str.replace(r'[^\d\.]', '', regex=True).astype(float)

# View the first few rows
print("Preview of dataset:")
display(df.head())

# Summary statistics
print("Summary statistics:")
display(df.describe())

# Rating Distribution - Bar Plot
plt.figure(figsize=(6, 4))
sns.countplot(x='Rating', data=df, order=df['Rating'].value_counts().index, palette='Pastel2')
plt.title('Distribution of Book Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Books')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Price Distribution - Histogram
plt.figure(figsize=(6, 4))
sns.histplot(df['Price'], bins=15, kde=True, color='skyblue')
plt.title('Price Distribution of Books')
plt.xlabel('Price (£)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Boxplot - Price by Rating
plt.figure(figsize=(6, 4))
sns.boxplot(x='Rating', y='Price', data=df, palette='Set3')
plt.title('Price Variation Across Ratings')
plt.xlabel('Rating')
plt.ylabel('Price (£)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 🔝 Top 10 Most Expensive Books - Bar Plot
top_10 = df.sort_values(by='Price', ascending=False).head(10)

plt.figure(figsize=(8, 5))
sns.barplot(x='Price', y='Title', data=top_10, palette='Spectral')
plt.title('Top 10 Most Expensive Books')
plt.xlabel('Price (£)')
plt.ylabel('Book Title')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Word Cloud of Book Titles
text = " ".join(title for title in df['Title'])

wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='tab10').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Book Titles")
plt.show()
