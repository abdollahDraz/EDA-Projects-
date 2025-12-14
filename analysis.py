import pandas as pd
import matplotlib.pyplot as plt
#['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name',
# 'Segment', 'Country', 'City', 'State', 'Postal Code', 'Region',
# 'Product ID', 'Category', 'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit'

df = pd.read_csv(r"E:\AI\instant program\Kaggle_Data\Customer Sales\Sample\Sample - Superstore.csv", encoding="latin1")
list(df.columns)

# Filter orders by customer
Tom_Boeckenhauer = df[df["Customer Name"] == "Tom Boeckenhauer"]
Tom_Boeckenhauer_5 =  df[df["Customer Name"] =="Tom Boeckenhauer"].sort_values(by ='Sales', ascending=False ).head()
centeral_region =  df[df["Region"] == "Central"][['Product Name', 'Sales']]

# History and Shipping Analysis
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
date_2017 = df[df['Order Date'].dt.year == 2017]
ordred_take_more_than_5 = df[(df['Ship Date'] - df['Order Date']).dt.days > 5]
Second_Class = df[df['Ship Mode'] == 'Second Class']

# Geographical analysis
Top_5_states = df['State'].value_counts().head()
west_orders  = df[df['Region'] == 'West']
Top_10_cities = df['City'].value_counts().head(10).sort_values()
postal_code_more_9000 = df[df['Postal Code'] > 9000].sort_values(by = 'Sales' , ascending = False  )

# Product Analysis
teq_orders = df[df['Category'] == 'Technology']
Office_Supplies= df[df['Category'] == 'Office Supplies']
top_10_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending= False).head(10)
min_10_products = df.groupby("Product Name")['Profit'].sum().sort_values(ascending= True).head(10)

# Sales analysis
mean_of_sales = df['Sales'].mean()
medin_of_sales = df['Sales'].median()
std_of_sales = df['Sales'].std()
sales_200_500 = df[( (df['Sales'] >= 2) & (df['Sales'] <= 500) )]
df['Sales_per_Quantity'] = df['Sales'] / df['Quantity']

# Discount analysis
no_discount = df[df['Discount'] ==  0]
num_no_discount = len(no_discount)
HighDiscount = df[df['Discount'] > .3]
df['High_Discount'] = df['Discount'] > .25 # compare all elements  .

# Profitability analysis
loss_orders = df[df['Profit'] < 0 ]
Top_20_profit_orders_0 = df.groupby('Product Name')['Profit'].sum().sort_values(ascending = False ).head(20)
Top_20_profit_orders_1 = df.sort_values(by = 'Profit', ascending = False).head(20)
df['Profit_Rate'] = (df['Profit']/df["Sales"] )
Top_state_profit  = df.groupby('State')['Profit'].sum().sort_values(ascending = False).head(1)
minimum_state_profit = df.groupby('State')['Profit'].sum().sort_values(ascending= True).head(1)

# Indexing
New_df = df.set_index('Order ID' )
spacific_order_0 = New_df.loc['CA-2016-138688']
spacific_order_1 = df.iloc[0:6 ,0:5 ]
New_df.set_index('Product Name' , inplace= True )
New_df = New_df.reset_index( )

# Data cleaning
df.dropna(subset=['Postal Code'], inplace= True )
df.fillna({"Profit" :df.Profit.median() } , inplace= True )
df['Ship Mode'] = df['Ship Mode'].replace('Standard Class', 'Standard')
region_map = {'West': 'W', 'East': 'E', 'Central': 'C', 'South': 'S'}
df['Region'] = df['Region'].replace( region_map )


# Reading and writing data
df.to_csv('customer_sales_profit_0.csv' , columns= ['Customer Name', 'State', 'Sales', 'Profit'], index= False )
df[['Country', 'City', 'State', 'Postal Code', 'Region']].to_csv('customer_sales_profit_1.csv' , index= False )
df.sample(7).to_csv('customer_sales_profit_2.csv', index= False)
product_data_Frame = df[['Product Name', 'Category', 'Sub-Category', 'Sales', 'Profit']] # product sheet
with pd.ExcelWriter('customer_sales_profit_3.xlsx') as writer :
    df.to_excel(writer ,sheet_name = 'Orders' , index= False )
    product_data_Frame.to_excel(writer, sheet_name = 'Products' , index= False )

# Sales distribution:-
#plt.figure(figsize= (7,5))
#plt.hist(df['Sales'] , density= True , bins= 30 , color='skyblue' , edgecolor = 'black')
#plt.title("distrepution of Salse ")
#plt.xlabel('Sales')
#plt.ylabel('frequency')
#plt.legend()
#plt.show()
#plt.savefig('Sales_plot.png')

# Sales by category :- (Pie Chart)
sales_by_category  = df.groupby('Category')['Sales'].sum()
x = sales_by_category.index
y = sales_by_category.values
plt.figure(figsize= (9,5))
plt.plot(x , y , color= 'red' , label = 'sales by category' , marker = '*' , linewidth = 1  )
plt.title('Total Salse by category')
plt.xlabel('category')
plt.ylabel('Total sales')
plt.legend()
plt.show()
plt.savefig('sales_by_category.png')

# Sales by region :-
Sales_by_region = df.groupby('Region')['Sales'].sum()
x = Sales_by_region.index
y = Sales_by_region.values
plt.plot(x , y ,color = 'blue' , label = 'Sales' , marker = 'o' , linewidth = 1 )
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total sales')
plt.legend()
plt.show()
plt.savefig('sales_by_region.png')


# Sales over time :- line chart
monthly_salse_2017 = df.groupby(date_2017['Order Date'].dt.month)['Sales'].sum()
x = monthly_salse_2017.index
y = monthly_salse_2017.values
plt.figure(figsize= (9,5))
plt.plot(x ,y ,color = 'purple' , marker = 'o' , linewidth = 1 , label = 'Sales' , markersize = 5 )
plt.title('Monthly Sales in 2017')
plt.xlabel('month')
plt.ylabel('Total sales')
plt.legend()
plt.show()
plt.savefig('monthly_salse_2017.png')

#Top_10_citys
# Sales by city (Top 10 cities)
import matplotlib.pyplot as plt


# Sales by city
plt.figure(figsize=(10,30))
x = Top_10_cities.index
y = Top_10_cities.values
plt.plot(x, y ,marker = 'o' ,linewidth = 1 ,markersize = 4 , color='teal', label='Top 10 cities')
plt.title('Top 10 Cities by Number of Orders')
plt.ylabel('Number of Orders')
plt.xlabel('City')
plt.legend()
plt.show()


# Sales vs. Profit
plt.figure(figsize = (10 , 30))
plt.scatter(df['Sales'],df['Profit'] , alpha = 0.5, color = 'black', label = '  Profit')
plt.title('Sales vs Profit')
plt.xlabel('Salse')
plt.ylabel('Profit')
plt.grid(True)
plt.legend()
plt.show()