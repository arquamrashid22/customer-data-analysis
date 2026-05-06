import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customers-1000.csv")

# -----------------------------
# Basic Exploration
# -----------------------------
print(df.head())
print(df.columns)
print("Total rows:", len(df))

# -----------------------------
# Top Countries
# -----------------------------
top_countries = df["Country"].value_counts().head()
print("\nTop Countries:\n", top_countries)

# -----------------------------
# Filter India Data
# -----------------------------
india_df = df[df["Country"] == "India"]
print("\nIndia Data:\n", india_df.head())

# -----------------------------
# Top First Names in India
# -----------------------------
top_names = india_df["First Name"].value_counts().head()
print("\nTop First Names in India:\n", top_names)

# -----------------------------
# Sorting
# -----------------------------
print("\nSorted by First Name:\n", df.sort_values(by="First Name").head())
print("\nIndia Sorted by Last Name:\n", india_df.sort_values(by="Last Name").head())

# -----------------------------
# Visualization 1: Top Countries
# -----------------------------
top_countries.plot(kind="bar")

plt.title("Top 5 Countries by Customers")
plt.xlabel("Country")
plt.ylabel("Count")

plt.show()

# -----------------------------
# Visualization 2: Top Names in India
# -----------------------------
top_names.plot(kind="bar")

plt.title("Top First Names in India")
plt.xlabel("First Name")
plt.ylabel("Frequency")

plt.show()

# -----------------------------
# Dynamic Insights
# -----------------------------
top_country = df["Country"].value_counts().idxmax()
top_country_count = df["Country"].value_counts().max()

top_name = india_df["First Name"].value_counts().idxmax()
top_name_count = india_df["First Name"].value_counts().max()

print("\n--- Insights ---")
print(f"The country with highest number of customers is {top_country} with {top_country_count} records")
print(f"The most common first name in India is {top_name} appearing {top_name_count} times")
print("Some names appear multiple times showing repetition in dataset")
print("Data distribution across countries is uneven")