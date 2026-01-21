import streamlit as st
import streamlit.components.v1 as components
import google.generativeai as genai
import os

# 1. Cấu hình API (Lấy từ Secrets của Streamlit)
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Bạn chưa cài đặt GEMINI_API_KEY trong phần Secrets!")

# 2. Đọc file HTML an toàn
current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "index.html")

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    components.html(html_code, height=1500, scrolling=True)
else:
    st.error(f"Không tìm thấy file index.html tại: {html_path}")
