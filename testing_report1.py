import pandas 
import numpy as np 
from collections import Counter 
pandas.set_option("display.width",1000)
train = pandas.read_csv("Final_Train_Dataset.csv")
test = pandas.read_csv("Final_Test_Dataset.csv")
print("Testing data shape",test.shape)
print("Training shape",train.shape)
print(train.head())

print("Training null count",train.isnull().sum())
print("Testing null count",test.isnull().sum())
cols = train.columns 
for a in cols:
    print(a,len(train[a].unique()))
cols = test.columns 
for a in cols:
    print(a,len(test[a].unique()))
print("Training data types",train.dtypes)
print("Testing data types",test.dtypes)
import xlrd
import csv

def csv_from_excel():
    wb = xlrd.open_workbook('sample_submission.xlsx')
    sh = wb.sheet_by_name('sample_submission')
    your_csv_file = open('sample.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()
csv_from_excel()
samp = pandas.read_csv("sample.csv")
print(samp["salary"].unique()," Salary ")
print(train["salary"].unique(),"Salary Train")

print(train["job_type"].unique(),"Job type train")
print(test["job_type"].unique(),"Job type test")
#All the job types are same with just cases changed so the entire column 
#is not required
#Convert object data types to integers 

min_exp = [int(val.split("-")[0].strip()) for val in train["experience"]]
train["min_exp"] = min_exp 
max_exp = [int(val.split("-")[1].split(" ")[0]) for val in train["experience"]]
train["max_exp"] = max_exp
max_sub_min = train["max_exp"].values - train["min_exp"].values
train["max_sub_min"] = max_sub_min

# print(train["job_description"].head())
# print(train["job_desig"].head())

import seaborn as sns 
import matplotlib.pyplot as plt 
sns.set(style="ticks", color_codes=True)
min_exp_0 = train.loc[train["salary"]=="0to3","max_sub_min"]
min_exp_3 = train.loc[train["salary"]=="3to6","max_sub_min"]
min_exp_6 = train.loc[train["salary"]=="6to10","max_sub_min"]
min_exp_10 = train.loc[train["salary"]=="10to15","max_sub_min"]
min_exp_15 = train.loc[train["salary"]=="15to25","max_sub_min"]
min_exp_25 = train.loc[train["salary"]=="25to50","max_sub_min"]
print(min_exp_0.describe())
print(min_exp_3.describe())
print(min_exp_6.describe())
print(min_exp_10.describe())
print(min_exp_15.describe())
print(min_exp_25.describe())
print(train[["max_sub_min","max_exp","min_exp"]].head())

#The conclusion derived after the first analysis is that
#I will only use min and max experience values to predict the salary
#And nothing else other than that.
print("The conclusion derived after the first analysis is that\
I will only use min and max experience values to predict the salary\
And nothing else other than that.")
