import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import OneHotEncoder



path =  r"E:\AI\instant program\Kaggle_Data\Buisness\Sample\Business_sales_EDA.csv"
df = pd.read_csv(path,sep=";")

# describe the data
info = df.info()
numircal_discribe = df.describe()






# Cleaning the data
Missing = df.isnull().sum()
df['name'] = df['name'].fillna(df['name'].mode()[0])
df['description'] = df['description'].fillna(df['description'].mode()[0])
Missing0 = df.isnull().sum()
Duplicates = df.duplicated().sum()













# Univariate Analysis :-

# Numerical columns :-

disc_price = df['price'].describe()
disc_salaes = df['Sales Volume'].describe()
print(disc_price)
print(disc_salaes)

plt.figure(figsize = (10 ,7))
sns.histplot(data = df , x ='price' , bins = 10 , kde = True)   # right skewed
plt.title('Disribution of Price')
plt.show()

plt.figure(figsize =(10 , 7))
sns.histplot(data= df , x = 'Sales Volume' , bins = 10 , kde =True)  # unnormal distribtion
plt.title('Distribution Of Salse Volume')
plt.show()

fig0 = px.box(data_frame= df , x = 'price' , title = 'Box Plot of Price')
fig0.show()






# Categorical columns :- and it bivariate categorical with categorical

count_Terms = df['terms'].value_counts()
print(count_Terms)
plt.figure(figsize=(10 , 7))
sns.countplot(df, x = 'terms', order= df['terms'].value_counts().index , hue='Promotion' )
plt.title('Count Plot of Terms by Brand')
plt.show()

count_section = df['section'].value_counts()
print(count_section)
plt.figure(figsize=(10 , 7))
sns.countplot(df , x ='section' , order=df['section'].value_counts().index ,  hue = 'terms')
plt.title('Count Plot of Section by Category')
plt.show()

count_seasonal = df.season.value_counts().sort_values()
plt.figure(figsize=(10 , 7))
sns.countplot(df , x = 'season' , order = df['season'].value_counts().sort_values().index , hue ='section')
plt.title('count of Seasonal by Section')
plt.show()


count_material = df.material.value_counts()
plt.figure(figsize=(15, 7))
sns.countplot(df , x = 'material' , order= df.material.value_counts().sort_index().index , hue ='Promotion' )
plt.title('Count Plot of Material by Promotion')
plt.show()


cout_permotion = df.Promotion.value_counts().sort_index()
fig1 = px.bar( x = cout_permotion.index, y  = cout_permotion.values , title = 'Count of Promotion Types' , labels= {'x' : 'permotion typed' , 'y' : 'Counter'})
fig1.show()

count_Origine = df.origin.value_counts().sort_values()
plt.figure(figsize=(20 , 7))
sns.countplot(df , x = 'origin' , order = df.origin.value_counts().sort_values().index , hue = 'terms')
plt.title('Count Plot of Origin by Terms')
plt.show()







# Bivariate Analysis :-

# numerical with numerical :-

df['new_category_price'] = pd.qcut(df['price'],4 , labels=['low','medium','high','expencive'])
Categorical_price_sales = df.groupby('new_category_price' , observed=True)['Sales Volume'].sum().reset_index().rename( columns ={'new_category_price':'price' , 'Sales Volume' : 'count'})
plt.figure(figsize = (10,10))
sns.barplot(data = Categorical_price_sales , x = 'price' , y = 'count' )
plt.title('distribution of Salse ')
plt.show()

# Categorical with categorical :-
fig3 = px.pie(data_frame= df , values='terms' , names='terms')
fig3.show()

# numerical with categorical :-

Cat_por_Salse = df.groupby('Promotion')['Sales Volume'].sum().reset_index().sort_values(by = ['Sales Volume'] , ascending = True)
Cat_por_Salse["percentage"] = (Cat_por_Salse['Sales Volume'] / Cat_por_Salse['Sales Volume'].sum() * 100).round(2)
fig2 = px.bar(Cat_por_Salse , x = 'Promotion', y = 'Sales Volume'  , text = 'percentage' )
fig2.show()

Cat_mat_price = df.groupby('material')['price'].sum().reset_index()
plt.figure(figsize = (15,10))
sns.barplot(data = Cat_mat_price, x = 'material', y = 'price')
plt.title('Price vs Material')
plt.xlabel('Material')
plt.ylabel('Price')
plt.show()


cat_origin_Sales_Volume = df.groupby('origin')['Sales Volume'].sum().reset_index()
cat_origin_Sales_Volume['persetage'] = (cat_origin_Sales_Volume['Sales Volume'] / cat_origin_Sales_Volume['Sales Volume'].sum() * 100).round(2)
print(cat_origin_Sales_Volume)
plt.figure(figsize = (15,10))
sns.barplot(cat_origin_Sales_Volume, x = 'origin', y = 'persetage')
plt.title('persentage of salse')
plt.xlabel('Origin')
plt.ylabel('percentage')
plt.show()



cat_sec_price = df.groupby('section')['price'].sum().reset_index()
cat_sec_price['percentage'] = (cat_sec_price['price']/cat_sec_price['price'].sum()*100).round(2)
plt.figure(figsize = (10,10))
sns.barplot(cat_sec_price  , x ='section' , y = 'percentage' )
plt.xticks(rotation = 90)
plt.xlabel('Section')
plt.ylabel('Percentage')
plt.show()


Cat_por_price = df.groupby('Promotion')['price'].sum().reset_index()
Cat_por_price ['pers'] = (Cat_por_price.price / Cat_por_price.price.sum()*100).round(3).astype(str)+'%'
print(Cat_por_Salse)
fig = px.bar(Cat_por_price , x = 'Promotion' , y = 'price' , text = 'pers')
fig.show()

CAT_season_price = df.groupby('season')['price'].sum().reset_index()
CAT_season_price['pers'] = (CAT_season_price['price'] / CAT_season_price['price'].sum() * 100).round(3).astype(str)+'%'
fig = px.pie(CAT_season_price , names='season', values='price' , hover_data='pers')
fig.show()


# One Hot encoding :-
OH = OneHotEncoder(sparse_output=False)
objects_column = [ 'Product Category', 'Promotion', 'Seasonal', 'brand', 'section', 'season', 'material', 'origin' , 'terms' , 'new_category_price' , 'Product Position']
OH_col = pd.DataFrame(OH.fit_transform(df[objects_column]))
OH_col.index = df.index
OH_col.columns = OH.get_feature_names_out()
DF = df.drop(objects_column, axis = 1)
df = pd.concat([DF, OH_col], axis = 1)



columns_numerical = ['Sales Volume','price', 'Product Position_Aisle', 'Product Position_End-cap', 'Product Position_Front of Store']
corr_matrix = df[columns_numerical].corr()
print(corr_matrix)
plt.figure(figsize = (50,50))
sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu")
plt.show()


# save
df.to_csv('buisness_EDA.csv', index=False)
