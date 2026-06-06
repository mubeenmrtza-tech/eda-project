
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

strength_col = "Concrete compressive strength(MPa, megapascals) "
cement_col = "Cement (component 1)(kg in a m^3 mixture)"
water_col = "Water  (component 4)(kg in a m^3 mixture)"
age_col = "Age (day)"

# ==========================
# HISTOGRAM
# ==========================

def histogram(df):

    st.subheader("📊 Strength Distribution Histogram")

    col1, col2 = st.columns([2,1])

    with col1:
        fig, ax = plt.subplots(figsize=(7,4))
        sns.histplot(df[strength_col], kde=True, color="cyan", ax=ax)
        ax.set_title("Concrete Strength Distribution")
        st.pyplot(fig)

    with col2:
        st.info("""
        This histogram shows the frequency distribution
        of concrete compressive strength values.

        It helps identify:
        - Most common strength range
        - Distribution pattern
        - Outliers
        """)

# ==========================
# SCATTER PLOT
# ==========================

def scatter_plot(df):

    st.subheader("🔵 Cement vs Strength")

    col1, col2 = st.columns([2,1])

    with col1:
        fig, ax = plt.subplots(figsize=(7,4))
        sns.scatterplot(
            x=df[cement_col],
            y=df[strength_col],
            color="orange",
            ax=ax
        )
        ax.set_title("Cement vs Strength")
        st.pyplot(fig)

    with col2:
        st.info("""
        This scatter plot shows the relationship
        between cement quantity and concrete strength.

        Higher cement generally increases strength.
        """)

# ==========================
# BOX PLOT
# ==========================

def box_plot(df):

    st.subheader("📦 Strength Box Plot")

    col1, col2 = st.columns([2,1])

    with col1:
        fig, ax = plt.subplots(figsize=(7,4))
        sns.boxplot(y=df[strength_col], color="lime", ax=ax)
        ax.set_title("Strength Spread")
        st.pyplot(fig)

    with col2:
        st.info("""
        Box plot visualizes:
        - Median
        - Quartiles
        - Outliers
        - Data spread
        """)

# ==========================
# HEATMAP
# ==========================

def heatmap_chart(df):

    st.subheader("🔥 Correlation Heatmap")

    col1, col2 = st.columns([2,1])

    with col1:
        fig, ax = plt.subplots(figsize=(8,5))
        sns.heatmap(
            df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm",
            ax=ax
        )
        st.pyplot(fig)

    with col2:
        st.info("""
        Heatmap shows correlation between variables.

        Darker colors indicate stronger relationships.
        """)

# ==========================
# LINE CHART
# ==========================

def line_chart(df):

    st.subheader("📈 Age vs Strength")

    col1, col2 = st.columns([2,1])

    with col1:
        grouped = df.groupby(age_col)[strength_col].mean()

        fig, ax = plt.subplots(figsize=(7,4))
        grouped.plot(ax=ax, color="yellow")
        ax.set_title("Average Strength by Age")
        st.pyplot(fig)

    with col2:
        st.info("""
        This line chart shows how curing age
        affects concrete strength.
        """)

# ==========================
# BAR CHART
# ==========================

def bar_chart(df):

    st.subheader("📊 Average Strength by Age")

    col1, col2 = st.columns([2,1])

    with col1:
        grouped = df.groupby(age_col)[strength_col].mean().head(10)

        fig, ax = plt.subplots(figsize=(7,4))
        grouped.plot(kind="bar", color="purple", ax=ax)
        st.pyplot(fig)

    with col2:
        st.info("""
        Bar chart compares average strength
        across different curing ages.
        """)

# ==========================
# PIE CHART
# ==========================

def pie_chart(df):

    st.subheader("🥧 Cement Categories")

    col1, col2 = st.columns([2,1])

    with col1:
        categories = ["Low", "Medium", "High"]

        values = [
            len(df[df[cement_col] < 200]),
            len(df[(df[cement_col] >= 200) & (df[cement_col] < 400)]),
            len(df[df[cement_col] >= 400])
        ]

        fig, ax = plt.subplots(figsize=(5,5))
        ax.pie(values, labels=categories, autopct='%1.1f%%')
        st.pyplot(fig)

    with col2:
        st.info("""
        Pie chart shows proportion of
        low, medium and high cement mixtures.
        """)

# ==========================
# VIOLIN PLOT
# ==========================

def violin_plot(df):

    st.subheader("🎻 Strength Violin Plot")

    col1, col2 = st.columns([2,1])

    with col1:
        fig, ax = plt.subplots(figsize=(7,4))
        sns.violinplot(y=df[strength_col], color="red", ax=ax)
        st.pyplot(fig)

    with col2:
        st.info("""
        Violin plot combines:
        - Distribution
        - Density
        - Spread
        """)

# ==========================
# COUNT PLOT
# ==========================

def count_plot(df):

    st.subheader("🔢 Age Frequency")

    col1, col2 = st.columns([2,1])

    with col1:
        fig, ax = plt.subplots(figsize=(7,4))
        sns.countplot(x=df[age_col], ax=ax)
        plt.xticks(rotation=90)
        st.pyplot(fig)

    with col2:
        st.info("""
        Count plot shows frequency
        of different curing ages.
        """)

# ==========================
# AREA CHART
# ==========================

def area_chart(df):

    st.subheader("🌊 Area Chart")

    col1, col2 = st.columns([2,1])

    with col1:
        grouped = df.groupby(age_col)[strength_col].mean()

        st.area_chart(grouped)

    with col2:
        st.info("""
        Area chart highlights cumulative
        strength trends over curing age.
        """)

