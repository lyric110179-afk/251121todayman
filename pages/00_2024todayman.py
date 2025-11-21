import streamlit as st
import random

# ---------------------------------------------------
# 12개월 모두 3명씩 유명인 데이터 완전 채움
# ---------------------------------------------------
FAMOUS_BY_MONTH = {
    1: [
        {"name": "마틴 루서 킹 주니어", "field": "인권운동가 ✊", "desc": "흑인 민권운동의 상징적 지도자."},
        {"name": "스티븐 호킹", "field": "물리학자 🧠", "desc": "블랙홀·우주론 연구의 선구자."},
        {"name": "엘비스 프레슬리", "field": "가수 🎤", "desc": "로큰롤의 황제."},
    ],
    2: [
        {"name": "찰스 다윈", "field": "생물학자 🐢", "desc": "자연선택 진화론 제시."},
        {"name": "에이브러햄 링컨", "field": "정치가 🇺🇸", "desc": "미국 16대 대통령, 노예제 폐지."},
        {"name": "슈베르트", "field": "작곡가 🎼", "desc": "낭만주의 음악의 선구자."},
    ],
    3: [
        {"name": "알베르트 아인슈타인", "field": "물리학자 ⚛️", "desc": "상대성이론 창시자."},
        {"name": "빈센트 반 고흐", "field": "화가 🎨", "desc": "후기 인상주의 대표 화가."},
        {"name": "레이디 가가", "field": "가수 🎤", "desc": "세계적 팝 아이콘."},
    ],
    4: [
        {"name": "레오나르도 다빈치", "field": "예술가 🖼️", "desc": "모나리자·최후의 만찬 작가."},
        {"name": "찰리 채플린", "field": "영화인 🎬", "desc": "영화 역사상 가장 영향력 있는 희극인."},
        {"name": "엘렌 드제너러스", "field": "방송인 🎙️", "desc": "토크쇼 진행자."},
    ],
    5: [
        {"name": "오드리 헵번", "field": "배우 🌸", "desc": "로마의 휴일의 주인공."},
        {"name": "조지 클루니", "field": "배우 🎬", "desc": "할리우드 스타 배우."},
        {"name": "마크 저커버그", "field": "기업가 💻", "desc": "페이스북 공동창업자."},
    ],
    6: [
        {"name": "마릴린 먼로", "field": "배우 🎬", "desc": "헐리우드의 상징."},
        {"name": "모건 프리먼", "field": "배우 🎞️", "desc": "중후한 목소리의 명배우."},
        {"name": "톰 홀랜드", "field": "배우 🕷️", "desc": "스파이더맨 배우."},
    ],
    7: [
        {"name": "프리다 칼로", "field": "화가 🎨", "desc": "멕시코의 상징적 화가."},
        {"name": "달라이 라마", "field": "지도자 ☸️", "desc": "평화·자비의 메시지를 전하는 지도자."},
        {"name": "50 센트", "field": "래퍼 🎧", "desc": "미국 힙합 아티스트."},
    ],
    8: [
        {"name": "버락 오바마", "field": "정치가 🌍", "desc": "미국 44대 대통령."},
        {"name": "루이 암스트롱", "field": "뮤지션 🎺", "desc": "재즈의 전설적 인물."},
        {"name": "메건 마클", "field": "배우 👑", "desc": "영국 왕실 출신 배우."},
    ],
    9: [
        {"name": "정국(BTS)", "field": "가수 🎤", "desc": "세계적인 K-POP 아티스트."},
        {"name": "젠데이아", "field": "배우 🎬", "desc": "스파이더맨·유포리아 주연."},
        {"name": "비욘세", "field": "가수 👑", "desc": "팝·R&B의 여왕."},
    ],
    10: [
        {"name": "말라라 유사프자이", "field": "교육운동가 ✏️", "desc": "최연소 노벨평화상 수상자."},
        {"name": "파블로 피카소", "field": "화가 🎨", "desc": "입체파의 창시자."},
        {"name": "카말라 해리스", "field": "정치가 🇺🇸", "desc": "미국 최초 여성 부통령."},
    ],
    11: [
        {"name": "마리 퀴리", "field": "과학자 🧪", "desc": "노벨상 2회 수상자."},
        {"name": "데이비드 게타", "field": "DJ 🎧", "desc": "세계적인 EDM 프로듀서."},
        {"name": "라이언 고슬링", "field": "배우 🎬", "desc": "라라랜드의 주연 배우."},
    ],
    12: [
        {"name": "아이작 뉴턴", "field": "물리학자 ⚖️", "desc": "고전역학의 창시자."},
        {"name": "테일러 스위프트", "field": "가수 🎤", "desc": "세계적 싱어송라이터."},
        {"name": "김연아", "field": "피겨스케이터 ⛸️", "desc": "대한민국의 피겨 영웅."},
    ],
}

# ---------------------------------------------------
# UI 구성
# ---------------------------------------------------
st.title("🌟 2024년 탄생 별 찾기 ⭐")
st.write("12개월 중 하나를 선택하면, 그 달에 태어난 **유명인 3명**을 소개해드릴게요!✨")

month = st.selectbox("📅 월을 선택하세요", list(range(1, 13)), format_func=lambda x: f"{x}월")

st.markdown("---")

people = FAMOUS_BY_MONTH.get(month)

st.write(f"🎉 **{month}월에 태어난 유명인 3명입니다!**")

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
