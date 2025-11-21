import datetime
import json
import urllib.request
import urllib.error

import streamlit as st


# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="내 생일과 같은 날 태어난 유명인 ✨",
    page_icon="🎂",
    layout="centered",
)

st.title("🎂 내 생일과 같은 날 태어난 유명인 찾기")
st.caption("2024년 달력에서 날짜를 고르면, 그 날짜에 태어난 전 세계 유명인을 3명 추천해 줄게요. 🌍")

st.markdown(
    """
    <style>
    /* 전체 배경과 카드 느낌 */
    .birthday-card {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 18px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 0.8rem;
        border: 1px solid rgba(0,0,0,0.04);
        transition: all 0.18s ease-in-out;
    }
    .birthday-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.12);
        border-color: rgba(59,130,246,0.35);
    }
    .birthday-name {
        font-size: 1.1rem;
        font-weight: 700;
    }
    .birthday-meta {
        font-size: 0.9rem;
        color: #64748b;
    }
    .birthday-desc {
        font-size: 0.95rem;
        margin-top: 0.35rem;
    }
    .pill {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        border-radius: 999px;
        padding: 0.2rem 0.7rem;
        background: rgba(59,130,246,0.06);
        color: #1d4ed8;
        font-size: 0.78rem;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================
# 위키피디아 API에서 생일 정보 가져오기
# =========================
def fetch_birthdays(selected_date: datetime.date):
    """선택한 날짜(월/일)에 태어난 유명인 목록을 위키피디아에서 가져옵니다."""
    month = f"{selected_date.month:02d}"
    day = f"{selected_date.day:02d}"

    # 공개 REST 엔드포인트 (별도 API 키 X)
    url = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/births/{month}/{day}"

    headers = {
        # User-Agent는 위키미디어 권장사항 (본인 이메일/사이트로 바꿔도 좋습니다)
        "User-Agent": "BirthdayStreamlitApp/1.0 (contact@example.com)"
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        st.error("⚠️ 위키백과 서버와 통신하는 동안 오류가 발생했어요. 잠시 후 다시 시도해 주세요.")
        st.caption(f"에러 메시지: {e}")
        return []
    except Exception as e:
        st.error("⚠️ 알 수 없는 오류가 발생했어요.")
        st.caption(f"에러 메시지: {e}")
        return []

    births = data.get("births", [])

    if not births:
        return []

    # 최근(가장 최신 연도) 인물 순으로 정렬
    births_sorted = sorted(births, key=lambda x: x.get("year", 0), reverse=True)
    return births_sorted


def extract_person_info(birth_entry):
    """위키피디아 birth 엔트리에서 이름, 연도, 설명, 링크를 뽑아줍니다."""
    year = birth_entry.get("year", None)
    pages = birth_entry.get("pages", [])
    page = pages[0] if pages else {}

    # 이름 후보들 중 하나 사용
    name = (
        page.get("normalizedtitle")
        or page.get("displaytitle")
        or page.get("title")
        or "이름 정보 없음"
    )

    description = (
        page.get("description")
        or page.get("extract")
        or birth_entry.get("text")
        or ""
    )

    # 데스크톱용 위키 링크
    content_urls = page.get("content_urls", {})
    desktop = content_urls.get("desktop", {})
    page_url = desktop.get("page")

    return {
        "name": name,
        "year": year,
        "description": description,
        "url": page_url,
    }


# =========================
# 날짜 입력 UI
# =========================
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("📅 2024년 중에서 날짜를 선택해 보세요")

with col2:
    st.write("")  # spacing
    st.write("")

today = datetime.date.today()
default_date = (
    today if today.year == 2024 else datetime.date(2024, 1, 1)
)

selected_date = st.date_input(
    "2024년 달력",
    value=default_date,
    min_value=datetime.date(2024, 1, 1),
    max_value=datetime.date(2024, 12, 31),
)

st.markdown("---")

# =========================
# 결과 영역
# =========================
if selected_date:
    st.markdown(
        f"### ✨ {selected_date.strftime('%Y년 %m월 %d일')}에 태어난 유명인 3명"
    )
    st.caption("날짜는 2024년이지만, **같은 월·일에 태어난 역사 속 인물들**을 찾아와요. 🎈")

    birthdays = fetch_birthdays(selected_date)

    if not birthdays:
        st.warning("이 날짜에 대한 정보를 찾지 못했어요. 다른 날짜도 한 번 선택해 볼까요? 🙂")
    else:
        # 상위 3명만 사용
        top_3 = birthdays[:3]

        for i, birth in enumerate(top_3, start=1):
            person = extract_person_info(birth)

            name = person["name"]
            year = person["year"]
            description = person["description"]
            url = person["url"]

            # 이모티콘 스타일
            icon = "🌟" if i == 1 else ("💫" if i == 2 else "⭐")

            st.markdown(
                f"""
                <div class="birthday-card">
                    <div class="birthday-meta">
                        <span class="pill">{icon} #{i} 추천 인물</span>
                    </div>
                    <div class="birthday-name" style="margin-top: 0.4rem;">
                        {name}
                    </div>
                    <div class="birthday-meta">
                        🗓️ 태어난 해: {year if year else "정보 없음"}
                    </div>
                    <div class="birthday-desc">
                        {description if description else "설명 정보가 없어요. 위키백과 페이지에서 더 확인해 보세요!"}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if url:
                st.markdown(
                    f"[🔎 위키백과에서 더 자세히 보기]({url})",
                    unsafe_allow_html=False,
                )

            st.markdown("")

        st.markdown("---")
        st.info(
            "💡 *Tip*: 여러 날짜를 눌러 보면서, 나와 같은 날 태어난 사람들뿐 아니라 "
            "세계 곳곳에서 어떤 인물들이 같은 날 태어났는지 비교해 보는 것도 재미있어요!"
        )
