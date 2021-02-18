#Bar Chart
#plotting a barchart 
#sns.barplot(x=data.index,y=data.units_of_value)
#this tells python that we want to create a bar chart
'''
#CODE
plt.figure(figsize=(12,6))
plt.title('The Plot')
plt.xlabel('X_label')
plt.ylabel('Y_label')
sns.barplot(x= data.index,y=data['info'])
plt.show()
'''

#HEATMAP
#heatmaps are ued to indicate or display patterns in a dataset
#it consis of cells that are colour coded

#code
'''
plt.figure(figsize=(12,6))
plt.title("The title")
sns.heatmaps(data=your_data,annot = True)
'''
#the sns.heatmap tells seaborn that we want to create a heatmap
#data = data tells seaborn  to use the data we pass into it.
#annot =True thsis ensures that the values for each cell
# appears on the chart
