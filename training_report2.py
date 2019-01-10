import pandas 
import numpy as np
train = pandas.read_csv("Final_Train_Dataset.csv")
test = pandas.read_csv("Final_Test_Dataset.csv")
print(len(train["location"].unique()))
print(len(test["location"].unique()))
print(">>>>>>>>>>>>>>>>>>>>>>")

#After converting location to lower case
train["location"] = train["location"].str.lower()
test["location"] = test["location"].str.lower()

print(len(train["location"].unique()))
print(len(test["location"].unique()))
print(">>>>>>>>>>>>>>>>>>>>>>")

#After removing location in brackets and taking only cities
train["location"] = [val.split("(")[0] for val in train["location"]]
test["location"] = [val.split("(")[0] for val in test["location"]]

print(len(train["location"].unique()))
print(len(test["location"].unique()))
print(">>>>>>>>>>>>>>>>>>>>>>")

#After taking the first location before comma 
train["location"] = [val.split(",")[0] for val in train["location"]] 
test["location"] = [val.split(",")[0] for val in test["location"]]

print(len(train["location"].unique()))
print(len(test["location"].unique()))
print(">>>>>>>>>>>>>>>>>>>>>>")

#After taking the first location before comma 
train["location"] = [val.split("/")[0] for val in train["location"]] 
test["location"] = [val.split("/")[0] for val in test["location"]]

print(sorted(train["location"].unique()))
print(sorted(test["location"].unique()))
print(">>>>>>>>>>>>>>>>>>>>>>")
loc_to_index = {val:ind for ind,val in enumerate(train["location"].unique())}
loc_to_index[None] = -1
test["location"] = test["location"].map(loc_to_index)

print(test.isnull().sum())
print("In this report I have tried to reduce the nuber of unique location\
by just grabbing the cities where they belong to.")
