# Scientific-Programming-Project: The Travel Destination Recommender

## Overview
__The Travel Destination Recommender__ is a _Python-based GUI application_ that recommends a travel destination based on user preferences, using machine learning. For the GUI it uses __Tkinter__ and to make the prediction of the destination it uses the __RandomForestClassifier__ from scikit-learn.

What can the user choose? The user has the following options to choose:

- Category: Choose a category the user would like to visit (e.g. City, Town, ...)
- Time to visit: Choose a time when the user would like to visit (e.g. Spring (April-May) or Fall (Sept-Oct), Year-round, ...)
- Cost of living: Choose how high the cost of living should be (e.g. Medium, High, ...)

After choosing the preferences, the application will recommend a travel destination, based on a pre-loaded dataset, using a __RandomForestClassifier__ to make a prediction.


## Installation & Setup
### Requirements
Be sure that you have Python installed, along with the dependencies:
```
pip install pandas scikit-learn tkinter
```
### Running the Application
1. Clone or download this repository
2. Ensure that you have the dataset "destinations.csv" in the same directory. You can get it from the repository or download it here: https://www.kaggle.com/datasets/faizadani/european-tour-destinations-dataset
3. Run the Python script
```
python TravelRecommender.py
```

## How it works
1. The program loads the data of the travel destinations from the CSV-file.
2. The user selects the prefered category, season to travel, and cost of living.
3. After hitting the Submit button, the input will be processed by the __Random Forest Classifier__ and it will predict a travel destination, based on the input of the user.
4. The recommended destination will be displayed in a frame, along with some information of the destination.


## Features
- An easy-to-use __Graphical User Interface__ to get the input of the user.
- Use of __Random Forest Classifier__ to recommend a destination for the user.
- A display of the recommended destination, with some useful information.


## Limitations
- The application is only based on the dataset, which means that the recommendations are only based on the data of this specific dataset.
- The user preferences are limited to three different categories, other categories could be added in the future.
- GUI doesn't deliver many options and is very basic, also room for improvement.
- The application uses basic machine learning, which can be enhanced to get more accurate predictions.


## Future Improvements
- Enhancing the machine learning of the program, to get better recommendations of travel destination.
- Provide more categories to choose for the user, to make predictions even more personalized.
- Use of more data of travel destinations, to get a wider range of options.
- Improve the GUI or convert the application to a web-based application.
- User feedback to get a better learning effect for the application.


https://github.com/user-attachments/assets/6d9ca125-0990-47df-bfe8-2bca6796ca6e

