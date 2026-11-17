import logging
import pandas as pd

from data_loader import load_spotify_data
from data_cleaner import clean_spotify_data

logging.basicConfig(level=logging.INFO)

df = load_spotify_data()
df = clean_spotify_data(df)

# 1. Most popular tracks
print("\nTOP 10 POPULAR TRACKS")
print(
    df.nlargest(10, "popularity")[
        ["track_name", "artists", "popularity"]
    ]
)

# 2. Average popularity by genre
print("\nTOP 10 GENRES BY POPULARITY")
genre_popularity = (
    df.groupby("track_genre")["popularity"]
    .mean()
    .sort_values(ascending=False)
)
print(genre_popularity.head(10))

# 3. Average audio features
print("\nAVERAGE AUDIO FEATURES")
print(
    df[["danceability", "energy", "valence", "acousticness", "tempo"]]
    .mean()
)

# 4. Most energetic tracks
print("\nTOP 10 ENERGETIC TRACKS")
print(
    df.nlargest(10, "energy")[
        ["track_name", "artists", "energy"]
    ]
)