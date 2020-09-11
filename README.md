# Analysis-of-My-Cardio-Activities

**Motivation:**

I finished my first half-marathon within 3 hours in 2019. It was a dreadful experience yet extremely rewarding. I did not train nor prepare myself for the marathon as it was a spontaneous decision, but I still managed to complete the 21km journey. Aside from the determination, 'NEVER GIVE UP' and 'don't want to lose face' spirit, I had to thank my 'once in a while' cardio activities (i.e. Running and Walking). Since 2014, I have been using a popular app called Runkeeper. It is an excellent app that keeps track of your runs, goals and improvements. In this project, I would like to humbly present the analysis of my Runkeeper Fitness data.

[![IMG-1575.jpg](https://i.postimg.cc/cLDnbYfh/IMG-1575.jpg)](https://postimg.cc/9D704D8w)

**Dataset:**  

Runkeeper records a wide range of information describing user's activities, route, distance, duration, average pace, average speed, calories burned and average heart rate. An amazing key feature of Runkeeper is its excellent data export. User is allowed to download her/his data from the personal profile section.


**Methods:**
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


**Analysis**
1. Obtain and review raw data

```
import pandas as pd

#Name the dataset file and create a dataframe
runkeeper = pd.read_csv('/Users/lamyingxian/Dropbox/Data Science Course/Projects/My Cardio Activities - Runkeeper/cardioActivities.csv')
```



