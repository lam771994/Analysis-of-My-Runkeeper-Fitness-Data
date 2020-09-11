# Analysis-of-My-Cardio-Activities :runner:


:muscle: **Motivation:** 

I finished my first half-marathon within 3 hours in 2019. It was a dreadful experience yet extremely rewarding. I did not train nor prepare myself for the marathon as it was a spontaneous decision, but I still managed to complete the 21km journey. Aside from the determination, 'NEVER GIVE UP' and 'don't want to lose face' spirit, I had to thank my 'once in a while' cardio activities (i.e. Running and Walking). Since 2014, I have been using a popular app called Runkeeper. It is an excellent app that keeps track of your runs, goals and improvements. In this project, I would like to humbly present the analysis of my Runkeeper Fitness data.

[![IMG-1575.jpg](https://i.postimg.cc/Njfym45D/IMG-1575.jpg)](https://postimg.cc/ZC2Kh6Pv)

<pre>
:bar_chart: **Dataset:**  

Runkeeper records a wide range of information describing user's activities, route, distance, duration, average pace, average speed, calories burned and average heart rate. An amazing key feature of Runkeeper is its excellent data export. User is allowed to download her/his data from the personal profile section.
</pre>




:page_facing_up: **Methods:**
1. Obtain and review raw data
2. Data preprocessing
3. Dealing with missing values
4. Ploting running data
5. Running statistics
6. Visualization with averages
7. Did I reach my goal?
8. Am I progressing?
9. Training intensity
10. Detailed summary report





:chart_with_upwards_trend: **Analysis:**


1. Obtain and review raw data

```
import pandas as pd

#Name the dataset file and create a dataframe
runkeeper = pd.read_csv('/Users/lamyingxian/Dropbox/Data Science Course/Projects/My Cardio Activities - Runkeeper/cardioActivities.csv')

#Brief look at the data
runkeeper.head()
```
[![Screenshot-2020-09-11-at-2-10-39-PM.png](https://i.postimg.cc/vTpf86Q9/Screenshot-2020-09-11-at-2-10-39-PM.png)](https://postimg.cc/1VrfJXV5)

:point_right: Since the console is not able to show all the 14 columns due to its limited space, I prefer to briefly look at the data in variable explorer.

[![Screenshot-2020-09-11-at-1-01-38-PM.png](https://i.postimg.cc/Xq4N3j5L/Screenshot-2020-09-11-at-1-01-38-PM.png)](https://postimg.cc/N9Cvkwp2)



```
#Summary of the data
runkeeper.info()
```
[![Screenshot-2020-09-11-at-2-14-43-PM.png](https://i.postimg.cc/zGMBs1Gb/Screenshot-2020-09-11-at-2-14-43-PM.png)](https://postimg.cc/xXvnmhHn)


:point_right: There are 234 data and 14 columns of data.

:point_right: 'Non-Null Count' means number of items in the specific column that are not zero/empty.

:point_right: 'Dtype' means the data types.
              Object: text or mixed numeric and non-numeric values.
              float64: decimal numbers.
              int64: real numbers.
              



2. Data Preprocessing




              


