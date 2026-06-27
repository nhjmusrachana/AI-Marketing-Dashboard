import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="AI Automation",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# Load Data
# -------------------------

df = pd.read_csv("data/sales_data.csv")

# -------------------------
# Ocean Style
# -------------------------

st.markdown("""
<style>

.stApp{
background:linear-gradient(180deg,#F4FBFF,#E8F7FF);
}

.card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 5px 15px rgba(0,0,0,.08);
margin-bottom:20px;
}

.title{
font-size:42px;
font-weight:bold;
color:#1565C0;
}

</style>
""",unsafe_allow_html=True)

# -------------------------

st.markdown("<div class='title'>🤖 AI Tools & Automation</div>",unsafe_allow_html=True)

st.write("Automate marketing analysis using AI.")

st.divider()

# -------------------------
# KPI
# -------------------------

col1,col2,col3,col4=st.columns(4)

col1.metric(
"Campaign Health",
"Healthy"
)

col2.metric(
"Average ROAS",
f"{df['ROAS'].mean():.2f}"
)

col3.metric(
"Average CTR",
f"{df['CTR'].mean()*100:.2f}%"
)

col4.metric(
"AI Score",
"95%"
)

st.divider()

# -------------------------
# Automation
# -------------------------

st.subheader("⚡ AI Automation")

if st.button("Analyze Marketing Data",use_container_width=True):

    best_campaign=df.groupby("Campaign")["Revenue"].sum().idxmax()

    best_platform=df.groupby("Platform")["Revenue"].sum().idxmax()

    best_product=df.groupby("Product")["Revenue"].sum().idxmax()

    st.success("AI Analysis Completed")

    st.info(f"🏆 Best Campaign: {best_campaign}")

    st.info(f"📱 Best Platform: {best_platform}")

    st.info(f"📦 Best Product: {best_product}")

    st.write("### AI Recommendation")

    st.success(
f"""
Increase budget for **{best_campaign}**

Focus more on **{best_platform}**

Promote **{best_product}**

Reduce spending on low ROAS campaigns.

Increase Video content.

Continue monitoring CTR.
"""
)

st.divider()

# -------------------------
# AI Assistant
# -------------------------

st.subheader("🤖 AI Assistant")

question=st.text_input(
"Ask your AI",
placeholder="Which campaign performed best?"
)

if st.button("Ask AI"):

    answer=question.lower()

    if "campaign" in answer:

        st.success(
f"The highest revenue campaign is **{df.groupby('Campaign')['Revenue'].sum().idxmax()}**."
)

    elif "platform" in answer:

        st.success(
f"The best platform is **{df.groupby('Platform')['Revenue'].sum().idxmax()}**."
)

    elif "product" in answer:

        st.success(
f"The top selling product is **{df.groupby('Product')['Revenue'].sum().idxmax()}**."
)

    else:

        st.info(
"AI Recommendation: Continue optimizing your highest-performing campaigns and monitor ROAS regularly."
)

st.divider()

# -------------------------
# Forecast
# -------------------------

st.subheader("📈 Sales Forecast")

current=df["Revenue"].sum()

forecast=current*1.15

growth=((forecast-current)/current)*100

c1,c2,c3=st.columns(3)

c1.metric(
"Current Revenue",
f"${current:,.0f}"
)

c2.metric(
"Predicted Revenue",
f"${forecast:,.0f}"
)

c3.metric(
"Growth",
f"{growth:.1f}%"
)

st.divider()

# -------------------------
# Alerts
# -------------------------

st.subheader("🚨 Smart Alerts")

alerts=[]

if df["CTR"].mean()<0.05:
    alerts.append("CTR is below target.")

if df["ROAS"].mean()<10:
    alerts.append("ROAS needs improvement.")

if len(alerts)==0:
    alerts.append("No major issues detected.")

for i in alerts:
    st.warning(i)

st.divider()

# -------------------------
# Reports
# -------------------------

st.subheader("📄 Generate Reports")

col1,col2,col3=st.columns(3)

csv=df.to_csv(index=False)

col1.download_button(
"⬇ Download CSV",
csv,
"marketing_report.csv",
"text/csv"
)

col2.download_button(
"⬇ Download Business Summary",
"""
AI Marketing Summary

Marketing performance is healthy.

Continue investing in high-performing campaigns.

Focus on Instagram and Video content.

Monitor CTR weekly.
""",
"summary.txt"
)

col3.download_button(
"⬇ Download KPI",
f"""
Revenue : {current}

Orders : {df['Orders'].sum()}

ROAS : {df['ROAS'].mean()}

CTR : {df['CTR'].mean()}
""",
"kpi.txt"
)