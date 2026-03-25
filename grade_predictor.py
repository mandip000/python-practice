# Beginner AI Project: Student Grade Predictor
# Author: Mandip Yadav

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample data: marks and corresponding grade score
# Grade mapping: A=4, B=3, C=2, D=1, F=0
data = {
    "Math": [95, 85, 76, 65, 55, 40],
    "Physics": [92, 80, 78, 60, 50, 35],
    "Chemistry": [90, 82, 75, 65, 55, 30],
    "Grade": [4, 3, 3, 2, 1, 0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features (input) and target (output)
X = df[["Math", "Physics", "Chemistry"]]
y = df["Grade"]

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Test prediction
print("Test Data Predictions:")
predictions = model.predict(X_test)
for i, pred in enumerate(predictions):
    print(f"Input marks: {X_test.iloc[i].to_dict()} --> Predicted Grade Score: {pred:.2f}")

# User input for prediction
print("\nPredict your grade:")
math = float(input("Enter Math marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

pred_grade = model.predict([[math, physics, chemistry]])[0]

# Map back to letter grade
if pred_grade >= 3.5:
    letter = "A"
elif pred_grade >= 2.5:
    letter = "B"
elif pred_grade >= 1.5:
    letter = "C"
elif pred_grade >= 0.5:
    letter = "D"
else:
    letter = "F"

print(f"Predicted Grade: {letter}")