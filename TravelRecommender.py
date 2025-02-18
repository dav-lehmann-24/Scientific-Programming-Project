import tkinter as tk
import pandas as pd
from tkinter import ttk
from sklearn.ensemble import RandomForestClassifier


class TravelRecommender:
    def __init__(self):
        # Initializing the GUI
        self.root = tk.Tk()
        self.root.title("Travel Destination Recommender")
        self.root.geometry("1500x800") # Set the initial window size
        self.root.state("zoomed") # Maximize the window

        self.data = None # Variable to store the dataset for the load_data function

        self.setup_gui() # Calling the function to set up the GUI
        self.load_data() # Calling the function to load the dataset

    def load_data(self):
        try:
            self.data = pd.read_csv('destinations.csv', na_values='N/A', encoding='latin1') # Load the CSV-file

        except Exception as e:
            print(f"Error in loading the dataset: {str(e)}") # Print the error, if the CSV file could not be loaded

    def setup_gui(self):
        # Creating and arranging GUI components
        # Labels
        titleLabel = tk.Label(self.root, text="Welcome to the Travel Destination Recommender!", font=("Arial", 26, "underline", "bold"), fg="blue")
        titleLabel.pack(pady=5)

        descrLabel = tk.Label(self.root, text="Please choose some of the options and you'll get your next travel destination!", font=("Arial", 20, "bold"), fg="black")
        descrLabel.place(x=0, y=80)

        categoryLabel = tk.Label(self.root, text="What do you want to see:", font=("Arial", 14), fg="black")
        categoryLabel.place(x=0, y=150)

        timeLabel = tk.Label(self.root, text="In which season of the year do you want to travel:", font=("Arial", 14), fg="black")
        timeLabel.place(x=0, y=200)

        costLabel = tk.Label(self.root, text="What is the cost of the living:", font=("Arial", 14), fg="black")
        costLabel.place(x=0, y=250)

        # Dropdown Menus with their options
        categoryOptions = ['', 'City', 'Town', 'Coastal Town', 'Coastal Region', 'Lake', 'Island',
                           'Coastal City', 'Region', 'Mountain Range', 'Valley', 'Forest', 'Theme Park',
                           'Garden', 'Amusement Park', 'Castle', 'District', 'Square', 'Museum', 'Beach',
                           'Cultural Center', 'Peninsula', 'Railway', 'Church', 'Monastery Complex',
                           'Archaeological Site', 'Fjord', 'National Park', 'Cliff', 'Village',
                           'Mountain Pass', 'Waterfall', 'Natural Site', 'Bazaar', 'Palace', 'Mosque',
                           'Site', 'Opera House', 'Street', 'Monastery', 'Prehistoric Site', 'Memorial',
                           'Neighborhood', 'Geothermal Spa', 'Glacier Lagoon', 'Fortress', 'Spa Town']

        self.selected_category = tk.StringVar() # Variable to store selected category
        self.selected_category.set(categoryOptions[0]) # Default value
        categoryDropdown = tk.OptionMenu(self.root, self.selected_category, *categoryOptions)
        categoryDropdown.place(x=220, y=150)

        timeOptions = ['', 'Spring (April-May) or Fall (Sept-Oct)', 'Summer (June-September)', 'Summer (June-August)', 'Winter (Dec-Mar) for skiing, Summer (Jun-Sept)', 'Year-round']
        self.selected_time = tk.StringVar()
        self.selected_time.set(timeOptions[0])
        timeDropdown = tk.OptionMenu(self.root, self.selected_time, *timeOptions)
        timeDropdown.place(x=420, y=200)

        costOptions = ['', 'Free', 'Medium', 'Medium-high', 'High', 'Extremely high']
        self.selected_cost = tk.StringVar()
        self.selected_cost.set(costOptions[0])
        costDropdown = tk.OptionMenu(self.root, self.selected_cost, *costOptions)
        costDropdown.place(x=250, y=250)

        # Submit Button with command
        submitButton = tk.Button(self.root, text="Submit", width=75, font="Arial", fg="black", bg="white", command=self.get_recommendation)
        submitButton.place(x=0, y=300)

        # Frame for recommendation
        self.result_frame = ttk.LabelFrame(self.root, text="Recommended Destination")
        self.result_frame.place(x=500, y=400, width=900, height=600)

        # Text to show the recommendation
        self.result_text = tk.Text(self.result_frame, wrap=tk.WORD, height=30, width=110)
        self.result_text.pack(padx=10, pady=10)

    def get_recommendation(self):
        if self.data is None:
            return # Stop function execution if the dataset is not loaded

        # Define features (user input) and target value (destination to predict) for the Random Forest
        FEATURES = ["Category", "Best Time to Visit", "Cost of Living"]
        TARGET_VALUE = "Destination"

        # Convert categorical features into numerical values (One-Hot Encoding)
        X = pd.get_dummies(self.data[FEATURES]) # Encode the categories to numerical values
        y = self.data[TARGET_VALUE]

        # Creating and train the Random Forest
        forest = RandomForestClassifier() # Initialize the model
        forest.fit(X, y) # Train the model using the dataset

        # Collect user inputs and store them in a DataFrame
        preferences_input = pd.DataFrame({
            'Category': [self.selected_category.get()],
            'Best Time to Visit': [self.selected_time.get()],
            'Cost of Living': [self.selected_cost.get()]
        })

        # Encode the user input to numerical values and adding missing training data columns
        preferences_input_encoded = pd.get_dummies(preferences_input) # Convert user input into numerical values (One-Hot Encoding)
        preferences_input_encoded = preferences_input_encoded.reindex(columns = X.columns) # Ensure that the encoded user input matches the training dataset columns

        # Random Forest prediction and filtering the row for this prediction
        pred_output = forest.predict(preferences_input_encoded)[0] # Get the predicted destination based on the user input
        pred_row = self.data[self.data[TARGET_VALUE] == pred_output] # Retrieve the row corresponding to the predicted destination

        # Format the result text for the result_frame
        result_text = f"""
    Destination: {pred_row['Destination'].iloc[0]}\n\n
    Region: {pred_row['Region'].iloc[0]}, {pred_row['Country'].iloc[0]}\n\n
    Description: {pred_row['Description'].iloc[0]}\n\n
    Details:
    - Category: {pred_row['Category'].iloc[0]}
    - Best Time to Visit: {pred_row['Best Time to Visit'].iloc[0]}
    - Cost of Living: {pred_row['Cost of Living'].iloc[0]}
    - Safety: {pred_row['Safety'].iloc[0]}
    - Cultural Significance: {pred_row['Cultural Significance'].iloc[0]}
    - Currency: {pred_row['Currency'].iloc[0]}
    - Majority Religion: {pred_row['Majority Religion'].iloc[0]}
    - Language: {pred_row['Language'].iloc[0]}
    """

        # Clear previous results and display the new recommendation
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result_text)

    def run(self):
        self.root.mainloop() # Start the GUI

if __name__ == "__main__":
    app = TravelRecommender()
    app.run() # Run the application