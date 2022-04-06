import streamlit as st

st.header('config.toml')

with open('.streamlit/config.toml') as f:
  lines = f.readlines()
  for line in lines:
    st.code(line)
