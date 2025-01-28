import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips)

# Create a scatter plot

sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title('Distance vs Orbital Period')
plt.savefig('ScatterPlot_SeaBorn.png')
plt.close()

# Create a line plot

sns.lineplot(x='total_bill', y='tip', data=tips)
plt.title('Distance vs Orbital Period')
plt.savefig('LinePlot_SeaBorn.png')
plt.close()
# Create a bar plot

sns.barplot(x='day', y='total_bill', data=tips)
plt.title('Day vs Total Bill')
plt.savefig('BarPlot_SeaBorn.png')
plt.close()
# Create a box plot

sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Day vs Total Bill')
plt.savefig('BoxPlot_SeaBorn.png')
plt.close()
# Create a violin plot

sns.violinplot(x='day', y='total_bill', data=tips)
plt.title('Day vs Total Bill')
plt.savefig('ViolinPlot_SeaBorn.png')
plt.close()
# Create a heat map

sns.heatmap(tips.corr(), annot=True)
plt.title('Correlation Heatmap')
plt.savefig('HeatMap_SeaBorn.png')

# Create a pair plot

sns.pairplot(tips)
plt.title('Pair Plot')
plt.savefig('PairPlot_SeaBorn.png')
plt.close()
# Create a count plot

sns.countplot(x='day', data=tips)
plt.title('Count Plot')
plt.savefig('CountPlot_SeaBorn.png')
plt.close()
# Create a swarm plot

sns.swarmplot(x='day', y='total_bill', data=tips)
plt.title('Swarm Plot')
plt.savefig('SwarmPlot_SeaBorn.png')
plt.close()
# Create a strip plot

sns.stripplot(x='day', y='total_bill', data=tips)
plt.title('Strip Plot')
plt.savefig('StripPlot_SeaBorn.png')
plt.close()
# Create a boxen plot

sns.boxenplot(x='day', y='total_bill', data=tips)
plt.title('Boxen Plot')
plt.savefig('BoxenPlot_SeaBorn.png')
plt.close()
# Create a point plot

sns.pointplot(x='day', y='total_bill', data=tips)
plt.title('Point Plot')
plt.savefig('PointPlot_SeaBorn.png')
plt.close()
# Create a violin plot with hue

sns.violinplot(x='day', y='total_bill', hue='sex', data=tips)
plt.title('Violin Plot with Hue')
plt.savefig('ViolinPlot_Hue_SeaBorn.png')
plt.close()
# Create a box plot with hue

sns.boxplot(x='day', y='total_bill', hue='sex', data=tips)
plt.title('Box Plot with Hue')
plt.savefig('BoxPlot_Hue_SeaBorn.png')
plt.close()
# Create a swarm plot with hue

sns.swarmplot(x='day', y='total_bill', hue='sex', data=tips)
plt.title('Swarm Plot with Hue')
plt.savefig('SwarmPlot_Hue_SeaBorn.png')
plt.close()
# Create a strip plot with hue

sns.stripplot(x='day', y='total_bill', hue='sex', data=tips)
plt.title('Strip Plot with Hue')
plt.savefig('StripPlot_Hue_SeaBorn.png')
plt.close()
# Create a boxen plot with hue

sns.boxenplot(x='day', y='total_bill', hue='sex', data=tips)
plt.title('Boxen Plot with Hue')
plt.savefig('BoxenPlot_Hue_SeaBorn.png')
plt.close()
# Create a point plot with hue

sns.pointplot(x='day', y='total_bill', hue='sex', data=tips)
plt.title('Point Plot with Hue')
plt.savefig('PointPlot_Hue_SeaBorn.png')
plt.close()
# Create a violin plot with hue and split

sns.violinplot(x='day', y='total_bill', hue='sex', split=True, data=tips)
plt.title('Violin Plot with Hue and Split')
plt.savefig('ViolinPlot_Hue_Split_SeaBorn.png')
plt.close()
# Create a box plot with hue and split

# sns.boxplot(x='day', y='total_bill', hue='sex', split=True, data=tips)
# plt.title('Box Plot with Hue and Split')
# plt.savefig('BoxPlot_Hue_Split_SeaBorn.png')