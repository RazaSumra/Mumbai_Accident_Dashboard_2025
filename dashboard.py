import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page config ---
st.set_page_config(layout="wide", page_title="Mumbai 2025 Accidents", initial_sidebar_state="expanded")

# --- Load CSV data ---
@st.cache_data
def load_data():
    return pd.read_csv("mumbai_accidents_2025.csv")  # 🟢 CSV file ka naam sahi se daalna

df = load_data()

# --- Sidebar Filters ---
st.sidebar.title("🔍 Filters")
area = st.sidebar.selectbox("Select Area", ["All"] + sorted(df["Area"].unique()))
vehicle = st.sidebar.selectbox("Select Vehicle", ["All"] + sorted(df["Vehicle_Type"].unique()))

# --- Filtered Data ---
filtered_df = df.copy()
if area != "All":
    filtered_df = filtered_df[filtered_df["Area"] == area]
if vehicle != "All":
    filtered_df = filtered_df[filtered_df["Vehicle_Type"] == vehicle]

# --- Main Dashboard ---
st.title("🚦 Mumbai Road Accident Dashboard - 2025")
st.markdown("### A glance into area-wise and vehicle-wise accident patterns")

# --- Metrics ---
col1, col2 = st.columns(2)
col1.metric("📌 Total Accidents", int(filtered_df["Accidents_Reported"].sum()))
col2.metric("📍 Unique Areas", filtered_df["Area"].nunique())

# --- Chart 1: Accidents by Reason ---
st.markdown("## 📊 Accidents by Reason")
fig1 = px.bar(filtered_df, x="Reason", y="Accidents_Reported", color="Vehicle_Type", template="plotly_dark")
st.plotly_chart(fig1, use_container_width=True)

# --- Chart 2: Vehicle-wise Accidents per Area ---
st.markdown("## 🚗 Vehicle-Wise Accidents per Area")
fig2 = px.bar(filtered_df, x="Area", y="Accidents_Reported", color="Vehicle_Type", barmode="group", template="plotly_dark")
st.plotly_chart(fig2, use_container_width=True)

# --- Data Table ---
st.markdown("## 📋 Filtered Data Table")
st.dataframe(filtered_df)
