'''# A better way to test your model

#What is cross-validation:
    #this is when we run our modeling process on different subsets of the data to get multiple measures to model
    #quality

# For example, we could begin by dividing the data into 5 pieces, 
# each 20% of the full dataset. In this case, 
# we say that we have broken the data into 5 "folds".

#Then, we run one experiment for each fold:

#In Experiment 1, we use the first fold as a validation (or holdout) set and everything else as training data. 
#This gives us a measure of model quality based on a 20% holdout set.
#In Experiment 2, we hold out data from the second fold (and use everything except the second fold for training the model). 
# The holdout set is then used to get a second estimate of model quality.
#We repeat this process, using every fold once as the holdout set. Putting this together, 100% of the data is used as holdout at some point, 
# and we end up with a measure of model quality that is based on all of the rows in the dataset (even if we don't use all rows simultaneously).

'''

'''
When should you use cross-validation?
Cross-validation gives a more accurate measure of model quality, 
which is especially important if you are making a lot of modeling decisions
 However, it can take longer to run, because it estimates multiple models (one for each fold).


So, given these tradeoffs, when should you use each approach?

For small datasets, where extra computational burden isn't a big deal, 
you should run cross-validation.
For larger datasets, a single validation set is sufficient. 
Your code will run faster, and you may have enough data that there's little 
need to re-use some of it for holdout.
There's no simple threshold for what constitutes a large vs. 
small dataset. But if your model takes a couple minutes or less to run, it's probably worth switching to cross-validation.

Alternatively, you can run cross-validation and see if the scores for each experiment seem close. 
If each experiment yields the same results, a single validation set is probably sufficient.

'''


'''import pandas as pd

# Read the data
data = pd.read_csv('../input/melbourne-housing-snapshot/melb_data.csv')

# Select subset of predictors
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]

# Select target
y = data.Price

'''
'''
Then, we define a pipeline that uses an imputer to fill in missing values and a random forest model to make predictions.

While it's possible to do cross-validation without pipelines, it is quite difficult! Using a pipeline will make the code remarkably straightforward.

from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

my_pipeline = Pipeline(steps=[('preprocessor', SimpleImputer()),
                              ('model', RandomForestRegressor(n_estimators=50,
                                                              random_state=0))
                             ])

'''

'''
We obtain the cross-validation scores with the cross_val_score() function from scikit-learn. We set the number of folds with the cv parameter.

from sklearn.model_selection import cross_val_score

# Multiply by -1 since sklearn calculates *negative* MAE
scores = -1 * cross_val_score(my_pipeline, X, y,
                              cv=5,
                              scoring='neg_mean_absolute_error')

print("MAE scores:\n", scores)
MAE scores:
 [301628.7893587  303164.4782723  287298.331666   236061.84754543
 260383.45111427]
The scoring parameter chooses a measure of model quality to report: in this case, we chose negative mean absolute error (MAE). The docs for scikit-learn show a list of options.

It is a little surprising that we specify negative MAE. Scikit-learn has a convention where all metrics are defined so a high number is better. Using negatives here allows them to be consistent with that convention, though negative MAE is almost unheard of elsewhere.

We typically want a single measure of model quality to compare alternative models. So we take the average across experiments.

'''


