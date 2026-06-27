import pandas as pd
import random
from datetime import datetime, timedelta

NUM_ROWS = 1000

campaigns = [
    "Summer Sale",
    "Flash Sale",
    "New Arrival",
    "Weekend Deal",
    "Buy 2 Get 1"
]

platforms = [
    "Facebook",
    "Instagram",
    "TikTok"
]

products = [
    "Oversized Hoodie",
    "Cargo Pants",
    "Sneakers",
    "Denim Jacket",
    "Tote Bag"
]

content_types = [
    "Video",
    "Image",
    "Carousel",
    "Reel"
]

start_date = datetime(2026, 4, 1)

rows = []

for _ in range(NUM_ROWS):
    date = start_date + timedelta(days=random.randint(0, 59))
    campaign = random.choice(campaigns)
    platform = random.choice(platforms)
    product = random.choice(products)
    content = random.choice(content_types)

    reach = random.randint(5000, 50000)
    ctr = round(random.uniform(0.02, 0.12), 4)
    clicks = int(reach * ctr)
    conversion_rate = round(random.uniform(0.02, 0.08), 4)
    orders = int(clicks * conversion_rate)

    ad_spend = round(random.uniform(20, 500), 2)
    price = random.randint(20, 60)
    revenue = orders * price
    roas = round(revenue / ad_spend, 2)

    rows.append([
        date.strftime("%Y-%m-%d"),
        campaign,
        platform,
        product,
        content,
        reach,
        clicks,
        orders,
        ad_spend,
        revenue,
        ctr,
        roas
    ])

df = pd.DataFrame(rows, columns=[
    "Date",
    "Campaign",
    "Platform",
    "Product",
    "Content Type",
    "Reach",
    "Clicks",
    "Orders",
    "Ad Spend",
    "Revenue",
    "CTR",
    "ROAS"
])

df.to_csv("data/sales_data.csv", index=False)

print("Dataset generated successfully!")
print(df.head())