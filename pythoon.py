import pandas as pd

df = pd.read_csv("netflix_titles.csv")
print(df.head())
print(df.info())

# Remove duplicates
df.drop_duplicates(inplace=True)
#inplace=True means the changes are applied directly to df

# Missing values
df.fillna("Unknown", inplace=True)

# Date conversion
df['date_added'] = pd.to_datetime(
    df['date_added'],
    errors='coerce'
)

# Extract Year
df['year_added'] = df['date_added'].dt.year

# Movies vs TV Shows
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=df, x='type')
plt.title("Movies vs TV Shows")
plt.show()

# Content Added by Year
yearly = df['year_added'].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(yearly.index, yearly.values)
plt.title("Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

#Top 10 Countries

top_country = (
    df['country']
    .str.split(',')
    .explode()
    .value_counts()
    .head(10)
)

top_country.plot(
    kind='bar',
    figsize=(10,5)
)
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

# Rating Distribution
plt.figure(figsize=(12,6))

sns.countplot(
    y='rating',
    data=df,
    order=df['rating']
    .value_counts()
    .index
)

plt.title("Ratings Distribution")
plt.show()

# Top Genres
genres = (
    df['listed_in']
    .str.split(',')
    .explode()
)

top_genres = genres.value_counts().head(15)

top_genres.plot(
    kind='barh',
    figsize=(10,6)
)

plt.title("Top Genres")
plt.show()

# Release Year Analysis
release = (
    df['release_year']
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(12,5))

plt.plot(
    release.index,
    release.values
)

plt.title("Content Release Trend")
plt.show()

# Top Directors
directors = (
    df['director']
    .value_counts()
    .head(10)
)

directors.plot(kind='bar')
plt.title("Top Directors")
plt.xlabel("Director")
plt.ylabel("Count")
plt.show()

# Top Actors
actors = (
    df['cast']
    .str.split(',')
    .explode()
    .value_counts()
    .head(15)
)

actors.plot(kind='barh')
plt.title("Top Actors")
plt.xlabel("Count")
plt.show()