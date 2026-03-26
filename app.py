import streamlit as st

st.set_page_config(
    page_title="仙逆入门",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


st.title("仙逆 入门演示")
st.header("仙逆 一级标题")
st.subheader("仙逆 二级标题")

st.write("动画版《仙逆》自2023年9月25日在腾讯视频开播以来，凭借电影级的画面质感、快节奏的叙事和精准的人物情感刻画，获得了极高的人气，被誉为国漫新标杆。")
st.write("播出信息：第一季（含年番）共128集，续作年番2已于2025年2月24日播出。")
st.write("口碑数据：腾讯视频站内评分高达9.2分，年番2豆瓣评分8.9分")
st.write("奖项荣誉：获得了“2025中国网络视听金橙指数年度网络动画片”奖项")
st.write("动画中最让观众津津乐道的，是主角王林在残酷修真世界中展现的杀伐果断与至情至性。他与李慕婉之间“我颠覆了整个苍穹，只为了那天，遮不住你要睁开的双眼”的深刻情感，更是贯穿全剧的灵魂所在。")
st.write("——————————————————————————————————————————————————————————————————————————————————————————————————————")

st.image("tu2.jpg", caption="仙逆 海报")
st.video("lixin.mp4")





people={
    "人物":["王林","李慕婉"],
    "身份":["主角","主角老婆"]
}

st.table(people)

















