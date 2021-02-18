#choosing plot types 
#trends - a trend is defined as a pattern of change.
    #sns.lineplot is used to show trends over a period of time, and multiple lines can be used to 
    # show trends in  more than one group.


#Relationships - different chart can be used to understand variables in your data
    #sns.barplot are useful for comparing quantities corresponding to different groups 
    #sns.heatmaps can be used to find color-coded patterns in tables of numbers. 
    #sns.scatterplot shows the relationship between two continuous variables ; if color coded we can show the 
    # relationship with a third categorical variable.
    #sns.regplot makes it easier to see any linear  relationship between two variables.
    #sns.lmplot you can draw multiple regression lines for multiple color-coded groups
    #sns.swarmplot show the relationship between a continious variable

#Distribution - we visualize distributions to show the possible values  that we can expect to see in a variable 
# along with how likely they are
    #sns.distplot - histograms show the distributio of a single numerical variable.
    #sns.kdeplot show the estimated smooth distribution of a single numerical variable 
    #sns.jointplot used to display a 2d kde plot with the corresponding kde plots for each individual variable




#Changing Styles with seaborn 
    #sns.set_style('dark ') allows for you to change the theme of the charts 
    # seaborn themes are ('darkgrid','whitegrid','ticks','dark','white')