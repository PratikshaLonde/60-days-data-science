import streamlit as st
import pandas as pd


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666666;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 600;
        margin-top: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown(
    '<div class="main-title">📊 Customer Intelligence Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Interactive business intelligence dashboard for customer analytics and predictive insights.</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("⚙️ Dashboard Controls")

uploaded_file = st.sidebar.file_uploader(
    "Upload Customer CSV",
    type=["csv"]
)


# --------------------------------------------------
# LOAD CUSTOMER DATA
# --------------------------------------------------

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.sidebar.success("Uploaded CSV loaded successfully!")

else:

    df = pd.read_csv("../cleaned_dataset.csv")

    st.sidebar.info("Using project customer dataset.")


# --------------------------------------------------
# DATE CONVERSION
# --------------------------------------------------

if "order_date" in df.columns:

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )


# --------------------------------------------------
# CHECK REQUIRED COLUMNS
# --------------------------------------------------

required_columns = [
    "customer_name",
    "sales",
    "profit",
    "order_id",
    "product_name",
    "category",
    "order_date"
]

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:

    st.error(
        "Missing required columns: "
        + ", ".join(missing_columns)
    )

    st.stop()


# --------------------------------------------------
# LOAD SEGMENT DATA
# --------------------------------------------------

segment_file = "../Day30/customer_segments_final.csv"

try:

    segment_data = pd.read_csv(segment_file)

except FileNotFoundError:

    segment_data = pd.DataFrame()


# --------------------------------------------------
# LOAD CHURN-RISK DATA
# --------------------------------------------------

risk_file = "../Day41/customer_risk_ranking.csv"

try:

    risk_data = pd.read_csv(risk_file)

except FileNotFoundError:

    risk_data = pd.DataFrame()


# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.markdown("---")
st.sidebar.subheader("🔎 Filters")


# Customer filter

customer_list = sorted(
    df["customer_name"]
    .dropna()
    .unique()
    .tolist()
)

selected_customer = st.sidebar.selectbox(
    "Customer",
    ["All Customers"] + customer_list
)


# Category filter

category_list = sorted(
    df["category"]
    .dropna()
    .unique()
    .tolist()
)

selected_category = st.sidebar.selectbox(
    "Category",
    ["All Categories"] + category_list
)


# --------------------------------------------------
# APPLY FILTERS
# --------------------------------------------------

filtered_df = df.copy()


if selected_customer != "All Customers":

    filtered_df = filtered_df[
        filtered_df["customer_name"]
        == selected_customer
    ]


if selected_category != "All Categories":

    filtered_df = filtered_df[
        filtered_df["category"]
        == selected_category
    ]


# --------------------------------------------------
# KPI CALCULATIONS
# --------------------------------------------------

total_revenue = filtered_df["sales"].sum()

total_profit = filtered_df["profit"].sum()

total_customers = filtered_df[
    "customer_name"
].nunique()

total_orders = filtered_df[
    "order_id"
].nunique()


# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📌 Key Performance Indicators</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "💰 Total Revenue",
        f"${total_revenue:,.2f}"
    )


with col2:

    st.metric(
        "📈 Total Profit",
        f"${total_profit:,.2f}"
    )


with col3:

    st.metric(
        "👥 Customers",
        f"{total_customers:,}"
    )


with col4:

    st.metric(
        "🛒 Orders",
        f"{total_orders:,}"
    )


# --------------------------------------------------
# DATASET SUMMARY
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📋 Dataset Summary</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    st.info(
        f"Total Records: {len(filtered_df):,}"
    )


with col2:

    st.info(
        f"Products: {filtered_df['product_name'].nunique():,}"
    )


with col3:

    st.info(
        f"Categories: {filtered_df['category'].nunique():,}"
    )


# --------------------------------------------------
# CUSTOMER SEGMENTATION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">👥 Customer Segmentation</div>',
    unsafe_allow_html=True
)


if not segment_data.empty:

    segment_counts = (
        segment_data["segment_name"]
        .value_counts()
        .reset_index()
    )

    segment_counts.columns = [
        "segment_name",
        "customer_count"
    ]

    col1, col2 = st.columns(2)


    with col1:

        st.write("#### Segment Distribution")

        st.bar_chart(
            segment_counts.set_index(
                "segment_name"
            )
        )


    with col2:

        st.write("#### Segment Summary")

        st.dataframe(
            segment_counts,
            use_container_width=True,
            hide_index=True
        )

else:

    st.warning(
        "Customer segmentation file not found."
    )


# --------------------------------------------------
# CHURN RISK
# --------------------------------------------------

st.markdown(
    '<div class="section-title">⚠️ Customer Churn Risk</div>',
    unsafe_allow_html=True
)


if not risk_data.empty:

    risk_counts = (
        risk_data["risk_level"]
        .value_counts()
        .reindex(
            [
                "Low Risk",
                "Medium Risk",
                "High Risk"
            ],
            fill_value=0
        )
        .reset_index()
    )

    risk_counts.columns = [
        "risk_level",
        "customer_count"
    ]

    col1, col2 = st.columns(2)


    with col1:

        st.write("#### Risk Distribution")

        st.bar_chart(
            risk_counts.set_index(
                "risk_level"
            )
        )


    with col2:

        st.write("#### Risk Summary")

        st.dataframe(
            risk_counts,
            use_container_width=True,
            hide_index=True
        )


else:

    st.warning(
        "Customer risk file not found."
    )


# --------------------------------------------------
# MONTHLY REVENUE
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📈 Monthly Revenue Trend</div>',
    unsafe_allow_html=True
)


filtered_df["year_month"] = (
    filtered_df["order_date"]
    .dt.to_period("M")
    .astype(str)
)


monthly_revenue = (
    filtered_df
    .groupby("year_month")["sales"]
    .sum()
    .reset_index()
)


monthly_revenue = monthly_revenue.set_index(
    "year_month"
)


st.line_chart(
    monthly_revenue["sales"]
)


# --------------------------------------------------
# PROFIT BY CATEGORY
# --------------------------------------------------

st.markdown(
    '<div class="section-title">💵 Profit by Category</div>',
    unsafe_allow_html=True
)


category_profit = (
    filtered_df
    .groupby("category")["profit"]
    .sum()
    .sort_values(ascending=False)
)


st.bar_chart(category_profit)


# --------------------------------------------------
# CUSTOMER DATA
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🔎 Customer Data</div>',
    unsafe_allow_html=True
)


display_columns = [
    "customer_name",
    "order_date",
    "category",
    "product_name",
    "sales",
    "profit"
]


available_columns = [
    column
    for column in display_columns
    if column in filtered_df.columns
]


st.dataframe(
    filtered_df[available_columns],
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Day 44/60 — ABTalksOnAI 60 Days Coding Challenge"
)