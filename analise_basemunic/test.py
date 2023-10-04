import pandas as pd
import numpy as np
import streamlit as st
import pandas as pd
import seaborn as sns
import requests

data = ('Call.csv')
df = pd.read_csv(data)

st.title('Dashboard Cliente')

df['Answer Rate'] = df['Answer Rate'].str.rstrip("%").astype(float)/100

incoming_avg= df['Incoming Calls'].mean()
answered_avg= df['Answered Calls'].mean()
ans_rate_avg = df['Answer Calls'].mean()


# Remove '%' symbol, convert to float, and handle non-numeric values
df['Answer Rate'] = pd.to_numeric(df['Answer Rate'].str.rstrip('%'), errors='coerce') / 100

col1, col2, col3 = st.columns(3)
col1.metric("Incoming Calls AVG", round(incoming_avg))
col2.metric("Answered Calls AVG", round(answered_avg))
col3.metric("Answer Rate AVG", round(ans_rate_avg))

st.line_chart(df[['Incoming Calls', 'Answered Calls']])