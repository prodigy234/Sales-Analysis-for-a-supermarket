import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('supermarket_sales.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M').dt.to_timestamp()
    df['Day'] = df['Date'].dt.day
    df['Hour'] = pd.to_datetime(df['Time'], format="%H:%M").dt.hour
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("📊 Filter Data")
branches = st.sidebar.multiselect("Select Branch(es):", options=df['Branch'].unique(), default=df['Branch'].unique())
cities = st.sidebar.multiselect("Select City(ies):", options=df['City'].unique(), default=df['City'].unique())
genders = st.sidebar.multiselect("Select Gender(s):", options=df['Gender'].unique(), default=df['Gender'].unique())
customer_types = st.sidebar.multiselect("Select Customer Type(s):", options=df['Customer type'].unique(), default=df['Customer type'].unique())

df_filtered = df[
    (df['Branch'].isin(branches)) &
    (df['City'].isin(cities)) &
    (df['Gender'].isin(genders)) &
    (df['Customer type'].isin(customer_types))
]

# Header
st.title("🛒 Supermarket Sales Dashboard")
st.caption("Visual & Interactive Analysis of Supermarket Sales Data")

# KPIs
st.subheader("📌 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${df_filtered['Total'].sum():,.2f}")
col2.metric("Total Quantity", int(df_filtered['Quantity'].sum()))
col3.metric("Avg. Rating", round(df_filtered['Rating'].mean(), 2))
col4.metric("Gross Income", f"${df_filtered['gross income'].sum():,.2f}")

# Tabs for Analysis
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📈 Trends", "📦 Products", "🌍 Regions", "🧍 Customers", "💳 Payments", "💡 Insights"
])

with tab1:
    st.subheader("📅 Monthly Trends")
    trend = df_filtered.groupby("Month")[['Total', 'Quantity']].sum().reset_index()
    fig = px.line(trend, x='Month', y=['Total', 'Quantity'], labels={'value': 'Amount', 'variable': 'Metric'})
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("📦 Product Line Performance")
    product = df_filtered.groupby("Product line")[['Quantity', 'Total']].sum().sort_values(by='Total', ascending=False).reset_index()
    fig1 = px.bar(product, x='Product line', y='Total', color='Product line', title="Revenue by Product Line")
    st.plotly_chart(fig1, use_container_width=True)

with tab3:
    st.subheader("📍 Regional Performance")
    branch_perf = df_filtered.groupby("Branch")[['Quantity', 'Total']].sum().reset_index()
    city_perf = df_filtered.groupby("City")[['Quantity', 'Total']].sum().reset_index()
    
    col1, col2 = st.columns(2)
    with col1:
        fig2 = px.bar(branch_perf, x='Branch', y='Total', color='Branch', title="Revenue by Branch")
        st.plotly_chart(fig2, use_container_width=True)
    with col2:
        fig3 = px.bar(city_perf, x='City', y='Total', color='City', title="Revenue by City")
        st.plotly_chart(fig3, use_container_width=True)

with tab4:
    st.subheader("👥 Customer Insights")
    gender_perf = df_filtered.groupby("Gender")[['Quantity', 'Total']].sum().reset_index()
    customer_perf = df_filtered.groupby("Customer type")[['Quantity', 'Total']].sum().reset_index()

    col1, col2 = st.columns(2)
    with col1:
        fig4 = px.pie(gender_perf, values='Total', names='Gender', title='Revenue by Gender')
        st.plotly_chart(fig4, use_container_width=True)
    with col2:
        fig5 = px.pie(customer_perf, values='Total', names='Customer type', title='Revenue by Customer Type')
        st.plotly_chart(fig5, use_container_width=True)

with tab5:
    st.subheader("💳 Payment Method Preferences")
    payment_dist = df_filtered['Payment'].value_counts(normalize=True).reset_index()
    payment_dist.columns = ['Payment Method', 'Percentage']
    fig6 = px.pie(payment_dist, names='Payment Method', values='Percentage', title="Payment Methods Distribution", hole=0.4)
    st.plotly_chart(fig6, use_container_width=True)

with tab6:
    st.subheader("📌 Actionable Insights")
    st.markdown("""
    1. 🎯 Focus marketing efforts on **high-performing product lines**.
    2. 📉 Investigate and improve **low-performing branches or cities**.
    3. 🧠 Use gender and customer type patterns for **targeted promotions**.
    4. 📦 Optimize inventory for **peak months** and **top-selling items**.
    5. 💳 Promote **efficient payment methods** and track customer behavior.
    6. 🔆 Ensure that the payment methods are smooth so as to improve the ease of transactions made.
    7. ♨️ Meticulously checkmate local issues like competition or poor customer experience in some branches or cities that underperformed.
    8. ♦️ While observing peaks and dips in monthly sales, discounts should be offered during slower months to boost sales.
    9. 🔊 Although the average rating, indicated customer satisfaction, there's need to maintain or improve customer satisfaction by addressing common complaints.
    """)

# Download filtered data
st.sidebar.markdown("### 📥 Download")
st.sidebar.download_button(
    label="Download Filtered CSV",
    data=df_filtered.to_csv(index=False).encode('utf-8'),
    file_name='filtered_supermarket_sales.csv',
    mime='text/csv'
)
