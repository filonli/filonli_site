import streamlit as st

def on_clk():
    print("click")

st.set_page_config(page_title="My Page",page_icon=":cry:",layout="centered")

st.subheader("label1")
st.title("title")
st.write("smothing")
st.write("[romsing>](https://gemini.google.com/app/99f6feb82a005d67)")
st.button("press me",on_click= on_clk)