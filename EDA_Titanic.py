import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from bokeh.palettes import viridis

# 'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex',
# 'Age', 'SibSp', 'Parch', 'Ticket',
# 'Fare', 'Cabin', 'Embarked'
# missing values   Age = 177 , Cabin = 687 , Embarked = 2
df = pd.read_csv(r"https://gist.githubusercontent.com/fyyying/4aa5b471860321d7b47fd881898162b7/raw/6907bb3a38bfbb6fccf3a8b1edfb90e39714d14f/titanic_dataset.csv")

# decribtion of Data
print(list(df.columns))
print(df.info())
print(df.describe())
print(df.shape)
print(df.index)
print(df.head())



# Showing missnig Data :-
missing_count = df.isnull().sum()
missing_pct = (df.isnull().mean()*100)
plt.figure(figsize = (10,10))                  # it clear to me the perentage of messing valuse , it for Engineer
sns.barplot(x = missing_pct.index, y = missing_pct.values , label = "Missing Data" , palette = 'viridis')
plt.xlabel("Name of category")
plt.ylabel("% Missing")
plt.legend()
plt.show()
plt.figure(figsize = (10,10))                       # it show me where posetion of missing Data  , it For engineer
sns.heatmap(df.isnull(), annot=True, cmap="YlGnBu")
plt.title("Missing Data")
plt.show()

# Clear missing Data :-
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Age'] = df['Age'].fillna(df.Age.median())
df['New Cabim'] = df['Cabin'].fillna('U').str[0]
df.drop('Cabin' , axis = 1, inplace = True)


# Univariate Analysis :-



PCT_Survived = df.Survived.value_counts(normalize = True)*100
COUNT_Survived = df.Survived.value_counts()

plt.figure(figsize = (10,10))
sns.countplot(data = df, x = 'Survived'  ,hue ='Sex'  )
plt.title('Survived vs Passengers')
plt.legend()
plt.show()

plt.figure(figsize = (10,10))
sns.barplot(x = PCT_Survived.index , y = PCT_Survived.values  )
plt.title('Percentage of Survived Gender')
plt.xlabel('kind of survived')
plt.ylabel('% survived')
plt.legend()
plt.show()






num_of_pass_Pclass = df.Pclass.value_counts()
PCT_Class = df.Pclass.value_counts(normalize = True)*100
plt.figure(figsize = (10,10))
sns.barplot(x = num_of_pass_Pclass.index, y = num_of_pass_Pclass.values )
plt.title('Number of Pass Class Per Person')
plt.xlabel('Class Per Person')
plt.ylabel('Number of Pass Class')
plt.legend()
plt.show()


plt.figure(figsize = (10,10))
sns.barplot(x = PCT_Class.index, y = PCT_Class.values )
plt.title('persentage of Pass Class Per Person')
plt.xlabel('Class Per Person')
plt.ylabel('persentage of Pass Class')
plt.legend()
plt.show()

plt.figure(figsize = (10,10))
sns.countplot(x = 'Pclass', data = df , hue = 'Survived')
plt.title('Survived vs Class')
plt.xlabel('Class')
plt.ylabel('Count')
plt.legend()
plt.show()








Num_of_Gender = df.Sex.value_counts()
PCT_gender = df.Sex.value_counts(normalize = True)*100

plt.figure(figsize = (10,10))
sns.barplot(x = Num_of_Gender.index , y = Num_of_Gender.values , palette = 'viridis')
plt.title('Number of Sex')
plt.xlabel('Kind of Gender')
plt.ylabel('Number of Gender')
plt.show()


plt.figure(figsize = (10,10))
sns.countplot( x = 'Sex' , hue = 'Fare', data = df)
plt.title('SEX vs FARE')
plt.show()



df['Age'].describe()

plt.figure(figsize = (10,10))
sns.histplot(df['Age'] , kde = True ,  bins = 5  , label = 'Age')
plt.title('Age Distribution')
plt.xlabel( 'Range of  Age')
plt.ylabel('Count')
plt.show()

plt.figure(figsize = (10,10))
sns.boxplot(x = df['Age'] )
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Distribution')
plt.show()


df['Kind of Age'] = pd.cut(df["Age"] , bins = [0 ,12,18 ,50 ,80] , labels = ['Child', 'Teen', 'Adult', 'Senior'])
Num_of_KindAge_count = df['Kind of Age'].value_counts()
plt.figure(figsize = (10,10))
sns.countplot(x = 'Kind of Age', data = df , palette = 'viridis' , hue = 'Survived')
plt.title('Kind of Age Distribution')
plt.show()





df['SibSp'].describe()
plt.figure(figsize = (10,10))
sns.countplot(x = 'SibSp' , hue = 'Survived', data = df)
plt.title('Distribution of Survival Status')
plt.show()

plt.figure(figsize = (10,10))
sns.countplot(x = 'SibSp' , hue = 'Fare', data = df)
plt.title('Distribution of Survival Status')
plt.show()


df['Parch'].describe()
plt.figure(figsize = (10,10))
sns.countplot(x = 'Parch' , hue = 'Survived', data = df)
plt.title('Distribution of Survival Status')
plt.show()

plt.figure(figsize = (10,10))
sns.countplot(x = 'Parch' , hue = 'Fare', data = df)
plt.title('Distribution of Survival Status')
plt.show()





df['Category of Fare'] = pd.cut(df['Fare'], bins =  [0.000000 , 7.910400 ,  14.454200 , 31.000000 , 512.329200] ,labels = ['Class_D' ,'Class_C' , 'Class_B' ,'Class_A'])
plt.figure(figsize = (10,10))
sns.countplot(x = 'Category of Fare', data = df , hue = 'Survived'  , palette = 'viridis')
plt.xticks(rotation = 90)
plt.title('Count of Fare Range')
plt.show()

plt.figure(figsize = (10,10))
sns.histplot(x = df.Fare , hue = 'Survived' , bins = 20   , data = df)
plt.title('Survived')
plt.xlabel('Fare')
plt.ylabel('Count')
plt.show()

plt.figure(figsize = (10,10))
sns.countplot(x = 'Category of Fare', data = df , hue = 'Sex'  , palette = 'viridis')
plt.xticks(rotation = 90)
plt.title('Count of Fare Range')
plt.show()

plt.figure(figsize = (10,10))
sns.histplot(data = df , x= 'Fare', bins = 20 , kde = True , palette ='darkblue' )
plt.xticks(rotation = 90)
plt.title('Fare distribution')
plt.show()

plt.figure(figsize = (10,10))
sns.boxplot(x = 'Fare' , data = df )
plt.title('distribution of Fare')
plt.show()




num_of_Embarked = df['Embarked'].value_counts()
PCT_Embarked = df.Embarked.value_counts(normalize = True)*100

plt.figure(figsize = (10,10))
sns.countplot(x = 'Embarked',hue = 'Category of Fare' , data = df)
plt.title('Embarked')
plt.show()

plt.figure(figsize = (10,10))
sns.countplot(x = 'Embarked',hue = 'Survived' , data = df)
plt.title('Embarked')
plt.show()









#Bivariate Analysis :-
plt.figure(figsize = (10,10))
sns.boxplot(x = 'Survived' , y = 'Age', data = df)
plt.title("distribution of Survival ")
plt.show()

plt.figure(figsize = (10,10))
sns.violinplot(x = 'Survived' , y = 'Age', data = df)
plt.title("distribution of Survival")
plt.show()

plt.figure(figsize = (10,10))
sns.boxplot(x = 'Survived', y = 'Fare', data = df)
plt.title('distribution of Fare For Survival')
plt.xlabel('Survived')
plt.ylabel('Fare')
plt.show()

fig = px.box(df , x = 'Survived', y = 'Age')
fig.show()

fig1 = px.box(df , x = 'Survived', y = 'Age')
fig1.show()


fig2 = px.histogram(df , x = 'Pclass', color = 'Survived' , title = 'distribution  of Survival Status by Pclass')
fig2.show()

fig3 = px.histogram(df, x ='Sex' , color ='Survived' , title = "distribution of Survival Status ")
fig3.show()

plt.figure(figsize = (10,10))
sns.scatterplot(data = df , x ='Age' , y = 'Fare' , label ="distribution of Fare by Age ")
plt.title('Distribution of Fare by Age')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()

plt.figure(figsize = (10,10))
sns.barplot(data = df , x = 'Category of Fare' , y = 'Age' )
plt.title('Distribution of Fare by Category of Age')
plt.xlabel('Category of Fare')
plt.ylabel('Age')
plt.show()

print(df[['Age', 'SibSp', 'Parch' , 'Survived', 'Fare' , 'Pclass']].dtypes)
numerical_columns = ['Age', 'SibSp', 'Parch' , 'Survived', 'Fare' , 'Pclass']
corr_matrix = df[numerical_columns].corr()
plt.figure(figsize = (10,10))
sns.heatmap(corr_matrix , annot = True , cmap="YlGnBu")
plt.title('Correlation Heatmap')
plt.show()


