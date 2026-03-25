# Unemployment Analysis using Python

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("unemployment_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Sort data
df = df.sort_values(by='Date')

# Take smaller sample for speed
df = df.head(100)

# 📊 Graph 1: Overall Trend
plt.figure(figsize=(8,4))
plt.plot(df['Date'], df['Estimated Unemployment Rate (%)'])
plt.title("Overall Unemployment Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("overall_trend.png")
plt.close()


# 📊 Graph 2: Top 3 States Comparison (light version)
top_states = df['Region'].unique()[:3]

for state in top_states:
    state_data = df[df['Region'] == state]
    plt.plot(state_data['Date'], state_data['Estimated Unemployment Rate (%)'], label=state)

plt.title("Top 3 States Comparison")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("state_comparison.png")
plt.close()

print("Graphs generated successfully!")
