import streamlit as st
import pandas as pd

from filters import apply_filters
from charts import (
    histogram,
    scatter_plot,
    box_plot,
    heatmap_chart,
    line_chart,
    bar_chart,
    pie_chart,
    violin_plot,
    count_plot,
    area_chart
)

st.set_page_config(
    page_title="Concrete Strength Dashboard",
    page_icon="🏗️",
    layout="wide"
)

# ==========================
# LOAD DATA
# ==========================

@st.cache_data
def load_data():
    df = pd.read_excel("data/Concrete_Data.xls")
    return df

df = load_data()

# ==========================
# HEADER
# ==========================

st.title("🏗️ Concrete Strength Analysis Dashboard")

st.markdown("""
### Exploratory Data Analysis Dashboard

This dashboard analyzes the relationship between concrete ingredients
and compressive strength using interactive filters and visualizations.
""")

# ==========================
# FILTERS
# ==========================

filtered_df = apply_filters(df)
if filtered_df.empty:
    st.error("No data available for selected filters.")
    st.stop()

# ==========================
# ==========================
# KPI SECTION (Professional)
# ==========================

st.markdown("## 📊 Dashboard Overview")

strength_col = "Concrete compressive strength(MPa, megapascals) "
cement_col = "Cement (component 1)(kg in a m^3 mixture)"
water_col = "Water  (component 4)(kg in a m^3 mixture)"

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📋 Total Records",
        value=f"{len(filtered_df):,}"
    )

with col2:
    st.metric(
        label="📈 Avg Strength",
        value=f"{filtered_df[strength_col].mean():.2f} MPa"
    )

with col3:
    st.metric(
        label="🚀 Max Strength",
        value=f"{filtered_df[strength_col].max():.2f} MPa"
    )

with col4:
    st.metric(
        label="📉 Min Strength",
        value=f"{filtered_df[strength_col].min():.2f} MPa"
    )

st.markdown("<br>", unsafe_allow_html=True)

col5, col6 = st.columns(2)

with col5:
    st.metric(
        label="🏗️ Avg Cement",
        value=f"{filtered_df[cement_col].mean():.2f} kg"
    )

with col6:
    st.metric(
        label="💧 Avg Water",
        value=f"{filtered_df[water_col].mean():.2f} kg"
    )

# ==========================
# DATA PREVIEW
# ==========================

st.subheader("📋 Filtered Dataset Preview")

if filtered_df.empty:
    st.warning("⚠️ No records found for selected filters.")
else:
    st.dataframe(
        filtered_df,
        use_container_width=True
    )

# ==========================
# DOWNLOAD BUTTON
# ==========================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Data",
    data=csv,
    file_name="filtered_concrete_data.csv",
    mime="text/csv"
)

st.divider()

# ==========================
# CHARTS SECTION
# ==========================

st.header("📈 Data Visualizations")

row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    histogram(filtered_df)

with row1_col2:
    scatter_plot(filtered_df)

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    box_plot(filtered_df)

with row2_col2:
    heatmap_chart(filtered_df)

row3_col1, row3_col2 = st.columns(2)

with row3_col1:
    line_chart(filtered_df)

with row3_col2:
    bar_chart(filtered_df)

row4_col1, row4_col2 = st.columns(2)

with row4_col1:
    pie_chart(filtered_df)

with row4_col2:
    violin_plot(filtered_df)

row5_col1, row5_col2 = st.columns(2)

with row5_col1:
    count_plot(filtered_df)

with row5_col2:
    area_chart(filtered_df)

st.divider()

# ==========================
# CORRELATION INSIGHTS
# ==========================

st.header("📌 Insights")

corr = filtered_df.corr(numeric_only=True)

strength_corr = corr[strength_col].sort_values(
    ascending=False
)

st.write(
    "### Correlation with Concrete Strength"
)

st.dataframe(strength_corr)

highest_positive = strength_corr.index[1]
highest_value = strength_corr.iloc[1]

st.success(
    f"Highest Positive Correlation: {highest_positive} ({highest_value:.2f})"
)

st.info(
    """
    Higher cement content and curing age generally
    improve compressive strength, while ingredient
    balance significantly affects final performance.
    """
)

st.divider()

st.markdown(
    """
    ### Dashboard Developed For EDA Project

    Interactive Data Visualization Dashboard
    using Pandas, Matplotlib, Seaborn and Streamlit.
    """
)
