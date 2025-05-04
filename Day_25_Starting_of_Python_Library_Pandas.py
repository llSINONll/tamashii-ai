import pandas as pd           #To import the pandas library as pd alias
df = pd.read_csv("iris.csv")  #making df dataframe variable to store csv data from iris.csv using pd.read_csv()

#Display First 5 (0-4) rows by default
print(df.head())

#To see the Basic Info
print(df.info())

#Statistical Summary
print(df.describe())

#Check for the missing values
print(df.isnull().sum())

#Filter Data

filtered_df = df[df['sepal_length'] > 5]
print(filtered_df)

#Group and Aggregate
grouped = df.groupby('species').mean()
print(grouped)


#Save to new csv
grouped.to_csv('grouped_data.csv')
