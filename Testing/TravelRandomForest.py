import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier

# Define feature columns (user input) and target value (destination to predict) for the Random Forest
FEATURES = ["Category", "Best Time to Visit", "Cost of Living"]
TARGET_VALUE = "Destination"

# Load the dataset from the CSV-file
df = pd.read_csv("destinations.csv", na_values="N/A", encoding="latin1")

# Convert categorical features into numerical values (One-Hot Encoding)
X = pd.get_dummies(df[FEATURES]) # Independent variables (features)
y = df[TARGET_VALUE] # Dependent variable (destination)

# Create and train the Random Forest
forest = RandomForestClassifier() # Initialize the model
forest.fit(X, y) # Train the model using the dataset

# Collect user inputs and store them in a DataFrame
pred_input = pd.DataFrame({
    "Category": ["Region"],
    "Best Time to Visit": ["Winter (Dec-Mar) for Northern Lights, Summer (Jun-Aug) for hiking"],
    "Cost of Living": ["Medium-high"]
})

pred_input_encoded = pd.get_dummies(pred_input) # Convert user input into numerical values (One-Hot Encoding)
pred_input_encoded = pred_input_encoded.reindex(columns = X.columns) # Ensure that the encoded user input matches the training dataset columns

pred_output = forest.predict(pred_input_encoded)[0] # Get the predicted destination based on the user input
pred_row = df[df[TARGET_VALUE] == pred_output] # Retrieve the row corresponding to the predicted destination

# Print details of the recommended destination
print(pred_row["Destination"].iloc[0])
print(pred_row["Region"].iloc[0])
print(pred_row["Country"].iloc[0])
print(pred_row["Currency"].iloc[0])
print(pred_row["Safety"].iloc[0])
print(pred_row["Cultural Significance"].iloc[0])
print(pred_row["Description"].iloc[0])