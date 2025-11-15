**Stock Market Data Cleaning & Visualization :**

This project demonstrates a complete workflow for cleaning, aggregating, and visualizing stock market data using Python, pandas, Parquet, and Streamlit. The interactive dashboard allows users to explore stock prices, volumes, sectors, and daily returns efficiently.

**Table of Contents :**

- Overview
- Setup & Installation
- Data Cleaning & Schema
- Aggregations
- Dashboard Usage
- Screenshots
- Project Structure

**Overview :**

This assignment covers the full data-processing pipeline:

- Cleaning raw financial CSV files
- Normalizing schema (headers, missing values, text case)
- Aggregating meaningful financial metrics
- Building an interactive Streamlit dashboard for visual analysis

**Setup & Installation :**

Requirements

- Python 3.8+
- pandas
- pyarrow
- streamlit

**Install Dependencies**

pip install pandas pyarrow streamlit

**Data Cleaning & Schema :**

Cleaning steps performed:

- Renamed column headers to snake_case
- Trimmed whitespace in column names and data fields
- Standardized text case
  	- Tickers → UPPERCASE
  	- Sectors → Title Case
- Normalized missing values ("", "NA", "N/A", "null", "-") into pd.NA
- Converted date columns to YYYY-MM-DD
- Converted numeric columns (prices, volume) to float
- Removed duplicate rows

**Output:**

cleaned.parquet — fully cleaned and normalized dataset.

**Aggregations :**

The following analytics Parquet files are generated:

File	Description
agg1.parquet :	Daily average close price by ticker
agg2.parquet	: Average trading volume grouped by sector
agg3.parquet	: Simple daily return calculated per ticker

**Dashboard Usage :**

After generating all Parquet files through the cleaning notebook, run the dashboard:

streamlit run app.py

**Dashboard Features**

- Ticker & Date Range Selection → Line chart of daily close price
- Sector-Based View → Bar chart of average volume
- Returns Analysis → Line chart showing daily returns per ticker

**Screenshots :**

Dashboard screenshots are available in the /screenshots directory, showcasing filtered charts, sector comparisons, and return visualizations.
