import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset

dataset = sns.load_dataset('titanic')

# Display the first few rows of the dataset

print(dataset.head(10))

# create a histogram based on the age in the dataset and save that in a PNG file with name hist_titanic.png inside the charts folder under the current folder

sns.histplot(dataset['age'], bins=30, kde=True)
plt.title('Age of People')
plt.savefig('charts/hist_titanic.png')
plt.close()

# Handilng missing value examples

dataset['age'].fillna(dataset['age'].mean(), inplace=True)

print(dataset.head(10))

print(dataset[dataset['embarked'].isnull()])
print('Printing unique values : ',dataset['embarked'].unique())

dataset['embarked'].fillna(dataset[dataset['embarked'].notna()]['embarked'].mode()[0], inplace=True)

print(dataset[dataset['embarked'].isna()])

# Handling imbalanced dataset example with up sampling
import numpy as np
import pandas as pd

np.random.seed(200)

# Creating data frame with 2 classes
n_samples = 1000
class_0_ratio = 0.9
n_class_0 = int(n_samples * class_0_ratio)
n_class_1 = n_samples - n_class_0

# Create data frame with imbalanced dataset

class_0 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=n_class_0),
    'feature_2': np.random.normal(loc=0, scale=1, size=n_class_0),
    'target': [0] * n_class_0
})

class_1 = pd.DataFrame({
    'feature_1': np.random.normal(loc=2, scale=1, size=n_class_1),
    'feature_2': np.random.normal(loc=2, scale=1, size=n_class_1),
    'target': [1] * n_class_1
})

print(class_0)
print(class_1)

# Combine the two data frames

balanced_dataset = pd.concat([class_0, class_1]).reset_index(drop=True)

print(balanced_dataset)

df_minority = balanced_dataset[balanced_dataset['target'] == 1]
df_majority = balanced_dataset[balanced_dataset['target'] == 0]

print(df_minority.count())
print(df_majority.count())

# Upsampling the minority class
from sklearn.utils import resample

# upsample the minority class using resample

df_minority_upsampled = resample(df_minority, replace=True, n_samples=len(df_majority), random_state=42)

print('Up sampled : ', df_minority_upsampled.count())
print('Up sampled : ', df_minority_upsampled.head())

# Combine the upsampled minority class with the original majority class
df_upsampled = pd.concat([df_majority, df_minority_upsampled])
print('Up sampled : ', df_upsampled['target'].value_counts())

# Down sampling the majority class

df_majority_downsampled = resample(df_majority, replace=False, n_samples=len(df_minority), random_state=42)

print('Down sampled : ', df_majority_downsampled.count())
print('Down sampled : ', df_majority_downsampled.head())

# Combine the downsampled majority class with the original minority class

df_downsampled = pd.concat([df_minority, df_majority_downsampled])
print('Down sampled : ', df_downsampled['target'].value_counts())

# SMOTE (Synthetic Minority Over-sampling Technique)

from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)

X_smote, y_smote = smote.fit_resample(balanced_dataset[['feature_1', 'feature_2']], balanced_dataset['target'])

print('SMOTE : ', pd.DataFrame(X_smote, columns=['feature_1', 'feature_2']).head())

# Using SMOTE by using a different library
from sklearn.datasets import make_classification
import pandas as pd
import matplotlib.pyplot as plt

X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, n_clusters_per_class=1, weights=[0.90], random_state=12)

print('Printing values from make_classification : ', X,y)

df1 = pd.DataFrame(X, columns=['f1', 'f2'])
df2 = pd.DataFrame(y, columns=['target'])
final_df = pd.concat([df1, df2], axis=1)

print('Printing values from SMOTE : ', final_df['target'].value_counts())

plt.scatter(final_df['f1'], final_df['f2'], c=final_df['target'])
plt.savefig('charts/before_smnote.png')
plt.close()

smote = SMOTE(random_state=42)

X_smote, y_smote = smote.fit_resample(final_df[['f1','f2']], final_df['target'])

print('SMOTE : ', pd.DataFrame(X_smote, columns=['feature_1', 'feature_2']).head())
df3 = pd.DataFrame(X_smote, columns=['f1', 'f2'])
df4 = pd.DataFrame(y_smote, columns=['target'])

final_df_oversampled = pd.concat([df3, df4], axis=1)

plt.scatter(final_df_oversampled['f1'], final_df_oversampled['f2'], c=final_df_oversampled['target'])
plt.savefig('charts/after_smnote.png')
plt.close()

# Finding outliers from a list of marks

marks = [4, 16, 18, 85, 92, 78, 95, 88, 80, 82, 90, 84, 86, 89, 94, 79, 81, 87, 200, 125]
minimum, maximum, median, Q1, Q3 = np.quantile(marks,[0,1,0.5,0.25,0.75])

print(minimum, maximum, Q1, Q3, median)

IQR = Q3 - Q1

print('IQR : ', IQR)

lower_bound = Q1 - 1.5 * IQR

upper_bound = Q3 + 1.5 * IQR

outliers = [x for x in marks if x < lower_bound or x > upper_bound]

print('Outliers : ', outliers)
print('lower bound : ', lower_bound)
print('upper bound : ', upper_bound)

sns.boxplot(marks)

plt.title('Sample Box Plot')
plt.savefig('charts/box_plot_find_outliers.png')
plt.close()

# Implementing data encoding

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# Creatre a dataframe with a list of colors

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'green', 'yellow', 'red']

df = pd.DataFrame(colors, columns=['color'])

print(df.head())
# Apply one hot encoder to the above data frame

encoder = OneHotEncoder()

encoded = encoder.fit_transform(df[['color']]).toarray()

encoded_df = pd.DataFrame(encoded, columns = encoder.get_feature_names_out())

print(encoded_df)

# Apply label encoder to the above data frame

le = LabelEncoder()

df['color_encoded'] = le.fit_transform(df['color'])

print(df)

# Apply Ordinal encoding to the above data frame

from sklearn.preprocessing import OrdinalEncoder

# Create a dataframe containing educational level

education = ['high school', 'Graduate','Post Graduate', 'PHD', 'high school', 'PHD', 'Graduate', 'PHD']

df['education'] = education

oe = OrdinalEncoder()

df['education_encoded_ordinal'] = oe.fit_transform(df[['education']])

print(df)



