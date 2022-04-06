import streamlit as st

st.header('config.toml')

backgroundColor = st.color_picker('Pick A Color', '#FFFFFF')

with open('.streamlit/config.toml', 'w+') as f:
  f.write('[theme]\n')
  f.write(f'primaryColor="#F63366"')
  f.write(f'backgroundColor="{backgroundColor}"')
  f.write(f'secondaryBackgroundColor="#F0F2F6"')
  f.write(f'textColor="#262730"')
  f.write(f'font="sans serif"')
