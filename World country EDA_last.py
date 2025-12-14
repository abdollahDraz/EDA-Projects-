from pydoc import describe
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# 'Country', 'Density\n(P/Km2)', 'Abbreviation', 'Agricultural Land( %)'
# , 'Land Area(Km2)', 'Armed Forces size', 'Birth Rate', 'Calling Code',
# 'Capital/Major City', 'Co2-Emissions', 'CPI', 'CPI Change (%)', 'Currency-Code',
# 'Fertility Rate', 'Forested Area (%)', 'Gasoline Price', 'GDP',
# 'Gross primary education enrollment (%)', 'Gross tertiary education enrollment (%)'
# , 'Infant mortality', 'Largest city', 'Life expectancy', 'Maternal mortality ratio'
# , 'Minimum wage', 'Official language', 'Out of pocket health expenditure',
# 'Physicians per thousand', 'Population', 'Population: Labor force participation (%)',
# 'Tax revenue (%)', 'Total tax rate', 'Unemployment rate', 'Urban_population', 'Latitude', 'Longitude'


df = pd.read_csv(r'E:\AI\instant program\Kaggle_Data\World\Sample\world-data-2023.csv')
shape = df.shape
describe_DataFrame = df.describe()

# Cleaning Data :-

# Handling Types :-
col_mony = ['Gasoline Price','GDP','Minimum wage']
change_Type = ['Density\n(P/Km2)','CPI','Land Area(Km2)' , 'Armed Forces size' , 'Co2-Emissions' , 'Population' , 'Urban_population']
Rating_col = ['Unemployment rate','Total tax rate','Tax revenue (%)','Population: Labor force participation (%)','Forested Area (%)','Birth Rate','Agricultural Land( %)','CPI Change (%)','Gross primary education enrollment (%)','Life expectancy','Gross tertiary education enrollment (%)','Maternal mortality ratio','Infant mortality', 'Out of pocket health expenditure' , ]

for col in col_mony:
   df[col] = df[col].astype(str)
   df[col] = df[col].str.replace('$', '', regex=False)
   df[col] = df[col].str.replace(',', '', regex=False)
   df[col] = df[col].str.strip()
   df[col] = df[col].astype(float)

for col in Rating_col:
    df[col] = df[col].astype(str)
    df[col] = df[col].str.replace('%', '', regex=False)
    df[col] = df[col].str.replace(',', '', regex=False)
    df[col] = df[col].str.strip()
    df[col] = df[col].astype(float)

for col in change_Type:
    df[col] = df[col].astype(str)
    df[col] = df[col].str.replace(',', '', regex=False)
    df[col] = df[col].astype(float)


# Handling Missing Values
Missing_columns_mean = [ 'Agricultural Land( %)','Birth Rate','CPI Change (%)','Fertility Rate','Forested Area (%)', 'Gasoline Price','GDP','Gross primary education enrollment (%)','Gross tertiary education enrollment (%)','Infant mortality','Unemployment rate', 'Tax revenue (%)', 'Total tax rate', 'Population: Labor force participation (%)' , 'Physicians per thousand','Out of pocket health expenditure' , 'Minimum wage' , 'Maternal mortality ratio' ,'Life expectancy' , ]
Unknown_values = ['Abbreviation' , 'Official language', 'Calling Code' , 'Capital/Major City', 'Currency-Code' ,'Largest city']
set_coloumns = ['Latitude', 'Longitude']

for col in Missing_columns_mean:
    df[col] = df[col].fillna(df[col].mean())

for col in Unknown_values:
    df[col] = df[col].fillna('UNKNOWN')

for col in set_coloumns :
    df[col] = df[col].fillna(0.)

# check if here any Mising values After Handling Missing values  ?

for col in df :
 PCT = (df[col].isnull().sum() / len(df[col])*100).round(2)
 print(f' {col} -------------- {PCT}')

 # Check if Data have duplicated values ?

dup = df.duplicated()
check = dup.value_counts() # no duplicated values
df.info()



# Arabic Country Data Frame :-
df_arab = df[df['Official language'] == 'Arabic' ].reset_index(drop=True)





# Analysis :-

# Univariate  Analysis:-

# Categorical Analysis:-

most_language = df['Official language'].value_counts().sort_values(ascending= False).drop('UNKNOWN').head(10)
print(most_language)
plt.figure(figsize = (10,10))
sns.barplot(x = most_language.index, y = most_language.values )
plt.title('Most  Official Language Counts')
plt.xlabel('Language')
plt.ylabel('Count')
plt.show()


most_currency_code = df['Currency-Code'].value_counts().sort_values(ascending=False).drop('UNKNOWN').head(7)
plt.figure(figsize = (10,10))
sns.barplot(x = most_currency_code.index , y = most_currency_code.values)
plt.title('Most currency codes')
plt.xlabel('Currency Code')
plt.ylabel('Count')
plt.show()

most_currency_code_arab = df_arab['Currency-Code'].value_counts().sort_values(ascending=False).drop('UNKNOWN').head(5)







# Population
describe_Populaion = df['Population'].describe()
print(describe_Populaion)
plt.figure(figsize = (10,10))
sns.histplot(data=df, x='Population', bins = 30 , kde = True)
plt.show()
#
country_Population = df.groupby('Country')['Population'].sum().reset_index()
country_Population.sort_values(by='Population', ascending=False, inplace=True)
most_10_country_population = country_Population[['Country' , 'Population']].head(10).reset_index().drop('index', axis=1)
fig = px.bar(most_10_country_population, x='Country', y='Population')
fig.show()

describe_Populaion_arab = df_arab['Population'].describe()
print(describe_Populaion_arab)
plt.figure(figsize = (10,10))
sns.histplot(data=df, x='Population', bins = 30 , kde = True)
plt.show()
#
country_Population_arab = df_arab.groupby('Country')['Population'].sum().reset_index()
country_Population_arab.sort_values(by='Population', ascending=False, inplace=True)
most_10_country_population = country_Population_arab[['Country' , 'Population']].head(10).reset_index().drop('index', axis=1)
fig = px.bar(most_10_country_population, x='Country', y='Population')
fig.show()






# Density (P/Km2)
Den_describe = df['Density\n(P/Km2)'].describe()
print(Den_describe)
fig = px.box(data_frame= df , x = 'Density\n(P/Km2)' , title = 'Distribution of Density P/Km2 by Country')
fig.show()

Countr_density = df.groupby('Country')['Density\n(P/Km2)'].sum().reset_index()
most_country_density = Countr_density[['Country','Density\n(P/Km2)' ]].sort_values(by=['Density\n(P/Km2)'], ascending=False).head(5).reset_index(drop=True)
plt.figure(figsize = (25,10))
sns.barplot(data= most_country_density , x = 'Country', y = 'Density\n(P/Km2)')
plt.title('Most Common Density Countries')
plt.xlabel('Countries')
plt.ylabel('Density P/Km2')
plt.show()


Den_describe_arab = df_arab['Density\n(P/Km2)'].describe()
print(Den_describe_arab)
fig = px.box(data_frame= df_arab , x = 'Density\n(P/Km2)' , title = 'Distribution of Density P/Km2 by Country')
fig.show()

Countr_density_arab = df_arab.groupby('Country')['Density\n(P/Km2)'].sum().reset_index()
most_country_density = Countr_density_arab[['Country','Density\n(P/Km2)' ]].sort_values(by=['Density\n(P/Km2)'], ascending=False).head(5).reset_index(drop=True)
plt.figure(figsize = (25,10))
sns.barplot(data= most_country_density , x = 'Country', y = 'Density\n(P/Km2)')
plt.title('Most Common Density Countries')
plt.xlabel('Countries')
plt.ylabel('Density P/Km2')
plt.show()




# Urban_population :-
Urban_describe = df['Urban_population'].describe()
print(Urban_describe)
plt.figure(figsize = (20,10))
sns.histplot(data = df , x = 'Urban_population' , bins = 100, kde = True)
plt.title(' distribution of  Urban population')
plt.show()
#
#
Country_Urban = df.groupby('Country')['Urban_population'].sum().reset_index()
most_10_Country_Urban = Country_Urban[['Country' , 'Urban_population']].sort_values(by='Urban_population' , ascending= False).head(10).reset_index(drop=True)
plt.figure(figsize = (25,10))
sns.barplot(data = most_10_Country_Urban , x = 'Country' , y = 'Urban_population' )
plt.title('Top 10 Urban Population by Country')
plt.xlabel('Country')
plt.ylabel('Urban Population')
plt.show()

Urban_describe_arab = df_arab['Urban_population'].describe()
print(Urban_describe_arab)
plt.figure(figsize = (20,10))
sns.histplot(data = df_arab , x = 'Urban_population' , bins = 100, kde = True)
plt.title(' distribution of  Urban population')
plt.show()
#
Country_Urban_arab = df_arab.groupby('Country')['Urban_population'].sum().reset_index()
most_10_Country_Urban_arab = Country_Urban_arab[['Country' , 'Urban_population']].sort_values(by='Urban_population' , ascending= False).head(10).reset_index(drop=True)
plt.figure(figsize = (25,10))
sns.barplot(data = most_10_Country_Urban_arab , x = 'Country' , y = 'Urban_population' )
plt.title('Top 10 Urban Population by Country')
plt.xlabel('Country')
plt.ylabel('Urban Population')
plt.show()





# Life expectancy
Life_expectancy_describtion = df['Life expectancy'].describe()
Life_expectancy_describtion_arab = df_arab['Life expectancy'].describe()
print(Life_expectancy_describtion)
print(Life_expectancy_describtion_arab)

plt.figure(figsize = (20,10))
sns.histplot(data = df , x ='Life expectancy' , bins = 30 , kde = True )  # left skeew
plt.title('Distribution of Life Expectancy')
plt.xlabel('Life expectancy')
plt.ylabel('Count')
plt.show()

plt.figure(figsize = (20,10))
sns.boxplot(data = df_arab , x = 'Life expectancy')
plt.title('Distribution of Arabic Life Expectancy')
plt.xlabel('Arabic Life Expectancy')
plt.ylabel('box plot')
plt.show()


Country_Life_expectancy = df.groupby('Country')['Life expectancy'].sum().reset_index()
country_Life_expectancy_arab = df_arab.groupby('Country')['Life expectancy'].sum().reset_index()
most_Life_expectancy_arab = df_arab[['Country' , 'Life expectancy']].sort_values(by = 'Life expectancy', ascending = False).reset_index(drop = True).head(5)
most_Life_expectancy = df[['Country' , 'Life expectancy']].sort_values(by = 'Life expectancy', ascending = False).reset_index(drop = True).head(10)
fig1 = px.bar(most_Life_expectancy, x = 'Country', y = 'Life expectancy')
fig1.show()
fig2 = px.bar(most_Life_expectancy_arab, x = 'Country', y = 'Life expectancy')
fig2.show()








# Infant mortality
Infant_mortality_describtion = df['Infant mortality'].describe()
Infant_mortality_describtion_arab = df_arab['Infant mortality'].describe()
print(Infant_mortality_describtion)
print(Infant_mortality_describtion_arab)

plt.figure(figsize = (20,10))
sns.histplot(data = df , x ='Infant mortality' , bins = 30 , kde = True )  # right skew
plt.title('Distribution of Infant mortality')
plt.xlabel('Infant mortality')
plt.ylabel('Count')
plt.show()

plt.figure(figsize = (20,10))
sns.histplot(data = df_arab , x = 'Infant mortality' , bins = 30 , kde = True ) # right skew
plt.title('Distribution of Arabic Infant mortality')
plt.xlabel('Arabic Infant mortality')
plt.ylabel('box plot')
plt.show()

#
Country_Infant_mortality = df.groupby('Country')['Infant mortality'].sum().reset_index()
country_Infant_mortality_arab = df_arab.groupby('Country')['Infant mortality'].sum().reset_index()
most_Infant_mortality_arab = df_arab[['Country' , 'Infant mortality']].sort_values(by = 'Infant mortality', ascending = False).reset_index(drop = True).head(5)
most_Infant_mortality = df[['Country' , 'Infant mortality']].sort_values(by = 'Infant mortality', ascending = False).reset_index(drop = True).head(10)
fig1 = px.bar(most_Infant_mortality, x = 'Country', y = 'Infant mortality')
fig1.show()
fig2 = px.bar(most_Infant_mortality_arab, x = 'Country', y = 'Infant mortality')
fig2.show()







# Maternal mortality ratio
Maternal_mortality_ratio_describtion = df['Maternal mortality ratio'].describe()
Maternal_mortality_ratio_describtion_arab = df_arab['Maternal mortality ratio'].describe()
print(Maternal_mortality_ratio_describtion)
print(Maternal_mortality_ratio_describtion_arab)

plt.figure(figsize = (20,10))
sns.histplot(data = df , x ='Maternal mortality ratio' , bins = 30 , kde = True )  # left skeew
plt.title('Distribution of Maternal mortality ratio')
plt.xlabel('Maternal mortality ratio')
plt.ylabel('Count')
plt.show()

plt.figure(figsize = (20,10))
sns.histplot(data = df_arab , x = 'Maternal mortality ratio' , bins = 30 , kde = True )
plt.title('Distribution of Arabic Maternal mortality ratio')
plt.xlabel('Arabic Maternal mortality ratio')
plt.ylabel('box plot')
plt.show()
#
#
Country_Maternal_mortality_ratio = df.groupby('Country')['Maternal mortality ratio'].sum().reset_index()
country_Maternal_mortality_ratio_arab = df_arab.groupby('Country')['Maternal mortality ratio'].sum().reset_index()
most_Maternal_mortality_ratio_arab = df_arab[['Country' , 'Maternal mortality ratio']].sort_values(by = 'Maternal mortality ratio', ascending = False).reset_index(drop = True).head(5)
most_Maternal_mortality_ratio = df[['Country' , 'Maternal mortality ratio']].sort_values(by = 'Maternal mortality ratio', ascending = False).reset_index(drop = True).head(10)
fig1 = px.bar(most_Maternal_mortality_ratio, x = 'Country', y = 'Maternal mortality ratio')
fig1.show()
fig2 = px.bar(most_Maternal_mortality_ratio_arab, x = 'Country', y = 'Maternal mortality ratio')
fig2.show()










# Fertility Rate
Fertility_Rate_description = df['Fertility Rate'].describe()
Fertility_Rate_description_arab = df_arab['Fertility Rate'].describe()
print(Fertility_Rate_description)
print(Fertility_Rate_description_arab)

plt.figure(figsize=(20,10))
sns.histplot(data=df, x='Fertility Rate', bins=30, kde=True)
plt.title('Distribution of Fertility Rate')
plt.xlabel('Fertility Rate')
plt.ylabel('Count')
plt.show()
#
plt.figure(figsize=(20,10))
sns.histplot(data=df_arab, x='Fertility Rate', bins=30, kde=True)
plt.title('Distribution of Arabic Fertility Rate')
plt.xlabel('Fertility Rate')
plt.ylabel('Count')
plt.show()
# #
# #
Country_Fertility_Rate = df.groupby('Country')['Fertility Rate'].sum().reset_index()
Country_Fertility_Rate_arab = df_arab.groupby('Country')['Fertility Rate'].sum().reset_index()
most_Fertility_Rate = df[['Country', 'Fertility Rate']].sort_values(by='Fertility Rate', ascending=False).reset_index(drop=True).head(10)
most_Fertility_Rate_arab = df_arab[['Country', 'Fertility Rate']].sort_values(by='Fertility Rate', ascending=False).reset_index(drop=True).head(5)
fig1 = px.bar(most_Fertility_Rate, x='Country', y='Fertility Rate')
fig1.show()
fig2 = px.bar(most_Fertility_Rate_arab, x='Country', y='Fertility Rate')
fig2.show()



# GPD
GDP_description = df['GDP'].describe()
GDP_description_arab = df_arab['GDP'].describe()
print(GDP_description)
print(GDP_description_arab)

plt.figure(figsize=(20,10))
sns.histplot(data=df, x='GDP', bins=30, kde=True)
plt.title('Distribution of GDP')
plt.xlabel('GDP')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(20,10))
sns.histplot(data=df_arab, x='GDP', bins=30, kde=True)
plt.title('Distribution of Arabic GDP')
plt.xlabel('GDP')
plt.ylabel('Count')
plt.show()
#
Country_GDP = df.groupby('Country')['GDP'].sum().reset_index()
Country_GDP_arab = df_arab.groupby('Country')['GDP'].sum().reset_index()
most_GDP = df[['Country', 'GDP']].sort_values(by='GDP', ascending=False).reset_index(drop=True).head(10)
most_GDP_arab = df_arab[['Country', 'GDP']].sort_values(by='GDP', ascending=False).reset_index(drop=True).head(5)
fig1 = px.bar(most_GDP, x='Country', y='GDP')
fig1.show()
fig2 = px.bar(most_GDP_arab, x='Country', y='GDP')
fig2.show()



# Tax revenue (%)
Tax_Revenue_description = df['Tax revenue (%)'].describe()  # normal distribution
Tax_Revenue_description_arab = df_arab['Tax revenue (%)'].describe()
print(Tax_Revenue_description)
print(Tax_Revenue_description_arab)

plt.figure(figsize=(20,10))
sns.histplot(data=df, x='Tax revenue (%)', bins=30, kde=True)
plt.title('Distribution of Tax revenue (%)')
plt.xlabel('Tax revenue (%)')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(20,10))
sns.histplot(data=df_arab, x='Tax revenue (%)', bins=30, kde=True)
plt.title('Distribution of Arabic Tax revenue (%)')
plt.xlabel('Tax revenue (%)')
plt.ylabel('Count')
plt.show()
#
Country_Tax_Revenue = df.groupby('Country')['Tax revenue (%)'].sum().reset_index()
Country_Tax_Revenue_arab = df_arab.groupby('Country')['Tax revenue (%)'].sum().reset_index()
most_Tax_Revenue = df[['Country', 'Tax revenue (%)']].sort_values(by='Tax revenue (%)', ascending=False).reset_index(drop=True).head(10)
most_Tax_Revenue_arab = df_arab[['Country', 'Tax revenue (%)']].sort_values(by='Tax revenue (%)', ascending=False).reset_index(drop=True).head(5)
fig1 = px.bar(most_Tax_Revenue, x='Country', y='Tax revenue (%)')
fig1.show()
fig2 = px.bar(most_Tax_Revenue_arab, x='Country', y='Tax revenue (%)')
fig2.show()







# Total tax rate
Total_Tax_Rate_description = df['Total tax rate'].describe()
Total_Tax_Rate_description_arab = df_arab['Total tax rate'].describe()
print(Total_Tax_Rate_description)
print(Total_Tax_Rate_description_arab)

plt.figure(figsize=(20,10))
sns.histplot(data=df, x='Total tax rate', bins=30, kde=True)
plt.title('Distribution of Total tax rate')
plt.xlabel('Total tax rate')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(20,10))
sns.histplot(data=df_arab, x='Total tax rate', bins=30, kde=True)
plt.title('Distribution of Arabic Total tax rate')
plt.xlabel('Total tax rate')
plt.ylabel('Count')
plt.show()
#
Country_Total_Tax_Rate = df.groupby('Country')['Total tax rate'].sum().reset_index()
Country_Total_Tax_Rate_arab = df_arab.groupby('Country')['Total tax rate'].sum().reset_index()
most_Total_Tax_Rate = df[['Country', 'Total tax rate']].sort_values(by='Total tax rate', ascending=False).reset_index(drop=True).head(10)
most_Total_Tax_Rate_arab = df_arab[['Country', 'Total tax rate']].sort_values(by='Total tax rate', ascending=False).reset_index(drop=True).head(5)
fig1 = px.bar(most_Total_Tax_Rate, x='Country', y='Total tax rate')
fig1.show()
fig2 = px.bar(most_Total_Tax_Rate_arab, x='Country', y='Total tax rate')
fig2.show()






# Unemployment rate
Unemployment_description = df['Unemployment rate'].describe()
Unemployment_description_arab = df_arab['Unemployment rate'].describe()
print(Unemployment_description)
print(Unemployment_description_arab)
#
plt.figure(figsize=(20,10))
sns.histplot(data=df, x='Unemployment rate', bins=30, kde=True)
plt.title('Distribution of Unemployment rate')
plt.xlabel('Unemployment rate')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(20,10))
sns.histplot(data=df_arab, x='Unemployment rate', bins=30, kde=True)
plt.title('Distribution of Arabic Unemployment rate')
plt.xlabel('Unemployment rate')
plt.ylabel('Count')
plt.show()
#
Country_Unemployment = df.groupby('Country')['Unemployment rate'].sum().reset_index()
Country_Unemployment_arab = df_arab.groupby('Country')['Unemployment rate'].sum().reset_index()
most_Unemployment = df[['Country', 'Unemployment rate']].sort_values(by='Unemployment rate', ascending=False).reset_index(drop=True).head(10)
most_Unemployment_arab = df_arab[['Country', 'Unemployment rate']].sort_values(by='Unemployment rate', ascending=False).reset_index(drop=True).head(5)
fig1 = px.bar(most_Unemployment, x='Country', y='Unemployment rate')
fig1.show()
fig2 = px.bar(most_Unemployment_arab, x='Country', y='Unemployment rate')
fig2.show()








# Minimum wage
Minimum_Wage_description = df['Minimum wage'].describe()
Minimum_Wage_description_arab = df_arab['Minimum wage'].describe()
print(Minimum_Wage_description)
print(Minimum_Wage_description_arab)

plt.figure(figsize=(20,10))
sns.histplot(data=df, x='Minimum wage', bins=30, kde=True)
plt.title('Distribution of Minimum wage')
plt.xlabel('Minimum wage')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(20,10))
sns.histplot(data=df_arab, x='Minimum wage', bins=30, kde=True)
plt.title('Distribution of Arabic Minimum wage')
plt.xlabel('Minimum wage')
plt.ylabel('Count')
plt.show()
#
Country_Minimum_Wage = df.groupby('Country')['Minimum wage'].sum().reset_index()
Country_Minimum_Wage_arab = df_arab.groupby('Country')['Minimum wage'].sum().reset_index()
most_Minimum_Wage = df[['Country', 'Minimum wage']].sort_values(by='Minimum wage', ascending=False).reset_index(drop=True).head(10)
most_Minimum_Wage_arab = df_arab[['Country', 'Minimum wage']].sort_values(by='Minimum wage', ascending=False).reset_index(drop=True).head(5)
fig1 = px.bar(most_Minimum_Wage, x='Country', y='Minimum wage')
fig1.show()
fig2 = px.bar(most_Minimum_Wage_arab, x='Country', y='Minimum wage')
fig2.show()





# Gasoline Price
Gasoline_Price_description = df['Gasoline Price'].describe()
Gasoline_Price_description_arab = df_arab['Gasoline Price'].describe()
print(Gasoline_Price_description)
print(Gasoline_Price_description_arab)

plt.figure(figsize=(20,10))
sns.histplot(data=df, x='Gasoline Price', bins=30, kde=True)
plt.title('Distribution of Gasoline Price')
plt.xlabel('Gasoline Price')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(20,10))
sns.histplot(data=df_arab, x='Gasoline Price', bins=30, kde=True)
plt.title('Distribution of Arabic Gasoline Price')
plt.xlabel('Gasoline Price')
plt.ylabel('Count')
plt.show()
#
Country_Gasoline_Price = df.groupby('Country')['Gasoline Price'].sum().reset_index()
Country_Gasoline_Price_arab = df_arab.groupby('Country')['Gasoline Price'].sum().reset_index()
most_Gasoline_Price = df[['Country', 'Gasoline Price']].sort_values(by='Gasoline Price', ascending=False).reset_index(drop=True).head(10)
most_Gasoline_Price_arab = df_arab[['Country', 'Gasoline Price']].sort_values(by='Gasoline Price', ascending=False).reset_index(drop=True).head(5)
fig1 = px.bar(most_Gasoline_Price, x='Country', y='Gasoline Price')
fig1.show()
fig2 = px.bar(most_Gasoline_Price_arab, x='Country', y='Gasoline Price')
fig2.show()





# Co2-Emissions
CO2_Emissions_description = df['Co2-Emissions'].describe()
CO2_Emissions_description_arab = df_arab['Co2-Emissions'].describe()
print(CO2_Emissions_description)
print(CO2_Emissions_description_arab)

plt.figure(figsize=(20,10))
sns.histplot(data=df, x='Co2-Emissions', bins=30, kde=True)
plt.title('Distribution of Co2-Emissions')
plt.xlabel('Co2-Emissions')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(20,10))
sns.histplot(data=df_arab, x='Co2-Emissions', bins=30, kde=True)
plt.title('Distribution of Arabic Co2-Emissions')
plt.xlabel('Co2-Emissions')
plt.ylabel('Count')
plt.show()
#
Country_CO2_Emissions = df.groupby('Country')['Co2-Emissions'].sum().reset_index()
Country_CO2_Emissions_arab = df_arab.groupby('Country')['Co2-Emissions'].sum().reset_index()
most_CO2_Emissions = df[['Country', 'Co2-Emissions']].sort_values(by='Co2-Emissions', ascending=False).reset_index(drop=True).head(10)
most_CO2_Emissions_arab = df_arab[['Country', 'Co2-Emissions']].sort_values(by='Co2-Emissions', ascending=False).reset_index(drop=True).head(5)
fig1 = px.bar(most_CO2_Emissions, x='Country', y='Co2-Emissions')
fig1.show()
fig2 = px.bar(most_CO2_Emissions_arab, x='Country', y='Co2-Emissions')
fig2.show()




# Forested Area (%)
Forested_Area_description = df['Forested Area (%)'].describe()
Forested_Area_description_arab = df_arab['Forested Area (%)'].describe()
print(Forested_Area_description)
print(Forested_Area_description_arab)

plt.figure(figsize=(20,10))
sns.histplot(data=df, x='Forested Area (%)', bins=30, kde=True)
plt.title('Distribution of Forested Area (%)')
plt.xlabel('Forested Area (%)')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(20,10))
sns.histplot(data=df_arab, x='Forested Area (%)', bins=30, kde=True)
plt.title('Distribution of Arabic Forested Area (%)')
plt.xlabel('Forested Area (%)')
plt.ylabel('Count')
plt.show()
#
Country_Forested_Area = df.groupby('Country')['Forested Area (%)'].sum().reset_index()
Country_Forested_Area_arab = df_arab.groupby('Country')['Forested Area (%)'].sum().reset_index()
most_Forested_Area = df[['Country', 'Forested Area (%)']].sort_values(by='Forested Area (%)', ascending=False).reset_index(drop=True).head(10)
most_Forested_Area_arab = df_arab[['Country', 'Forested Area (%)']].sort_values(by='Forested Area (%)', ascending=False).reset_index(drop=True).head(5)
fig1 = px.bar(most_Forested_Area, x='Country', y='Forested Area (%)')
fig1.show()
fig2 = px.bar(most_Forested_Area_arab, x='Country', y='Forested Area (%)')
fig2.show()



# Out of pocket health expenditure
Out_of_Pocket_description = df['Out of pocket health expenditure'].describe()
Out_of_Pocket_description_arab = df_arab['Out of pocket health expenditure'].describe()
print(Out_of_Pocket_description)
print(Out_of_Pocket_description_arab)

plt.figure(figsize=(20,10))
sns.histplot(data=df, x='Out of pocket health expenditure', bins=30, kde=True)
plt.title('Distribution of Out of pocket health expenditure')
plt.xlabel('Out of pocket health expenditure')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(20,10))
sns.histplot(data=df_arab, x='Out of pocket health expenditure', bins=30, kde=True)
plt.title('Distribution of Arabic Out of pocket health expenditure')
plt.xlabel('Out of pocket health expenditure')
plt.ylabel('Count')
plt.show()
#
Country_Out_of_Pocket = df.groupby('Country')['Out of pocket health expenditure'].sum().reset_index()
Country_Out_of_Pocket_arab = df_arab.groupby('Country')['Out of pocket health expenditure'].sum().reset_index()
most_Out_of_Pocket = df[['Country', 'Out of pocket health expenditure']].sort_values(by='Out of pocket health expenditure', ascending=False).reset_index(drop=True).head(10)
most_Out_of_Pocket_arab = df_arab[['Country', 'Out of pocket health expenditure']].sort_values(by='Out of pocket health expenditure', ascending=False).reset_index(drop=True).head(5)
fig1 = px.bar(most_Out_of_Pocket, x='Country', y='Out of pocket health expenditure')
fig1.show()
fig2 = px.bar(most_Out_of_Pocket_arab, x='Country', y='Out of pocket health expenditure')
fig2.show()






# Physicians per thousand
Physicians_description = df['Physicians per thousand'].describe()
Physicians_description_arab = df_arab['Physicians per thousand'].describe()
print(Physicians_description)
print(Physicians_description_arab)

plt.figure(figsize=(20,10))
sns.histplot(data=df, x='Physicians per thousand', bins=30, kde=True)
plt.title('Distribution of Physicians per thousand')
plt.xlabel('Physicians per thousand')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(20,10))
sns.histplot(data=df_arab, x='Physicians per thousand', bins=30, kde=True)
plt.title('Distribution of Arabic Physicians per thousand')
plt.xlabel('Physicians per thousand')
plt.ylabel('Count')
plt.show()
#
Country_Physicians = df.groupby('Country')['Physicians per thousand'].sum().reset_index()
Country_Physicians_arab = df_arab.groupby('Country')['Physicians per thousand'].sum().reset_index()
most_Physicians = df[['Country', 'Physicians per thousand']].sort_values(by='Physicians per thousand', ascending=False).reset_index(drop=True).head(10)
most_Physicians_arab = df_arab[['Country', 'Physicians per thousand']].sort_values(by='Physicians per thousand', ascending=False).reset_index(drop=True).head(5)
fig1 = px.bar(most_Physicians, x='Country', y='Physicians per thousand')
fig1.show()
fig2 = px.bar(most_Physicians_arab, x='Country', y='Physicians per thousand')
fig2.show()




# Gross primary education enrollment (%)
Primary_Education_description = df['Gross primary education enrollment (%)'].describe()
Primary_Education_description_arab = df_arab['Gross primary education enrollment (%)'].describe()
print(Primary_Education_description)
print(Primary_Education_description_arab)

plt.figure(figsize=(20,10))
sns.histplot(data=df, x='Gross primary education enrollment (%)', bins=30, kde=True)
plt.title('Distribution of Gross primary education enrollment (%)')
plt.xlabel('Gross primary education enrollment (%)')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(20,10))
sns.histplot(data=df_arab, x='Gross primary education enrollment (%)', bins=30, kde=True)
plt.title('Distribution of Arabic Gross primary education enrollment (%)')
plt.xlabel('Gross primary education enrollment (%)')
plt.ylabel('Count')
plt.show()
#
Country_Primary_Education = df.groupby('Country')['Gross primary education enrollment (%)'].sum().reset_index()
Country_Primary_Education_arab = df_arab.groupby('Country')['Gross primary education enrollment (%)'].sum().reset_index()
most_Primary_Education = df[['Country', 'Gross primary education enrollment (%)']].sort_values(by='Gross primary education enrollment (%)', ascending=False).reset_index(drop=True).head(10)
most_Primary_Education_arab = df_arab[['Country', 'Gross primary education enrollment (%)']].sort_values(by='Gross primary education enrollment (%)', ascending=False).reset_index(drop=True).head(5)
fig1 = px.bar(most_Primary_Education, x='Country', y='Gross primary education enrollment (%)')
fig1.show()
fig2 = px.bar(most_Primary_Education_arab, x='Country', y='Gross primary education enrollment (%)')
fig2.show()




# Gross tertiary education enrollment (%)
Tertiary_Education_description = df['Gross tertiary education enrollment (%)'].describe()
Tertiary_Education_description_arab = df_arab['Gross tertiary education enrollment (%)'].describe()
print(Tertiary_Education_description)
print(Tertiary_Education_description_arab)

plt.figure(figsize=(20,10))
sns.histplot(data=df, x='Gross tertiary education enrollment (%)', bins=30, kde=True)
plt.title('Distribution of Gross tertiary education enrollment (%)')
plt.xlabel('Gross tertiary education enrollment (%)')
plt.ylabel('Count')
plt.show()
#
plt.figure(figsize=(20,10))
sns.histplot(data=df_arab, x='Gross tertiary education enrollment (%)', bins=30, kde=True)
plt.title('Distribution of Arabic Gross tertiary education enrollment (%)')
plt.xlabel('Gross tertiary education enrollment (%)')
plt.ylabel('Count')
plt.show()
# #
Country_Tertiary_Education = df.groupby('Country')['Gross tertiary education enrollment (%)'].sum().reset_index()
Country_Tertiary_Education_arab = df_arab.groupby('Country')['Gross tertiary education enrollment (%)'].sum().reset_index()
most_Tertiary_Education = df[['Country', 'Gross tertiary education enrollment (%)']].sort_values(by='Gross tertiary education enrollment (%)', ascending=False).reset_index(drop=True).head(10)
most_Tertiary_Education_arab = df_arab[['Country', 'Gross tertiary education enrollment (%)']].sort_values(by='Gross tertiary education enrollment (%)', ascending=False).reset_index(drop=True).head(5)
fig1 = px.bar(most_Tertiary_Education, x='Country', y='Gross tertiary education enrollment (%)')
fig1.show()
fig2 = px.bar(most_Tertiary_Education_arab, x='Country', y='Gross tertiary education enrollment (%)')
fig2.show()













# Bivariate Analysis :-

# numerical  with numerical :-


# Tax revenue (%) -  GDP
Tax_revenue_GDP = df.groupby('Country')[['Tax revenue (%)','GDP']].sum().reset_index()
Tax_revenue_GDP_arab = df_arab.groupby('Country')[['Tax revenue (%)','GDP']].sum().reset_index()
print(Tax_revenue_GDP)
print(Tax_revenue_GDP_arab)


Max_GDP_for_Tax_Revenue =  Tax_revenue_GDP[['Country', 'Tax revenue (%)','GDP']].sort_values(by = 'GDP', ascending= False).reset_index(drop=True).head(10)
Max_GDP_for_Tax_Revenue_arab = Tax_revenue_GDP_arab[['Country', 'Tax revenue (%)','GDP']].sort_values(by = 'GDP', ascending= False).reset_index(drop=True).head(5)
print(Max_GDP_for_Tax_Revenue)
print(Max_GDP_for_Tax_Revenue_arab)

Min_GDP_for_Tax_Revenue = Tax_revenue_GDP[['Country', 'Tax revenue (%)','GDP']].sort_values(by = 'GDP' , ascending= True).reset_index(drop= True).head(10)
Min_GDP_for_Tax_Revenue_arab = Tax_revenue_GDP_arab[['Country', 'Tax revenue (%)','GDP']].sort_values(by = 'GDP', ascending= True).reset_index(drop=True).head(5)
print(Min_GDP_for_Tax_Revenue)
print(Min_GDP_for_Tax_Revenue_arab)


fig_scatter0 = px.scatter(Tax_revenue_GDP , x = 'GDP', y = 'Tax revenue (%)' ,hover_name = 'Country' )
fig_scatter0.show()
fig_scatter_arab0 = px.scatter(Tax_revenue_GDP , x = 'GDP', y = 'Tax revenue (%)' ,hover_name = 'Country' )
fig_scatter_arab0.show()




fig_max_0 = px.bar(Max_GDP_for_Tax_Revenue , x = 'GDP', y = 'Tax revenue (%)' , color = 'Country')
fig_max_0.show()
fig_max_arab_0 = px.bar(Max_GDP_for_Tax_Revenue_arab , x = 'GDP', y = 'Tax revenue (%)' , color = 'Country')
fig_max_arab_0.show()


fig_min_0 = px.bar(Min_GDP_for_Tax_Revenue , x = 'GDP', y = 'Tax revenue (%)' , color = 'Country')
fig_min_0.show()
fig_min_arab_0 = px.bar(Min_GDP_for_Tax_Revenue_arab , x = 'GDP', y = 'Tax revenue (%)' , color = 'Country')
fig_min_arab_0.show()



# Unemployment rate - GDP
Unemployment_GDP = df.groupby('Country')[['Unemployment rate','GDP']].sum().reset_index()
Unemployment_GDP_arab = df_arab.groupby('Country')[['Unemployment rate','GDP']].sum().reset_index()
print(Unemployment_GDP)
print(Unemployment_GDP_arab)

Max_GDP_for_Unemployment = Unemployment_GDP.sort_values(by='GDP', ascending=False).head(10).reset_index(drop=True)
Max_GDP_for_Unemployment_arab = Unemployment_GDP_arab.sort_values(by='GDP', ascending=False).head(5).reset_index(drop=True)
print(Max_GDP_for_Unemployment)
print(Max_GDP_for_Unemployment_arab)

Min_GDP_for_Unemployment = Unemployment_GDP.sort_values(by='GDP', ascending=True).head(10).reset_index(drop=True)
Min_GDP_for_Unemployment_arab = Unemployment_GDP_arab.sort_values(by='GDP', ascending=True).head(5).reset_index(drop=True)
print(Min_GDP_for_Unemployment)
print(Min_GDP_for_Unemployment_arab)

fig_scatter_1 = px.scatter(Unemployment_GDP, x='GDP', y='Unemployment rate', hover_name='Country')
fig_scatter_1.show()
fig_scatter_arab_1 = px.scatter(Unemployment_GDP_arab, x='GDP', y='Unemployment rate', hover_name='Country')
fig_scatter_arab_1.show()

fig_max_1 = px.bar(Max_GDP_for_Unemployment, x='GDP', y='Unemployment rate', color='Country')
fig_max_1.show()
fig_max_arab_1 = px.bar(Max_GDP_for_Unemployment_arab, x='GDP', y='Unemployment rate', color='Country')
fig_max_arab_1.show()

fig_min_1 = px.bar(Min_GDP_for_Unemployment, x='GDP', y='Unemployment rate', color='Country')
fig_min_1.show()
fig_min_arab_1 = px.bar(Min_GDP_for_Unemployment_arab, x='GDP', y='Unemployment rate', color='Country')
fig_min_arab_1.show()





# Life expectancy - Physicians per thousand :-
Life_Physicians = df.groupby('Country')[['Life expectancy','Physicians per thousand']].sum().reset_index()
Life_Physicians_arab = df_arab.groupby('Country')[['Life expectancy','Physicians per thousand']].sum().reset_index()
print(Life_Physicians)
print(Life_Physicians_arab)

Max_Life_for_Physicians = Life_Physicians.sort_values(by='Life expectancy', ascending=False).head(10).reset_index(drop=True)
Max_Life_for_Physicians_arab = Life_Physicians_arab.sort_values(by='Life expectancy', ascending=False).head(5).reset_index(drop=True)
print(Max_Life_for_Physicians)
print(Max_Life_for_Physicians_arab)

Min_Life_for_Physicians = Life_Physicians.sort_values(by='Life expectancy', ascending=True).head(10).reset_index(drop=True)
Min_Life_for_Physicians_arab = Life_Physicians_arab.sort_values(by='Life expectancy', ascending=True).head(5).reset_index(drop=True)
print(Min_Life_for_Physicians)
print(Min_Life_for_Physicians_arab)

fig_scatter = px.scatter(Life_Physicians, x='Life expectancy', y='Physicians per thousand', hover_name='Country')
fig_scatter.show()
fig_scatter_arab = px.scatter(Life_Physicians_arab, x='Life expectancy', y='Physicians per thousand', hover_name='Country')
fig_scatter_arab.show()

fig_max = px.bar(Max_Life_for_Physicians, x='Life expectancy', y='Physicians per thousand', color='Country')
fig_max.show()
fig_max_arab = px.bar(Max_Life_for_Physicians_arab, x='Life expectancy', y='Physicians per thousand', color='Country')
fig_max_arab.show()

fig_min = px.bar(Min_Life_for_Physicians, x='Life expectancy', y='Physicians per thousand', color='Country')
fig_min.show()
fig_min_arab = px.bar(Min_Life_for_Physicians_arab, x='Life expectancy', y='Physicians per thousand', color='Country')
fig_min_arab.show()





# Fertility Rate -  Urban_population :-
Fertility_Urban = df.groupby('Country')[['Fertility Rate','Urban_population']].sum().reset_index()
Fertility_Urban_arab = df_arab.groupby('Country')[['Fertility Rate','Urban_population']].sum().reset_index()
print(Fertility_Urban)
print(Fertility_Urban_arab)

Max_Urban_for_Fertility = Fertility_Urban.sort_values(by='Urban_population', ascending=False).head(10).reset_index(drop=True)
Max_Urban_for_Fertility_arab = Fertility_Urban_arab.sort_values(by='Urban_population', ascending=False).head(5).reset_index(drop=True)
print(Max_Urban_for_Fertility)
print(Max_Urban_for_Fertility_arab)

Min_Urban_for_Fertility = Fertility_Urban.sort_values(by='Urban_population', ascending=True).head(10).reset_index(drop=True)
Min_Urban_for_Fertility_arab = Fertility_Urban_arab.sort_values(by='Urban_population', ascending=True).head(5).reset_index(drop=True)
print(Min_Urban_for_Fertility)
print(Min_Urban_for_Fertility_arab)

fig_scatter = px.scatter(Fertility_Urban, x='Urban_population', y='Fertility Rate', hover_name='Country')
fig_scatter.show()
fig_scatter_arab = px.scatter(Fertility_Urban_arab, x='Urban_population', y='Fertility Rate', hover_name='Country')
fig_scatter_arab.show()

fig_max = px.bar(Max_Urban_for_Fertility, x='Urban_population', y='Fertility Rate', color='Country')
fig_max.show()
fig_max_arab = px.bar(Max_Urban_for_Fertility_arab, x='Urban_population', y='Fertility Rate', color='Country')
fig_max_arab.show()

fig_min = px.bar(Min_Urban_for_Fertility, x='Urban_population', y='Fertility Rate', color='Country')
fig_min.show()
fig_min_arab = px.bar(Min_Urban_for_Fertility_arab, x='Urban_population', y='Fertility Rate', color='Country')
fig_min_arab.show()





# Co2-Emissions - GDP :-
CO2_GDP = df.groupby('Country')[['Co2-Emissions','GDP']].sum().reset_index()
CO2_GDP_arab = df_arab.groupby('Country')[['Co2-Emissions','GDP']].sum().reset_index()
print(CO2_GDP)
print(CO2_GDP_arab)

Max_CO2_for_GDP = CO2_GDP.sort_values(by='Co2-Emissions', ascending=False).head(10).reset_index(drop=True)
Max_CO2_for_GDP_arab = CO2_GDP_arab.sort_values(by='Co2-Emissions', ascending=False).head(5).reset_index(drop=True)
print(Max_CO2_for_GDP)
print(Max_CO2_for_GDP_arab)

Min_CO2_for_GDP = CO2_GDP.sort_values(by='Co2-Emissions', ascending=True).head(10).reset_index(drop=True)
Min_CO2_for_GDP_arab = CO2_GDP_arab.sort_values(by='Co2-Emissions', ascending=True).head(5).reset_index(drop=True)
print(Min_CO2_for_GDP)
print(Min_CO2_for_GDP_arab)

fig_scatter = px.scatter(CO2_GDP, x='Co2-Emissions', y='GDP', hover_name='Country')
fig_scatter.show()
fig_scatter_arab = px.scatter(CO2_GDP_arab, x='Co2-Emissions', y='GDP', hover_name='Country')
fig_scatter_arab.show()

fig_max = px.bar(Max_CO2_for_GDP, x='Co2-Emissions', y='GDP', color='Country')
fig_max.show()
fig_max_arab = px.bar(Max_CO2_for_GDP_arab, x='Co2-Emissions', y='GDP', color='Country')
fig_max_arab.show()

fig_min = px.bar(Min_CO2_for_GDP, x='Co2-Emissions', y='GDP', color='Country')
fig_min.show()
fig_min_arab = px.bar(Min_CO2_for_GDP_arab, x='Co2-Emissions', y='GDP', color='Country')
fig_min_arab.show()




# Co2-Emissions -  Forested Area (%) :-
CO2_Forested = df.groupby('Country')[['Co2-Emissions','Forested Area (%)']].sum().reset_index()
CO2_Forested_arab = df_arab.groupby('Country')[['Co2-Emissions','Forested Area (%)']].sum().reset_index()
print(CO2_Forested)
print(CO2_Forested_arab)

Max_CO2_for_Forested = CO2_Forested.sort_values(by='Co2-Emissions', ascending=False).head(10).reset_index(drop=True)
Max_CO2_for_Forested_arab = CO2_Forested_arab.sort_values(by='Co2-Emissions', ascending=False).head(5).reset_index(drop=True)
print(Max_CO2_for_Forested)
print(Max_CO2_for_Forested_arab)

Min_CO2_for_Forested = CO2_Forested.sort_values(by='Co2-Emissions', ascending=True).head(10).reset_index(drop=True)
Min_CO2_for_Forested_arab = CO2_Forested_arab.sort_values(by='Co2-Emissions', ascending=True).head(5).reset_index(drop=True)
print(Min_CO2_for_Forested)
print(Min_CO2_for_Forested_arab)

fig_scatter = px.scatter(CO2_Forested, x='Co2-Emissions', y='Forested Area (%)', hover_name='Country')
fig_scatter.show()
fig_scatter_arab = px.scatter(CO2_Forested_arab, x='Co2-Emissions', y='Forested Area (%)', hover_name='Country')
fig_scatter_arab.show()

fig_max = px.bar(Max_CO2_for_Forested, x='Co2-Emissions', y='Forested Area (%)', color='Country')
fig_max.show()
fig_max_arab = px.bar(Max_CO2_for_Forested_arab, x='Co2-Emissions', y='Forested Area (%)', color='Country')
fig_max_arab.show()

fig_min = px.bar(Min_CO2_for_Forested, x='Co2-Emissions', y='Forested Area (%)', color='Country')
fig_min.show()
fig_min_arab = px.bar(Min_CO2_for_Forested_arab, x='Co2-Emissions', y='Forested Area (%)', color='Country')
fig_min_arab.show()




# Nimerical with Categorical :-
#  note here  you can use ( groupby - mean ) :-  (Categorical  columns is Currency-Code - Official language - Country  )


# GDP - Official language
Mean_GDP_Official_Language = df.groupby('Official language')['GDP'].mean().reset_index()
Mean_GDP_Official_Language = Mean_GDP_Official_Language[Mean_GDP_Official_Language['Official language'] != 'UNKNOWN']
Max_mean_GDP_Official_Language = Mean_GDP_Official_Language[['Official language','GDP']].sort_values(by='GDP', ascending=False).reset_index(drop=True).head(10)
Min_mean_GDP_Official_Language =  Mean_GDP_Official_Language[['Official language','GDP']].sort_values(by='GDP', ascending=True).reset_index(drop=True).head(10)
print(Max_mean_GDP_Official_Language)
print(Min_mean_GDP_Official_Language)

fig = px.bar(Mean_GDP_Official_Language , x = 'Official language', y = 'GDP')
fig.show()

fig_max = px.bar(Max_mean_GDP_Official_Language , x = 'Official language', y = 'GDP')
fig_max.show()

fig_min = px.bar(Min_mean_GDP_Official_Language , x = 'Official language', y = 'GDP')
fig_min.show()



# GDP - Currency-Code
Mean_GDP_Currency_code = df.groupby('Currency-Code')['GDP'].mean().reset_index()
Mean_GDP_Official_Language = Mean_GDP_Currency_code[Mean_GDP_Currency_code['Currency-Code'] != 'UNKNOWN']
Max_mean_Currency_Code = Mean_GDP_Currency_code[['Currency-Code','GDP']].sort_values(by='GDP', ascending=False).reset_index(drop=True).head(10)
Min_mean_Currency_Code =  Mean_GDP_Currency_code[['Currency-Code','GDP']].sort_values(by='GDP', ascending=True).reset_index(drop=True).head(10)
print(Max_mean_Currency_Code)
print(Min_mean_Currency_Code)

fig = px.bar(Mean_GDP_Currency_code , x = 'Currency-Code', y = 'GDP')
fig.show()

fig_max = px.bar(Max_mean_Currency_Code , x = 'Currency-Code', y = 'GDP')
fig_max.show()

fig_min = px.bar(Min_mean_Currency_Code , x = 'Currency-Code', y = 'GDP')
fig_min.show()










# Life expectancy - Official language
Mean_life_exceptancy_language = df.groupby('Official language')['Life expectancy'].mean().reset_index()
Mean_life_exceptancy_language = Mean_life_exceptancy_language[Mean_life_exceptancy_language['Official language'] != 'UNKNOWN']
Max_Mean_life_exceptancy_language  = Mean_life_exceptancy_language[['Official language', 'Life expectancy' ]].sort_values(by='Life expectancy', ascending=False).reset_index(drop=True).head(5)
Min_Mean_life_exceptancy_language  = Mean_life_exceptancy_language[['Official language', 'Life expectancy' ]].sort_values(by='Life expectancy', ascending=True).reset_index(drop=True).head(5)
print(Max_Mean_life_exceptancy_language)
print(Min_Mean_life_exceptancy_language)

fig = px.bar(Mean_life_exceptancy_language , x = 'Official language', y = 'Life expectancy' , title = 'Mean life expectancy')
fig.show()

fig_max = px.bar(Max_Mean_life_exceptancy_language , x = 'Official language' , y = 'Life expectancy' , title = 'Max life expectancy language')
fig_max.show()

fig_min = px.bar(Min_Mean_life_exceptancy_language , x = 'Official language' , y ='Life expectancy' , title = 'Min life expectancy language')
fig_min.show()





# Fertility Rate -  Official language :-
Mean_Fertility_Rate_language = df.groupby('Official language')['Fertility Rate'].mean().reset_index()
Mean_Fertility_Rate_language = Mean_Fertility_Rate_language[Mean_Fertility_Rate_language['Official language'] !='English']
Max_Mean_Fertility_Rate_language = Mean_Fertility_Rate_language[['Official language', 'Fertility Rate']].sort_values(by='Fertility Rate', ascending=False).reset_index(drop=True).head(5)
Min_Mean_Fertility_Rate_language = Mean_Fertility_Rate_language[['Official language', 'Fertility Rate']].sort_values(by='Fertility Rate', ascending=True).reset_index(drop= True).head(5)
print(Max_Mean_Fertility_Rate_language)
print(Min_Mean_Fertility_Rate_language)

fig = px.bar(Mean_Fertility_Rate_language , x = 'Official language', y = 'Fertility Rate')
fig.show()

fig_max = px.bar(Max_Mean_Fertility_Rate_language , x = 'Official language', y = 'Fertility Rate')
fig_max.show()

fig_min = px.bar(Min_Mean_Fertility_Rate_language , x = 'Official language', y = 'Fertility Rate')
fig_min.show()



# Gasoline Price  - Currency-Code
Mean_Gasoline_Currency_code = df.groupby('Currency-Code')['Gasoline Price'].mean().reset_index()
Mean_Gasoline_Currency_code = Mean_Gasoline_Currency_code[Mean_Gasoline_Currency_code['Currency-Code'] != 'UNKNOWN']

Max_mean_Gasoline_Code = Mean_Gasoline_Currency_code[['Currency-Code','Gasoline Price']].sort_values(by='Gasoline Price', ascending=False).head(10).reset_index(drop=True)
Min_mean_Gasoline_Code = Mean_Gasoline_Currency_code[['Currency-Code','Gasoline Price']].sort_values(by='Gasoline Price', ascending=True).head(10).reset_index(drop=True)

print(Max_mean_Gasoline_Code)
print(Min_mean_Gasoline_Code)

fig = px.bar(Mean_Gasoline_Currency_code , x='Currency-Code', y='Gasoline Price')
fig.show()

fig_max = px.bar(Max_mean_Gasoline_Code , x='Currency-Code', y='Gasoline Price')
fig_max.show()

fig_min = px.bar(Min_mean_Gasoline_Code , x='Currency-Code', y='Gasoline Price')
fig_min.show()


# Currency-Code  -  Minimum wage
Mean_MinWage_Currency_code = df.groupby('Currency-Code')['Minimum wage'].mean().reset_index()
Mean_MinWage_Currency_code = Mean_MinWage_Currency_code[Mean_MinWage_Currency_code['Currency-Code'] != 'UNKNOWN']

Max_mean_MinWage_Code = Mean_MinWage_Currency_code[['Currency-Code','Minimum wage']].sort_values(by='Minimum wage', ascending=False).head(10).reset_index(drop=True)
Min_mean_MinWage_Code = Mean_MinWage_Currency_code[['Currency-Code','Minimum wage']].sort_values(by='Minimum wage', ascending=True).head(10).reset_index(drop=True)

print(Max_mean_MinWage_Code)
print(Min_mean_MinWage_Code)

fig = px.bar(Mean_MinWage_Currency_code , x='Currency-Code', y='Minimum wage')
fig.show()

fig_max = px.bar(Max_mean_MinWage_Code , x='Currency-Code', y='Minimum wage')
fig_max.show()

fig_min = px.bar(Min_mean_MinWage_Code , x='Currency-Code', y='Minimum wage')
fig_min.show()


# Currency-Code - Total tax rate
Mean_TotalTax_Currency_code = df.groupby('Currency-Code')['Total tax rate'].mean().reset_index()
Mean_TotalTax_Currency_code = Mean_TotalTax_Currency_code[Mean_TotalTax_Currency_code['Currency-Code'] != 'UNKNOWN']

Max_mean_TotalTax_Code = Mean_TotalTax_Currency_code[['Currency-Code','Total tax rate']].sort_values(by='Total tax rate', ascending=False).head(10).reset_index(drop=True)
Min_mean_TotalTax_Code = Mean_TotalTax_Currency_code[['Currency-Code','Total tax rate']].sort_values(by='Total tax rate', ascending=True).head(10).reset_index(drop=True)

print(Max_mean_TotalTax_Code)
print(Min_mean_TotalTax_Code)

fig = px.bar(Mean_TotalTax_Currency_code , x='Currency-Code', y='Total tax rate')
fig.show()

fig_max = px.bar(Max_mean_TotalTax_Code , x='Currency-Code', y='Total tax rate')
fig_max.show()

fig_min = px.bar(Min_mean_TotalTax_Code , x='Currency-Code', y='Total tax rate')
fig_min.show()



# Currency-Code -  Tax revenue (%
Mean_TaxRevenue_Currency_code = df.groupby('Currency-Code')['Tax revenue (%)'].mean().reset_index()
Mean_TaxRevenue_Currency_code = Mean_TaxRevenue_Currency_code[Mean_TaxRevenue_Currency_code['Currency-Code'] != 'UNKNOWN']

Max_mean_TaxRevenue_Code = Mean_TaxRevenue_Currency_code[['Currency-Code','Tax revenue (%)']].sort_values(by='Tax revenue (%)', ascending=False).head(10).reset_index(drop=True)
Min_mean_TaxRevenue_Code = Mean_TaxRevenue_Currency_code[['Currency-Code','Tax revenue (%)']].sort_values(by='Tax revenue (%)', ascending=True).head(10).reset_index(drop=True)

print(Max_mean_TaxRevenue_Code)
print(Min_mean_TaxRevenue_Code)

fig = px.bar(Mean_TaxRevenue_Currency_code , x='Currency-Code', y='Tax revenue (%)')
fig.show()

fig_max = px.bar(Max_mean_TaxRevenue_Code , x='Currency-Code', y='Tax revenue (%)')
fig_max.show()

fig_min = px.bar(Min_mean_TaxRevenue_Code , x='Currency-Code', y='Tax revenue (%)')
fig_min.show()


# Out of pocket health expenditure - Currency-Code
Mean_OutOfPocket_Currency_code = df.groupby('Currency-Code')['Out of pocket health expenditure'].mean().reset_index()
Mean_OutOfPocket_Currency_code = Mean_OutOfPocket_Currency_code[Mean_OutOfPocket_Currency_code['Currency-Code'] != 'UNKNOWN']

Max_mean_OutOfPocket_Code = Mean_OutOfPocket_Currency_code[['Currency-Code','Out of pocket health expenditure']].sort_values(by='Out of pocket health expenditure', ascending=False).head(10).reset_index(drop=True)
Min_mean_OutOfPocket_Code = Mean_OutOfPocket_Currency_code[['Currency-Code','Out of pocket health expenditure']].sort_values(by='Out of pocket health expenditure', ascending=True).head(10).reset_index(drop=True)

print(Max_mean_OutOfPocket_Code)
print(Min_mean_OutOfPocket_Code)

fig = px.bar(Mean_OutOfPocket_Currency_code , x='Currency-Code', y='Out of pocket health expenditure')
fig.show()

fig_max = px.bar(Max_mean_OutOfPocket_Code , x='Currency-Code', y='Out of pocket health expenditure')
fig_max.show()

fig_min = px.bar(Min_mean_OutOfPocket_Code , x='Currency-Code', y='Out of pocket health expenditure')
fig_min.show()







# Official language -  Out of pocket health expenditure
Mean_OutOfPocket_Language = df.groupby('Official language')['Out of pocket health expenditure'].mean().reset_index()
Mean_OutOfPocket_Language = Mean_OutOfPocket_Language[Mean_OutOfPocket_Language['Official language'] != 'UNKNOWN']

Max_mean_OutOfPocket_Lang = Mean_OutOfPocket_Language[['Official language','Out of pocket health expenditure']].sort_values(by='Out of pocket health expenditure', ascending=False).head(10).reset_index(drop=True)
Min_mean_OutOfPocket_Lang = Mean_OutOfPocket_Language[['Official language','Out of pocket health expenditure']].sort_values(by='Out of pocket health expenditure', ascending=True).head(10).reset_index(drop=True)

print(Max_mean_OutOfPocket_Lang)
print(Min_mean_OutOfPocket_Lang)

fig = px.bar(Mean_OutOfPocket_Language , x='Official language', y='Out of pocket health expenditure')
fig.show()

fig_max = px.bar(Max_mean_OutOfPocket_Lang , x='Official language', y='Out of pocket health expenditure')
fig_max.show()

fig_min = px.bar(Min_mean_OutOfPocket_Lang , x='Official language', y='Out of pocket health expenditure')
fig_min.show()













# categorical with categorical

#Official language - Currency-Code
num_Currency_code_language = df.groupby('Official language')['Currency-Code'].nunique().reset_index()
num_Currency_code_language = num_Currency_code_language [num_Currency_code_language['Official language'] != 'UNKNOWN']
most_language_have_curreny_code = num_Currency_code_language [['Official language','Currency-Code']].sort_values(by = 'Currency-Code', ascending= False).reset_index(drop = True).head(5)

fig = px.bar(num_Currency_code_language , x ='Official language' , y = 'Currency-Code')
fig.show()

fig_most = px.bar(most_language_have_curreny_code , x = 'Official language' , y = 'Currency-Code')
fig_most.show()


#Currency-Code - Official language
Currency_languge_common = df[df['Currency-Code'] != 'UNKNOWN'].groupby('Currency-Code')['Official language'].value_counts().reset_index()
print(Currency_languge_common)
Currency_languge_common_counter = df[df['Currency-Code'] != 'UNKNOWN'].groupby('Currency-Code')['Official language'].nunique()
Currency_have_more_than_one_language = Currency_languge_common_counter[Currency_languge_common_counter > 1].reset_index().rename(columns={'Official language':'Official languages'})

fig = px.bar(Currency_have_more_than_one_language  ,  x = 'Currency-Code',  y = 'Official languages')
fig.show()

fig_1 = px.bar(Currency_languge_common , x='Currency-Code' , y ='count' , color ='Official language' )
fig_1.show()






# correlation :-
numerical_columns = df.select_dtypes(include ='float').columns.to_list()
print(numerical_columns)
corr_matrix = df[numerical_columns].corr()
print(corr_matrix)


plt.figure(figsize=(80,80))
sns.heatmap(corr_matrix, annot=True)
plt.show()


fig = px.imshow(corr_matrix , text_auto= True , title='Correlation Matrix' , color_continuous_scale= 'Viridis' )
fig.update_layout(xaxis_title = 'Columns' , yaxis_title = 'Columns ' , width = 1500 , height = 1500 )
fig.show()


sns.pairplot(df[['GDP','Life expectancy','Minimum wage','Birth Rate' ,'Out of pocket health expenditure' ,'Physicians per thousand']])
plt.show()


# Maoing plot :-
# Maping plot for all numerical column :-
for col in numerical_columns:
      if col !=  'Latitude' and  col != 'Longitude' :
         fig_GDP = px.scatter_geo(df , lat ='Latitude'  , lon= 'Longitude' , color= col , projection= 'natural earth' , title= f'{col} per capita' , hover_name='Country' , size_max= 15 )
         fig_GDP.show()

















