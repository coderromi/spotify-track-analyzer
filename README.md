
# Spotify Track Analyzer

## Overview
A Python-based data analysis project that explores Spotify tracks using data cleaning, exploratory data analysis (EDA), and visualization.

## Dataset
- Original records: 114,000
- Cleaned records: 113,549
- Features after cleaning: 20

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure
- data/raw: Original dataset
- data/processed: Cleaned dataset
- src: Python source code
- outputs/plots: Generated visualizations
- logs: Project logs

## Data Cleaning
- Removed unnecessary index column.
- Removed records with missing essential values.
- Removed duplicate track and genre combinations.

## Analysis
- Track popularity distribution
- Average popularity by genre
- Audio feature analysis
- Danceability vs energy relationship
- Top energetic tracks

## Visualizations
Three visualizations are saved in outputs/plots.

## How to Run
1. Activate the virtual environment.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run `python src/eda.py`.
4. Run `python src/visualize.py`.

## Outcome
The project demonstrates practical data loading, cleaning, analysis, and visualization using Python.
