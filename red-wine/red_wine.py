import numpy as np
import pandas as pd
from time import time
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

red_wine_quality_file = "../WineDataSets/winequality-red.csv"

red_wine_quality_data = pd.read_csv(red_wine_quality_file, sep=";")

# Display the first five records
display(red_wine_quality_data.head(n=5))
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

print("\nRed Wine Data Set has {} rows and {} columns".format(n_wines, n_columns))
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
