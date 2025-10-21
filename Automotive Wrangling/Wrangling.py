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

print("count value types in each column with'.value_counts()'method\n")
print(df["num-of-doors"].value_counts())

print(
    "We can also use the '.idxmax()' method to calculate the most common type automatically\n"
)
print(df["num-of-doors"].value_counts().idxmax())

# replace the missing num-of-doors values by the most frequent
# df["num-of-doors"].replace(np.nan, "four", inplace=True)
# df.dropna(subset=["price"], axis=0, inplace=True)
# df.reset_index(drop=True, inplace=True)
# df.head()

print(" \t Correct data format \n")
print(df.dtypes)

print("convert data types to proper format \n")
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

print(" \t Data types after conversion \n")
print(df.dtypes)

print("Now you finally obtained the cleansed data set with no missing values and with all data in its proper format.")