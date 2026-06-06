import streamlit as st

def apply_filters(df):

    st.sidebar.header("🔍 Interactive Filters")

    cement_col = "Cement (component 1)(kg in a m^3 mixture)"
    water_col = "Water  (component 4)(kg in a m^3 mixture)"
    age_col = "Age (day)"

    # Dropdown Options
    cement_options = ["All"] + sorted(df[cement_col].unique().tolist())
    water_options = ["All"] + sorted(df[water_col].unique().tolist())
    age_options = ["All"] + sorted(df[age_col].unique().tolist())

    # Dropdown Filters
    cement_value = st.sidebar.selectbox(
        "Cement Value",
        cement_options
    )

    water_value = st.sidebar.selectbox(
        "Water Value",
        water_options
    )

    age_value = st.sidebar.selectbox(
        "Age",
        age_options
    )

    # Start with full dataset
    filtered_df = df.copy()

    # Apply filters only if user selects a value
    if cement_value != "All":
        filtered_df = filtered_df[
            filtered_df[cement_col] == cement_value
        ]

    if water_value != "All":
        filtered_df = filtered_df[
            filtered_df[water_col] == water_value
        ]

    if age_value != "All":
        filtered_df = filtered_df[
            filtered_df[age_col] == age_value
        ]

    st.sidebar.markdown("---")
    st.sidebar.success(f"Filtered Rows: {len(filtered_df)}")

    return filtered_df