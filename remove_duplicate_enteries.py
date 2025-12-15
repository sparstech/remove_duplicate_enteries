#I received daily production data from the field. The dataset contains:
# Duplicate records
# Negative production values
# Unrealistic oil rates
#Write a program to:
# Remove duplicate (well, date) entries
# Remove records with negative oil or water production
# Flag oil production above 40,000 bbl/day as "SUSPECT"
import pandas as pd
# Sample data creation for demonstration
data = {
    "well": ["A", "B", "C", "A", "B", "D"],
    "date": ["2023-01-01", "2023-01-01", "2023-01-01", "2023-01-01", "2023-01-01", "2023-01-01"],
    "oil_production": [500, 650, 750, 550, 680, 45],
    "water_production": [45, 67, 89, 48, 72, 9]
}
df = pd.DataFrame(data)
# Remove duplicate (well, date) entries
df = df.drop_duplicates(subset=["well", "date"])
# Remove records with negative oil or water production
df = df[(df["oil_production"] >= 0) & (df["water_production"] >= 0)]
# Flag oil production above 40,000 bbl/day as "SUSPECT"
df["flag"] = df["oil_production"].apply(lambda x: "SUSPECT" if x > 40000 else "NORMAL")
print(df)