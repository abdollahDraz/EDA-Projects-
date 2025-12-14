import pandas as pd
import matplotlib.pyplot as plt
#'gender', 'race/ethnicity', 'parental level of education',
# 'lunch', 'test preparation course', 'math score',
# 'reading score', 'writing score'
df = pd.read_csv(r"E:\AI\instant program\Kaggle_Data\Student Perfomance\StudentsPerformance.csv")
print(list(df.columns))
df_discribe = df.describe()
frist_7_rows = df.head(7)
rows_columns = df.shape
name_of_columns = list(df.columns)
math_geder = df[['math score', 'gender']]
Score_more_90 = df[df['math score'] > 90 ]
male = df[df['gender'] == 'male'] [['gender' ,'math score', 'reading score', 'writing score']]
mean_of_math = df['math score'].mean()
print(mean_of_math)
std_of_reading = df['reading score'].std()
max_score_of_writing = df.sort_values(by = ['writing score'], ascending = False).head(10)[ ['gender','writing score']]
df.sort_values(by = 'math score' , ascending = False , inplace = True)
num_of_gender = df['gender'].value_counts()
df['avg_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
top_10_avr = df.sort_values(by = ['avg_score'], ascending = False).head(10)
mean_of_grade_of_parental_level_of_education =df.groupby("parental level of education")[['math score', 'reading score', 'writing score']].mean()
grade_of_parental_level_of_education = df.groupby("parental level of education")[['math score', 'reading score', 'writing score']].sum()
Table_mean_of_math = df.pivot_table(index ='gender' , columns =  'lunch' ,values = 'math score'   ,aggfunc = 'mean' )
ranmdom_row = df.sample(1)
df.rename(columns = {'math score' : 'Math score'} , inplace = True )
df.drop(columns ='lunch' , inplace = False)
done_preparation_course = df[df['test preparation course' ] == 'completed']
df[(df['gender'] == 'female' ) & (df['Math score'] > 95)]['gender'].value_counts()
df.loc[10]['Math score']
df.iloc[ : 10]
def Overall_assessment_tester (avrage_score) :
    if avrage_score >= 90:
        return 'excellent'
    elif avrage_score >= 80 and avrage_score <= 90:
        return 'very good'
    elif avrage_score >= 70 and avrage_score <= 80:
        return 'good'
    elif avrage_score >= 60 and avrage_score <= 70:
        return 'acceptable'
    else:
        return 'failed'
df['Overall_assessment'] = df['avg_score'].apply(Overall_assessment_tester)
mean_math = df.groupby('gender')['Math score'].mean()
df['reading score'].value_counts().index[0]
copy = df.copy()
df.fillna( 0 , inplace = True )
df.to_csv("Students_New.csv", index=False)
summary_stats = df[[ 'Math score', 'reading score', 'writing score']].describe()
gender_avg = df.groupby('gender')[['Math score', 'reading score', 'writing score']].mean()
Top_10_math_score = df['Math score'].sort_values(ascending = False ).head(10)
testcourse_count  = df['test preparation course'].value_counts().reset_index()
testcourse_count.columns = ['Course_Status','Count']
with pd.ExcelWriter( r"E:\AI\instant program\Kaggle_Data\Student Perfomance\Analysis_Result.xlsx") as writer:
    df.to_excel(writer , sheet_name = 'Raw Data' , index = False)
    summary_stats.to_excel(writer , sheet_name= 'Statistics' , index = False)
    gender_avg.to_excel(writer , sheet_name = 'Gender Average', index = False )
    Top_10_math_score.to_excel(writer , sheet_name = 'Top Math Students', index = False)
    testcourse_count.to_excel(writer , sheet_name = 'Course Analysis' , index = False )


# visulation

# counter  of gender :-
plt.figure(figsize = (7, 5))
df['gender'].value_counts().plot(kind = 'bar' , label = 'num of studet ' , color = ['steelblue', 'salmon'] , edgecolor = 'blue')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend()
plt.title('counter of gender ')
plt.show()
plt.savefig("counter_gender.png")


# distribution of Math Score :-
plt.figure(figsize= (7 , 5 ))
df['Math score'].hist(bins = 100 , label = "Math score" , color = 'blue' , edgecolor = 'red' , grid =True)
plt.xlabel("Range of Math scores")
plt.ylabel("count")
plt.legend(ncol = 1 , loc = 'upper right')
plt.title("Math score distribution")
plt.show()
plt.savefig("distribution_Math_score.png")


# Test Preparation Course :-
plt.figure(figsize = (7 , 5 ))
df['parental level of education'].value_counts().plot(kind = 'pie' , autopct = '%1.1f%%' )
plt.title("Test Preparation Course")
plt.show()



# math score for gender :-
plt.figure(figsize = (7 , 5 ))
df.boxplot(column= 'Math score' , by = "gender" , grid= False)
plt.title("Math score for gender")
plt.xlabel("Gender")
plt.ylabel("Math score")
plt.suptitle("")
plt.legend()
plt.show()


# Top 10 Math scores :-
plt.figure(figsize = (7 , 5 ))
x = Top_10_math_score.index
y = Top_10_math_score.values
plt.plot( x,y , marker = 'o' , color = 'blue' , markersize = 2 , label = 'Math score'  , linewidth = 1 )
plt.title("Top 10 Math Students")
plt.xlabel("Student index ")
plt.ylabel("Math score")
plt.legend()
plt.show()


# distribution of Math score and reading score
plt.figure(figsize = (7 , 5 ))
plt.scatter(df['Math score']  , df['reading score']  , alpha= .5 , color = 'blue' , label= 'Math score and reading score'  )
plt.title("Math score and reading score")
plt.xlabel("Math score")
plt.ylabel("reading score")
plt.legend()
plt.show()

# apply subplot :-
fig , axs  = plt.subplots( 2 ,3, figsize = (18 ,10 )) # fig is figure , axs is matrix contian 2 axis

# 1
x = df['gender'].value_counts().index
y = df['gender'].value_counts().values
axs[0,0].bar(x , y  , color = 'black' , edgecolor = "red" )
axs[0,0].set_title("Conter of Gender")
axs[0,0].set_xlabel("Gender")
axs[0,0].set_ylabel("count")

# 2
x = df['Math score']
axs[0,1].hist(x , bins = 10 , color = 'blue' , edgecolor = 'red' , label = "distribution of Math score" )
axs[0,1].set_title("Math score")
axs[0,1].set_xlabel("Math score")
axs[0,1].grid(True)
axs[0,1].set_ylabel("count")



# 3
df['test preparation course'].value_counts().plot(kind = 'pie', autopct='%1.1f%%' , ax = axs[0,2])
axs[0,2].set_title("Test Preparation Course Distribution")

# 4
df.boxplot(column = 'Math score' , by = 'gender' , ax = axs[1 , 0] , label = " math score")
plt.suptitle("")
axs[1,0].set_xlabel("Gender")
axs[1,0].set_ylabel("Math score")
axs[1,0].set_title("Math score - gender")


# 5
x = Top_10_math_score.index
y = Top_10_math_score.values
axs[1,1].plot(x ,y ,color = 'blue', marker= "*"  , label = "Top 10 Math score" , linewidth = 1  , markersize = 2 )
axs[1,1].set_title("Top 10 Math Students")
axs[1,1].set_xlabel("Student index ")
axs[1,1].set_ylabel("Math score")
axs[1,1].grid(True)


# 6
axs[1,2].scatter(df['Math score'] , df['reading score']  , alpha = .5 , color = 'blue' , label= 'Math score and reading score' )
axs[1,2].set_title("Math score and reading score")
axs[1,2].set_xlabel("Math score")
axs[1,2].set_ylabel("reading score")






plt.legend()
plt.show()
plt.savefig("summary.png")







