import streamlit as st

st.header('config.toml')

with open('.streamlit/config.toml') as f:
  lines = f.readlines()
  st.code(st.write(lines))
