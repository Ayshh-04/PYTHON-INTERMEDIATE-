# # with open("weather_data.csv") as weather:
# #     data=weather.readlines()
# #     print(data)                   # issue this data needs too much cleaning and refining and that where import csv  comes in

# import csv
# # with open("weather_data.csv") as weather:
# #     data=csv.reader(weather)
# #     # print(data)
# #     # for row in data:
# #     #     print(row)     #gives value in separate strings much easier to work 
    
# #     temparture=[]
# #     next(data) #it skips first row and reads data
# #     for row in data:
# #         temparture.append(int(row[1]))
    
# #     print(temparture)

#     #csv works on csv data but i it has too many columns and we are working with too much data that where panda comes in



# import pandas

# # print(pandas.__version__) # to check if installed

# data=pandas.read_csv("weather_data.csv")
# # # print(data)
# # print(data["temp"])


# # data_dict=data.to_dict()
# # print(data_dict)

# # temp_list=data["temp"].to_list()
# # print(temp_list)

# # sum =sum(temp_list)
# # avg=sum/len(temp_list)
# # print(avg)

# # print(data["temp"].mean()) #done in single line

# # print(data["temp"].max())


# #data in column 
# # print(data["temp"])
# # print(data.temp)

# #data access in rows
# # print(data.day=="Monday") # in this it shows true or false available in whole row 
# # print(data[data.day=="Monday"]) # in this itgives row 
# # print(data[data.temp==data.temp.max()])

# # monday=data[data.day=="Monday"]
# # print(monday.condition)

# #CREATE DATAFRAME FROM SCRATCH
# # data_dictionary={
# #     "roommates":["ayush","sujal","sannidhya","shivam","swaraj","om"],
# #     "age":[18,19,20,21,22,23]
# # }
# # data_frame_creation=pandas.DataFrame(data_dictionary)
# # print(data_frame_creation)

# # data_frame_creation.to_csv("creating_frame_demo")

# import pandas

# data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# gray_squirrals= len(data[data["Primary Fur Color"]=="Gray"])
# cinamon_squirrals= len(data[data["Primary Fur Color"]=="Cinnamon"])
# black_squirrals= len(data[data["Primary Fur Color"]=="Black"])

# data_dict={
#     "fur_color":["Gray","Cinnamon","Black"],
#     "Count":[gray_squirrals,cinamon_squirrals,black_squirrals]
# }
# count_squirrals=pandas.DataFrame(data_dict)
# print(count_squirrals)

# count_squirrals.to_csv("SQUIRRAL COU")