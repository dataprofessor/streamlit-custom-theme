import streamlit as st

st.header('Contents of config.toml')

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number is:', number)

with open('.streamlit/config.toml') as f:
  for line in f:
    st.write(line)
