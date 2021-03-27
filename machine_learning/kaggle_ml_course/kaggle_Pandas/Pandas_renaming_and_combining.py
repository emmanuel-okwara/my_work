#Introduction 
    # Renaming 
        # The first function to be introduced id the rename 
        # function or method which lets you change index names and or column names
        # For example to change the points columm in our dataset to score , we would 
        # annotate this as reviews.rename(columns ={"points" : 'score'})
        # rename() lets you rename index or column values by specifying a index or column keyword parameter
        # Python Dictionaries are the most convienient 
        
        # To change the value of the index 
        # It will be annotated like reviews.rename(index = {0: "firstEntry",1:"secondEntry"})
        # In doing so you are able to assign the name of the index to a row.
        
        # To rename indices more efficiently you could use set_index() 
        # Both the row index and the column  index can have their own name attribute
        # The rename_axis() method may be used to change these names for example
        # reviews.rename_axis('wines',axis='rows').rename_axis('fields', axis="columns") 
    # Combining 
        # When performing operations on a dataset, we will sometimes need to combine different DataFrames and/or Series in non-trivial ways.
        # Pandas has three core mrthods for doing this. In order of increasing complexity 
        # These are concat(),join(),merge(). Most of what merge() can do can also be done more simply with join()
        # The simplest combining fucntion method is concat() , given a list of elements, this function will smush those elements together along an axis
        # For example 
        # candian_youtube = pd.read_csv(file_location)
        # british_youtube = pd.read_csv(file_location)
        # And to concat this two file together
        # pd.concat([candian_youtube, british_youtube]) 
        # The middlemost combiner in terms of complexity is join()
        # join() lets you combine different DataFrame objects which have an index in common 
        # left = canadian_youtube.set_index(["title","trendeing_date)"]) 
        # right = british_youtube.set_index(["title",'trending_date'])
        # left.join(right,lsuffix="_CAN",rsuffix="_UK")
        # The lsuffix and rsuffix parameters are necessary here because the data has the same 
        # column names in both British and Canadian datasets        
        # if this wasn't true 
        #                                                                   