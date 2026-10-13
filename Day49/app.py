
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Customer Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

DATA_PATH = Path(__file__).parent.parent / "Day48" / "cleaned_customer_data.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

st.title("📊 Customer Intelligence Platform")
st.write("Customer, Sales and Profitability Analytics")

st.sidebar.header("Dashboard Filters")

segments = ["All"] + sorted(df["segment"].dropna().unique().tolist())
selected_segment = st.sidebar.selectbox("Customer Segment", segments)

categories = ["All"] + sorted(df["category"].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("Product Category", categories)

filtered_df = df.copy()

if selected_segment != "All":
    filtered_df = filtered_df[filtered_df["segment"] == selected_segment]

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["category"] == selected_category]

total_sales = filtered_df["sales"].sum()
total_profit = filtered_df["profit"].sum()
total_orders = filtered_df["order_id"].nunique()
total_customers = filtered_df["customer_name"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"{total_sales:,.2f}")
col2.metric("Total Profit", f"{total_profit:,.2f}")
col3.metric("Unique Orders", f"{total_orders:,}")
col4.metric("Unique Customers", f"{total_customers:,}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Monthly Sales")
    monthly_sales = filtered_df.groupby("order_month")["sales"].sum()
    st.bar_chart(monthly_sales)

with right:
    st.subheader("Monthly Profit")
    monthly_profit = filtered_df.groupby("order_month")["profit"].sum()
    st.bar_chart(monthly_profit)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Profit by Product Category")
    category_profit = filtered_df.groupby("category")["profit"].sum()
    st.bar_chart(category_profit)

with right:
    st.subheader("Sales by Customer Segment")
    segment_sales = filtered_df.groupby("segment")["sales"].sum()
    st.bar_chart(segment_sales)

st.divider()

st.subheader("Customer Data Preview")
st.dataframe(filtered_df.head(100), use_container_width=True)

st.caption(f"Showing {len(filtered_df):,} records after applying filters.")


st.divider()

st.subheader("📌 Business Insights")

if not filtered_df.empty:
    best_category = (
        filtered_df.groupby("category")["profit"].sum().idxmax()
    )
    best_segment = (
        filtered_df.groupby("segment")["sales"].sum().idxmax()
    )
    best_month = (
        filtered_df.groupby("order_month")["sales"].sum().idxmax()
    )

    st.write(f"🏆 Most profitable product category: **{best_category}**")
    st.write(f"👥 Highest sales customer segment: **{best_segment}**")
    st.write(f"📈 Highest sales month: **{best_month}**")

    if total_profit > 0:
        profit_margin = (total_profit / total_sales * 100) if total_sales else 0
        st.metric("Overall Profit Margin", f"{profit_margin:.2f}%")
else:
    st.info("No records match the selected filters.")

