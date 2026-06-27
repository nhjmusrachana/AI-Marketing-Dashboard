import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="AI Content Generator",
    page_icon="🤖",
    layout="wide"
)

# ==========================
# OCEAN BLUE STYLE
# ==========================

st.markdown("""
<style>

.stApp{
    background:linear-gradient(180deg,#F4FBFF,#E8F6FF);
}

.block-container{
    padding-top:2rem;
}

.title{
    font-size:42px;
    color:#0B5CAD;
    font-weight:bold;
}

.subtitle{
    color:#5F7E9C;
    font-size:18px;
}

.result-box{
    background:white;
    border-radius:15px;
    padding:20px;
    border-left:6px solid #2196F3;
    box-shadow:0px 5px 15px rgba(0,0,0,.08);
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================

st.markdown("<div class='title'>🤖 AI Content Generator</div>", unsafe_allow_html=True)

st.markdown(
"<div class='subtitle'>Generate professional marketing content using AI.</div>",
unsafe_allow_html=True)

st.write("")

# ==========================
# INPUTS
# ==========================

left,right=st.columns([1,1])

with left:

    product=st.text_input(
        "📦 Product Name",
        placeholder="Nike Shoes"
    )

    platform=st.selectbox(
        "📱 Platform",
        [
            "Facebook",
            "Instagram",
            "TikTok"
        ]
    )

    audience=st.selectbox(
        "🎯 Audience",
        [
            "Students",
            "Women",
            "Men",
            "Parents",
            "Everyone"
        ]
    )

with right:

    tone=st.selectbox(
        "😊 Tone",
        [
            "Friendly",
            "Professional",
            "Luxury",
            "Funny",
            "Exciting"
        ]
    )

    promotion=st.text_input(
        "🏷 Promotion",
        placeholder="20% OFF"
    )

    emoji=st.checkbox(
        "Include Emojis",
        value=True
    )

st.divider()

tab1,tab2,tab3,tab4,tab5=st.tabs([
    "📱 Social Caption",
    "🛒 Product Description",
    "📧 Email",
    "📣 CTA",
    "#️⃣ Hashtags"
])

# =====================================
# SOCIAL CAPTION
# =====================================

with tab1:

    if st.button("🚀 Generate Caption",use_container_width=True):

        if product=="":

            st.warning("Please enter product name.")

        else:

            fire="🔥" if emoji else ""
            star="✨" if emoji else ""

            caption=f"""
{fire} {product}

Looking for something amazing?

Introducing our newest {product} specially designed for {audience.lower()}.

🎉 Promotion:
{promotion}

Tone:
{tone}

Shop today before this offer ends!

{star} Available now on {platform}.

#Sale #Marketing #Business #AI
"""

            st.success("Caption Generated!")

            st.text_area(
                "Generated Caption",
                caption,
                height=260
            )

# =====================================
# PRODUCT DESCRIPTION
# =====================================

with tab2:

    if st.button("Generate Product Description",use_container_width=True):

        description=f"""
{product}

Our premium {product} is designed for {audience.lower()} who want quality, comfort and style.

Main Benefits

✔ High Quality

✔ Modern Design

✔ Affordable Price

✔ Perfect Daily Use

Promotion:
{promotion}

Order today while stock lasts.
"""

        st.text_area(
            "Product Description",
            description,
            height=250
        )

# =====================================
# EMAIL
# =====================================

with tab3:

    if st.button("Generate Email",use_container_width=True):

        email=f"""
Subject:
Exclusive Offer on {product}

Dear Customer,

We are excited to introduce our latest {product}.

Promotion:
{promotion}

This offer is available for a limited time.

Thank you for choosing us.

Best Regards,
Marketing Team
"""

        st.text_area(
            "Marketing Email",
            email,
            height=260
        )

# =====================================
# CTA
# =====================================

with tab4:

    if st.button("Generate CTA",use_container_width=True):

        ctas=[
            "Shop Now",
            "Buy Today",
            "Limited Time Offer",
            "Order Before It Ends",
            "Grab Yours Today",
            "Don't Miss Out"
        ]

        for c in ctas:
            st.info(c)

# =====================================
# HASHTAGS
# =====================================

with tab5:

    if st.button("Generate Hashtags",use_container_width=True):

        tags=f"""
#{product.replace(" ","")}

#Marketing

#Business

#Promotion

#Sale

#Trending

#{platform}

#{audience.replace(" ","")}
"""

        st.code(tags)

# ==============================
# HISTORY
# ==============================

st.divider()

st.subheader("📊 Generation Summary")

col1,col2,col3=st.columns(3)

col1.metric("Today's Generation",12)
col2.metric("AI Templates",5)
col3.metric("Last Updated",datetime.now().strftime("%H:%M"))