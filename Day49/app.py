
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Customer Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

DATA_PATH = (
    Path(__file__).parent.parent
    / "Day48"
    / "cleaned_customer_data.csv"
)


@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)
    data["order_date"] = pd.to_datetime(
        data["order_date"], errors="coerce"
    )
    return data


try:
    df = load_data()
except Exception as error:
    st.error(f"Unable to load the dataset: {error}")
    st.stop()


# ---------- STYLING ----------
st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
    color: #e5e7eb;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stSidebar"] * {
    color: #e5e7eb;
}

[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span {
    color: #e5e7eb;
}

.block-container {
    padding-top: 1.8rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    color: #f8fafc;
}

[data-testid="stMetric"] {
    background-color: #172033;
    border: 1px solid #293750;
    padding: 18px;
    border-radius: 12px;
}

[data-testid="stMetricLabel"] {
    color: #a5b4fc;
}

div[data-testid="stMetricValue"] {
    color: #ffffff;
}

[data-testid="stDataFrame"] {
    border: 1px solid #293750;
    border-radius: 10px;
}

.stButton > button,
.stDownloadButton > button {
    border-radius: 8px;
    font-weight: 600;
}

/* Make sidebar filter values readable */
[data-testid="stSidebar"] [data-baseweb="select"] {
    color: #111827;
}

[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background-color: #ffffff;
    border: 1px solid #64748b;
    border-radius: 8px;
}

[data-testid="stSidebar"] [data-baseweb="select"] input {
    color: #111827 !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] div {
    color: #111827;
}

[data-testid="stSidebar"] input {
    color: #111827 !important;
    background-color: #ffffff !important;
}

[data-testid="stSidebar"] button {
    color: #111827 !important;
}

[data-testid="stSidebar"] button:hover {
    border-color: #60a5fa;
}
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.title("📊 Customer Intelligence Platform")
st.markdown(
    "A unified workspace for customer, sales and profitability analytics."
)
st.caption(
    "CUSTOMER ANALYTICS  /  SALES PERFORMANCE  /  BUSINESS INSIGHTS"
)
st.divider()


# ---------- SIDEBAR ----------
st.sidebar.title("📊 Customer Intelligence")
st.sidebar.caption("Analytics workspace")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Sales & Profit",
        "Customer Data",
        "Business Insights"
    ]
)

st.sidebar.divider()
st.sidebar.subheader("Dashboard Filters")

segments = ["All"] + sorted(
    df["segment"].dropna().unique().tolist()
)
categories = ["All"] + sorted(
    df["category"].dropna().unique().tolist()
)

selected_segment = st.sidebar.selectbox(
    "Customer Segment", segments
)
selected_category = st.sidebar.selectbox(
    "Product Category", categories
)

min_date = df["order_date"].min().date()
max_date = df["order_date"].max().date()

date_range = st.sidebar.date_input(
    "Order Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if st.sidebar.button("Reset filters", use_container_width=True):
    st.session_state["Customer Segment"] = "All"
    st.session_state["Product Category"] = "All"
    st.session_state["Order Date Range"] = (min_date, max_date)
    st.rerun()


# ---------- FILTER DATA ----------
filtered_df = df.copy()

if selected_segment != "All":
    filtered_df = filtered_df[
        filtered_df["segment"] == selected_segment
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["category"] == selected_category
    ]

if date_range and len(date_range) == 2:
    start_date, end_date = date_range
    filtered_df = filtered_df[
        filtered_df["order_date"].dt.date.between(
            start_date, end_date
        )
    ]


# ---------- METRICS ----------
total_sales = filtered_df["sales"].sum()
total_profit = filtered_df["profit"].sum()
total_orders = filtered_df["order_id"].nunique()
total_customers = filtered_df["customer_name"].nunique()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales else 0
)

st.caption(
    f"Showing {len(filtered_df):,} records after applying filters."
)


# ---------- OVERVIEW ----------
if page == "Overview":
    st.subheader("Business Overview")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sales", f"{total_sales:,.2f}")
    col2.metric("Total Profit", f"{total_profit:,.2f}")
    col3.metric("Unique Orders", f"{total_orders:,}")
    col4.metric("Unique Customers", f"{total_customers:,}")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("Monthly Sales")
        if not filtered_df.empty:
            monthly_sales = (
                filtered_df.groupby("order_month")["sales"]
                .sum().sort_index()
            )
            st.bar_chart(monthly_sales)
        else:
            st.info("No data available for these filters.")

    with right:
        st.subheader("Monthly Profit")
        if not filtered_df.empty:
            monthly_profit = (
                filtered_df.groupby("order_month")["profit"]
                .sum().sort_index()
            )
            st.bar_chart(monthly_profit)
        else:
            st.info("No data available for these filters.")

    st.divider()
    st.subheader("Profitability Summary")

    col1, col2 = st.columns(2)
    col1.metric("Overall Profit Margin", f"{profit_margin:.2f}%")
    col2.metric(
        "Average Sales per Order",
        f"{total_sales / total_orders:,.2f}"
        if total_orders else "0.00"
    )


# ---------- SALES & PROFIT ----------
elif page == "Sales & Profit":
    st.subheader("📈 Sales & Profitability Analysis")

    left, right = st.columns(2)

    with left:
        st.markdown("#### Profit by Product Category")
        if not filtered_df.empty:
            category_profit = (
                filtered_df.groupby("category")["profit"]
                .sum().sort_values(ascending=False)
            )
            st.bar_chart(category_profit)
        else:
            st.info("No data available for these filters.")

    with right:
        st.markdown("#### Sales by Customer Segment")
        if not filtered_df.empty:
            segment_sales = (
                filtered_df.groupby("segment")["sales"]
                .sum().sort_values(ascending=False)
            )
            st.bar_chart(segment_sales)
        else:
            st.info("No data available for these filters.")

    st.divider()
    st.subheader("Monthly Sales and Profit")

    if not filtered_df.empty:
        monthly_data = (
            filtered_df.groupby("order_month")[["sales", "profit"]]
            .sum().sort_index()
        )
        st.line_chart(monthly_data)
    else:
        st.info("No data available for these filters.")


# ---------- CUSTOMER DATA ----------
elif page == "Customer Data":
    st.subheader("🧾 Customer Data Explorer")
    st.write("Search and review filtered order records.")

    search_text = st.text_input(
        "Search customer, order ID or product",
        placeholder="Enter a customer, order ID or product name"
    )

    search_df = filtered_df.copy()

    if search_text:
        search_mask = pd.Series(False, index=search_df.index)

        for column in [
            "customer_name", "order_id", "product_name"
        ]:
            if column in search_df.columns:
                search_mask |= (
                    search_df[column].astype(str)
                    .str.contains(search_text, case=False, na=False)
                )

        search_df = search_df[search_mask]

    st.caption(f"{len(search_df):,} matching records")

    st.dataframe(
        search_df,
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        "Download filtered data (CSV)",
        data=search_df.to_csv(index=False).encode("utf-8"),
        file_name="filtered_customer_data.csv",
        mime="text/csv"
    )


# ---------- BUSINESS INSIGHTS ----------
elif page == "Business Insights":
    st.subheader("💡 Business Insights")

    if filtered_df.empty:
        st.info("No records match the selected filters.")
    else:
        best_category = (
            filtered_df.groupby("category")["profit"]
            .sum().idxmax()
        )
        best_segment = (
            filtered_df.groupby("segment")["sales"]
            .sum().idxmax()
        )
        best_month = (
            filtered_df.groupby("order_month")["sales"]
            .sum().idxmax()
        )

        st.success(
            f"Most profitable product category: **{best_category}**"
        )
        st.info(
            f"Customer segment with highest sales: **{best_segment}**"
        )
        st.info(
            f"Month with highest sales: **{best_month}**"
        )

        st.divider()
        st.subheader("Financial Summary")

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Sales", f"{total_sales:,.2f}")
        col2.metric("Total Profit", f"{total_profit:,.2f}")
        col3.metric("Profit Margin", f"{profit_margin:.2f}%")

        st.caption(
            "Insights describe historical data and do not establish cause and effect."
        )


# ---------- FOOTER ----------
st.divider()
st.caption(
    "Customer Intelligence Platform | Day 52/60 — ABTalksOnAI"
)
