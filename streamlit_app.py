import streamlit as st
import streamlit.components.v1 as components

# Cấu hình trang web (tên tab, favicon)
st.set_page_config(page_title="INNERLY - Cân bằng cảm xúc", layout="wide")

# Đọc file HTML của bạn
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Hiển thị file HTML lên giao diện Streamlit
# Lưu ý: Bạn có thể điều chỉnh height (chiều cao) cho phù hợp với trang web của mình
components.html(html_code, height=2500, scrolling=True)

# CSS để xóa bỏ các khoảng trắng mặc định của Streamlit (giúp web trông chuyên nghiệp hơn)
st.markdown("""
    <style>
        .main > div { padding: 0; }
        iframe { border: none; }
        header { visibility: hidden; }
        footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)
