import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#'product_id', 'product_name', 'category', 'discounted_price'
# , 'actual_price', 'discount_percentage', 'rating', 'rating_count', 'about_product',
# 'user_id', 'user_name', 'review_id', 'review_title'
# , 'review_content', 'img_link', 'product_link'

# EDA
df = pd.read_csv(r"E:\AI\instant program\Kaggle_Data\Amzoon\Sample\amazon.csv")
print(df.head(10))
print(f"befor drop duplicates values :- {df.shape}")
df.index
df.describe()
df.info()
#NAN ---- rating_count   2
df.isnull().sum()

# Cleaning
df.drop_duplicates()
#print(f"after drop duplicates values {df.shape}")
def extract_main_category(Categoryvalue) :
    if isinstance(Categoryvalue,str) :
        return Categoryvalue.split("|")[0].strip()
    else :
        return 'unknown'
df['Main Category'] = df['category'].apply(extract_main_category)
df['discounted_price'] = df['discounted_price'].str.replace('₹','').str.replace(',','').astype(float)
df['actual_price'] = df['actual_price'].str.replace(',','').str.replace('₹','').astype(float)
df['discount_percentage'] = df['discount_percentage'].astype(str).str.replace('%','').astype(float)
df['rating'] =  df['rating'].replace('|', np.nan).astype(float)
df['rating_count'] = df['rating_count'].astype(str).str.replace(',','').astype(float)


# Anaylysis numircal Data

Numerical_Columns = ['discounted_price', 'actual_price', 'discount_percentage' , 'rating', 'rating_count']



# Descriptive Statistics :- (mean - median - max - min - std)
#print(df[Numerical_Columns].describe())





# Univariate Analysis :- analysis one numircal column (histogram + kde plot  )
for col in Numerical_Columns :
     plt.figure(figsize=(7,5))
     sns.histplot(df[col] , kde =True , color="darkred" , bins = 20 , label = f'{col} distribution')
     plt.title(f"Distribution of {col}")
     plt.xlabel(col)
     plt.ylabel('count')
     plt.legend()
     plt.show()



# Bivariate Analysis :- analysis two  columns (Scatter plot)()
# Two numircal columns
plt.figure(figsize=(7,5))
sns.lmplot( x='discounted_price',
       y='rating', hue = 'Main Category'
      , data=df )
plt.title("Discounted Price vs Rating with Regression Line")
plt.xlabel('discounted price')
plt.ylabel('rating')
plt.show()
plt.figure(figsize=(7,5))
sns.lmplot(x = 'discount_percentage' , y = 'rating_count' ,data = df )
plt.title("Discount % vs Rating Count with Regression Line")
plt.xlabel('discounted percentage')
plt.ylabel('rating count')
plt.show()
# one numercal column with one categoreical column
plt.figure(figsize=(15,30))
sns.boxplot(x = 'Main Category' , y = 'discount_percentage' , data = df )
plt.title('persent of discounted price for categoricals ')
plt.xlabel('Main Category')
plt.ylabel('Discount Percentage')
plt.show()
plt.figure(figsize=(15,30))
sns.boxplot(x = 'Main Category' , y = 'discounted_price' , data = df )
plt.title('price for categoricals ')
plt.xlabel('Main Category')
plt.ylabel('prices')
plt.show()





# Multivariate Analysis :- analysis more than two columns (Heat map for numerical Data) .
Numerical_Matrix = df[Numerical_Columns].corr()
plt.figure(figsize = (10,10))
sns.heatmap(Numerical_Matrix, annot=True ,  cmap="YlGnBu")
plt.title('Numerical Correlation')
plt.show()




# Category-wise Analysis :-
# Analysis
Category_Count = df['Main Category'].value_counts()
Mean_price_Categoies = df.groupby("Main Category")['discounted_price'].mean().sort_values(ascending = False)
Mean_Rating_Categories = df.groupby("Main Category")['rating'].mean().sort_values(ascending = False)
Mean_of_Rating_count  = df.groupby('Main Category')['rating_count'].mean().sort_values(ascending = False)
# vesualization
plt.figure(figsize = (30,15))   # For Category_Count
sns.countplot(data = df , x = 'Main Category' )
plt.xlabel('Main Category')
plt.ylabel('Count')
plt.title("counter of main categories")
plt.show()
plt.figure(figsize = (30,15)) # for Mean_price_Categoies
sns.barplot(x = "Main Category", y = "discounted_price", data = df  )
plt.title("Discounted Price vs Rating of Main Categories")
plt.xlabel("Main Category")
plt.ylabel("Discounted Price")
plt.show()
plt.figure(figsize = (30,10))   # for Mean_Rating_Categories
sns.barplot(x = 'Main Category', y = 'rating', data = df)
plt.title('Rating vs Main Category')
plt.xlabel('Main Category')
plt.ylabel('Rating')
plt.show()
plt.figure(figsize = (30,10))
sns.barplot(x = 'Main Category', y = 'rating_count' , data = df)
plt.title('Rating vs Main Category')
plt.xlabel('Main Category')
plt.ylabel('Rating counter')
plt.show()






