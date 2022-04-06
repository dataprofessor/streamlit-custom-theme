import streamlit as st

st.header('Contents of config.toml')

st.slider('Test', 0, 10, 5)

with open('.streamlit/config.toml') as f:
  for line in f:
    st.write(line)
