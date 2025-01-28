import pandas as pd

data=[1,2,3,4,5]
data1 = {"name":"Kousik", "age":"25", "gender": "Male"}
series=pd.Series(data)
print(series)
series1 = pd.Series(data1)
print(series1)
index = ["var1", "var2", "var3", "var4", "var5"]
series=pd.Series(data, index)
print(series)

# DataFrame example

data = {
    "name": ["John", "Anna", "Peter", "Linda"],
    "age": [25, 30, 28, 22],
    "city": ["New York", "Los Angeles", "Paris", "Tokyo"]
}
dataFrame = pd.DataFrame(data)
print(dataFrame)

# Adding a new column to the DataFrame

dataFrame["country"] = ["USA", "Canada", "France", "Japan"]
print(dataFrame)

# Removing a column from the DataFrame

del dataFrame["country"]
print(dataFrame)

# Changing the data type of a column

dataFrame["age"] = dataFrame["age"].astype(int)
print(dataFrame)

# Filtering rows based on a condition

filtered_data = dataFrame[dataFrame["age"] > 23]
print(filtered_data)

# Sorting rows in ascending order

sorted_data = dataFrame.sort_values(by="age")
print(sorted_data)

# Sorting rows in descending order

sorted_data = dataFrame.sort_values(by="age", ascending=False)
print(sorted_data)

# Merging two DataFrames

data2 = {
    "name": ["Linda", "Peter"],
    "age": [22, 28],
    "city": ["Tokyo", "Paris"]
}
dataFrame2 = pd.DataFrame(data2)
merged_data = pd.concat([dataFrame, dataFrame2])
print(merged_data)

df=pd.read_csv("data.csv")

# Print the first 5 rows
print(df.head(5))

# Print the last 5 rows
print(df.tail(5))

print(df["Name"], df["City"])

# print(df.loc[0][0])
# print(df.loc[0][1])
print(df.iloc[0][1])

# Updating value in dataframe

df["Age"] = df["Age"] + 1
print(df)

print(df.describe())

# Find out missing values

print(df.isnull().sum())

# Filling missing values

df["Address2"].fillna("N/A", inplace=True)
print(df)

print(df.dtypes)

df1 = pd.read_csv("salesData.csv")
print(df1)
print(df1.dtypes)

# Change a column type

df1["Total Revenue"] = df1["Total Revenue"].astype(float)
print(df1)

# Calculate sum of a column

print(df1["Total Revenue"].sum())

df1["Discounted Revenue"] = df1["Total Revenue"] - df1["Total Revenue"] * 0.1
print(df1)

df1.rename(columns={"Total Revenue":"Revenue"}, inplace=True)
print(df1)

# del df1["Discounted Price"]

# Group by a column

grouped_data = df1.groupby("Seller Category")["Revenue"]
print(grouped_data.sum())

grouped_data = df1.groupby(["Seller Category","Sales Location"])["Revenue"].agg(["mean", "sum", "count"])
print(grouped_data)

# merging dataframes

df2 = pd.read_csv("productData.csv")
merged_data = pd.merge(df1, df2, on="Product ID")
print(merged_data)

# Aggregating data
