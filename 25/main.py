# with open("weather_data.csv", "r") as csvFile:
#     data = csvFile.readlines()
#     print(data)
import csv
import pandas

# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#     print(temps)

data = pandas.read_csv("weather_data.csv")
# print(data.temp)
# dict = data.to_dict()
# print(dict)
# list = data["temp"]
# # Column
# # data["column"]
# print(list.max())
# print(list.mean())

# Row
# var = data[data.temp == data.temp.max()]
# monday = data[data.day == "Monday"];
# fharen = monday.temp[0]*9/5+32

# create dataframe

# data_dict = {
#     "students": ["amy", "james"],
#     "scores": [12, 32]
# }
#
# ua = pandas.DataFrame(data_dict)
# ua.to_csv("new_data.csv")

import pandas

squirl_data = pandas.read_csv("fixed_data.csv")
gray_squirls = len(squirl_data[squirl_data.Primary_Fur_Color == "Gray"])
red_squirls = len(squirl_data[squirl_data.Primary_Fur_Color == "Cinnamon"])
black_squirls = len(squirl_data[squirl_data.Primary_Fur_Color == "Black"])

result_dict = {
    "Fur Culor": ["grey", "red", "black"],
    "Count": [gray_squirls , red_squirls, black_squirls]
}

final = pandas.DataFrame(result_dict)
final.to_csv("squirrel_count")