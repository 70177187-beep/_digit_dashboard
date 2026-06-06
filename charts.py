import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# BAR CHART

def bar_chart(df):

    fig, ax = plt.subplots(figsize=(8,5))

    df["digit"].value_counts().plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Digit Count")

    st.pyplot(fig)

# PIE CHART

def pie_chart(df):

    fig, ax = plt.subplots(figsize=(8,8))

    df["digit"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )

    ax.set_ylabel("")

    ax.set_title("Digit Distribution")

    st.pyplot(fig)

# HISTOGRAM

def histogram(df):

    fig, ax = plt.subplots(figsize=(10,5))

    ax.hist(df["pixel_10"], bins=20)

    ax.set_title("Pixel 10 Distribution")

    st.pyplot(fig)

# SCATTER

def scatter_plot(df):

    fig, ax = plt.subplots(figsize=(8,5))

    sns.scatterplot(
        data=df,
        x="pixel_5",
        y="pixel_20",
        hue="digit",
        ax=ax
    )

    st.pyplot(fig)

# BOX PLOT

def box_plot(df):

    fig, ax = plt.subplots(figsize=(10,5))

    sns.boxplot(
        data=df,
        x="digit",
        y="pixel_15",
        ax=ax
    )

    st.pyplot(fig)

# HEATMAP

def heatmap(df):

    fig, ax = plt.subplots(figsize=(12,8))

    sns.heatmap(
        df.corr(),
        cmap="viridis",
        ax=ax
    )

    st.pyplot(fig)

# LINE CHART

def line_chart(df):

    fig, ax = plt.subplots(figsize=(10,5))

    df["pixel_1"].head(100).plot(ax=ax)

    ax.set_title("Pixel 1 Trend")

    st.pyplot(fig)

# AREA CHART

def area_chart(df):

    st.area_chart(
        df[["pixel_1","pixel_2"]].head(100)
    )

# COUNT PLOT

def count_plot(df):

    fig, ax = plt.subplots(figsize=(8,5))

    sns.countplot(
        data=df,
        x="digit",
        ax=ax
    )

    st.pyplot(fig)

# VIOLIN PLOT

def violin_plot(df):

    fig, ax = plt.subplots(figsize=(10,5))

    sns.violinplot(
        data=df,
        x="digit",
        y="pixel_25",
        ax=ax
    )

    st.pyplot(fig)