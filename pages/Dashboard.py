import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------
# PAGE CONFIG
# ------------------------

st.set_page_config(
    page_title="OceanAI Dashboard",
    page_icon="🌊",
    layout="wide"
)

# ------------------------
# OCEAN BLUE THEME
# ------------------------

st.markdown("""
<style>

.stApp{
    background:#EEF7FD;
}

[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#0B4F8C,#1976D2);
}

[data-testid="stSidebar"] *{
    color:white;
}

h1,h2,h3{
    color:#0B4F8C;
}

div[data-testid="metric-container"]{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 6px 15px rgba(0,0,0,.08);
    border-left:6px solid #2196F3;
}

</style>
""", unsafe_allow_html=True)

# ------------------------
# LOAD DATA
# ------------------------

df = pd.read_csv("data/sales_data.csv")

# ------------------------
# SIDEBAR
# ------------------------

st.sidebar.title("🌊 OceanAI")

platform = st.sidebar.multiselect(
    "Platform",
    df.Platform.unique(),
    default=df.Platform.unique()
)

campaign = st.sidebar.multiselect(
    "Campaign",
    df.Campaign.unique(),
    default=df.Campaign.unique()
)

product = st.sidebar.multiselect(
    "Product",
    df.Product.unique(),
    default=df.Product.unique()
)

df = df[
    (df.Platform.isin(platform))
    &
    (df.Campaign.isin(campaign))
    &
    (df.Product.isin(product))
]

# ------------------------
# HEADER
# ------------------------

st.title("🌊 OceanAI Marketing Dashboard")

st.caption("AI Powered Marketing Performance Analytics")

st.divider()

# ------------------------
# KPI
# ------------------------

col1,col2,col3,col4,col5 = st.columns(5)

col1.metric(
    "💰 Revenue",
    f"${df['Revenue'].sum():,.0f}"
)

col2.metric(
    "📦 Orders",
    f"{df['Orders'].sum():,}"
)

col3.metric(
    "💵 Ad Spend",
    f"${df['Ad Spend'].sum():,.0f}"
)

col4.metric(
    "🚀 ROAS",
    f"{df['ROAS'].mean():.2f}"
)

col5.metric(
    "📈 CTR",
    f"{df['CTR'].mean()*100:.2f}%"
)

st.divider()

# ------------------------
# ROW 1
# ------------------------

left,right = st.columns(2)

with left:

    revenue_campaign = df.groupby(
        "Campaign"
    )["Revenue"].sum().reset_index()

    fig = px.bar(
        revenue_campaign,
        x="Campaign",
        y="Revenue",
        color="Revenue",
        title="Revenue by Campaign",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(fig,width="stretch")

with right:

    revenue_platform = df.groupby(
        "Platform"
    )["Revenue"].sum().reset_index()

    fig2 = px.pie(
        revenue_platform,
        names="Platform",
        values="Revenue",
        hole=.55,
        color_discrete_sequence=px.colors.sequential.Blues
    )

    st.plotly_chart(fig2,width="stretch")

# ------------------------
# ROW 2
# ------------------------

left,right = st.columns(2)

with left:

    product = df.groupby(
        "Product"
    )["Revenue"].sum().reset_index()

    fig3 = px.bar(
        product,
        x="Product",
        y="Revenue",
        color="Revenue",
        title="Top Products",
        color_continuous_scale="Tealgrn"
    )

    st.plotly_chart(fig3,width="stretch")

with right:

    trend = df.groupby(
        "Date"
    )["Revenue"].sum().reset_index()

    fig4 = px.line(
        trend,
        x="Date",
        y="Revenue",
        markers=True,
        title="Revenue Trend"
    )

    fig4.update_traces(line_color="#1976D2")

    st.plotly_chart(fig4,width="stretch")

# ------------------------
# AI INSIGHT
# ------------------------

st.divider()

st.subheader("🤖 AI Marketing Recommendation")

best_campaign = (
    df.groupby("Campaign")["Revenue"]
    .sum()
    .idxmax()
)

best_product = (
    df.groupby("Product")["Revenue"]
    .sum()
    .idxmax()
)

best_platform = (
    df.groupby("Platform")["Revenue"]
    .sum()
    .idxmax()
)

highest_sale = df["Revenue"].max()

st.success(f"""

🏆 **Best Campaign:** {best_campaign}

📦 **Best Product:** {best_product}

📱 **Best Platform:** {best_platform}

💰 **Highest Revenue:** ${highest_sale:,.0f}

### 💡 AI Recommendation

• Increase advertising budget for **{best_campaign}**

• Focus more marketing on **{best_platform}**

• Promote **{best_product}** using Video and Carousel content

• Monitor campaigns with ROAS below the average and optimize or pause them.

""")

# ------------------------
# DATASET
# ------------------------

with st.expander("📄 Marketing Dataset"):

    st.dataframe(df,width="stretch")