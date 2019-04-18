# %%
import numpy as np
import pandas as pd
from time import time
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

# %%
red_wine_quality_file = "C:\\Github\\Wine-Quality-DS\\WineDataSets\\winequality-red.csv"
red_wine_quality_data = pd.read_csv(red_wine_quality_file, sep=";")

# Display the first five records
# display(red_wine_quality_data.head(n=5))
# red_wine_quality_data.info()

n_wines = red_wine_quality_data.shape[0]
n_columns = red_wine_quality_data.shape[1]

# Number of wines with quality rating above 6
quality_above_6 = red_wine_quality_data.loc[(
    red_wine_quality_data['quality'] > 6)]
n_above_6 = quality_above_6.shape[0]

# Number of wines with qualitu rating between 5 and 6
quality_between_5_and_6 = red_wine_quality_data.loc[(
    (red_wine_quality_data['quality'] >= 5) & (red_wine_quality_data['quality'] <= 6))]
n_between_5_and_6 = quality_between_5_and_6.shape[0]

# Number of wines with quality below 5
quality_below_5 = red_wine_quality_data.loc[(
    red_wine_quality_data['quality'] < 5)]
n_below_5 = quality_below_5.shape[0]

# Percentage of wines with quality rating above 6
above_6_percentage = n_above_6*100/n_wines

# Percentage of wines with quality rating between 5 and 6
between_5_and_6_percentage = n_between_5_and_6*100/n_wines

# Percentage of wines with quality below 5
below_5_percentage = n_below_5*100/n_wines

print("\n====================")
print("Data Set Information")
print("====================")
print("Red Wine Data Set has {} rows and {} columns".format(n_wines, n_columns))
print("Total number of wine data: {}".format(n_wines))
print("Wines with rating 7 and above: {}".format(n_above_6))
print("Wines with rating between 5 and 6: {}".format(n_between_5_and_6))
print("Wines with rating less than 5: {}".format(n_below_5))
print("Percentage of wines with quality 7 and above: {:.2f}%".format(
    above_6_percentage))
print("Percentage of wines with quality bewteen 5 and 6: {:.2f}%".format(
    between_5_and_6_percentage))
print("Percentage of wines with quality below 5: {:.2f}%".format(
    below_5_percentage))
print("\nAdditional Informaiton")
display(np.round(red_wine_quality_data.describe()))

# Display Scatter Plot for Red Wine Quality Data
# %%
pd.plotting.scatter_matrix(red_wine_quality_data,
                           alpha=0.3, figsize=(40, 40), diagonal='kde')


# Display Heat Map for Red Wine Quality Data
# %%
red_wine_correlation = red_wine_quality_data.corr()
plt.figure(figsize=(14, 12))
red_wine_heatmap = sns.heatmap(
    red_wine_correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")


# Visualize the co-relation between pH and fixed Acidity
# Create a new dataframe containing only pH and fixed acidity
# columns to visualize their co-relations
# %%
fixedAcidity_pH_data = red_wine_quality_data[['pH', 'fixed acidity']]


# Initialize a joint-grid with the dataframe, using seaborn library
gridA = sns.JointGrid(x="fixed acidity", y="pH",
                      data=fixedAcidity_pH_data, size=6)

# Draw a regression plot in the grid
gridA = gridA.plot_joint(sns.regplot, scatter_kws={"s": 10})

# Draw a distribution plot in the same grid
gridaA = gridA.plot_marginals(sns.distplot)


# Visualize the co-relation between Fixed Acidity and Citric Acid
# %%
fixedAcidity_citricAcid_data = red_wine_quality_data[[
    'citric acid', 'fixed acidity']]
gridB = sns.JointGrid(x="fixed acidity", y="citric acid",
                      data=fixedAcidity_citricAcid_data, size=6)
gridB = gridB.plot_joint(sns.regplot, scatter_kws={"s": 10})
gridB = gridB.plot_marginals(sns.distplot)


# Visualize the co-relation between Volatile Acidity vs Quality
# %%
volatileAcidity_quality_data = red_wine_quality_data[[
    'quality', 'volatile acidity']]
fig, axs = plt.subplots(ncols=1, figsize=(10, 6))
sns.barplot(x='quality', y='volatile acidity',
            data=volatileAcidity_quality_data, ax=axs)
plt.title('Quality vs Volatile Acidity')

plt.tight_layout()
plt.show()
plt.gcf().clear()


# Visualize the co-relation between Alchol and Quality
# %%
alcohol_quality_data = red_wine_quality_data[['alcohol', 'quality']]
fig, axs = plt.subplots(ncols=1, figsize=(10, 6))
sns.barplot(x='quality', y='alcohol', data=alcohol_quality_data, ax=axs)
plt.title('Quality vs Alcohol')

plt.tight_layout()
plt.show()
plt.gcf().clear()
