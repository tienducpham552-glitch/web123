import streamlit as st
import streamlit.components.v1 as components
import google.generativeai as genai

# 1. Cấu hình API Gemini từ Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Xử lý logic Chatbot (Python làm thay Cloudflare)
def get_ai_response(user_input):
    try:
        response = model.generate_content(f"Bạn là Innerly, người bạn thấu cảm. Trả lời ngắn gọn: {user_input}")
        return response.text
    except Exception as e:
        return f"Lỗi: {str(e)}"

# 3. Giao diện chính
st.set_page_config(page_title="INNERLY", layout="wide")

# Kiểm tra file HTML
import os
html_path = os.path.join(os.path.dirname(__file__), "index.html")

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # Ở đây chúng ta hiển thị HTML của bạn
    components.html(html_code, height=2500, scrolling=True)
else:
    st.error("Không thấy file index.html!")
