import streamlit as st

st.header('config.toml')

with open('.streamlit/config.toml') as f:
  contents = f.read()
  print(contents)

#st.write(primaryColor)
