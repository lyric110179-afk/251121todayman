import streamlit as st


# ---------------------------------------------------
# 데이터를 월별 + 필터 속성까지 포함해 구성
# 각 인물에 "nationality", "category" 컬럼 추가
# ---------------------------------------------------

FAMOUS_BY_MONTH = {
    1: [
        {"name": "마틴 루서 킹 주니어", "field": "인권운동가 ✊", "desc": "흑인 민권운동의 상징.", 
         "nationality": "world", "category": "activist"},
        {"name": "스티븐 호킹", "field": "물리학자 🧠", "desc": "블랙홀 연구의 선구자.",
         "nationality": "world", "category": "scientist"},
        {"name": "엘비스 프레슬리", "field": "가수 🎤", "desc": "로큰롤의 황제.",
         "nationality": "world", "category": "entertainer"},
    ],
    2: [
        {"name": "찰스 다윈", "field": "생물학자 🐢", "desc": "자연선택 진화론 제시.",
         "nationality": "world", "category": "scientist"},
        {"name": "에이브러햄 링컨", "field": "정치가 🇺🇸", "desc": "노예제 폐지 대통령.",
         "nationality": "world", "category": "politics"},
        {"name": "슈베르트", "field": "작곡가 🎼", "desc": "낭만주의 음악 선구자.",
         "nationality": "world", "category": "entertainer"},
    ],
    3: [
        {"name": "알베르트 아인슈타인", "field": "물리학자 ⚛️", "desc": "상대성이론 창시자.",
         "nationality": "world", "category": "scientist"},
        {"name": "빈센트 반 고흐", "field": "화가 🎨", "desc": "후기 인상주의 거장.",
         "nationality": "world", "category": "artist"},
        {"name": "레이디 가가", "field": "가수 🎤", "desc": "세계적인 팝 아이콘.",
         "nationality": "world", "category": "entertainer"},
    ],
    4: [
        {"name": "레오나르도 다빈치", "field": "예술가 🖼️", "desc": "르네상스 거장.",
         "nationality": "world", "category": "artist"},
        {"name": "찰리 채플린", "field": "영화인 🎬", "desc": "희극 영화의 전설.",
         "nationality": "world", "category": "entertainer"},
        {"name": "엘렌 드제너러스", "field": "방송인 🎙️", "desc": "유명 토크쇼 진행자.",
         "nationality": "world", "category": "entertainer"},
    ],
    5: [
        {"name": "오드리 헵번", "field": "배우 🌸", "desc": "로마의 휴일 주연.",
         "nationality": "world", "category": "entertainer"},
        {"name": "조지 클루니", "field": "배우 🎬", "desc": "헐리우드 스타.",
         "nationality": "world", "category": "entertainer"},
        {"name": "마크 저커버그", "field": "기업가 💻", "desc": "페이스북 창업자.",
         "nationality": "world", "category": "tech"},
    ],
    6: [
        {"name": "마릴린 먼로", "field": "배우 🎬", "desc": "헐리우드 상징.",
         "nationality": "world", "category": "entertainer"},
        {"name": "모건 프리먼", "field": "배우 🎞️", "desc": "중후한 명배우.",
         "nationality": "world", "category": "entertainer"},
        {"name": "톰 홀랜드", "field": "배우 🕷️", "desc": "스파이더맨 배우.",
         "nationality": "world", "category": "entertainer"},
    ],
    7: [
        {"name": "프리다 칼로", "field": "화가 🎨", "desc": "멕시코의 전설적 화가.",
         "nationality": "world", "category": "artist"},
        {"name": "달라이 라마", "field": "지도자 ☸️", "desc": "평화의 상징.",
         "nationality": "world", "category": "religion"},
        {"name": "50 센트", "field": "래퍼 🎧", "desc": "미국 힙합 아티스트.",
         "nationality": "world", "category": "entertainer"},
    ],
    8: [
        {"name": "버락 오바마", "field": "정치가 🌍", "desc": "미국 44대 대통령.",
         "nationality": "world", "category": "politics"},
        {"name": "루이 암스트롱", "field": "뮤지션 🎺", "desc": "재즈의 전설.",
         "nationality": "world", "category": "entertainer"},
        {"name": "메건 마클", "field": "배우 👑", "desc": "영국 왕실 출신 배우.",
         "nationality": "world", "category": "entertainer"},
    ],
    9: [
        {"name": "정국(BTS)", "field": "가수 🎤", "desc": "세계적 K-POP 스타.",
         "nationality": "korea", "category": "entertainer"},
        {"name": "젠데이아", "field": "배우 🎬", "desc": "스파이더맨 주연.",
         "nationality": "world", "category": "entertainer"},
        {"name": "비욘세", "field": "가수 👑", "desc": "팝·R&B의 여왕.",
         "nationality": "world", "category": "entertainer"},
    ],
    10: [
        {"name": "말라라 유사프자이", "field": "교육활동가 ✏️", "desc": "노벨평화상 최연소 수상자.",
         "nationality": "world", "category": "activist"},
        {"name": "파블로 피카소", "field": "화가 🎨", "desc": "입체파 창시자.",
         "nationality": "world", "category": "artist"},
        {"name": "카말라 해리스", "field": "정치가 🇺🇸", "desc": "미국 최초 여성 부통령.",
         "nationality": "world", "category": "politics"},
    ],
    11: [
        {"name": "마리 퀴리", "field": "과학자 🧪", "desc": "노벨상 2회 수상.",
         "nationality": "world", "category": "scientist"},
        {"name": "데이비드 게타", "field": "DJ 🎧", "desc": "EDM 프로듀서.",
         "nationality": "world", "category": "entertainer"},
        {"name": "라이언 고슬링", "field": "배우 🎬", "desc": "라라랜드 주연.",
         "nationality": "world", "category": "entertainer"},
    ],
    12: [
        {"name": "아이작 뉴턴", "field": "물리학자 ⚖️", "desc": "만유인력 법칙.",
         "nationality": "world", "category": "scientist"},
        {"name": "테일러 스위프트", "field": "가수 🎤", "desc": "세계적 싱어송라이터.",
         "nationality": "world", "category": "entertainer"},
        {"name": "김연아", "field": "피겨스케이터 ⛸️", "desc": "대한민국의 피겨 영웅.",
         "nationality": "korea", "category": "sports"},
    ],
}


# ---------------------------------------------------
# UI 구성
# ---------------------------------------------------

st.title("🌟 2024년 탄생 별 찾기 + 필터 ⭐")

st.write("**달을 선택하고, 필터를 선택하면 조건에 맞는 유명인 3명을 보여줘요!**")

# 월 선택
month = st.selectbox("📅 월 선택", list(range(1, 13)), format_func=lambda x: f"{x}월")

# 필터 선택
filter_option = st.radio(
    "🔎 필터 선택",
    ("전체", "한국인만", "전 세계 유명인", "과학자만"),
    horizontal=True
)

st.markdown("---")

# 선택된 달의 데이터 가져오기
people = FAMOUS_BY_MONTH[month]

# 필터 적용
if filter_option == "한국인만":
    people = [p for p in people if p["nationality"] == "korea"]

elif filter_option == "전 세계 유명인":
    people = [p for p in people if p["nationality"] == "world"]

elif filter_option == "과학자만":
    people = [p for p in people if p["category"] == "scientist"]

# 필터 후에도 3명이 보이도록 (필요 시 랜덤 보완)
if len(people) < 3:
    # 현재 달의 전체 데이터에서 부족한 만큼 랜덤 채우기
    remain = 3 - len(people)
    extra = random.sample(FAMOUS_BY_MONTH[month], remain)
    # 중복 방지
    for e in extra:
        if e not in people:
            people.append(e)

# ---------------------------------------------------
# 출력
# ---------------------------------------------------

st.write(f"🎉 **{month}월 – '{filter_option}' 필터 결과입니다.**")

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
