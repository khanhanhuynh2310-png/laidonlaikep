import streamlit as st

st.set_page_config(
    page_title="Ứng dụng tính tiền gửi tiết kiệm",
    page_icon="ViTam.png"
)
# Tiêu đề ứng dụng
col1, col2 = st.columns([1, 6])

with col1:
    st.image("ViTam.png", width=1280)

with col2:
    st.title("Ứng dụng tính tiền gửi tiết kiệm_Vĩ Tâm")

# Nhập dữ liệu
C = st.number_input(
    "Nhập số tiền khách hàng gửi tiết kiệm (triệu đồng)",
    min_value=0.0,
    value=100.0
