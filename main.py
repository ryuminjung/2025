import streamlit as st

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="MBTI 궁합 테스트", page_icon="💘", layout="centered")

st.title("💘 MBTI 궁합 테스트")
st.write("당신의 MBTI를 선택하면, 친구로서와 연인으로서 잘 맞는 MBTI와 그 이유를 알려드릴게요!")

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
        "friend_desc": "지적인 대화를 즐기며 새로운 아이디어를 함께 발전시킵니다.",
        "love_desc": "서로의 장단점을 보완하며 안정감과 설렘을 동시에 줍니다.",
        "img": "https://i.ibb.co/xq8bYjD/love1.jpg"
    },
    "INTP": {
        "matches": ["ENTJ", "ESTJ"],
        "friend_desc": "서로 다른 시각에서 문제를 분석하고 해결책을 찾습니다.",
        "love_desc": "논리와 추진력을 조화롭게 결합하여 함께 성장합니다.",
        "img": "https://i.ibb.co/4RsYRY4/love5.jpg"
    },
    "ENTJ": {
        "matches": ["INTP", "INFJ"],
        "friend_desc": "목표 지향적인 대화를 나누며 서로에게 동기를 부여합니다.",
        "love_desc": "이끌어 주고 지지해 주며 이상적인 파트너가 됩니다.",
        "img": "https://i.ibb.co/0cBzGzg/love6.jpg"
    },
    "ENTP": {
        "matches": ["INFJ", "ENTJ"],
        "friend_desc": "활발한 토론과 새로운 도전을 즐깁니다.",
        "love_desc": "서로의 에너지가 잘 맞아 열정적인 관계를 형성합니다.",
        "img": "https://i.ibb.co/P6wkgmR/love4.jpg"
    },
    "INFJ": {
        "matches": ["ENFP", "ENTP"],
        "friend_desc": "깊은 공감과 이해를 바탕으로 진솔한 우정을 나눕니다.",
        "love_desc": "서로의 내면을 존중하며 안정적이고 따뜻한 관계를 유지합니다.",
        "img": "https://i.ibb.co/8m4pbtB/love3.jpg"
    },
    "INFP": {
        "matches": ["ENFJ", "ENTJ"],
        "friend_desc": "감정과 가치관을 공유하며 진심 어린 대화를 나눕니다.",
        "love_desc": "서로의 꿈을 지지하며 함께 성장하는 연인이 됩니다.",
        "img": "https://i.ibb.co/wpnrXJ2/love7.jpg"
    },
    "ENFJ": {
        "matches": ["INFP", "ISFP"],
        "friend_desc": "다른 사람의 장점을 발견하고 격려합니다.",
        "love_desc": "따뜻함과 배려로 깊이 있는 관계를 만듭니다.",
        "img": "https://i.ibb.co/kc7hBnD/love8.jpg"
    },
    "ENFP": {
        "matches": ["INFJ", "INTJ"],
        "friend_desc": "즐거운 모험과 다양한 활동을 함께합니다.",
        "love_desc": "상대방의 계획성과 본인의 자유로움이 잘 어우러집니다.",
        "img": "https://i.ibb.co/7NwR4f2/love2.jpg"
    },
    "ISTJ": {
        "matches": ["ESFP", "ESTP"],
        "friend_desc": "신뢰와 책임감을 바탕으로 오랜 우정을 유지합니다.",
        "love_desc": "상대방의 활발함과 자신의 안정성이 조화를 이룹니다.",
        "img": "https://i.ibb.co/Zh8cQkb/love9.jpg"
    },
    "ISFJ": {
        "matches": ["ESFP", "ESTP"],
        "friend_desc": "작은 배려와 관심으로 관계를 돈독히 합니다.",
        "love_desc": "따뜻한 성격이 활발한 파트너와 잘 어울립니다.",
        "img": "https://i.ibb.co/tbdzTtv/love10.jpg"
    },
    "ESTJ": {
        "matches": ["ISTP", "INTP"],
        "friend_desc": "목표 달성을 위해 체계적으로 협력합니다.",
        "love_desc": "안정적인 기반 위에서 함께 성장합니다.",
        "img": "https://i.ibb.co/t3Sn2mg/love11.jpg"
    },
    "ESFJ": {
        "matches": ["ISFP", "INFP"],
        "friend_desc": "다정하고 사교적인 성격으로 편안한 관계를 형성합니다.",
        "love_desc": "서로를 잘 돌보며 안정적인 사랑을 이어갑니다.",
        "img": "https://i.ibb.co/zrCjqmV/love12.jpg"
    },
    "ISTP": {
        "matches": ["ESTJ", "ESFJ"],
        "friend_desc": "새로운 경험과 실용적인 조언을 주고받습니다.",
        "love_desc": "서로의 성격 차이가 관계를 더 풍부하게 만듭니다.",
        "img": "https://i.ibb.co/QkFnHNd/love13.jpg"
    },
    "ISFP": {
        "matches": ["ENFJ", "ESFJ"],
        "friend_desc": "감정을 솔직하게 표현하며 깊은 유대를 형성합니다.",
        "love_desc": "부드럽고 따뜻한 사랑을 나눕니다.",
        "img": "https://i.ibb.co/Tk7cHn7/love14.jpg"
    },
    "ESTP": {
        "matches": ["ISFJ", "ISTJ"],
        "friend_desc": "활동적인 에너지로 즐거운 시간을 보냅니다.",
        "love_desc": "즉흥적인 매력이 관계를 신나게 만듭니다.",
        "img": "https://i.ibb.co/N7jBp9K/love15.jpg"
    },
    "ESFP": {
        "matches": ["ISTJ", "ISFJ"],
        "friend_desc": "함께 웃고 즐길 수 있는 시간이 많습니다.",
        "love_desc": "상대방의 차분함이 자신의 활발함과 잘 어울립니다.",
        "img": "https://i.ibb.co/gFJtBVR/love16.jpg"
    }
}

# --- 사용자 입력 ---
user_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_types)

# --- 결과 출력 ---
if user_mbti:
    match_info = mbti_data[user_mbti]
    st.subheader(f"💡 {user_mbti}와 어울리는 MBTI")
    st.write(", ".join(match_info["matches"]))

    st.markdown("### 👯‍♀️ 친구로서 궁합")
    st.info(match_info["friend_desc"])

    st.markdown("### 💖 연인으로서 궁합")
    st.success(match_info["love_desc"])

    st.image(match_info["img"], use_column_width=True)
