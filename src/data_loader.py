from pathlib import Path
import logging

import pandas as pd

logging.basicConfig(level=logging.INFO)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "spotify_tracks.csv"


def load_spotify_data(file_path: Path = DATA_PATH) -> pd.DataFrame:
    """Load Spotify track data from a CSV file."""

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    df = pd.read_csv(file_path)

    logging.info("Successfully loaded %d tracks", len(df))

    return df