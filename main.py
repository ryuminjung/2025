import streamlit as st

st.set_page_config(page_title="MBTI 궁합 테스트 (상세 설명)", page_icon="💘", layout="centered")

st.title("💘 MBTI 궁합 테스트 — 친구/연인별 상세 이유")
st.write("각 추천 MBTI에 대해 **친구로서**와 **연인으로서** 왜 잘 맞는지 구체적으로 설명해줍니다. (일반화된 경향 참고용)")

mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti_data = {
    "INTJ": {
        "matches": {
            "ENFP": {
                "friend_desc": "ENFP의 외향성과 풍부한 아이디어가 INTJ의 구조적 사고에 활력을 불어넣습니다. ENFP는 사교적 자극을 제공하고, INTJ는 ENFP의 아이디어를 현실성 있게 정리해 서로 보완합니다.",
                "love_desc": "ENFP의 감정 표현과 즉흥적인 애정 표현이 INTJ에게 정서적 온기를 주고, INTJ의 장기적 계획과 안정감이 ENFP에게 안전감을 줍니다. 서로의 자유와 독립을 존중하면 관계의 균형이 잘 맞습니다."
            },
            "ENTP": {
                "friend_desc": "ENTP와의 토론은 INTJ의 관점을 넓혀주며, ENTP는 이론을 실험해 보는 역할을 합니다. 지적 자극이 많은 활동에서 자연스럽게 에너지를 합칩니다.",
                "love_desc": "두 유형 모두 지적 자극을 중시해 연인으로서 대화와 프로젝트에서 활력을 냅니다. 다만 논쟁적 순간에 INTJ의 단호함과 ENTP의 논쟁 욕구가 충돌할 수 있어 규칙적 소통이 필요합니다."
            }
        }
    },

    "INTP": {
        "matches": {
            "ENTJ": {
                "friend_desc": "ENTJ의 구조화와 추진력이 INTP의 풍부한 아이디어를 실제로 시도하게 만듭니다. 실무적 협력이나 토론에서 상호 보완이 잘 됩니다.",
                "love_desc": "ENTJ는 관계에서 방향성을 제시하고, INTP는 창의적 해결책과 유연한 사고로 ENTJ를 보완합니다. 감정표현 방식이 달라 충돌이 있을 수 있으니 기대치를 명확히 하는 것이 중요합니다."
            },
            "ESTJ": {
                "friend_desc": "ESTJ의 실용성과 규칙성은 INTP의 추상적 사고를 현실적 결과로 연결시켜 줍니다. 프로젝트나 일상 운영에서 좋은 파트너가 됩니다.",
                "love_desc": "ESTJ의 일상적 안정과 책임감이 INTP에게 기반을 제공하고, INTP는 관계에 아이디어와 유머를 더합니다. 서로의 생활방식 차이를 존중하면 조화롭습니다."
            }
        }
    },

    "ENTJ": {
        "matches": {
            "INTP": {
                "friend_desc": "INTP의 폭넓은 아이디어와 분석력이 ENTJ의 목표 달성에 필요한 전략적 통찰을 제공합니다. 토론·계획 단계에서 시너지가 큽니다.",
                "love_desc": "ENTJ의 추진력과 리더십은 INTP의 창의적 기여를 현실로 만들고, INTP는 ENTJ에게 새로운 관점을 제시해 관계의 신선함을 유지합니다. 역할 분담이 잘 맞으면 안정적 파트너십이 됩니다."
            },
            "INFJ": {
                "friend_desc": "INFJ의 사람 중심적 통찰이 ENTJ의 목표 지향성과 균형을 이루어 팀으로서 깊이 있는 결정을 돕습니다. INFJ는 인간관계를, ENTJ는 구조를 담당합니다.",
                "love_desc": "연인 관계에서는 INFJ의 공감능력이 ENTJ의 단호함을 부드럽게 만들고, ENTJ는 관계에 실질적 방향성을 제공합니다. 감정의 민감함을 존중하면 깊은 유대가 형성됩니다."
            }
        }
    },

    "ENTP": {
        "matches": {
            "INFJ": {
                "friend_desc": "INFJ의 통찰과 가치 중심적 관점이 ENTP의 아이디어를 깊이 있게 다듬어 줍니다. ENTP는 INFJ를 사회적으로 활발히 이끌어주며 상호 보완적입니다.",
                "love_desc": "ENTP의 유머와 창의성이 INFJ의 내면 세계를 환기시키고, INFJ는 ENTP에게 정서적 안정과 깊은 이해를 제공합니다. 서로의 표현 방식 차이를 이해해야 오해를 줄일 수 있습니다."
            },
            "ENTJ": {
                "friend_desc": "두 유형 모두 아이디어와 실행을 중시해 프로젝트 파트너로 강합니다. 활발한 논의와 빠른 의사결정에서 에너지를 나눕니다.",
                "love_desc": "지적 경쟁과 추진력이 결합된 역동적인 관계가 됩니다. 권한과 역할을 분명히 하지 않으면 주도권 경쟁이 발생할 수 있으니 협의가 중요합니다."
            }
        }
    },

    "INFJ": {
        "matches": {
            "ENFP": {
                "friend_desc": "ENFP의 외향적 활기와 다양성 추구가 INFJ의 내면적 통찰에 새로운 경험을 더해 줍니다. 감정적 공감과 아이디어 공유에서 깊은 유대가 생깁니다.",
                "love_desc": "가치와 의미를 중시하는 공통점으로 정서적 연결이 깊습니다. ENFP의 표현력이 INFJ에게 신뢰감을 주고, INFJ의 헌신이 ENFP에게 안정감을 줍니다."
            },
            "ENTP": {
                "friend_desc": "ENTP의 발산적 아이디어가 INFJ의 통찰을 자극해 서로 성장하게 합니다. 토론에서 서로에게 새로운 시각을 제공하는 친구가 됩니다.",
                "love_desc": "연인으로서 서로의 다른 방식(ENTP의 경쾌함 vs INFJ의 깊이)이 매력으로 작용하나, 민감한 주제에서는 INFJ가 상처받을 수 있어 세심한 소통이 필요합니다."
            }
        }
    },

    "INFP": {
        "matches": {
            "ENFJ": {
                "friend_desc": "ENFJ의 대인능력과 격려가 INFP의 이상과 감정을 실현하는 데 도움을 줍니다. 서로의 감정과 가치를 존중하는 우정이 형성됩니다.",
                "love_desc": "ENFJ는 감정 표현과 실천으로 INFP를 보살피고, INFP는 ENFJ에게 진심 어린 지지와 창의적 영감을 제공합니다. 상호 인정이 핵심입니다."
            },
            "ENTJ": {
                "friend_desc": "ENTJ의 체계와 추진력이 INFP의 이상을 실천으로 옮기게 도와주며, INFP는 ENTJ에게 인간적 관점을 제공합니다.",
                "love_desc": "연인으로서는 ENTJ의 결단력과 INFP의 가치관이 서로를 보완합니다. 가치 충돌 때 감정적 민감성을 배려하는 노력이 필요합니다."
            }
        }
    },

    "ENFJ": {
        "matches": {
            "INFP": {
                "friend_desc": "INFP의 진심과 가치 중심적 태도를 ENFJ가 잘 이해하고 지지해 줍니다. 서로의 장점을 발견해 격려하는 친구가 됩니다.",
                "love_desc": "연인으로는 ENFJ의 적극적 돌봄과 INFP의 깊은 헌신이 만나 안정적이고 따뜻한 관계를 만듭니다. 서로의 감정적 요구를 존중하면 깊어진다."
            },
            "ISFP": {
                "friend_desc": "ISFP의 감각적 예술성과 ENFJ의 사람 중심적 리더십이 서로에게 영감을 줍니다. ISFP는 ENFJ에게 감성적 균형을 제공합니다.",
                "love_desc": "연인으로는 ENFJ가 사회적·감정적 케어를 하고 ISFP는 부드러운 애정을 행동으로 보여줘 안정적 관계가 됩니다. 서두르지 않는 배려가 중요합니다."
            }
        }
    },

    "ENFP": {
        "matches": {
            "INFJ": {
                "friend_desc": "INFJ의 깊이와 ENFP의 외향적 폭발력이 서로의 세계를 넓혀줍니다. 창의적 활동·대화에서 자연히 어울립니다.",
                "love_desc": "감정과 가치를 중시하는 공감대가 강해 연인으로서 친밀감이 깊습니다. ENFP의 활력과 INFJ의 안정적 공감이 좋은 균형을 이룹니다."
            },
            "INTJ": {
                "friend_desc": "INTJ의 계획성과 ENFP의 즉흥성이 아이디어를 실제로 만들어 내는 조화를 이룹니다. 서로가 서로의 부족한 부분을 채워줍니다.",
                "love_desc": "INTJ의 장기적 비전과 ENFP의 열정이 결합해 관계가 성장합니다. 자유와 개인시간을 존중하면 더 안정적입니다."
            }
        }
    },

    "ISTJ": {
        "matches": {
            "ESFP": {
                "friend_desc": "ESFP의 즉흥적 즐거움이 ISTJ의 규칙적 생활을 활기차게 만들며, ISTJ는 ESFP에게 신뢰와 책임감을 제공합니다.",
                "love_desc": "연인으로는 ISTJ의 안정성과 ESFP의 활발함이 서로에게 필요한 균형을 줍니다. 일상 실무분담을 맞추면 갈등이 줄어듭니다."
            },
            "ESTP": {
                "friend_desc": "ESTP의 문제해결적 행동성이 ISTJ의 신중함과 만나 실용적 협력이 잘 됩니다. 함께 행동할 때 효율적입니다.",
                "love_desc": "모험과 안정의 조합으로 연인 생활이 활기차지만, 충동적 결정에서 ISTJ가 불안해할 수 있어 사전 합의가 도움됩니다."
            }
        }
    },

    "ISFJ": {
        "matches": {
            "ESFP": {
                "friend_desc": "ESFP의 활달함이 ISFJ의 세심한 배려를 밝게 해 주며, ISFJ는 ESFP의 감정을 안정적으로 돌봅니다.",
                "love_desc": "따뜻한 돌봄과 즐거운 활동이 결합된 관계가 형성됩니다. 작은 배려와 표현이 신뢰를 강화합니다."
            },
            "ESTP": {
                "friend_desc": "ESTP의 에너지와 문제해결력이 실용적 도움을 주고, ISFJ는 ESTP에게 안정적 지지와 세부 관리를 제공합니다.",
                "love_desc": "연인으로는 즉흥성과 세심함이 균형을 이루면 서로에게 좋은 자극이 됩니다. 감정표현의 빈도 차이를 이해해야 합니다."
            }
        }
    },

    "ESTJ": {
        "matches": {
            "ISTP": {
                "friend_desc": "ISTP의 현실적인 기술력과 ESTJ의 조직력이 만나 실무적으로 강력한 팀을 이룹니다. 문제 해결에서 효율적입니다.",
                "love_desc": "연인으로는 역할 분담이 명확하고 실용적이며 안정적입니다. ISTP의 자유를 존중해 주면 갈등이 적습니다."
            },
            "INTP": {
                "friend_desc": "INTP의 창의적 문제해결과 ESTJ의 실행력이 조화를 이룹니다. 아이디어가 현실이 되는 파트너십입니다.",
                "love_desc": "ESTJ는 실천으로 관계를 안정시키고 INTP는 새로운 관점과 유연함을 제공합니다. 소통의 방식 차이를 좁혀야 합니다."
            }
        }
    },

    "ESFJ": {
        "matches": {
            "ISFP": {
                "friend_desc": "ISFP의 감성적 섬세함을 ESFJ가 사회적으로 지지하고, ISFP는 ESFJ에게 진솔한 예술적·감정적 인사이트를 제공합니다.",
                "love_desc": "연인으로는 서로를 돌보는 방식이 자연스러워 안정적이고 따뜻한 관계가 됩니다. 작은 배려와 표현이 큰 의미를 가집니다."
            },
            "INFP": {
                "friend_desc": "INFP의 내적 가치관을 ESFJ가 실용적 지원과 사회적 연결로 돕습니다. 서로의 강점을 보완해 주는 우정입니다.",
                "love_desc": "감성적 공감과 실제적 돌봄이 결합되어 안정적 연애가 형성됩니다. 상대의 감정적 필요를 세심히 챙기는 것이 중요합니다."
            }
        }
    },

    "ISTP": {
        "matches": {
            "ESTJ": {
                "friend_desc": "ESTJ의 규칙성과 ISTP의 문제해결 기술이 만나 실용적 협업이 잘됩니다. 둘 다 '해결'에 초점을 맞추는 성향이 강합니다.",
                "love_desc": "연인으로는 즉흥적 활동과 조직적 생활이 균형을 이루면 흥미롭고 안정적입니다. 사생활 존중이 핵심입니다."
            },
            "ESFJ": {
                "friend_desc": "ESFJ의 사교성과 배려가 ISTP의 실용적 사고를 인간적으로 보완합니다. 서로의 다른 접근법이 유익합니다.",
                "love_desc": "연인으로서는 ESFJ의 돌봄이 ISTP의 실용성을 보완하고, ISTP의 독립성이 ESFJ에게 새로운 관점을 제공합니다. 감정표현의 방식 차이를 인지하세요."
            }
        }
    },

    "ISFP": {
        "matches": {
            "ENFJ": {
                "friend_desc": "ENFJ의 사람 중심적 리더십이 ISFP의 감성적 표현을 사회적으로 빛나게 해 줍니다. 서로의 강점을 자연스럽게 끌어냅니다.",
                "love_desc": "연인으로서 ENFJ의 적극적 돌봄과 ISFP의 섬세한 애정 표현이 맞물려 부드럽고 따뜻한 관계를 만듭니다. 감정적 안전감이 중요합니다."
            },
            "ESFJ": {
                "friend_desc": "ESFJ는 ISFP의 감성을 이해하고 일상에서 돌봐주며, ISFP는 ESFJ에게 진솔한 감정과 창의적 취향을 제공합니다.",
                "love_desc": "연인 관계에서는 서로의 배려와 표현 방식이 잘 맞아 안정감 있는 사랑을 나눕니다. 작은 제스처가 큰 신뢰를 만듭니다."
            }
        }
    },

    "ESTP": {
        "matches": {
            "ISFJ": {
                "friend_desc": "ISFJ의 신중함과 ESTP의 모험성이 서로를 보완해 즐거운 경험과 동시에 안정적인 지원을 제공합니다.",
                "love_desc": "연인으로는 즉흥적인 활동과 세심한 돌봄이 결합해 균형을 이루면 활기찬 관계가 됩니다. 안전과 흥분의 균형이 포인트입니다."
            },
            "ISTJ": {
                "friend_desc": "ISTJ의 계획성과 ESTP의 실행력이 만나 현실적인 결과를 잘 만들어냅니다. 활동적 프로젝트에서 좋은 파트너입니다.",
                "love_desc": "연인으로는 스릴 넘치는 순간과 일상의 안정이 조화되면 서로에게 만족감을 줍니다. 서로의 우선순위를 맞추는 노력이 중요합니다."
            }
        }
    },

    "ESFP": {
        "matches": {
            "ISTJ": {
                "friend_desc": "ISTJ의 신중함이 ESFP의 즉흥성과 어우러져 즐거운 활동을 안정적으로 즐기게 합니다. 서로 다른 에너지가 균형을 이룹니다.",
                "love_desc": "연인으로는 ESFP의 밝은 에너지와 ISTJ의 믿음직함이 서로를 보완합니다. 일상에서 책임 분담을 잘하면 충돌이 적습니다."
            },
            "ISFJ": {
                "friend_desc": "ISFJ의 세심함이 ESFP의 활력을 안정적으로 지지해 주며, ESFP는 ISFJ에게 즐거움과 사회적 기회를 제공합니다.",
                "love_desc": "따뜻한 돌봄과 활발한 생활이 결합되어 연인으로서 즐거운 관계를 만듭니다. 소통과 이해가 관계 유지의 핵심입니다."
            }
        }
    }
}

# --- 사용자 입력 및 출력 UI ---
user_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_types)

if user_mbti:
    data = mbti_data.get(user_mbti)
    if not data:
        st.warning("선택하신 MBTI에 대한 정보가 없습니다.")
    else:
        matches = data["matches"]
        st.subheader(f"🔎 {user_mbti}에게 추천되는 MBTI")
        st.write(", ".join(matches.keys()))

        # 보이는 형태: 두 매칭을 좌우 컬럼으로 깔끔하게 표시 (대부분 2개)
        match_items = list(matches.items())
        if len(match_items) == 2:
            col1, col2 = st.columns(2)
            for col, (mtype, descs) in zip((col1, col2), match_items):
                with col:
                    st.markdown(f"### {mtype}")
                    st.markdown("**👯 친구로서 이유**")
                    st.write(descs["friend_desc"])
                    st.markdown("**💖 연인으로서 이유**")
                    st.write(descs["love_desc"])
        else:
            # 일반 루프 (만약 매칭 수가 2가 아닐 때)
            for mtype, descs in match_items:
                st.markdown(f"### {mtype}")
                st.markdown("**👯 친구로서 이유**")
                st.write(descs["friend_desc"])
                st.markdown("**💖 연인으로서 이유**")
                st.write(descs["love_desc"])

        st.markdown("---")
        st.caption("※ 설명은 MBTI의 일반적 경향을 바탕으로 한 참고용입니다. 개인차가 크니 실제 관계에서는 대화와 상호 존중이 가장 중요합니다.")
