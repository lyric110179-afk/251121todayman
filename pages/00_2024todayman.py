import streamlit as st
import random   # 🔥 반드시 필요! (NameError 해결)

# ---------------------------------------------------
# 12개월 데이터 (한국인/세계/과학자 분류 포함)
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
        {"name": "찰스 다윈", "field": "생물학자 🐢", "desc": "자연선택 진화론 창시.",
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
        {"name": "레이디 가가", "field": "가수 🎤", "desc": "폐쇄적 음악 세계 구축.",
         "nationality": "world", "category": "entertainer"},
    ],
    4: [
        {"name": "레오나르도 다빈치", "field": "예술가 🖼️", "desc": "르네상스의 천재.",
         "nationality": "world", "category": "artist"},
        {"name": "찰리 채플린", "field": "영화인 🎬", "desc": "영화 역사상 가장 위대한 희극인.",
         "nationality": "world", "category": "entertainer"},
        {"name": "엘렌 드제너러스", "field": "방송인 🎙️", "desc": "유명 토크쇼 진행자.",
         "nationality": "world", "category": "entertainer"},
    ],
    5: [
        {"name": "오드리 헵번", "field": "배우 🌸", "desc": "로마의 휴일 주연.",
         "nationality": "world", "category": "entertainer"},
        {"name": "조지 클루니", "field": "배우 🎬", "desc": "오스카 수상 배우.",
         "nationality": "world", "category": "entertainer"},
        {"name": "마크 저커버그", "field": "기업가 💻", "desc": "페이스북 창업자.",
         "nationality": "world", "category": "tech"},
    ],
    6: [
        {"name": "마릴린 먼로", "field": "배우 🎬", "desc": "헐리우드의 전설.",
         "nationality": "world", "category": "entertainer"},
        {"name": "모건 프리먼", "field": "배우 🎞️", "desc": "중후한 목소리의 명배우.",
         "nationality": "world", "category": "entertainer"},
        {"name": "톰 홀랜드", "field": "배우 🕷️", "desc": "스파이더맨 배우.",
         "nationality": "world", "category": "entertainer"},
    ],
    7: [
        {"name": "프리다 칼로", "field": "화가 🎨", "desc": "자전적 상징주의 화가.",
         "nationality": "world", "category": "artist"},
        {"name": "달라이 라마", "field": "지도자 ☸️", "desc": "평화와 자비의 지도자.",
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
        {"name": "정국 (BTS)", "field": "가수 🎤", "desc": "세계적 K-Pop 아이돌.",
         "nationality": "korea", "category": "entertainer"},
        {"name": "젠데이아", "field": "배우 🎬", "desc": "스파이더맨 주연 배우.",
         "nationality": "world", "category": "entertainer"},
        {"name": "비욘세", "field": "가수 👑", "desc": "팝·R&B의 여왕.",
         "nationality": "world", "category": "entertainer"},
    ],
    10: [
        {"name": "말라라 유사프자이", "field": "교육활동가 ✏️", "desc": "최연소 노벨평화상 수상자.",
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

st.title("🌟 2024년 탄생 별 찾기 + 필터 🌟")
st.write("달과 필터를 선택하면 조건에 맞는 **유명인 3명**을 보여줘요!")

month = st.selectbox("📅 월 선택", range(1, 13), format_func=lambda x: f"{x}월")

filter_option = st.radio(
    "🔎 필터 선택",
    ["전체", "한국인만", "전 세계 유명인”, “과학자만"],
    horizontal=True
)

st.markdown("---")

people = FAMOUS_BY_MONTH[month]

# ----------------------------
# 필터 적용
# ----------------------------
if filter_option == "한국인만":
    people = [p for p in people if p["nationality"] == "korea"]

elif filter_option == "전 세계 유명인":
    people = [p for p in people if p["nationality"] == "world"]

elif filter_option == "과학자만":
    people = [p for p in people if p["category"] == "scientist"]


# 3명 미만이면 부족한 만큼 같은 달에서 랜덤 보충
if len(people) < 3:
    remain = 3 - len(people)
    candidates = [p for p in FAMOUS_BY_MONTH[month] if p not in people]

    if len(candidates) >= remain:
        people += random.sample(candidates, remain)
    else:
        people += candidates  # 남은 수만큼만 보충


# ----------------------------
# 출력
# ----------------------------
st.write(f"🎉 **{month}월 – '{filter_option}' 결과입니다!**")

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
            <div style="font-size:1.1rem; font-weight:700;">{p['name']}</div>
            <div style="color:#777; font-size:0.9rem; margin-bottom:0.3rem;">{p['field']}</div>
            <div style="font-size:0.9rem; line-height:1.35;">{p['desc']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
