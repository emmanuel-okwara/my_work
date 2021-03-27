# often we want to group our data, and then do something specific to the group the data is in.
# To do this we use the groupby() method to do this.
# Group Analysis
    # To replicate the actions of the value_counts() methods
    # You could annotate data.groupby('column').column.count()
    # Eg reviews.groupby('points').points.count() 
    # The groupby created a group of reviews which allotted the same point values 
    # to the given wines.Then each of these groups , we grabbed the points()
    # Column and counted how many times it appeared. value_counts is just a
    # Shortcut to this groupby() operation
    # 
    # 
    # 
    # You can think of each group we generate as being a Slice of our 
    # DataFrame containing only data with the values that match
    # This dataframe is accessible to us directly using the apply() method, and we can then manipulate
    # the data in any way we see fit.
    # Here's one way of selecting the name of the first wine reviewed for each winery in the dataset:
    # reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
    # 
# For even more fine-grained control,you can also group by more than one column.
# For an example, here's how we would pick out the best wine by country and province.
# reviews.groupby(['country','province']).apply(lambda df: df.iloc[df.points.idxmax()])
# Another groupby() worth mentioning is the agg(), which lets you run a bunch of different 
# Functions on your DataFrame simultaneously. For example we can generate a statistical summary of the dataset as follows:
# For example reviews.groupby(['country']).price.agg([len,min,max])
# This will return 
#           len     min     max
#  country                      
#  Argenti  3800.0  4.0     230.0
#  Aremenia 2.0     14.0    15.0  ..etc
# Effective use of the groupby() function will let you be able to execute lots of really powerful things with your dataset
# Multi-Indexes 
    # A multi-index differs from a regular index in that it has multiple levels.
    # For example:
    # countries_reviewed  = reviews.groupby(['country']).description.agg([len])
    # And when we call countries reviewed it will give us a list of countries and provinces with their len 
    # 
#Multi-indicies have serveral methods for dealing with their tiered structure which are absent for single level indicies.
# They also require two levels of label inorder to retrieve a value.
# Dealing with multi-index output is a common 'gotcha' for users new to pandas.
# However, in general the multi-index method you will use most often is the one for converting back to a regualar index, the reset_index() method 
# Basically countries_reviewedl.reset_index() will reset the index of the grouped data back to what it was before 
# 
# Sorting 
    #Looking again at cv(country reviews ) we can see that grouping returns data in index order, not in value,
    # to get the data in the order we want them in we can sort it oueselves. The sort_values() method is handy for this.
    # For example 
    # Countries_reviewed = Countries_reviewed.reset_index()
    # Countries_reviewed.sort_values(by='len')
    # 
    # The sort_values() id set to an ascending_sort, where the lowest values go first.
    # However, most of the time we want a decending sort where the higher numbers go first .
    # To write this we denote it as
    # countries_reviewed.sort_values(by='len', ascending = False) # This will cause the data to start from the highest values to the lowest value
    # 
    # To sort by  index values you can use the method sort_index()
    # Know that you can sort by more than one column at a time :
    # For example 
    # Countries_reviewed.sort_values(by = ["countries", 'len'])                                                                 