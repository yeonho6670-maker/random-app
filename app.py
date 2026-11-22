import random
import streamlit as st

# 웹 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

# 제목 및 안내 문구
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("무엇을 먹을지 고민된다면 아래 버튼을 눌러 메뉴를 뽑아보세요!")

# 추천할 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
menus = [
    "김치찌개 🍲",
    "돈까스 🍛",
    "제육볶음 🥓",
    "초밥 🍣",
    "파스타 🍝",
    "햄버거 🍔",
    "쌀국수 🍜",
    "비빔밥 🥗",
    "짜장면 & 탕수육 🥢",
    "떡볶이 & 튀김 🍢",
    "순대국밥 🥣",
    "샌드위치 & 샐러드 🥪",
    "마라탕 🌶️",
    "치킨마요 덮밥 🍗",
]

st.divider()

# 버튼을 누르면 실행되는 로직
if st.button("🎲 점심 메뉴 뽑기!", type="primary", use_container_width=True):
    selected_menu = random.choice(menus)
    st.success(f"오늘의 추천 점심 메뉴는 **{selected_menu}** 입니다!")
    st.balloons()
