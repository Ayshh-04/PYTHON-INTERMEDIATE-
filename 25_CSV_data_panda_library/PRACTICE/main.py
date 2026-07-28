import pandas as pd

data_file=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#print start and end top and bottom 10 rows
# print(data_file.head(10))
# print(data_file.tail(10))

# data_file.to_excel("2018_Central_Park_Squirrel_Census_.xlsx", sheet_name="squirrals", index=False)  #index fals helps ot store row index label

# print(data_file.info())   # print techical info like row column and datatype
#print(data_file.describe()) #summary of table
# print(data_file.sample(5)) #prints random 5 as defined

# print(data_file["Age"])
# specific_column=data_file[["Primary Fur Color","Age"]]  # use two brackets when inputing multiple columns 
# print(specific_column.head(5))

#print specific rows iloc method
# print(data_file.iloc[20:41])

#print with sepcification
# print(data_file[data_file["Primary Fur Color"] == "Gray"].head())