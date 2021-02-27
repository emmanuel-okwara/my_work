#creating and writing using [pandas]
    #pandas is the most popular python library for data analysis

#importing pandas
import pandas as pd

#there are two core objects in pandas: the Dataframe and the Series.
    #DataFrame
        #A dataframe is a table. it contains an array of individual entries
        #each of which has a certain value. each entry corresponds to a row and a column.
        #pd.DataFrame({'Yes':[50,21],'no':[131,21]})
        #output
        #   YES    NO
        # 0  50    131
        # 1  21    21
        # You can create string,int,float tables 

    #Series
        # A series is a sequence of data values , if a Dataframe is a table 
        # a Series is a list and you can create one with nothing more than a list
        #pd.Series([1,2,3,4,5]) this is a series
        # in essense a series is  a single column of a dataframe
        #So you can assign column values to the Series the same way as before,
        #  using an index parameter. 
        # However,a Series does not have a column name, 
        # it only has one overall name:
#Reading data files
    #pandas can be used to read all sort of data
    # pd.read_clipboard
    # pd.read_csv
    # pd.read_excel
    # pd.read_json
    # and other file storages
    # we can use the shape attribute to check how large the DataFrame is 
    # eg wine_reviews.shape
    #  output = (S129971,14) 14 columns and 129971 rows

    # you can examine the content of the data using data.head()
    #the pd.read_csv has over 30 optional parameters you can specify
    #you can the index column using index_col.

# i am going to be exporting a dataframe i will create
data = pd.DataFrame([['hello','my','what'],['name','is','do'],['emmanuel','okwara','jog']],columns=['noun','Adjective','verb'])
data.to_csv('dataset.csv')
data.to_html('dataset.html')

#This is how it works.
#cool!!!🦞🐙🦑🦐 enjoy the food.
