import streamlit as st

# MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI 궁합 데이터 (예시)
mbti_matches = {
    "INTJ": ["ENFP", "ENTP"],
    "INTP": ["ENTJ", "ESTJ"],
    "ENTJ": ["INTP", "INFJ"],
    "ENTP": ["INFJ", "ENTJ"],
    "INFJ": ["ENFP", "ENTP"],
    "INFP": ["ENFJ", "ENTJ"],
    "ENFJ": ["INFP", "ISFP"],
    "ENFP": ["INFJ", "INTJ"],
    "ISTJ": ["ESFP", "ESTP"],
    "ISFJ": ["ESFP", "ESTP"],
    "ESTJ": ["ISTP", "INTP"],
    "ESFJ": ["ISFP", "INFP"],
    "ISTP": ["ESTJ", "ESFJ"],
    "ISFP": ["ENFJ", "ESFJ"],
    "ESTP": ["ISFJ", "ISTJ"],
    "ESFP": ["ISTJ", "ISFJ"],
}

# 앱 제목
st.title("MBTI 궁합 테스트 💘")

# 사용자 입력
user_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_types)

if user_mbti:
    matches = mbti_matches.get(user_mbti, [])
    if matches:
        st.subheader(f"💡 {user_mbti}와 어울리는 MBTI")
        for m in matches:
            st.write(f"- {m}")
    else:
        st.write("궁합 정보가 없습니다.")

