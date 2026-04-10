"""
Iris Species Explorer — Streamlit Dashboard
============================================
An interactive dashboard for exploring the classic Iris dataset.

Charts
------
- Scatter plot  : sepal length vs width, coloured by species
- Histogram     : sepal length distribution per species
- Cumulative histogram : sepal length cumulative distribution
- Pie charts    : species share by count, petal length, and petal width
- Summary table : descriptive statistics for all numeric columns

Sidebar filters
---------------
- Species multi-select
- Sepal length range slider
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# ── Page configuration ───────────────────────────────────────────────────
st.set_page_config(
    layout="wide",
    page_icon=":bar_chart:",
    page_title="Iris Explorer",
    initial_sidebar_state="expanded",
)

# ── Load data ─────────────────────────────────────────────────────────
@st.cache_data
def load_data() -> pd.DataFrame:
    """Read the Iris CSV and return a cleaned DataFrame."""
    return pd.read_csv("iris.csv")

df_raw = load_data()

# ── Sidebar filters ──────────────────────────────────────────────────
st.sidebar.header("Filters")

all_species = sorted(df_raw["species"].unique())
selected_species = st.sidebar.multiselect(
    "Species",
    options=all_species,
    default=all_species,
)

min_sl, max_sl = float(df_raw["sepal_length"].min()), float(df_raw["sepal_length"].max())
sepal_range = st.sidebar.slider(
    "Sepal Length range",
    min_value=min_sl,
    max_value=max_sl,
    value=(min_sl, max_sl),
    step=0.1,
)

df = df_raw[
    df_raw["species"].isin(selected_species)
    & df_raw["sepal_length"].between(*sepal_range)
].copy()

if df.empty:
    st.warning("No data matches the current filters. Adjust the sidebar options.")
    st.stop()

# ── Dashboard title ───────────────────────────────────────────────────
st.title(":bar_chart: Iris Species Explorer")
st.caption(f"Showing **{len(df):,}** of **{len(df_raw):,}** records")

st.divider()

# ── Row 1: Scatter ──────────────────────────────────────────────────────
st.subheader("Sepal Dimensions")
st.plotly_chart(
    px.scatter(
        data_frame=df,
        x="sepal_length",
        y="sepal_width",
        color="species",
        title="Sepal Length vs Sepal Width",
        labels={"sepal_length": "Sepal Length (cm)", "sepal_width": "Sepal Width (cm)"},
    ),
    use_container_width=True,
)

st.divider()

# ── Row 2: Histograms ───────────────────────────────────────────────────
st.subheader("Sepal Length Distribution")
col_hist, col_cum = st.columns(2)

with col_hist:
    st.plotly_chart(
        px.histogram(
            data_frame=df,
            x="sepal_length",
            nbins=30,
            color="species",
            text_auto=True,
            title="Sepal Length — Frequency",
            labels={"sepal_length": "Sepal Length (cm)", "count": "Count"},
        ),
        use_container_width=True,
    )

with col_cum:
    st.plotly_chart(
        px.histogram(
            data_frame=df,
            x="sepal_length",
            nbins=30,
            color="species",
            cumulative=True,
            title="Sepal Length — Cumulative",
            labels={"sepal_length": "Sepal Length (cm)", "count": "Cumulative Count"},
        ),
        use_container_width=True,
    )

st.divider()

# ── Row 3: Pie charts ───────────────────────────────────────────────────
st.subheader("Species Composition")
col1, col2, col3 = st.columns(3)

with col1:
    st.plotly_chart(
        px.pie(
            data_frame=df,
            names="species",
            title="Share by Count",
        ),
        use_container_width=True,
    )

with col2:
    st.plotly_chart(
        px.pie(
            data_frame=df,
            names="species",
            values="petal_length",
            title="Share by Petal Length",
        ),
        use_container_width=True,
    )

with col3:
    st.plotly_chart(
        px.pie(
            data_frame=df,
            names="species",
            values="petal_width",
            title="Share by Petal Width",
        ),
        use_container_width=True,
    )

st.divider()

# ── Row 4: Summary statistics ─────────────────────────────────────────────────
st.subheader("Descriptive Statistics")
st.dataframe(df.describe().T.style.format("{:.2f}"), use_container_width=True)
