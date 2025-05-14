import streamlit as st
import pandas as pd

st.title("다기능 데이터 도구 🔧")

# 사이드바에서 기능 선택
option = st.sidebar.selectbox("기능을 선택하세요", ["CSV 불러오기", "필터링", "데이터 통계", "기타 기능"])

# 각 기능에 따른 인터페이스와 출력
if option == "CSV 불러오기":
    st.header("📄 CSV 파일 불러오기")
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("데이터프레임 로딩 성공!")
        st.dataframe(df)

elif option == "필터링":
    st.header("🔍 데이터 필터링")
    # 예시용 데이터
    data = pd.DataFrame({
        "이름": ["철수", "영희", "민수", "수지"],
        "나이": [25, 30, 22, 28],
        "도시": ["서울", "부산", "서울", "대전"]
    })
    city = st.selectbox("도시 선택", data["도시"].unique())
    filtered = data[data["도시"] == city]
    st.write("🔎 필터링된 결과:")
    st.dataframe(filtered)

elif option == "데이터 통계":
    st.header("📊 기본 통계 정보")
    df = pd.DataFrame({
        "매출": [10000, 25000, 17000, 30000, 12000],
        "비용": [7000, 12000, 8000, 20000, 9000]
    })
    df["이익"] = df["매출"] - df["비용"]
    st.write("데이터프레임:")
    st.dataframe(df)
    st.write("📈 이익 통계:")
    st.write(df["이익"].describe())

elif option == "기타 기능":
    st.header("🧪 기타 기능 테스트")
    input_text = st.text_input("아무 텍스트나 입력하세요")
    if st.button("출력"):
        st.write("입력한 내용:", input_text)
