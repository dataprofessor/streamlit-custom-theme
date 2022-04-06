import streamlit as st

st.header('Contents of config.toml')

number = st.slider('Test', 0, 10, 5)
st.write(number)

with open('.streamlit/config.toml') as f:
  for line in f:
    st.write(line)
