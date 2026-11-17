import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)


def clean_spotify_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean Spotify track data."""

    df = df.copy()

    # Remove unnecessary index column
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")

    # Remove records missing essential information
    df = df.dropna(
        subset=["track_id", "track_name", "artists"]
    )

    # Remove duplicate track/genre combinations
    df = df.drop_duplicates(
        subset=["track_id", "track_genre"]
    )

    logging.info("Cleaning completed: %d tracks", len(df))

    return df


if __name__ == "__main__":
    from data_loader import load_spotify_data
    from pathlib import Path

    raw_df = load_spotify_data()
    cleaned_df = clean_spotify_data(raw_df)

    output_path = Path(__file__).resolve().parent.parent / "data" / "processed" / "spotify_tracks_cleaned.csv"

    cleaned_df.to_csv(output_path, index=False)

    print("Cleaned dataset saved successfully!")
    print("Final shape:", cleaned_df.shape)