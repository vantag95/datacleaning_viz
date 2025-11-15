Stock Market Data Cleaning & Visualization
This project demonstrates cleaning, aggregating, and visualizing stock market data using Python (pandas), Parquet files, and Streamlit. The dashboard helps users interactively analyze stock metrics for multiple tickers and sectors.

Table of Contents
Overview

Setup & Installation

Data Cleaning & Schema

Aggregations

Dashboard Usage

Screenshots

Project Structure

Overview
This assignment covers:

Cleaning raw financial CSV data

Normalizing schema (standardized columns, missing values, text case, etc.)

Aggregating useful metrics (average prices, volumes, returns)

Interactive visualization using Streamlit

Setup & Installation

Requirements:

Python 3.8+

pandas

pyarrow

streamlit

Installation instructions:

pip install pandas pyarrow streamlit

Data Cleaning & Schema
Steps performed:

Renamed headers to snake_case

Trimmed whitespace on headers & values

Standardized text case (tickers uppercase, sectors title case)

Standardized all missing values ("", NA, N/A, null, -) to pd.NA

Converted dates to yyyy-MM-dd

Converted number columns to float (prices, volume)

Deduplicated rows

Output: cleaned.parquet

Aggregations

Aggregates computed from cleaned data and saved as Parquet:

agg1.parquet: Daily average close price by ticker

agg2.parquet: Average volume by sector

agg3.parquet: Simple daily return by ticker

Dashboard Usage

Run the cleaning and aggregation notebook to produce parquet outputs.

Start the Streamlit app:

streamlit run app.py

Interact with:

Ticker, date range: Line chart of daily close

Sector: Bar chart of average volume

Daily return: Line chart by ticker

Screenshots:

You can find dashboard screenshots in the /screenshots folder, showing various filtered and charted outputs.

Project Structure

/datacleaning_viz
 ├─ data_cleaning.ipynb        # Data cleaning & aggregation notebook
 ├─ cleaned.parquet           # Cleaned, normalized dataset
 ├─ agg1.parquet              # Daily avg close by ticker
 ├─ agg2.parquet              # Avg volume by sector
 ├─ agg3.parquet              # Daily return by ticker
 ├─ app.py                    # Streamlit dashboard
 ├─ README.md                 # Project documentation
 └─ /screenshots              # Images of dashboard and visualizations
