import datetime as dt
import random

import streamlit as st


# -----------------------------
# 간단한 스타일 설정 (기본 기능만 사용)
# -----------------------------
st.markdown(
    """
    <style>
    .birthday-caption {
        font-size: 0.95rem;
        color: #666666;
    }
    .birthday-card {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        border-radius: 18px;
        padding: 1.1rem 1.4rem;
        margin-bottom: 0.8rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.04);
    }
    .birthday-name {
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 0.2rem;
    }
    .birthday-field {
        font-size: 0.9rem;
        color: #888888;
        margin-bottom: 0.35rem;
    }
    .birthday-desc {
        font-size: 0.9rem;
        line-height: 1.4;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# 데이터: 일부 날짜의 실제 유명인 생일 예시
# (월, 일) 기준으로 3명씩
# -----------------------------
FAMOUS_BIRTHDAYS = {
    # 1월 8일 – 과학·음악의 별 ⭐
    (1, 8): [
        {
            "name": "엘비스 프레슬리",
            "field": "가수 · 배우 🎤",
            "desc": "‘로큰롤의 황제’로 불리며 20세기 대중음악에 큰 영향을 준 미국 가수.",
        },
        {
            "name": "데이비드 보위",
            "field": "뮤지션 · 아티스트 🌌",
            "desc": "혁신적인 콘셉트와 퍼포먼스로 유명한 영국의 전설적인 록 뮤지션.",
        },
        {
            "name": "스티븐 호킹",
            "field": "이론물리학자 🧠",
            "desc": "블랙홀과 우주론 연구로 유명한 영국의 세계적 과학자.",
        },
    ],
    # 2월 12일 – 같은 날 태어난 두 거장 🏛️
    (2, 12): [
        {
            "name": "에이브러햄 링컨",
            "field": "정치가 · 미국 16대 대통령 🇺🇸",
            "desc": "노예제 폐지와 미국 남북전쟁의 수습으로 잘 알려진 대통령.",
        },
        {
            "name": "찰스 다윈",
            "field": "자연과학자 🐢",
            "desc": "진화론과 자연선택 이론을 제시한 영국의 생물학자.",
        },
        {
            "name": "크리스티나 리치",
            "field": "배우 🎬",
            "desc": "〈아담스 패밀리〉 등 다양한 작품에 출연한 미국 배우.",
        },
    ],
    # 3월 14일 – 파이(π)데이의 스타들 🥧
    (3, 14): [
        {
            "name": "알베르트 아인슈타인",
            "field": "물리학자 ⚛️",
            "desc": "상대성이론을 제시한 20세기 과학의 상징적인 인물.",
        },
        {
            "name": "스테픈 커리",
            "field": "농구 선수 🏀",
            "desc": "3점 슛 혁명으로 NBA 스타일을 바꾼 골든스테이트 워리어스의 스타.",
        },
        {
            "name": "마이클 케인",
            "field": "배우 🎭",
