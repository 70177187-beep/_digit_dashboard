import streamlit as st

def sidebar_filters(df):

    st.sidebar.markdown("""
    <style>

    /* SIDEBAR */

    section[data-testid="stSidebar"] {

        background: linear-gradient(
            180deg,
            #0B1120 0%,
            #111827 100%
        );

        border-right: 2px solid #1E3A8A;
    }

    /* SIDEBAR CONTAINER */

    .sidebar-container {

        background: rgba(30, 41, 59, 0.65);

        padding: 20px;

        border-radius: 20px;

        border: 1px solid rgba(125,211,252,0.25);

        box-shadow: 0px 0px 18px rgba(125,211,252,0.10);

        margin-top: 10px;
    }

    /* SIDEBAR TITLE */

    .sidebar-title {

    color: #7DD3FC;

    font-size: 34px;

    font-weight: 800;

    line-height: 1.2;

    margin-bottom: 10px;

    text-shadow:
        0px 0px 5px rgba(125,211,252,0.9),
        0px 0px 12px rgba(56,189,248,0.8),
        0px 0px 22px rgba(56,189,248,0.5);
}

    /* SUBTITLE */

    .sidebar-subtitle {

        color: #CBD5E1;

        font-size: 14px;

        margin-bottom: 20px;
    }

    /* FILTER TITLE */

    .filter-title {

        color: white;

        font-size: 22px;

        font-weight: 700;

        margin-bottom: 18px;
    }

    /* MULTISELECT */

    div[data-baseweb="select"] {

        background-color: #0F172A !important;

        border-radius: 14px !important;

        border: 1px solid #38BDF8 !important;

        box-shadow: 0px 0px 10px rgba(56,189,248,0.15);
    }

    /* TEXT INPUT */

    .stTextInput input {

        background-color: #0F172A !important;

        color: white !important;

        border-radius: 12px !important;

        border: 1px solid #38BDF8 !important;
    }

    /* LABELS */

    label {

        color: white !important;

        font-weight: 600 !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # SIDEBAR TOP CONTAINER

   st.sidebar.markdown("# 🔢 Digit Recognition Dashboard")
    st.sidebar.caption("Professional Machine Learning Analytics")
    st.sidebar.markdown("### Dashboard Filters")   
    st.sidebar.success("FILTERS.PY UPDATED")
    # DIGIT FILTER

    selected_digits = st.sidebar.multiselect(
        "Select Digits",
        options=sorted(df["digit"].unique()),
        default=sorted(df["digit"].unique())
    )

    # EXTRA CHART FILTER

    

    # SAVE CHARTS

    

    # FILTER DATA

    filtered_df = df[
        df["digit"].isin(selected_digits)
    ]

    return filtered_df
