import pandas as pd
import matplotlib.pyplot as plt


# ==========================
# Task A - Load Dataset
# ==========================

df = pd.read_csv(
    "data/cloud_usage_dataset.csv",
    parse_dates=["date"]
)


print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 10 Rows:")
print(df.head(10))


# Missing value check

print("\nMissing Values:")
print(df.isnull().sum())


# Handle missing rows

df = df.dropna()


print("\nTotal Cost:")
print(df["cost_usd"].sum())


print("\nAverage Daily Cost:")

daily_cost = df.groupby("date")["cost_usd"].sum()

print(daily_cost.mean())



# ==========================
# Task B - CO2 Calculation
# ==========================


df["co2e_kg"] = (
    (df["cpu_hours"] * 0.0002)
    +
    (df["storage_gb"] * 0.0006 / 30)
    +
    (df["data_transfer_gb"] * 0.001)
)


print("\nTotal CO2e:")
print(df["co2e_kg"].sum())


print("\nCO2 by service:")
print(
    df.groupby("service_type")["co2e_kg"].sum()
)


print("\nCO2 by team:")
print(
    df.groupby("team")["co2e_kg"].sum()
)



# ==========================
# Task C - Visualization
# ==========================


# Daily CO2 line chart

daily_co2 = df.groupby("date")["co2e_kg"].sum()

plt.figure(figsize=(10,5))

plt.plot(
    daily_co2.index,
    daily_co2.values
)

plt.xlabel("Date")
plt.ylabel("CO2e KG")
plt.title("Daily Carbon Emission")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "data/daily_co2_chart.png"
)

plt.close()



# Region CO2 bar chart


region_co2 = df.groupby("region")["co2e_kg"].sum()


plt.figure(figsize=(8,5))

plt.bar(
    region_co2.index,
    region_co2.values
)


plt.xlabel("Region")
plt.ylabel("CO2e KG")
plt.title("Carbon Emission By Region")


plt.tight_layout()

plt.savefig(
    "data/region_co2_chart.png"
)

plt.close()



# ==========================
# Task D - Save Dataset
# ==========================


df.to_csv(
    "data/cloud_usage_enriched.csv",
    index=False
)


print("\nCompleted Successfully")