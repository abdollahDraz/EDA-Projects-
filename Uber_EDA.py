import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from pylint import modify_sys_path

# 'START_DATE*', 'END_DATE*', 'CATEGORY*', 'START*', 'STOP*', 'MILES*', 'PURPOSE*'


# Missing Data :-
# START_DATE*      0
# END_DATE*
# CATEGORY*
# START*
# STOP*
# MILES*           0
# PURPOSE*       503





df = pd.read_csv(r'https://raw.githubusercontent.com/EshitaNandy/Uber-Trip-Analysis/master/My%20Uber%20Drives%20-%202016.csv')
# print(df.info())
# print(df.head())
# print(df.describe())
# print(df.isnull().sum())



# Cleaning Data :-
df.drop(1155 , inplace=True)
df['START_DATE*'] = pd.to_datetime(df['START_DATE*'])
df['END_DATE*'] = pd.to_datetime(df['END_DATE*'])
# extract new columns for analysis .
df['Month'] = df['START_DATE*'].dt.month
df['Day'] = df['START_DATE*'].dt.day
df['Hour'] = df['START_DATE*'].dt.hour
df['Name of day'] = df['START_DATE*'].dt.day_name()
# Handling missing values .
df.dropna( subset=['END_DATE*','CATEGORY*','START*','STOP*'],inplace=True)
df['PURPOSE*'] = df['PURPOSE*'].fillna('Unkown')
# print(df.isnull().sum())


# Analysis :-
# Descriptive Statistics  (For numerical variable)
# print(df['MILES*'].describe())
# plt.figure(figsize =(10 , 10))
# sns.histplot(data = df , x = 'MILES*' , kde = True  )
# plt.title('Distribution of MILES')
# plt.xlabel('MILES')
# plt.ylabel('counts')
# plt.show()

# plt.figure(figsize = (10,10))
# sns.boxplot(data = df, x = 'MILES*')
# plt.title('Box Plot of MILES')
# plt.show()

# count_Month = df['Month'].value_counts().sort_index()
# count_day = df['Name of day'].value_counts().sort_index()
# plt.figure(figsize = (10,10))
# sns.countplot(data = df , x = 'Month', color = 'blue' , hue = 'Name of day' )
# plt.xlabel('Month')
# plt.ylabel('Count')
# plt.show()

# count_hour = df['Hour'].value_counts().sort_values(ascending=False)
# print(count_hour)
# plt.figure(figsize = (10,10))
# sns.countplot( x = df['Hour'] , hue = df['CATEGORY*'] )
# plt.xlabel('Hour')
# plt.ylabel('Count')
# plt.show()


# Heat_map_table = df.pivot_table(index= 'Hour', columns='Name of day' ,values='MILES*' , aggfunc='count')
# print(Heat_map_table)
# plt.figure(figsize = (10,10))
# sns.heatmap(Heat_map_table, annot=True, cmap='YlGnBu')
# plt.title('Heat Map Table of miles for houres')
# plt.show()


# weak_Day_counts  = df['Name of day'].value_counts().reindex(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
# fig = px.line(x = weak_Day_counts.index,y = weak_Day_counts.values)
# fig.show()

most_started = df['START*'].value_counts().sort_values(ascending=False).head(10)
# plt.figure(figsize = (20,15))
# sns.barplot(x = most_started.index,y = most_started.values  )
# plt.xlabel('name Of Station')
# plt.ylabel('Count')
# plt.show()

df_count_Start = df.groupby(['START*' ,'CATEGORY*']).size().reset_index(name='COUNT')  # creat new Data Frame
# fig = px.bar(df_count , x = 'START*' , y =  'COUNT' , color = 'CATEGORY*')
# fig.show()

# most_ended = df['STOP*'].value_counts().sort_values(ascending=False).head(10)
# plt.figure(figsize = (25,10))
# sns.barplot(x = most_ended.index , y = most_ended.values , label = 'Counter')
# plt.title('Most Ended by Stations')
# plt.xlabel('name Of Station')
# plt.ylabel('Count')
# plt.show()

# df_count_stop = df.groupby(['STOP*' , 'CATEGORY*']).size().reset_index(name='COUNT')
# fig = px.bar(df_count_stop , x='STOP*' , y='COUNT', color='CATEGORY*' , title= 'Count of Station Stops')
# fig.show()
# fig.show()

df['Timing'] = df['START_DATE*'] - df['END_DATE*']
df.Timing = df.Timing.dt.total_seconds()/60
df.Timing = df.Timing.abs()

long_Timing = df['Timing'].sort_values(ascending=False).head(10)
# plt.figure(figsize = (10,10))
# sns.barplot( data = df,x = df['Timing'].sort_values(ascending=False).head(10).index , y = df['Timing'].sort_values(ascending=False).head(10).values, hue = 'CATEGORY*' )
# plt.title('Long Timing')
# plt.show()
dF_long_time = df[['Timing' ,'CATEGORY*' ,'MILES*' ]].sort_values(by='Timing' , ascending=False).head(10)
#print(dF_long_time)
# print(df['Timing'].describe())
# numerical_colums = ['Timing' , 'MILES*' ,'Month' , 'Hour' ,'Day']
# corr_matrix = df[numerical_colums].corr()
# print(corr_matrix)
# plt.figure(figsize = (10,10))
# sns.heatmap(corr_matrix,annot=True,fmt='g',cmap='YlGnBu')
# plt.title('Correlation Matrix')
# plt.show()

# plt.figure(figsize = (10,10))
# sns.barplot(data = dF_long_time , x = 'Timing' , y = 'MILES*', hue = 'CATEGORY*')
# plt.title('Distribution of MILES per Timing')
# plt.show()

median_Timing = df.groupby(['Day','Name of day'])["Timing"].median().reset_index()
#print(median_Timing)
# plt.figure(figsize = (30,30))
# sns.lineplot(data = median_Timing , x = 'Day' , y = 'Timing' , marker = 'o' , label = 'Median Timing')
# plt.xlabel('Day')
# plt.ylabel('TIMING')
# plt.title('Median Timing')
# plt.show()

# plt.figure(figsize = (30,30))
# sns.boxplot(data = df, x = 'Day', y = 'Timing' )
# plt.xlabel('Day')
# plt.ylabel('TIMING')
# plt.title('Distribution of TIMING')
# plt.show()


# last_df = median_Timing.groupby("Name of day")["Timing"].median().reset_index()
# plt.figure(figsize = (10,10))
# sns.lineplot(x='Name of day' , y='Timing' , data=last_df , marker='o' , color='blue' , linewidth=2 ,markersize=5 , markerfacecolor='red'  )
# plt.title('Median Timing  per Day')
# plt.xlabel('Day')
# plt.ylabel('Timing')
# plt.show()



# month_timing = df.groupby('Month')['Timing'].median().reset_index()
# print(month_timing)
# fig = px.line(month_timing, x='Month', y='Timing' , text='Timing' )
# fig.update_traces(textposition="bottom right")
# fig.show()


# plt.figure(figsize=(20 , 10))
# sns.countplot(data=df, x = 'Month')
# plt.title('number of trips per month')
# plt.xlabel('Month')
# plt.ylabel('Number of trips')
# plt.show()

df['speed'] = (df['MILES*']/df['Timing'])*96.56064
speed_per_day = df.groupby('Day')['speed'].mean().reset_index()
print(speed_per_day)


# لسه مخلصتش شغل عليه 