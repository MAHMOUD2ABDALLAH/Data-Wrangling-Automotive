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


print("Transform mpg to L/100km")
print(df.head())
if 'city-mpg' in df.columns:
    # Convert and keep in same position
    df['city-mpg'] = 235 / pd.to_numeric(df['city-mpg'], errors='coerce')
    df = df.rename(columns={'city-mpg': 'city-L/100km'})
    
if 'highway-mpg' in df.columns:
    # Convert and keep in same position
    df['highway-mpg'] = 235 / pd.to_numeric(df['highway-mpg'], errors='coerce')
    df = df.rename(columns={'highway-mpg': 'highway-L/100km'})

print(df.head())