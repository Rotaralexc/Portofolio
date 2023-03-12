import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Rotar Alex")
    content = """"
    Hello, my name is Alex!
    University fresh graduated and for the moment working as an System Test Engineer at NTT DATA Romania.
    I am extremply motivated to learn new thing and to apply them in the real world as projects.
    """
    st.info(content)

content2 = """"
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)