import streamlit as st
import pandas as pd
agg1 = pd.read_parquet('agg1.parquet')
agg2 = pd.read_parquet('agg2.parquet')
agg3 = pd.read_parquet('agg3.parquet')
st.title('Stock Market Dashboard')
ticker = st.selectbox('Choose ticker', sorted(agg1["ticker"].dropna().unique()))
date_range = st.date_input('Choose date range', [])
if date_range and len(date_range) == 2:
    start, end = [d.strftime('%Y-%m-%d') for d in date_range]
    filtered = agg1[(agg1['ticker'] == ticker) & (agg1['trade_date'] >= start) & (agg1['trade_date'] <= end)]
else:
    filtered = agg1[agg1['ticker'] == ticker]
st.line_chart(filtered.set_index('trade_date')['close_price'])
st.bar_chart(agg2.set_index('sector')['volume'])
ticker_ret = st.selectbox('Ticker for Return', sorted(agg3["ticker"].dropna().unique()))
filtered_ret = agg3[agg3['ticker'] == ticker_ret]
st.line_chart(filtered_ret.set_index('trade_date')['daily_return'])
