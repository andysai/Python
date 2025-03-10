# -*- coding: utf-8 -*-
"""Descriptive Statistics II - EXERCISE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aZTCamI8BVVZLOpRkVwUWZ_VQ6oriq3n

---
# Crash Course Python for Data Science - Intro to Statistics
---
# 02 - Descriptive Statistics II
---

##STOP! BEFORE GOING ANY FURTHER...

1. Click "File" at the top.
2. Then, "Save a Copy in Drive."
3. Change the file name to something else, so you can differenciate it from the workshop notes. For example, put your name at the beggining: "Grace_Stats 2-EXERCISE".

Now you have a copy of this notebook in your Drive account. This is the copy you'll edit and save for your own archives. You can come back to it as many times as you like to practice again! Be sure to do this for ***every*** exercise!

Remember, this exercises are open book, open neighbour, open everything! Try to do them on your own before looking at the solution samples. Join the slack channel to ask your questions. I will be in the channel too!

### Import Numpy, pandas, and matplotlib
"""

import numpy as np, pandas as pd, matplotlib.pyplot as plt

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

print('Libraries imported!')

"""### Import the data in the CSV file
Today you'll be working with the tips dataset from the lecture. You can find the data [here](https://raw.githubusercontent.com/axrd/datasets/master/tipdata.csv). 
"""

# Run this cell to import the data

df = pd.read_csv('https://raw.githubusercontent.com/axrd/datasets/master/tipdata.csv', index_col=0)

"""### Print out the first 10 rows"""

### YOUR CODE GOES HERE ###
df.head(10)

#@title Double click here for a sample solution
df.head(10)

"""### Print out the last 10 rows"""

### YOUR CODE GOES HERE ###
df.tail(10)

#@title Double click here for a sample solution

df.tail(10)

"""### Examine total bill and tip to identify any correlation. Calculate the correlation coefficient, AND plot both features as a scatterplot."""

### YOUR CODE GOES HERE ###
df['tip'].corr(df['total_bill'])

#@title Double click here for a sample solution

df['tip'].corr(df['total_bill'])

### YOUR CODE GOES HERE FOR THE PLOT ###
df.plot.scatter(x='total_bill', y='tip')

#@title Double click here for a sample solution

df.plot.scatter(x='total_bill', y='tip');

"""### Examine size and total bill to identify any correlation. Calculate the correlation coefficient, AND plot both features as a scatterplot."""

### YOUR CODE GOES HERE ###
df['size'].corr(df['total_bill'])

#@title Double click here for a sample solution

df['size'].corr(df['total_bill'])

### YOUR CODE GOES HERE FOR THE PLOT ###
df.plot.scatter(x='size', y='total_bill')

#@title Double click here for a sample solution

df.plot.scatter(x='size', y='total_bill');

"""### Examine size and tip to identify any correlation. Calculate the correlation coefficient, AND plot both features as a scatterplot."""

### YOUR CODE GOES HERE ###
df['size'].corr(df['tip'])

#@title Double click here for a sample solution

df['size'].corr(df['tip'])

### YOUR CODE GOES HERE FOR THE PLOT ###
df.plot.scatter(x='size', y='tip')

#@title Double click here for a sample solution

df.plot.scatter(x='size', y='tip');