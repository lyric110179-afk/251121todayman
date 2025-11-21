import streamlit as st
import random
import datetime as dt


# -----------------------------
# 유명인 데이터 (월/일 기준)
# -----------------------------
FAMOUS_BIRTHDAYS = {
    (1, 8): [
        {"name": "엘비스 프레슬리", "field": "가수 🎤", "desc": "로큰롤의 황제."},
        {"name": "데이비드 보위", "field": "뮤지션 🌌", "desc": "독창적 음악 세계."},
        {"name": "스티븐 호킹", "field": "과학자 🧠", "desc": "블랙홀 연구 선구자."},
    ],
    (3, 14): [
        {"name": "알베르트 아인슈타인", "field": "물리학자 ⚛️", "desc": "상대성이론 창시자."},
        {"name": "스테픈 커리", "field": "농구선수 🏀", "desc": "NBA 슈팅 혁명가."},
        {"name": "마이클 케인", "field": "배우 🎭", "desc": "영국의 명배우."},
    ],
    (6, 1): [
        {"name": "마릴린 먼로", "field": "배우 🎬", "desc": "헐리우드 아이콘."},
        {"name": "모건 프리먼", "field": "배우 🎞️", "desc": "중후한 목소리의 배우."},
        {"name": "톰 홀랜드", "field": "배우 🕷️", "desc": "스파이더맨 주연."},
    ],
    (9, 1): [
        {"name": "정국(BTS)", "field": "가수 🎤", "desc": "세계적인 K-POP 아티스트."},
        {"name": "젠데이아", "field": "배우 🎬", "desc": "스파이더맨·유포리아 출연."},
        {"name": "글로리아 에스테판", "field": "가수 🎶", "desc": "라틴팝의 선구자."},
    ],
    (12, 25): [
        {"name": "아이작 뉴턴", "field": "과학자 ⚖️", "desc": "만유인력 법칙 발견."},
        {"name": "험프리 보가트", "field": "배우 🎬", "desc": "카사블랑카 주연."},
        {"name": "애니 레녹스", "field": "가수 🎹", "desc": "유리스믹스 보컬."},
    ],
    (12, 30): [
        {"name": "뷔(BTS)", "field": "가수 🎨", "desc": "BTS의 비주얼 아티스트."},
        {"name": "타이거 우즈", "field": "골프선수 ⛳", "desc": "세계적인 골프 레전드."},
        {"name": "르브론 제임스", "field": "농구선수 🏀", "desc": "‘킹’으로 불리는 슈퍼스타."},
    ]
}


# -----------------------------
# 함수: 선택한 월에서 랜덤 날짜로 3명 추천
# -----------------------------
def get_people_by_month(month: int):
    # 선택한 월에 포함된 모든 날짜 찾기
    candidates = [k for k in FAMOUS_BIRTHDAYS if k[0] == month]

    if not candidates:
        return None, "😅 이 달은 아직 데이터가 없어요!"

    # 월에 포함된 날짜 중 하나 랜덤 선택
    selected_key = random.choice(candidates)
    day = selected_key[1]

    people = FAMOUS_BIRTHDAYS[selected_key]

    msg = f"🎉 **{month}월 {day}일** 생일의 유명 인물 3명을 소개할게요!"
    return people, msg



# -----------------------------
# UI 화면
# -----------------------------
st.title("🌟 2024년 탄생 별 찾기 ⭐")

st.write("2024년 **12개월 중 한 달**을 선택하면, 그 달에 태어난 **유명인 3명**을 랜덤으로 소개해줘요! 😊")

# 월 선택
month = st.selectbox("📅 월을 선택하세요", list(range(1, 13)), format_func=lambda x: f"{x}월")

st.markdown("---")

# 추천된 유명인
people, msg = get_people_by_month(month)

st.write(msg)

if people:
    for p in people:
        st.markdown(
            f"""
            <div style="
                background:#ffffff;
                border-radius:14px;
                padding:1rem 1.2rem;
                margin-bottom:0.8rem;
                box-shadow:0 4px 10px rgba(0,0,0,0.08);
            ">
                <div style="font-size:1.05rem; font-weight:700;">{p['name']}</div>
                <div style="color:#777; font-size:0.9rem; margin-bottom:0.3rem;">{p['field']}</div>
                <div style="font-size:0.9rem; line-height:1.35;">{p['desc']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
