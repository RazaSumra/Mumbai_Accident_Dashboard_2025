import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="🚧 Mumbai Accidents 2025", layout="wide", initial_sidebar_state="expanded")

@st.cache_data
def load_data():
    return pd.read_csv("mumbai_accidents_2025.csv")

df = load_data()

st.markdown("""
    <style>
        body { background-color: #111; color: #fff; }
        .main { background: linear-gradient(to right, #232526, #414345); }
        .block-container { padding-top: 1rem; }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 🛣️🚗 *Mumbai Accident Dashboard 2025* 🚓🛵")
st.markdown("##### 'Visual insights into vehicle-wise road accidents across Mumbai'")
st.markdown("_")

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/201/201818.png", width=100)
st.sidebar.title("🎛️ Filter Panel")

area = st.sidebar.selectbox("📍 Select Area", ["All"] + sorted(df["Area"].unique()))
vehicle = st.sidebar.selectbox("🚘 Select Vehicle", ["All"] + sorted(df["Vehicle_Type"].unique()))

filtered_df = df.copy()
if area != "All":
    filtered_df = filtered_df[filtered_df["Area"] == area]
if vehicle != "All":
    filtered_df = filtered_df[filtered_df["Vehicle_Type"] == vehicle]

col1, col2, col3 = st.columns(3)
col1.metric("🧾 Total Accidents", int(filtered_df["Accidents_Reported"].sum()))
col2.metric("📌 Areas Covered", filtered_df["Area"].nunique())
col3.metric("🛺 Vehicle Types", filtered_df["Vehicle_Type"].nunique())

st.markdown("_")

st.markdown("""
    <div style='text-align:center; font-size:25px; margin-bottom:20px;'>
        🚗 💥 🛵 💥 🚚 💥 🚓<br>
        <span style='font-size:18px;'>Analyzing patterns of road accidents — Let's reduce them together!</span>
    </div>
""", unsafe_allow_html=True)

st.markdown("## 📊 Accidents by Reason")
fig1 = px.bar(filtered_df, x="Reason", y="Accidents_Reported", color="Vehicle_Type", template="plotly_dark", title="Top Reasons of Accidents")
st.plotly_chart(fig1, use_container_width=True)

st.markdown("## 🛺 Vehicle-Wise Accidents by Area")
fig2 = px.bar(filtered_df, x="Area", y="Accidents_Reported", color="Vehicle_Type", barmode="group", template="plotly_dark", title="Area-wise Vehicle Accident Distribution")
st.plotly_chart(fig2, use_container_width=True)

with st.expander("🔎 View Filtered Data Table"):
    st.dataframe(filtered_df)

st.markdown("""
    <hr style='border:1px solid #666;'>
    <div style='text-align:center; font-size:14px; color:#888;'>
        Dashboard by <b>Raza Sumra</b> 🚀 | Built with ❤️ using Streamlit
    </div>
""", unsafe_allow_html=True)
