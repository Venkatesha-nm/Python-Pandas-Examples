import pandas as pd


# DataFrame constructor syntax
#pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)


# Create pandas DataFrame from List
technolgies = [["Spark",20000, "30days"],["Pandas",25000,"40days"]]
df = pd.DataFrame(technolgies)
#print(df)

# Add Column & Row Labels to the DataFrame
column_names = ["Courses", "Fee", "Duration"]
row_abel = ['a','b']
df = pd.DataFrame(technolgies,columns=column_names,index=row_abel)
#print(df)

#data type of each column
#print(df.dtypes)

## Set custom types to DataFrame
types= {'Courses': str, 'Fee': float, 'Duration':str}
df1= df.astype(types)
#print(df1.dtypes)

# Create DataFrame from Dict
technologies = {
              'Courses':["Spark","Pandas"],
              'Fee': [20000, 25000 ],
              'Duration': ["30days", "40days"]
               }
df = pd.DataFrame(technologies)
#print(df)

# Create DataFrame with Index
technologies = {
              'Courses':["Spark","Pandas"],
              'Fee': [20000, 25000 ],
              'Duration': ["30days", "40days"]
               }
row_labels = ['a1','a2']
df = pd.DataFrame(technologies)
#print(df)

# Creates DataFrame from list of dict
technologies = [
    {'Courses': "Spark", 'Fee':20000,'Duration':"30days"},
    {'Courses':"Pandas",'Fee':25000,'Duration':'40days'}
]
df = pd.DataFrame(technologies)
#print(df)

# Create pandas Series
courses = pd.Series(["Spark","Pandas"])
fees = pd.Series([20000,25000])
duration = pd.Series(["30days","40days"])

df = pd.concat([courses,fees,duration],axis=1)
#print(df)

# Assign Index to Series
index_labels = ['r1','r2']
courses.index = index_labels
fees.index = index_labels
duration.index = index_labels

df = pd.concat({'Coureses': courses,
                'Course_Fee': fees,
               'Course_Duration':duration},axis=1)
#print(df)

#Creating DataFrame using zip() function
#Multiple lists can be merged using zip() method and the output is used to create a DataFrame.
courses = ["Spark","Pandas"]
fee = [20000,25000]
Duration = ["30days","40days"]
# Merge lists by using zip().
tuple_list = list(zip(courses,fee,Duration))
df = pd.DataFrame(tuple_list, columns = ['Courses','Fee','Duration'])
#print(df)

# Create Empty DataFrame
df = pd.DataFrame()
#print(df)

# Copy DataFrame to another
df2 = df.copy()
print(df)



