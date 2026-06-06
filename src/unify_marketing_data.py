import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

facebook = pd.read_csv(
    os.path.join(BASE_DIR, "data", "01_facebook_ads.csv")
)

google = pd.read_csv(
    os.path.join(BASE_DIR, "data", "02_google_ads.csv")
)

tiktok = pd.read_csv(
    os.path.join(BASE_DIR, "data", "03_tiktok_ads.csv")
)

# Add platform names
facebook["platform"] = "Facebook"
google["platform"] = "Google"
tiktok["platform"] = "TikTok"

# Standardize spend column
google.rename(columns={"cost": "spend"}, inplace=True)
tiktok.rename(columns={"cost": "spend"}, inplace=True)

# Keep common fields
facebook_clean = facebook[
    [
        "date",
        "platform",
        "campaign_name",
        "impressions",
        "clicks",
        "spend",
        "conversions"
    ]
]

google_clean = google[
    [
        "date",
        "platform",
        "campaign_name",
        "impressions",
        "clicks",
        "spend",
        "conversions"
    ]
]

tiktok_clean = tiktok[
    [
        "date",
        "platform",
        "campaign_name",
        "impressions",
        "clicks",
        "spend",
        "conversions"
    ]
]

# Combine datasets
combined = pd.concat(
    [facebook_clean, google_clean, tiktok_clean],
    ignore_index=True
)

# Create KPI metrics
combined["CTR"] = (
    combined["clicks"] / combined["impressions"]
) * 100

combined["CPC"] = (
    combined["spend"] / combined["clicks"]
)

os.makedirs(
    os.path.join(BASE_DIR, "outputs"),
    exist_ok=True
)

combined.to_csv(
    os.path.join(BASE_DIR, "outputs", "marketing_unified.csv"),
    index=False
)

print("Unified dataset created successfully!")
print(combined.head())
print("\nShape:", combined.shape)