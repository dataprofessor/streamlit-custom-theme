import streamlit as st

st.header('config.toml')

with open('.streamlit/config.toml', 'a+') as f:
  f.write('[theme]\n')
  f.write(f'primaryColor="#F63366"')
  f.write(f'backgroundColor="#FFFFFF"')
  f.write(f'secondaryBackgroundColor="#F0F2F6"')
  f.write(f'textColor="#262730"')
  f.write(f'font="sans serif"')
