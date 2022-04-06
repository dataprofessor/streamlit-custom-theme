import streamlit as st

st.header('config.toml')

backgroundColor = st.color_picker('Pick A Color', '#FFFFFF')

with open('.streamlit/config.toml') as f:
  lines = f.readlines()
  for line in lines:
    st.write(line)
