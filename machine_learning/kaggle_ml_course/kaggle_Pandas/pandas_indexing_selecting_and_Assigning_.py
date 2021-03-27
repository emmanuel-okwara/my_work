#selecting specific valued of a pandas Dataframe or Series 
#to work on is an implicit step in almost any data operation you will run

#Native accessors
    #native python objects  provide good ways of indexing data
    #Pandas carries all of these over which helps make it easy to start with.

    #these are two ways of selecting a specific series out of a dataframe
    #data.properties (metod)
    #OR data['properties'][num]

#indexing in pandas
    #panda has its own accessor operators LOC and ILOC
    #for more advanced operations , these are the ones you're supposed to be using 
#index based selections
    #pandas indexing works in one of two ways 
        #index-based-selection:
            #this is when you select data based on its numerical position in the data
            #iloc follows this paradigm
                #eg
                    #data.iloc[0]
                #both loc and iloc are row first,column-second
                #this is the opposite of what we do in python.
                #so something like this data.iloc[:,0] select all the data in the first column
        #label based selections 
            #this is where loc is used 
            #for example data.loc[0,'country']
            #with loc you can specify how many columns you want to select
            #data.loc[:,['column','column1','column2']]
#Choosing between loc and iloc:
    #when choosing what to use you have to remember the two distinct difference 
    #between the two
#Manipulating the index
    #we can manipulate the index of a dataset using set_index()
    #eg data.set_index('title')
#Conditional selection
    #you can select columns based on conditions that is met by the 
    #columns 
    #eg
        #data.loc[data.country == 'Italy']
        #data.loc[(data.country == 'Italy') & (data.point >= 90)]
        # you can use the & ampersnd sign to to bring two questions together
        #you can use the | sign to give an or condition to tell the dataset to select one 
        # one condition or another.
#pandas come with built in conditional selectors 
    #the first is (isin) 'isin' is lets you select data whose values is in the list of values.
    #for example data.loc[data.country.isin(['italy','France'])]
    #The second is isnull() and its comparison notnull()

#Assigning data 
    #assigning data to a dataframe is easy. you can either assign
    # a constant value or an iterable value
    # assigning a constant value
        #data.['column'] = value // the value can be an interger or a string 
    # assigning an iterable 
        #data.['column'] = range(len(data),0,-1) 