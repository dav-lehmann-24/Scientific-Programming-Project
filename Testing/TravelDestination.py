import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotly import express as px

# Load the dataset from the CSV-file
df = pd.read_csv('destinations.csv', na_values='N/A', encoding='latin1')

# Display the first 10 rows of the dataset to get an overview
print(df.head(10))
print("---------------------------------------------------------------------------------------------------------------")

# Display information about the dataset, including column names, non-null values and data types
print(df.info())
print("---------------------------------------------------------------------------------------------------------------")

# Show the number of missing values (NaN) in each column
print(df.isnull().sum())
print("---------------------------------------------------------------------------------------------------------------")

# Display the number of unique values in each column
print(df.nunique())
print("---------------------------------------------------------------------------------------------------------------")

# Create a pie chart to show the distribution of travel destinations by country
fig = px.pie(df, names="Country", title="Distribution of Countries")
fig.update_traces(textposition="inside", textinfo="percent+label") # Show percentage and labels inside the pie slices
fig.show() # Display the pie chart

# Create a bar chart to show the distribution of cost of living across different countries
plt.figure(figsize=(12, 6)) # Set the figure size for better readability
sns.countplot(x='Country', hue='Cost of Living', data=df) # Create a count plot grouped by country and cost of living
plt.title('Cost of Living in the different countries') # Set the title of the plot
plt.xlabel('Country') # Label the x-axis
plt.ylabel('Count') # Label the y-axis
plt.xticks(rotation=90) # Rotate x-asis labels for better visibility
plt.legend(title='Cost of Living') # Add a legend to indicate different cost categories
plt.show() # Display the bar chart

# Create another pie chart to show the distribution of different currencies used in the dataset
fig = px.pie(df, names="Currency", title="Distribution of Currencies")
fig.update_traces(textposition="inside", textinfo="percent+label") # SHow percentage and labels inside the pie slices
fig.show() # Display the pie chart