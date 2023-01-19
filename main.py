# collecting data from file and saving it in other one

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") #read file and save it to data
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"]) #give data lines where color= gray , and count it 
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"]) #give data lines where color= cinamon , and count it 
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"]) #give data lines where color= black , and count it 
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

#create dict with counted data
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

#create dataframe from the dict and save it to new file squirrel_count.csv
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

