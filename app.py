import streamlit as st
import pandas as pd

from charts import *
from filters import *

# PAGE CONFIG

st.set_page_config(
    page_title="Digit Dashboard",
    layout="wide"
)

# PREMIUM THEME

st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {

    background: linear-gradient(
        135deg,
        #0F172A,
        #111827,
        #1E293B
    );
}

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #0F172A,
        #111827
    );

    border-right: 2px solid #334155;
}

/* KPI CARDS */

div[data-testid="metric-container"] {

    background: linear-gradient(
        135deg,
        #0284C7,
        #0369A1
    );

    padding: 22px;

    border-radius: 22px;

    border: 2px solid #38BDF8;

    box-shadow: 0px 0px 12px rgba(56,189,248,0.30);
}

/* KPI LABEL */

div[data-testid="metric-container"] label {

    color: white !important;

    font-size: 22px !important;

    font-weight: bold !important;
}

/* KPI VALUE */

div[data-testid="metric-container"] [data-testid="stMetricValue"] {

    color: #E0F2FE !important;

    font-size: 42px !important;

    font-weight: bold !important;
}

/* TABLE */

[data-testid="stDataFrame"] {

    border-radius: 15px;

    overflow: hidden;

    border: 1px solid #334155;
}

/* SUBHEADERS */

h3 {

    color: #7DD3FC !important;

    font-weight: 700 !important;
}

</style>
""", unsafe_allow_html=True)

# LOAD DATA

try:

    df = pd.read_csv("optdigits.csv")

except:

    try:

        df = pd.read_excel(
            "optdigits.xlsx",
            engine="openpyxl"
        )

    except Exception as e:

        st.error(f"Dataset Error: {e}")

        st.stop()

# AUTO COLUMN NAMES

if "digit" not in df.columns:

    total_cols = len(df.columns)

    pixel_cols = [
        f"pixel_{i}"
        for i in range(total_cols - 1)
    ]

    df.columns = pixel_cols + ["digit"]

# MAIN TITLE

st.markdown("""
<h1 style='
font-size:60px;
color:#7DD3FC;
font-weight:800;
text-shadow: 0px 0px 5px rgba(125,211,252,0.5);
margin-bottom:0px;
'>
🔢 Digit Recognition Dashboard
</h1>
""", unsafe_allow_html=True)

# SUBTITLE

st.markdown("""
<p style='
font-size:22px;
color:#CBD5E1;
margin-top:0px;
'>
Professional Machine Learning Data Visualization Dashboard
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# FILTERS

df = sidebar_filters(df)

# KPI SECTION

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Records",
    len(df)
)

col2.metric(
    "Unique Digits",
    df["digit"].nunique()
)

col3.metric(
    "Avg Pixel 0",
    round(df["pixel_0"].mean(),2)
)

col4.metric(
    "Avg Pixel 1",
    round(df["pixel_1"].mean(),2)
)

st.markdown("---")

# DATASET

st.subheader("📊 Dataset Preview")

st.dataframe(
    df,
    use_container_width=True
)

st.markdown("---")

# DEFAULT CHARTS

col5, col6 = st.columns(2)

with col5:

    st.subheader("📈 Bar Chart")

    bar_chart(df)

with col6:

    st.subheader("🥧 Pie Chart")

    pie_chart(df)

st.markdown("---")
# EXTRA CHARTS

chart_options = st.sidebar.multiselect(
    "Select Additional Charts",
    [
        "All Charts",
        "Histogram",
        "Box Plot",
        "Heatmap",
        "Area Chart",
        "Count Plot",
        "Violin Plot"
    ]
)

if "All Charts" in chart_options:

    chart_options = [
        "Histogram",
        "Box Plot",
        "Heatmap",
        "Area Chart",
        "Count Plot",
        "Violin Plot"
    ]

for chart in chart_options:

    st.markdown("---")

    if chart == "Histogram":

        st.subheader("📊 Histogram")

        histogram(df)

    elif chart == "Box Plot":

        st.subheader("📦 Box Plot")

        box_plot(df)

    elif chart == "Heatmap":

        st.subheader("🔥 Heatmap")

        heatmap(df)

    elif chart == "Area Chart":

        st.subheader("🌊 Area Chart")

        area_chart(df)

    elif chart == "Count Plot":

        st.subheader("📌 Count Plot")

        count_plot(df)

    elif chart == "Violin Plot":

        st.subheader("🎻 Violin Plot")

        violin_plot(df)