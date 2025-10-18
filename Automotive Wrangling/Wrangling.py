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


print("Calculate the mean value for the 'normalized-losses' column \n")
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print(df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=False))

print("Calculate the mean value for the 'bore' column\n")
avg_bore = df["bore"].astype("float").mean(axis=0)
print(df["bore"].replace(np.nan, avg_bore, inplace=False))

print(" Replace NaN in 'stroke' column\n")
avg_stroke = df["stroke"].astype("float").mean(axis=0)
df["stroke"].replace(np.nan, avg_stroke, inplace=False)