import matplotlib.pyplot as plt

# Create a simple figure and axis
x_axis = [1,2,3,4,5]
y_axis = [10,-20,25,-30,35]
plt.plot(x_axis, y_axis, color="red", linestyle="--", marker="o", linewidth=3, markersize=10)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.title("Simple plot")
plt.savefig("SimplePlot.png", dpi=300)
plt.close()

x_axis = [1,2,3,4,5]
y_axis = [10,-20,25,-30,35]
z_axis = [1,-2,2,-3,3]
y1_axis = [4,-2,5,0,9]
z1_axis = [1,-20,2,-30,3]
plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.plot(x_axis, y_axis, color="red", linestyle="--", marker="o", linewidth=3, markersize=10)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.title("Plot 1")

plt.subplot(2,2,2)
plt.plot(x_axis, z_axis, color="blue", linestyle="solid", marker="o", linewidth=3, markersize=10)
plt.xlabel("x axis")
plt.ylabel("z axis")
plt.grid(True)
plt.title("Plot 2")

plt.subplot(2,2,3)
plt.plot(x_axis, y1_axis, color="green", linestyle="-", marker="o", linewidth=3, markersize=10)
plt.xlabel("x axis")
plt.ylabel("z axis")
plt.grid(True)
plt.title("Plot 3")

plt.subplot(2,2,4)
plt.plot(x_axis, z1_axis, color="yellow", linestyle="-.", marker="o", linewidth=3, markersize=10)
plt.xlabel("x axis")
plt.ylabel("z axis")
plt.grid(True)
plt.title("Plot 4")

plt.savefig("MultiPlot.png", dpi=300)
plt.close()

#Line plot with multiple series

x_axis = [1,2,3,4,5]
series1_y_axis = [10,20,30,40,50]
series2_y_axis = [5,15,25,35,45]
plt.plot(x_axis, series1_y_axis, color="red", label="Series 1")
plt.plot(x_axis, series2_y_axis, color="blue", label="Series 2")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.grid(True)
plt.title("Line plot with multiple series")
plt.savefig("MultiSeriesPlot.png", dpi=300)
plt.close()
#Bar plot

x_axis = [5,9,2,8,1]
y_axis = [10,20,30,40,50]
plt.bar(x_axis, y_axis, color="green")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.savefig("BarPlot.png", dpi=300)
plt.close()

#Scatter plot
x_axis = [1,2,3,4,5]
y_axis = [10,20,25,30,35]
plt.scatter(x_axis, y_axis, color="red")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.savefig("ScatterPlot.png", dpi=300)
plt.close()

#Pie chart

labels = ["Python", "Java", "C++", "JavaScript", "Ruby"]
sizes = [10, 45, 5, 35, 5]
explode = (0, 0.3, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%", shadow=False, startangle=90)
plt.axis("equal")
plt.savefig("PiChartPlot.png", dpi=300)
plt.close()

#3D plot

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
x_axis = [1,2,3,4,5]
y_axis = [10,20,30,40,50]
z_axis = [1,2,3,4,5]
ax.scatter(x_axis, y_axis, z_axis, color="red")
plt.savefig("3DPlot.png", dpi=300)
plt.close()

#Box plot

data = [1,2,3,4,5,6,7,8,9,10]
plt.boxplot(data)
plt.savefig("BoxPlot.png", dpi=300)
plt.close()

#Histogram

data = [1,2,3,4,5,6,7,8,9,10]
plt.hist(data, bins=5)
plt.savefig("HistogramPlot.png", dpi=300)
plt.close()

#Violin plot

# data = [1,2,3,4,5,6,7,8,9,10]
# plt.violinplot(data)
# plt.savefig("ViolinPlot.png", dpi=300)

#Heatmap

import numpy as np

data = np.random.rand(10, 10)
plt.imshow(data, cmap=plt.cm.hot)
plt.colorbar()
plt.savefig("HeatmapPlot.png", dpi=300)
plt.close()

#Contour plot

x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.contourf(X, Y, Z, cmap=plt.cm.jet)
plt.colorbar()
plt.savefig("ContourPlot.png", dpi=300)
plt.close()

#Quiver plot

# x = np.linspace(-3, 3, 200)
# y = np.linspace(-3, 3, 200)
# X, Y = np.meshgrid(x, y)
# U = np.sin(X)
# V = np.cos(Y)
# plt.quiver(X, Y, U, V)
# plt.savefig("QuiverPlot.png", dpi=300)

import pandas as pd

SalesData = pd.read_csv("SalesData.csv")
SalesData_GroupBy_Product = SalesData.groupby("Product ID")["Total Revenue"].sum()
SalesData_GroupBy_Product.plot(kind="bar", color="teal")
plt.savefig("SalesDataPlot.png", dpi=300)
# x = np.linspace(-3, 3, 200)
# y = np.linspace(-3, 3, 200)
# X, Y = np.meshgrid(x, y)
# U = np.sin(X)
# V = np.cos(Y)
# plt.streamplot(X, Y, U, V)
# plt.savefig("StreamPlot.png", dpi=300)

