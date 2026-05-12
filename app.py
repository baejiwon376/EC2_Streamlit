import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="EC2 Streamlit Practice",
    layout="centered"
)

print(f"[LOG] Streamlit app rerun at {datetime.now()}")

st.title("EC2 Streamlit")
st.write("AWS Learner Lab EC2 환경 실행 확인.")

st.divider()

name = st.text_input("이름 입력")

if name:
    print(f"[LOG] User typed name: {name}")

message = st.text_area("메세지 입력")

if message:
    print(f"[LOG] User typed message: {message}")

if st.button("결과 확인"):
    print(f"[LOG] Button clicked at {datetime.now()}")
    st.success(f"{name}님, EC2에서 Streamlit 정상 실행 확인")
    st.write("입력한 메시지:")
    st.info(message)

st.divider()
