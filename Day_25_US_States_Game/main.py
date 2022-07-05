import csv
import math
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "grey"])
print(grey_squirrel)













# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# temperatures = data["temp"].to_list()
# length = len(temperatures)
# average = sum(temperatures)/length
# print(average)
# maximum = data["temp"].max()
# print(data[data.temp == maximum])

# monday = data[data.day == "Monday"]
# print(monday.temp)
# fahrenheit = int(monday).temp * (9 / 5) + 32
# print(fahrenheit)
