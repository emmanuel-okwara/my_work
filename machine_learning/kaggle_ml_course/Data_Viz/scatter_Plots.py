#SCATTER PLOTS

#to create a scatterplot we use the
#sns.scatterplot() and specify the values for 
#The Horizontal x-axis (x=data['column']),and
#The vertical y-axis (y=data['column']).

#To double-check the strength of this relationship, 
# you might like to add a regression line, 
# or the line that best fits the 
# We do this by changing the command to sns.
# regplot.

#using the sns.regplot we are able to draw a line of best fit 
#to better explain the relationship between the data on your chart.


#Color-coded scatter plots
#We can use scatter plots to display the relationships between (not two, but...) three variables! 
# One way of doing this is by color-coding the points.

#For instance, to understand how smoking affects the relationship between BMI and insurance costs, 
# we can color-code the points by 'smoker', a
# nd plot the other two columns ('bmi', 'charges') on the axes.

#Example 
#sns.scatterplot(x=data_x_axis,y=data_y_axis,hue = data.yes_or_no_column)
#you can use the sns.lmplot command to add two regression lines coressponding to the different sets 
#of data on your chart
#SNIPPET
#sns.lmplot(x='data_x_axis_column',y='data_y_axis_column',hue='data_yes_or_no',data=dataset)
#you select the columns for your chart and then load the data

#Another chart
#sns.swarmplot(x=data_x_axis,
#               y= data_y_axis)

