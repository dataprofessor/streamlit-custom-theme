import streamlit as st

st.header('Contents of config.toml')

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number is:', number)

st.code("""
  [theme]
  primaryColor="#F39C12"
  backgroundColor="#2E86C1"
  secondaryBackgroundColor="#AED6F1"
  textColor="#FFFFFF"
  font="monospace"
""")
