#Michael Bermudez
#4/22/21
#This code reads in a csv file and does the following:
#1) Prints out how many rows of data there is in the csv file.
#2) Removes rows from the read csv file with invalid Profit values and prints
# an accurate number of valid entries
#3) Converts the updated file into a JSON file called data2.json
#4) Orders the data based on profit value and prints the top 20 highest profit.

import pandas as pd
import json

col_list = "Profit (in millions)"
#open csv file using pandas and store into df
with open('data.csv', newline='') as csvfile:

    df = pd.read_csv(csvfile)   
#convert the df file into dictionary for easier use later and store in values
values = df.to_dict('records')

#1)
print("Number of rows in this csv file: ", len(values))

#use a list comprehension inorder to remove invalid entries while iterating 
#through the dictionary list of values
data2_json = [x for x in values if not x[col_list] == "N.A."]

#2)
print("Number of rows in file after removing invalid rows: ", len(data2_json))

#3) Converts the updated file into a JSON file called data2.json
with open('data2.json', 'w') as f:
    json.dump(data2_json, f)

#4) Orders the data based on profit value and prints the top 20 highest profit
# sorted from lowest to highest so order must be reversed
output = sorted(data2_json, key = lambda k: float(k[col_list]), reverse=True)

for item in range(len(output[:19])) :
    print(output[item])
        
