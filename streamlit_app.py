import streamlit as st

st.header('config.toml')

with open('.streamlit/config.toml') as f:
  contents = f.read()
  st.write(contents)

#st.write(primaryColor)
