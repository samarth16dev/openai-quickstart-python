import matplotlib as plt
import numpy as np
import pandas as pd
import requests

print("⚡ Step 1: Fetching mock data via 'requests' API call...")
# Fetching actual mock transaction/price data from a public API
response = requests.get("https://typicode.com")
data = response.json()[:20]  # Grab the first 20 records

print("\n🐼 Step 2: Structuring and cleaning with 'pandas'...")
# Convert JSON raw data into a structured DataFrame
df = pd.DataFrame(data)

# Let's mock up some stock/token prices and volumes for these 20 items
df["price"] = [
    100 + i * 2.5 + (np.sin(i) * 5) for i in range(20)
]  # Generates an upward wavy trend
df["volume"] = [500 + (i * 50) for i in range(20)]
print(df[["id", "title", "price", "volume"]].head())

print("\n🔢 Step 3: Performing mathematical AI features with 'numpy'...")
# Calculate log returns or simple price moving averages using NumPy array math
prices_array = df["price"].to_numpy()
moving_average = np.convolve(prices_array, np.ones(3) / 3, mode="same")
df["moving_avg"] = moving_average

# NumPy quick conditional logic: flag high-value assets
df["signal"] = np.where(df["price"] > 120, "Buy/Hold", "Under Valued")
print(df[["id", "price", "moving_avg", "signal"]].tail())

print("\n📊 Step 4: Visualizing everything with 'matplotlib'...")
plt.figure(figsize=(10, 5))

# Plot the raw price vs the NumPy moving average
plt.plot(df["id"], df["price"], marker="o", label="Raw Asset Price", color="blue")
plt.plot(
    df["id"],
    df["moving_avg"],
    linestyle="--",
    label="3-Period Smooth Trend (NP)",
    color="orange",
)

# Customize the chart
plt.title("AI Data Pipeline Sandbox (Requests -> Pandas -> NumPy -> Matplotlib)")
plt.xlabel("Asset ID")
plt.ylabel("Value (USD)")
plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)

print("📉 Displaying plot... (Close the plot window to finish the script)")
plt.show()
