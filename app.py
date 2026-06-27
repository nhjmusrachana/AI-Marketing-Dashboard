import streamlit as st

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="AI Marketing Analytics",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------------
# BLUE OCEAN THEME
# -------------------------------------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(180deg,#F5FBFF,#EAF6FF);
}

/* Sidebar */
[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#0B4F8C,#1976D2);
}

[data-testid="stSidebar"] *{
    color:white;
}

/* Main Title */
.main-title{
    font-size:55px;
    font-weight:800;
    color:#0B4F8C;
}

/* Subtitle */
.subtitle{
    font-size:22px;
    color:#4B6584;
}

/* Feature Cards */
.feature{
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 8px 20px rgba(0,0,0,.08);
    margin-bottom:20px;
    transition:0.3s;
}

.feature:hover{
    transform:translateY(-5px);
    box-shadow:0px 15px 30px rgba(0,0,0,.15);
}

.footer{
    text-align:center;
    color:gray;
    padding-top:20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# HERO SECTION
# -------------------------------------------------------

st.markdown("""
<div class="main-title">
📊 AI Marketing Analytics
</div>

<div class="subtitle">
Transform marketing data into actionable business insights using Artificial Intelligence.
</div>
""", unsafe_allow_html=True)

st.write("")

# -------------------------------------------------------
# INTRODUCTION
# -------------------------------------------------------

st.info("""
## 👋 Welcome

This portfolio project demonstrates the practical skills of an **AI Specialist** and **Data Analyst**.

### Key Capabilities

- 📈 Marketing Data Analytics
- 🤖 AI Business Intelligence
- 📊 Interactive Dashboards
- 💰 Revenue & Sales Analysis
- 🎯 Campaign Performance Tracking
- 📦 Product Performance Analysis
- 📱 Platform Comparison
- 📑 Automated Reporting
- 💡 AI-Based Recommendations
""")

st.write("")

# -------------------------------------------------------
# FEATURES
# -------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div class="feature">

# 📊 Dashboard

Professional marketing dashboard featuring:

✔ Executive KPI Cards

✔ Revenue Monitoring

✔ Orders Overview

✔ Campaign Analysis

✔ Product Performance

✔ Platform Comparison

✔ Interactive Charts

✔ Marketing Filters

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="feature">

# 🤖 AI Intelligence

Artificial Intelligence features include:

✔ Business Insights

✔ Marketing Recommendations

✔ Best Campaign Detection

✔ ROAS Analysis

✔ Sales Analytics

✔ Trend Prediction

✔ Performance Reports

✔ Decision Support

</div>
""", unsafe_allow_html=True)

st.write("")

# -------------------------------------------------------
# PROJECT MODULES
# -------------------------------------------------------

st.subheader("🚀 Project Modules")

progress = 100
st.progress(progress)

col1, col2 = st.columns(2)

with col1:
    st.success("""
📊 Dashboard

Complete interactive dashboard
""")

    st.success("""
📈 Sales Analytics

Advanced sales analysis
""")

with col2:
    st.success("""
🤖 AI Insights

AI-powered business recommendations
""")

    st.success("""
📄 Reports

Professional business reporting
""")

st.write("")

# -------------------------------------------------------
# TECHNOLOGY STACK
# -------------------------------------------------------

st.subheader("🛠 Technology Stack")

st.markdown("""
- 🐍 Python
- 📊 Streamlit
- 📈 Plotly
- 🐼 Pandas
- 🔢 NumPy
- 🤖 Artificial Intelligence
- 📉 Data Analytics
- 💼 Business Intelligence
""")

st.write("")

# -------------------------------------------------------
# QUICK START
# -------------------------------------------------------

st.success("""
### 👈 Navigation Guide

Use the left sidebar to explore:

📊 Dashboard

📈 Sales Analytics

🤖 AI Insights

📄 Reports

Each module is designed to simulate a real-world AI Marketing Analytics platform.
""")

st.divider()

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------

st.markdown("""
<div class="footer">

© 2026 AI Marketing Analytics

Built with ❤️ using Python, Streamlit, Plotly & Artificial Intelligence

</div>
""", unsafe_allow_html=True)