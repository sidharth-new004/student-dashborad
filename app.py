import streamlit as st
from pathlib import path 

st.set_page_config(
    page_title="student task dashborad",
    layout="wide"
)

html_file = path("index.html").read_text(encoding="utf-8")

st.component.v1.html(html_file, height=900, scrolling=True)