import pandas as pd

# Reading data from a HTML file
dataFrame = pd.read_html("salesData.html", header=0)
print(dataFrame)

url="https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
dataFrame = pd.read_html(url, header=0)

print("=================Reading from wiki first 5 rows=============================")
# Print the first 5 rows
df=dataFrame[0].head(5)
print(df.iloc[:,2:5])

print("=================Reading from wiki last 5 rows=====================================")
# Print the last 5 rows
df=dataFrame[0].tail(5)
print(df.iloc[:,2:5])

print("=================Selecting specific columns===============================================")
# Selecting specific columns
df=dataFrame[0][["Location", "Population"]]
print(df.head(10))

print("=================Filtering Data===============================================")
# Filtering data
df=dataFrame[0][dataFrame[0]["Population"] > 1000000000]
print(df.head(5))

print("=================Sorting Data===============================================")
# Sorting data
df=dataFrame[0].sort_values("Population", ascending=False)
print(df.head(10))

