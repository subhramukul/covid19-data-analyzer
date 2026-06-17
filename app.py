import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data_loader import load_data, get_country_list
from visualizations import (
    plot_daily_cases,
    plot_vaccination,
    plot_choropleth
)

st.set_page_config(page_title="COVID-19 Data Analyzer", layout="wide")

st.title("🦠 COVID-19 Data Analyzer")
st.markdown("Real-time pandemic data analysis and visualization dashboard.")

# Load data
with st.spinner("Loading data..."):
    df = load_data()

countries = get_country_list(df)

# Sidebar filters
st.sidebar.header("🔍 Filters")
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=countries,
    default=["India", "United States", "United Kingdom"]
)

metric = st.sidebar.selectbox(
    "Select Metric",
    ["new_cases", "new_deaths", "total_cases", "total_deaths"]
)

# Filter data
filtered_df = df[df["location"].isin(selected_countries)]

# Layout
col1, col2, col3 = st.columns(3)

latest = df[df["location"] == "World"].sort_values("date").iloc[-1]
col1.metric("🌍 Total Cases (World)", f"{int(latest.get('total_cases', 0)):,}")
col2.metric("💀 Total Deaths (World)", f"{int(latest.get('total_deaths', 0)):,}")
col3.metric("💉 People Vaccinated", f"{int(latest.get('people_vaccinated', 0)):,}")

st.markdown("---")

# Charts
st.subheader("📈 Daily Trends")
st.plotly_chart(plot_daily_cases(filtered_df, metric), use_container_width=True)

st.subheader("💉 Vaccination Progress")
st.plotly_chart(plot_vaccination(filtered_df), use_container_width=True)

st.subheader("🗺️ Global Case Distribution")
st.plotly_chart(plot_choropleth(df), use_container_width=True)

st.markdown("---")
st.caption("Data Source: Our World in Data | disease.sh API")
