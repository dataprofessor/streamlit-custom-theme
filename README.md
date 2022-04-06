# Theming with config.toml

`config.toml` is a configuration file stored in the same folder as the app in `.streamlit`.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st-config.toml/)

## Code
Here's how to use st.write:
```python
import streamlit as st

st.header('Theming with config.toml')

st.write('Contents of the config.toml file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` like so:
```python
import streamlit as st
```

This is followed by creating a header text for the app:
```python
st.header('Theming with config.toml')
```



## Further reading

