import streamlit as st

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="MBTI 궁합 테스트", page_icon="💘", layout="centered")

st.title("💘 MBTI 궁합 테스트")
st.write("당신의 MBTI를 선택하면, 가장 잘 어울리는 MBTI와 그 이유를 알려드릴게요!")

# --- MBTI 데이터 ---
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti_data = {
    "INTJ": {
        "matches": ["ENFP", "ENTP"],
        "desc": "전략가형인 INTJ는 창의적이고 자유로운 ENFP, ENTP와 최고의 시너지를 냅니다.",
        "img": "https://i.ibb.co/xq8bYjD/love1.jpg"
    },
    "ENFP": {
        "matches": ["INFJ", "INTJ"],
        "desc": "자유로운 영혼 ENFP는 깊이 있는 INFJ, 계획적인 INTJ와 잘 맞아요.",
        "img": "https://i.ibb.co/7NwR4f2/love2.jpg"
    },
    "INFJ": {
        "matches": ["ENFP", "ENTP"],
        "desc": "따뜻한 이상주의자 INFJ는 활발한 ENFP, ENTP와 조화를 이룹니다.",
        "img": "https://i.ibb.co/8m4pbtB/love3.jpg"
    },
    "ENTP": {
        "matches": ["INFJ", "ENTJ"],
        "desc": "도전적인 ENTP는 진중한 INFJ, 리더형 ENTJ와 잘 맞습니다.",
        "img": "https://i.ibb.co/P6wkgmR/love4.jpg"
    },
    # 나머지는 필요 시 동일한 구조로 추가 가능
}

# --- 사용자 입력 ---
user_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_types)

# --- 결과 출력 ---
if user_mbti:
    if user_mbti in mbti_data:
        match_info = mbti_data[user_mbti]
        
        st.subheader(f"💡 {user_mbti}와 어울리는 MBTI")
        st.write(", ".join(match_info["matches"]))
        
        st.info(match_info["desc"])
        st.image(match_info["img"], use_column_width=True)
    else:
        st.warning("아직 이 MBTI의 궁합 정보가 준비되지 않았어요 😅")
