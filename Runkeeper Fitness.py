#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:46:36 2020

@author: lamyingxian
"""

#########Analysis of My Runkeeper Fitness Data##########

##Obtain & review raw data

import pandas as pd

#Name the dataset file and create a dataframe
runkeeper = pd.read_csv('/Users/lamyingxian/Dropbox/Data Science Course/Projects/My Cardio Activities - Runkeeper/cardioActivities.csv',parse_dates=['Date'],index_col='Date')

#Brief look at the data
runkeeper.head()

#Summary of the data
runkeeper.info()


##Data Preprocessing

#Define list of columns to be deleted
col_deleted = ['Activity Id','Route Name','Average Heart Rate (bpm)','Friend\'s Tagged','Notes','GPX File'] 

#Delete unnecessary columns
runkeeper.drop(col_deleted,axis=1,inplace=True)

#Check the columns to ensure the unnecessary columns are deleted
runkeeper.columns
#Count types of training activities
runkeeper['Type'].value_counts()

#Check any missing values 
runkeeper.isnull().sum()

##Dealing with missing values for each training activity type (filling with median)
median_running = runkeeper[runkeeper['Type'] == 'Running']['Distance (km)'].median()
median_running #3.5
runkeeper['Distance (km)'].fillna(median_running,inplace=True)

median_walking = runkeeper[runkeeper['Type'] == 'Walking']['Distance (km)'].median()
median_walking #1.62
runkeeper['Distance (km)'].fillna(median_walking,inplace=True)

median_cycling = runkeeper[runkeeper['Type'] == 'Cycling']['Distance (km)'].median()
median_cycling #6.52
runkeeper['Distance (km)'].fillna(median_cycling,inplace=True)

#Check any missing values again
runkeeper.isnull().sum()


## Plot Running Data

# Import matplotlib, set style and ignore warning
import matplotlib.pyplot as plt
%matplotlib inline
import warnings
plt.style.use('ggplot')
warnings.filterwarnings(
    action='ignore', module='matplotlib.figure', category=UserWarning,
    message=('This figure includes Axes that are not compatible with tight_layout, so results might be incorrect.')
)

# Choosing only running for analysis
df_run = runkeeper[runkeeper['Type'] == 'Running'].copy()

#Prepare data subsetiing period from 2014 to 2020
runs_subset_2014_2020 = df_run['2020':'2014']

runs_subset_2014_2020.plot(subplots=True,
                           sharex=False,
                           figsize=(12,16),
                           linestyle='none',
                           marker='o',
                           markersize=5,
                          )

# Show plot
plt.show()

##Running Statistics
#Prepare data subsetiing period from 2014 to 2020
runs_subset_2014_2020 = df_run['2020':'2014']

#Calculate annual statistics (My average run in last 7 years)
annual_average = runs_subset_2014_2020.resample('A').mean()
annual_average

#Calculate weekly statistics (My weekly run in last 7 years)
weekly_average = runs_subset_2014_2020.resample('W').mean().mean()
weekly_average

#No. of Training per week I had on average
weekly_counts_average = runs_subset_2014_2020['Distance (km)'].resample('W').count().mean()
weekly_counts_average

## Did I reach my goals?
# Prepare data
df_run_dist_annual = df_run['2020':'2014']['Distance (km)'].resample('A').sum()

# Create plot
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 5))

# Plot and customize
ax = df_run_dist_annual.plot(marker='*', markersize=10, linewidth=0, color='blue')
ax.set(ylim=[0, 300], 
       xlim=['2013','2021'],
       ylabel='Distance (km)',
       xlabel='Years',
       title='Annual totals for distance')

ax.axhspan(200, 300, color='green', alpha=0.4)
ax.axhspan(100, 200, color='yellow', alpha=0.3)
ax.axhspan(0, 50, color='red', alpha=0.2)

# Show plot
plt.show()


##Am I progressing?

# Import required library
import statsmodels.api as sm

# Prepare data
df_run_dist_wkly = df_run['2020':'2014']['Distance (km)'].resample('W').bfill()
df_run_dist_wkly = df_run_dist_wkly.dropna(axis=0)
decomposed = sm.tsa.seasonal_decompose(df_run_dist_wkly, extrapolate_trend=1, period=52)

# Create plot
fig = plt.figure(figsize=(10, 5))

# Plot and customize
ax = decomposed.trend.plot(label='Trend', linewidth=2)
ax = decomposed.observed.plot(label='Observed', linewidth=0.5)

ax.legend()
ax.set_title('Running distance trend')

# Show plot
plt.show()


## Summary Report
# Concatenating three DataFrames
df_walk = runkeeper[runkeeper['Type'] == 'Walking'].copy()
df_cycle = runkeeper[runkeeper['Type'] == 'Cycling'].copy()
df_run_walk_cycle = df_run.append([df_walk, df_cycle]).sort_index(ascending=False)

dist_climb_cols, speed_col = ['Distance (km)', 'Climb (m)'], ['Average Speed (km/h)']

# Calculating total distance and climb in each type of activities
df_totals = df_run_walk_cycle.groupby('Type')[dist_climb_cols].sum()

#Totals for different training types:
display(df_totals)

# Calculating summary statistics for each type of activities 
df_summary = df_run_walk_cycle.groupby('Type')[dist_climb_cols + speed_col].describe()

# Combine totals with summary
for i in dist_climb_cols:
    df_summary[i, 'total'] = df_totals[i]

print('Summary statistics for different training types:')
df_summary_total = df_summary.stack()

