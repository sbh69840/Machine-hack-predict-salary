import pandas 
import numpy as np 
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

train = pandas.read_csv("Final_Train_Dataset.csv")
test = pandas.read_csv("Final_Test_Dataset.csv")
min_exp = [int(val.split("-")[0].strip()) for val in train["experience"]]
train["min_exp"] = min_exp 
max_exp = [int(val.split("-")[1].split(" ")[0]) for val in train["experience"]]
train["max_exp"] = max_exp
train = train.drop(train.columns[train.columns.str.contains\
('unnamed',case = False)],axis = 1)
train = train.drop(["job_description","job_desig",\
"job_type","key_skills"],axis=1)

min_exp = [int(val.split("-")[0].strip()) for val in test["experience"]]
test["min_exp"] = min_exp 
max_exp = [int(val.split("-")[1].split(" ")[0]) for val in test["experience"]]
test["max_exp"] = max_exp
test = test.drop(["job_description","job_desig",\
"job_type","key_skills"],axis=1)

sal_unique = train["salary"].unique()
sal_to_index = {val:ind for ind,val in enumerate(sal_unique)}
ind_to_sal = {ind:val for ind,val in enumerate(sal_unique)}

train["location"] = [val.split("(")[0] for val in train["location"].str.lower()]
test["location"] = [val.split("(")[0] for val in test["location"].str.lower()]
train["location"] = [val.split(",")[0] for val in train["location"]] 
test["location"] = [val.split(",")[0] for val in test["location"]]
train["location"] = [val.split("/")[0] for val in train["location"]] 
test["location"] = [val.split("/")[0] for val in test["location"]]
loc_to_index = {val:ind for ind,val in enumerate(train["location"].unique())}

train["location"] = train["location"].map(loc_to_index)
test["location"] = test["location"].map(loc_to_index)

train["salary"] = train["salary"].map(sal_to_index)

exp_unique = train["experience"].unique()
exp_to_index = {val:ind for ind,val in enumerate(exp_unique)}
ind_to_exp = {ind:val for ind,val in enumerate(exp_unique)}
train["experience"] = train["experience"].map(exp_to_index)
test["experience"] = test["experience"].map(exp_to_index)

X = train[["min_exp","max_exp","location","company_name_encoded"\
,"experience"]].values 
y = train["salary"].values 
# y = to_categorical(y,6)
X_train,X_val,y_train,y_val = train_test_split(X,y,stratify=y,test_size=0.1)
X_test = test[["min_exp","max_exp","location","company_name_encoded"\
,"experience"]].values
print(X_test.shape)

#Build the model using randomforestclassifier
from sklearn.ensemble import RandomForestClassifier 
clf = RandomForestClassifier(n_estimators=1000, max_depth=4,random_state=0)
clf.fit(X_train,y_train)
print(clf.feature_importances_)
print(clf.score(X_val,y_val))
sadasd=asdas
# X_train = np.expand_dims(X_train,axis=-1)
# X_val = np.expand_dims(X_val,axis=-1)
# X_test = np.expand_dims(X_test,axis=-1)

# y_train = np.expand_dims(y_train,axis=-1)
# y_val = np.expand_dims(y_val,axis=-1)

#Build the model using keras 

from keras.models import Sequential 
from keras.layers import Dense,Conv1D,MaxPooling1D,Flatten
from keras.callbacks import ModelCheckpoint


path = "model_3_layer_com.h5"
check = ModelCheckpoint(path,monitor="val_acc",verbose=1,save_best_only=True\
,mode="max")
model = Sequential()
model.add(Dense(32,activation="relu",input_dim=X_train.shape[1]))
model.add(Dense(16,activation="relu"))
model.add(Dense(6,activation="softmax"))
model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
model.fit(X_train,y_train,batch_size=100,epochs=100,validation_data=(X_val,\
y_val),verbose=0,callbacks=[check])

# from keras.models import load_model 
# model = load_model("model_3_layer_com.h5")
# result = model.predict(X_test)
# new_res = []
# for a in result:
#     new_res.append(sal_unique[a.tolist().index(max(a))])
# test["salary"] = new_res 
# test = test.drop(["min_exp","max_exp","experience","company_name_encoded\
# "],axis=1)
# test.to_csv("Submit.csv",index=False)
# new_tes = pandas.read_csv("Submit.csv")
# writer = pandas.ExcelWriter('submit1.xlsx')
# new_tes.to_excel(writer,"Sheet1",index=False)
# writer.save()