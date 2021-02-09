import pandas as pd
from pandas.core.arrays import sparse
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
import xgboost


file_data_loctaion = ['./train.csv','./test.csv']

#creating the file data
x = pd.read_csv(file_data_loctaion[0])


#Changing the negative values to positive
'''for i in range(len(x['Cost'])):
    if x.Cost[i] < 0 :
        x.Cost[i] = x.Cost[i]*-1

'''
#assignment
X = x.drop(['Cost','Customer Id'],axis=1)
y = x.Cost

print(len(y))
#getting numeric and object Columns 
num_cols = [cols for cols in X.columns if X[cols].dtype in ['int64','float64','float32','int32']]
object_cols = [cols for cols in X.columns if X[cols].dtype =='object']


#assingning the train and test data for training
x_train,x_test,y_train,y_test =train_test_split(X,y,train_size=0.8)

#x_train_num_and_onject_data
x_train_number_cols = x_train[num_cols]
x_train_object_cols = x_train[object_cols]

#x_test_num and object cols
x_test_number_cols = x_test[num_cols]
x_test_object_cols = x_test[object_cols]

#Transformer
imputer = SimpleImputer(strategy ='mean')
x_train_imputed = pd.DataFrame(imputer.fit_transform(x_train_number_cols))
x_test_imputed = pd.DataFrame(imputer.transform(x_test_number_cols))
#replace_cols 
x_train_imputed.columns = x_train_number_cols.columns
x_test_imputed.columns = x_test_number_cols.columns

#cat transformer 
OneHot = OneHotEncoder(handle_unknown = 'ignore',sparse =False)
x_train_encoded = pd.DataFrame(OneHot.fit_transform(x_train_object_cols))
x_test_encoded = pd.DataFrame(OneHot.transform(x_test_object_cols))

#replace Index
x_train_encoded.index = x_train_object_cols.index
x_test_encoded.index = x_test_object_cols.index

#data concatenation
X_train = pd.concat([x_train_imputed,x_train_encoded])
X_test = pd.concat([x_test_imputed,x_test_encoded])

#model
regressor_model = xgboost.XGBRegressor(n_estimators = 500,learning_rate = 0.05)
regressor_model.fit(X_train,y_train)

w = regressor_model.predict(X_test)

print(100*max(0,1-metrics.mean_squared_log_error(y_test,w)))
r