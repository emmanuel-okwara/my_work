from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics
from xgboost import XGBRegressor
import pandas as pd
from pandas.core.arrays import categorical
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, _name_estimators
from sklearn.model_selection  import train_test_split , cross_validate
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer
from xgboost.callback import EarlyStopping
from collections import Counter
import numpy as np

#file_locations = ['C:\\Users\\okwar\\Pictures\\hacker_earth_ml_model_dataset\\dataset\\train.csv','C:\\Users\\okwar\\Pictures\\hacker_earth_ml_model_dataset\\dataset\\test.csv']
file_location =['./train.csv','./test.csv']
training_data_ = pd.read_csv(file_location[0])
training_data =training_data_.copy()
testing_data = pd.read_csv(file_location[1])

for i in range(len(training_data.Cost)):
    if training_data.Cost[i] < 0 :
        training_data.Cost[i] = training_data.Cost[i]*-1

#changing data
s_d = training_data['Delivery Date'].copy()
d_d = training_data['Scheduled Date'].copy()

training_data['Scheduled Date'] = s_d
training_data['Delivery Date'] = d_d

#training_data
Y_train = training_data.Cost
x_train = training_data.drop(['Cost','Customer Id','Remote Location'],axis = 1)


#print(x_train['Artist Name'])
#print(x_train.columns)

#test_data 
test_d = testing_data[x_train.columns]

#testing and validating data
X_train,X_valid,y_train,y_valid =train_test_split(x_train,Y_train,train_size=0.8,test_size=0.2)

#print(y_.head())
#print(test_d)

#getting the numerical and categorical columns that will be used for transformation
num_cols = [cols for cols in x_train.columns if x_train[cols].dtype in ['int64','float64'] ]
cat_cols = [cols for cols in x_train.columns if x_train[cols].dtype =='object']

#print(num_cols,cat_cols)

numerical_transformer = SimpleImputer(strategy ='constant')

categorical_transformer =Pipeline(steps=[('imputer',SimpleImputer(strategy ='constant')),
('OneHot',OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(transformers=[('num',numerical_transformer,num_cols),('cat',categorical_transformer,cat_cols)])



#now the model
#model = RandomForestRegressor(n_estimators = 100,n_jobs = 2)
model = DecisionTreeRegressor( max_leaf_nodes = 1350)
#model = LinearRegression()


#model = RandomForestRegressor(n_estimators = 100,n_jobs =700)
real_model = Pipeline(steps=[('preprocessor',preprocessor),('model',model)])

real_model.fit(X_train,y_train)
preds = real_model.predict(X_valid)
new_preds = real_model.predict(test_d)

#print(100*max(0,1-metrics.mean_squared_log_error(y_valid,preds)))


#compress = dict(method='zip',archive_name='out.csv')

output = pd.DataFrame({'Customer Id':testing_data['Customer Id'], 'Cost':new_preds})
output.to_csv('out.csv',index='Customer Id')


print(100*max(0,1-metrics.mean_squared_log_error(y_valid,preds)))