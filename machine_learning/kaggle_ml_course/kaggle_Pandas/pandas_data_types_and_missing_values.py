

# Dtypes
# The data type for a column in a DataFrame or a Series id known as the dtype.
# You can use the dtype property to grab the type of a specific column
# For example to get the data type of a price column in a dataframe
# reviews.price.dtype
# This will return 
# dtype("float64") or dtype("int64")    
# Alternatively the dtypes() property returns the dtype of every column in the DataFrame
# it's possible to convert a column of one type into another wherever such a conversion makes sense by using the astype() 
# Function for example , we may transform the points columns from it's existing int64 datatype to a float64 DATa type 
# To do this you can type reviews.points.astype('float64')
# Pandas also support more exotic data-types, such as categorical data and timeseries data
# Because these datatypes are more rarely used , we will them.


# Missing Data
    # Entries missing values are given the value NaN, short for "Not a Number".
    # For technical reasons these NaN values are always of the float64 dtype.
    # Pandas provides some methods specific to a missing data, To select the NaN entries you can use pd.isnull() or its companion (pd.notnull()) 
    # Replacing missing values is a common operation. Pandas provides a really handy method for this problem fillna()
    # fillna() provides a few different strategies for mitigating  such data
    # 
    # For example 
    # reviews.region_2.fillna('1') this will convert all the nan values into 1 objects 
    # we could fill each missing value with the first non-null values that appears sometimes after the given record in the database 
    # This is known as the backfill strategy 
    # Alternatively, we may have a non-nulll value that we would like to replace.
    # suppose that since this dataset was published, reviewer Kerin O'Keefe has changed her Twitter handle from @kerinokeefe to @kerino. 
    # one way to reflect this in the dataset is using the replace() method:
    # eg. reviews.taster_twitter_handle.replace("@kerinokeefe","kerino")
    # 
    # Thus this will reflect across the dataset and the name will be updated as instructed.
    # The replace() method is used for replacing missing data which is given some kind of sentinel value in the dataset: things like "unknown" , "Undisclosed", "Invalid" and so on.
    #                                                                                                     
    #                                                                    
    #                                                                           