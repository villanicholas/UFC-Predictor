# UFC-Predictor

Demo Link: https://www.youtube.com/watch?v=qM7PbgJr_Uw

UFC Fight Winner Prediction Script
This project predicts the winner between two UFC fighters using a pre-trained Gradient Boosting model based on fighter statistics.

Features
Pre-Trained Model: Utilizes a Gradient Boosting Classifier for prediction.
Dynamic Feature Engineering: Computes features like height difference, reach advantage, and age difference dynamically.
Comprehensive Dataset: Works with a dataset (ufc_fighters_statsnew.csv) containing fighter statistics such as:
Height, reach, wins, losses, and draws.
Significant strikes, takedown averages, and defense percentages.
Additional features like win_percentage, total_fights, and age.
Key Assumptions
The dataset is formatted correctly with all necessary columns.
The model was trained with specific feature names and expects a consistent format during predictions.
How It Works
Data Preprocessing:

Converts fighter height from string format (e.g., 5'8") to numeric (in inches).
Handles missing values by imputing with the median value for numeric columns.
Encodes categorical features using one-hot encoding.
Feature Preparation:

Dynamically computes features for both fighters (e.g., height difference, reach advantage).
Aligns the feature set with the model's training requirements.
Prediction:

Predicts the winner based on input fighter names.

Dependencies
Python Libraries:
pandas: For data manipulation.
joblib: For loading the pre-trained model.
scikit-learn: For Gradient Boosting and evaluation metrics.
Usage
Prepare the Dataset:

Ensure the dataset file (ufc_fighters_statsnew.csv) is in the same directory as this script.
The dataset should include fighter statistics with columns like height, reach, wins, losses, sapm, etc.
Specify Fighter Names:

Replace fighter1 and fighter2 in the script with actual fighter names from the dataset.
Run the Script:

Execute the script to predict the winner between the two fighters.
Interpret the Output:

The script will print the feature set used for prediction and the predicted winner.
