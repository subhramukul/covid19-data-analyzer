

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def plot_daily_cases(df, metric="new_cases"):
    """Line chart of daily cases/deaths with 7-day rolling average."""
    label_map = {
        "new_cases": "Daily New Cases",
        "new_deaths": "Daily New Deaths",
        "total_cases": "Total Cases",
        "total_deaths": "Total Deaths"
    }
    fig = px.line(
        df,
        x="date",
        y=metric,
        color="location",
        title=f"{label_map.get(metric, metric)} Over Time",
        labels={"date": "Date", metric: label_map.get(metric, metric), "location": "Country"},
        template="plotly_dark"
    )
    fig.update_traces(line=dict(width=2))
    fig.update_layout(
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig


def plot_vaccination(df):
    """Bar chart comparing vaccination progress across countries."""
    latest = df.groupby("location").apply(
        lambda x: x.sort_values("date").iloc[-1]
    ).reset_index(drop=True)

    latest = latest[latest["people_vaccinated"] > 0].sort_values(
        "people_vaccinated", ascending=False
    ).head(20)

    fig = px.bar(
        latest,
        x="location",
        y="people_vaccinated",
        title="💉 People Vaccinated by Country (Top 20)",
        labels={"location": "Country", "people_vaccinated": "People Vaccinated"},
        color="people_vaccinated",
        color_continuous_scale="Teal",
        template="plotly_dark"
    )
    fig.update_layout(xaxis_tickangle=-45, showlegend=False)
    return fig


def plot_choropleth(df):
    """Choropleth world map of total confirmed cases."""
    latest = df.groupby("location").apply(
        lambda x: x.sort_values("date").iloc[-1]
    ).reset_index(drop=True)

    fig = px.choropleth(
        latest,
        locations="iso_code",
        color="total_cases",
        hover_name="location",
        color_continuous_scale="Reds",
        title="🗺️ Global Total Confirmed Cases",
        template="plotly_dark"
    )
    fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
    return fig
