import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("ramen-ratings.csv")

print("Rows, Columns:", df.shape)
print("\nColumns:", list(df.columns))
print("\nMissing values per column:\n", df.isna().sum())

print("\nBasic stats (numeric):\n", df.select_dtypes(include="number").describe())


# Top Brands
if 'Brand' in df.columns:
    print("\nTop 10 brands by count:")
    print(df['Brand'].value_counts().head(10))
# Style Distribution
if 'Style' in df.columns:
    print("\nStyle counts:")
    print(df['Style'].value_counts())
# Country Distribution (top 10)
if 'Country' in df.columns:
    print("\nTop countries:")
    print(df['Country'].value_counts().head(10))
# Stars Distribution
if 'Stars' in df.columns:
    d2 = df.copy()
    d2['Stars'] = pd.to_numeric(d2['Stars'], errors='coerce')
    ax = d2['Stars'].dropna().plot(kind='hist', bins=20, edgecolor='black', title='Stars Distribution')
    ax.set_xlabel('Stars')
    plt.tight_layout()
    plt.show()
