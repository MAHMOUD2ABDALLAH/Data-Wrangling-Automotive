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
