import streamlit as st

st.header('config.toml')

with open('.streamlit/config.toml') as f:
  for line in f:
    st.write(line)
