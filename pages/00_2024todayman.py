import datetime as dt
import random
import streamlit as st

# -----------------------------
# UI 스타일
# -----------------------------
st.markdown(
    """
    <style>
    .birthday-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .birthday-name {
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 0.2rem;
    }
    .birthday-field {
        font-size: 0.9rem;
        color: #777;
        margin-bottom: 0.25rem;
    }
    .birthday-desc {
        font-size: 0.9rem;
        line-height: 1.35;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# 데이터
# -----------------------------
FAMOUS_BIRTHDAYS = {
    (1, 8): [
        {"name": "엘비스 프레슬리", "field": "가수 🎤", "desc": "로큰롤의 황제."},
        {"name": "데이비드 보위", "field": "뮤지션 🌌", "desc": "혁신적인 음악."},
        {"name": "스티븐 호킹", "field": "과학자 🧠", "desc": "블랙홀 연구의 선구자."},
    ],
    (3, 14): [
        {"name": "알베르트 아인슈타인", "field": "물리학자 ⚛️", "desc": "상대성이론의 창시자."},
        {"name": "스테픈 커리", "field": "농구선수 🏀", "desc": "NBA 3점 슛 혁신."},
        {"name": "마이클 케인", "field": "배우 🎭", "desc": "영국의 명배우."},
    ],
    (6, 1): [
        {"name": "마릴린 먼로", "field": "배우 🎬", "desc": "헐리우드의 상징적 배우."},
        {"name": "모건 프리먼", "field": "배우 🎞️", "desc": "중후한 목소리의 배우."},
        {"name": "톰 홀랜드", "field": "배우 🕷️", "desc": "스파이더맨 주연."},
    ],
    (12, 25): [
        {"name": "아이작 뉴턴", "field": "과학자 ⚖️", "desc": "만유인력 법칙 발견."},
        {"name": "험프리 보가트", "field": "배우 🎬", "desc": "〈카사블랑카〉 주연."},
        {"name": "애니 레녹스", "field": "가수 🎹", "desc": "유리스믹스 보컬."},
    ],
}

# -----------------------------
# 함수
# -----------------------------
def get_people_for_date(selected_date: dt.date):
    key = (selected_date.month, selected_date.day)

    if key in FAMOUS_BIRTHDAYS:
        return FAMOUS_BIRTHDAYS[key], f"🎉 {selected_date.month}월 {selected_date.day}일 생일의 인물!"
    else:
        # 같은 월 추천
        same_month = [k for k in FAMOUS_BIRTHDAYS if k[0] == selected_date.month]
        if same_month:
            alt_key = random.choice(same_month)
            return FAMOUS_BIRTHDAYS[alt_key], f"😊 이 날짜는 데이터가 없어요.\n대신 **{alt_key[0]}월 {alt_key[1]}일** 생일의 인물을 보여줄게요!"
        else:
            # 전체에서 랜덤
            any_key = random.choice(list(FAMOUS_BIRTHDAYS.keys()))
            return FAMOUS_BIRTHDAYS[any_key], "🔍 데이터가 없어 랜덤 추천을 제공합니다!"

# -----------------------------
# UI 화면
# -----------------------------
st.title("🌟 오늘의 탄생 별 찾기 (2024) ⭐")

selected_date = st.date_input(
    "📅 2024년 날짜를 선택하세요",
    min_value=dt.date(2024, 1, 1),
    max_value=dt.date(2024, 12, 31),
    value=dt.date(2024, 1, 1)
)

st.markdown("---")

people, msg = get_people_for_date(selected_date)
st.write(msg)

for p in people:
    st.markdown(
        f"""
        <div class="birthday-card">
            <div class="birthday-name">{p['name']}</div>
            <div class="birthday-field">{p['field']}</div>
            <div class="birthday-desc">{p['desc']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
