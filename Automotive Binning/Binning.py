from asyncio.windows_events import NULL
from fileinput import filename
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print(
    "_________________________________________ Getting started with Data Wrangling __________________________________________\n"
)
# filename which is auto.csv in the repository
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
headers = [
    "symboling",
    "normalized-losses",
    "make",
    "fuel-type",
    "aspiration",
    "num-of-doors",
    "body-style",
    "drive-wheels",
    "engine-location",
    "wheel-base",
    "length",
    "width",
    "height",
    "curb-weight",
    "engine-type",
    "num-of-cylinders",
    "engine-size",
    "fuel-system",
    "bore",
    "stroke",
    "compression-ratio",
    "horsepower",
    "peak-rpm",
    "city-mpg",
    "highway-mpg",
    "price",
]

print("verifying headers\n")
df = pd.read_csv(filename, names=headers)
print(df.head())

print("replace '?' to NaN\n")
df.replace("?", np.nan, inplace=True)
print(df.head(5))

print("Evaluating for Missing Data\n")
missing_data = df.notnull()
print(missing_data.head(5))

print("Count missing values in each column\n")
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")


print("Replace NaN in 'normalized-losses' column \n")
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
df["normalized-losses"] = df["normalized-losses"].replace(np.nan, int(avg_norm_loss))
print(df["normalized-losses"])

print("Replace NaN in  'bore' column\n")
avg_bore = df["bore"].astype("float").mean(axis=0)
df["bore"] = df["bore"].replace(np.nan, avg_bore)
print(df["bore"])

print("Replace NaN in 'stroke' column\n")
avg_stroke = df["stroke"].astype("float").mean(axis=0)
df["stroke"] = df["stroke"].replace(np.nan, avg_stroke)
print(df["stroke"])

print("Replace NaN in 'horsepower' column\n")
avg_horsepower = df["horsepower"].astype("float").mean(axis=0)
df["horsepower"] = df["horsepower"].replace(np.nan, avg_horsepower)
print(df["horsepower"])


print("Use the Pandas method 'cut' to segment the 'horsepower' column into 3 bins")
df["horsepower"] = df["horsepower"].astype(int, copy=True)
plt.hist(df["horsepower"])
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
plt.show()

print("Applying 3 bins spaces by using 4 dividers")
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
print(bins)

print(
    "group names & Apply the function 'cut' to determine what each value of df['horsepower'] belongs to"
)
group_names = ["Low", "Medium", "High"]
df["horsepower-binned"] = pd.cut(
    df["horsepower"], bins, labels=group_names, include_lowest=True
)
print(df[["horsepower", "horsepower-binned"]].head(20))

print("Now we successfully narrowed down the intervals from 59 to 3")
plt.bar(group_names, df["horsepower-binned"].value_counts())
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
plt.show()
