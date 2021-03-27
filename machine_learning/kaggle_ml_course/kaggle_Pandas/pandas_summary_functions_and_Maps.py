#Introduction 
    #this topic will cover the different operations that can be performed on a dataframe 
    #SUMMARY FUNCTIONS
        #one of the summary function that comes with pandas is the describe() method
            #this method generates a high level summary of the attributes 
            #of the given columns 
            #something to note is that this method is self aware and changes based on the dataset you pass to it 
        #If you want to get some particular simple summary statistics about a column in a DataFrame or Series , there is a helpful pandas 
        #function that makes this happen
            #you can use the mean() method to get the mean of a numerical columns 
            #To see a list of unique values in a datasets column you can use the unique() method or data.unique()
            #To see a list of unique values and how often the occur in the dataset
            # you use the value_counts() method 
#Maps 
    #
    # a map is a term borrowed from mathematics  for a function that takes one set of values and maps them to another set of values 
    # there are two mapping functions that you will often use 
    # map() is the first method 
    # suppose we wanted to remean the scores the wines recevied to 0 we can do this as follows 
    # data_mean = data.points.mean()
    # data.points.map(lambda x : x - data_mean)
        # the function you pass to map() should expect a single value from series and return a transformed version of the value 
    # apply is an equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.
    # def remean_points(row):
        #data.points = data.points - data_mean
        # return row
        # 
    # data.apply(remean_points,axis='columns)
    # applies a function on all the columns in a dataset if you dont specify whether rows or columns 
    #if you specify the axis and pass a function like sum it will create a series with the result of the returned values
    # A faster way of remeaning the point columns 
        #data.mean = data.points.mean()
        # data.points - data.mean
    #you could also perform addition of columns 
        #data.country + '-' + data.region_1
        # these types of operations are faster than map and apply because they use speed ups built into pandas 
        # All all of the standard python operators work in this manner
        # however they are not as flexible as map() and apply()
        # which can do more advanced things like applying conditional logic which cannot be done 
        # with addition and subtraction alone
        