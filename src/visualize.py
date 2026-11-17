import logging
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from data_loader import load_spotify_data
from data_cleaner import clean_spotify_data

logging.basicConfig(level=logging.INFO)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PLOT_DIR = PROJECT_ROOT / "outputs" / "plots"
PLOT_DIR.mkdir(parents=True, exist_ok=True)

df = clean_spotify_data(load_spotify_data())

sns.set_theme(style="whitegrid")

# 1. Popularity distribution
plt.figure(figsize=(10, 5))
sns.histplot(df["popularity"], bins=30, kde=True)
plt.title("Distribution of Spotify Track Popularity")
plt.xlabel("Popularity")
plt.ylabel("Number of Tracks")
plt.savefig(PLOT_DIR / "popularity_distribution.png")
plt.close()

# 2. Top 10 genres by average popularity
genre_popularity = (
    df.groupby("track_genre")["popularity"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
sns.barplot(x=genre_popularity.values, y=genre_popularity.index)
plt.title("Top 10 Genres by Average Popularity")
plt.xlabel("Average Popularity")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig(PLOT_DIR / "genre_popularity.png")
plt.close()

# 3. Relationship between danceability and energy
sample_df = df.sample(n=min(5000, len(df)), random_state=42)

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=sample_df,
    x="danceability",
    y="energy",
    alpha=0.4
)
plt.title("Danceability vs Energy")
plt.savefig(PLOT_DIR / "danceability_vs_energy.png")
plt.close()

logging.info("All visualisations saved successfully.")