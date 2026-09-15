import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
 
    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)
 
    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
 
# Update these two lines to include 'app/'
csvFilePath = r'app/data.csv'
jsonFilePath = r'app/data.json'

csv_to_json(csvFilePath, jsonFilePath)

'''
data.csv 
a,b,c
25,84,com
41,52,org
58,79,io
93,21,co

OUTPUT :
data.json
[
    {
        "a": "25",
        "b": "84",
        "c": "com"
    },
    {
        "a": "41",
        "b": "52",
        "c": "org"
    },
    {
        "a": "58",
        "b": "79",
        "c": "io"
    },
    {
        "a": "93",
        "b": "21",
        "c": "co"
    }
]
'''
