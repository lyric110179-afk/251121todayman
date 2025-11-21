import streamlit as st
from datetime import date

# ---------------- 기본 설정 ----------------
st.set_page_config(
    page_title="2025 생일 유명인 찾기",
    page_icon="🎂",
    layout="centered",
)

# ---------------- 데이터: 날짜별 유명인 ----------------
# (예시용 데이터입니다. 필요한 날짜를 계속 추가해서 확장하면 돼요!)
BIRTHDAYS = {
    # 2월 11일
    (2, 11): [
        {
            "name": "토머스 에디슨",
            "field": "발명가",
            "desc": "전구와 축음기 등 수많은 발명을 남긴 ‘발명의 왕’ 💡",
            "emoji": "💡",
        },
        {
            "name": "제니퍼 애니스톤",
            "field": "배우",
            "desc": "미국 시트콤 <프렌즈>로 유명한 배우 🎬",
            "emoji": "🎬",
        },
        {
            "name": "테일러 로트너",
            "field": "배우",
            "desc": "<트와일라잇> 시리즈로 알려진 미국 배우 🐺",
            "emoji": "🌙",
        },
    ],
    # 3월 14일
    (3, 14): [
        {
            "name": "알베르트 아인슈타인",
            "field": "물리학자",
            "desc": "상대성이론으로 유명한 20세기 대표 과학자 🧠",
            "emoji": "🧠",
        },
        {
            "name": "스테판 커리",
            "field": "농구선수",
            "desc": "NBA 최정상급 3점 슈터, 골든스테이트 워리어스 스타 🏀",
            "emoji": "🏀",
        },
        {
            "name": "시몬 바일스",
            "field": "체조선수",
            "desc": "올림픽 금메달 여러 개를 딴 미국 체조 여제 🤸‍♀️",
            "emoji": "🤸‍♀️",
        },
    ],
    # 6월 18일
    (6, 18): [
        {
            "name": "폴 매카트니",
            "field": "뮤지션",
            "desc": "비틀즈 멤버이자 전설적인 싱어송라이터 🎵",
            "emoji": "🎵",
        },
        {
            "name": "블레이크 쉘튼",
            "field": "가수",
            "desc": "미국 컨트리 음악의 인기 가수이자 TV 쇼 코치 🎤",
            "emoji": "🎤",
        },
        {
            "name": "리처드 매든",
            "field": "배우",
            "desc": "<왕좌의 게임> 롭 스타크로 유명한 배우 🐺",
            "emoji": "🎭",
        },
    ],
    # 7월 6일
    (7, 6): [
        {
            "name": "프리다 칼로",
            "field": "화가",
            "desc": "강렬한 자기표현으로 유명한 멕시코 초현실주의 화가 🎨",
            "emoji": "🎨",
        },
        {
            "name": "50 센트",
            "field": "래퍼",
            "desc": "‘In Da Club’으로 유명한 미국 래퍼 💿",
            "emoji": "🎧",
        },
        {
            "name": "제14대 달라이 라마",
            "field": "종교 지도자",
            "desc": "세계 평화와 자비를 강조해 온 티베트 불교 지도자 🕊️",
            "emoji": "🕊️",
        },
    ],
    # 1월 15일
    (1, 15): [
        {
            "name": "마틴 루터 킹 주니어",
            "field": "인권운동가",
            "desc": "“I Have a Dream” 연설로 유명한 미국 흑인 인권운동가 ✊",
            "emoji": "✊",
        },
        {
            "name": "피트불",
            "field": "뮤지션",
            "desc": "‘Mr. Worldwide’로 불리는 글로벌 팝·힙합 아티스트 🌍",
            "emoji": "🎶",
        },
        {
            "name": "드루 브리스",
            "field": "미식축구 선수",
            "desc": "NFL 전설적인 쿼터백 중 한 명 🏈",
            "emoji": "🏈",
        },
    ],
    # 9월 5일
    (9, 5): [
        {
            "name": "프레디 머큐리",
            "field": "가수",
            "desc": "퀸(Queen)의 폭발적인 보컬, 록의 아이콘 🎤",
            "emoji": "🎤",
        },
        {
            "name": "마이클 키튼",
            "field": "배우",
            "desc": "<배트맨>, <버드맨>으로 잘 알려진 명배우 🦇",
            "emoji": "🎬",
        },
        {
            "name": "로즈 맥고완",
            "field": "배우",
            "desc": "영화·드라마로 활동하며 사회운동에도 참여한 배우 💬",
            "emoji": "🎭",
        },
    ],
    # 12월 25일
    (12, 25): [
        {
            "name": "아이작 뉴턴",
            "field": "물리학자",
            "desc": "고전역학의 기초를 세운 과학 혁명의 주역 🍎",
            "emoji": "📐",
        },
        {
            "name": "험프리 보가트",
            "field": "배우",
            "desc": "<카사블랑카>로 유명한 고전 헐리우드 스타 🎞️",
            "emoji": "🎞️",
        },
        {
            "name": "애니 레녹스",
            "field": "가수",
            "desc": "유리스믹스(Eurythmics)의 보컬이자 솔로 아티스트 🎙️",
            "emoji": "🎙️",
        },
    ],
}

EXAMPLE_DATES = [
    date(2025, 1, 15),
    date(2025, 2, 11),
    date(2025, 3, 14),
    date(2025, 6, 18),
    date(2025, 7, 6),
    date(2025, 9, 5),
    date(2025, 12, 25),
]

# ---------------- 상단 제목 & 설명 ----------------
st.markdown(
    """
    <h1 style="text-align:center; margin-bottom:0.5rem;">
        🎂 2025 나와 같은 생일 유명인 찾기
    </h1>
    <p style="text-align:center; color:#666; font-size:0.95rem;">
        2025년 달력에서 날짜를 하나 고르면,<br>
        그 날짜에 태어난 세계적인 유명인 3명을 깔끔하게 보여드려요 ✨
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("")

# ---------------- 날짜 선택 위젯 ----------------
st.markdown("### 📅 2025년에서 날짜를 골라보세요")

selected_date = st.date_input(
    "날짜 선택",
    value=date(2025, 1, 1),
    min_value=date(2025, 1, 1),
    max_value=date(2025, 12, 31),
)

month_day = (selected_date.month, selected_date.day)
people = BIRTHDAYS.get(month_day)

st.write("")

# ---------------- 결과 출력 ----------------
if people:
    st.markdown(
        f"""
        <h3 style="margin-top:0.5rem;">
            🌟 {selected_date.strftime('%Y년 %m월 %d일')}에 태어난 유명인 3명
        </h3>
        """,
        unsafe_allow_html=True,
    )

    for idx, p in enumerate(people, start=1):
        st.markdown(
            f"""
            <div style="
                padding:1rem 1.1rem;
                border-radius:1rem;
                border:1px solid #eee;
                margin-bottom:0.7rem;
                background:linear-gradient(135deg, #ffffff, #f9fafb);
                box-shadow:0 4px 10px rgba(0,0,0,0.03);
            ">
                <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.3rem;">
                    <span style="font-size:1.5rem;">{p['emoji']}</span>
                    <h4 style="margin:0; font-size:1.05rem;">
                        #{idx} {p['name']}
                    </h4>
                </div>
                <p style="margin:0.1rem 0; color:#555;">
                    <b>분야</b> · {p['field']}
                </p>
                <p style="margin:0.2rem 0 0; color:#777; font-size:0.9rem;">
                    {p['desc']}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

else:
    st.markdown(
        f"""
        <div style="
            padding:1rem 1.1rem;
            border-radius:1rem;
            border:1px solid #e5e7eb;
            background-color:#f9fafb;
            margin-top:0.5rem;
        ">
            <p style="margin:0; color:#555;">
                아직 <b>{selected_date.strftime('%m월 %d일')}</b>에 대한 데이터가 준비되지 않았어요 😢<br>
                아래 예시 날짜들 중 하나를 선택해 보거나,<br>
                코드를 수정해서 더 많은 유명인을 직접 추가해 보세요!
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------- 예시 날짜 버튼 ----------------
st.markdown("#### 💡 예시로 눌러볼 만한 날짜들")

cols = st.columns(len(EXAMPLE_DATES))

for col, d in zip(cols, EXAMPLE_DATES):
    with col:
        st.markdown(
            f"""
            <div style="
                text-align:center;
                padding:0.4rem 0.2rem;
                border-radius:999px;
                border:1px solid #e5e7eb;
                font-size:0.8rem;
                background-color:#ffffff;
                ">
                {d.strftime('%m/%d')}
            </div>
            """,
            unsafe_allow_html=True,
        )

st.caption("✏️ *BIRTHDAYS 딕셔너리에 (월, 일)을 키로 해서 인물을 계속 추가하면 완성도를 높일 수 있어요!*")
