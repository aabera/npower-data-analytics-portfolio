import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load data
df = pd.read_csv("diabetic_data.csv")

# 2. Advanced Feature Engineering (Mapping string ranges to numeric midpoints)
age_mapping = {
    "[0-10)": 5, "[10-20)": 15, "[20-30)": 25, "[30-40)": 35, "[40-50)": 45,
    "[50-60)": 55, "[60-70)": 65, "[70-80)": 75, "[80-90)": 85, "[90-100)": 95
}
df["age_numeric"] = df["age"].map(age_mapping)

# [FIX] Handle missing data: Drop rows where age mapping failed to prevent scikit-learn ValueError
df = df.dropna(subset=["age_numeric"])

# 3. Target Feature Engineering (Creating binary 1s and 0s)
df["readmitted_binary"] = (df["readmitted"] != "NO").astype(int)

# 4. Isolate Features Matrix (X) and Target Vector (y)
features = [
    "age_numeric", "time_in_hospital", "num_lab_procedures", 
    "num_procedures", "num_medications", "number_outpatient", 
    "number_emergency", "number_inpatient", "number_diagnoses"
]
X = df[features]
y = df["readmitted_binary"]

# 5. Data Splitting (Freeze split across sessions)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Model Construction & Fitting
# [ENHANCEMENT] Added class_weight="balanced" to counter class imbalance in readmission rates
model = DecisionTreeClassifier(max_depth=5, class_weight="balanced", random_state=42)
model.fit(X_train, y_train)

# 7. Prediction Generation & Final Evaluations
y_pred = model.predict(X_test)

print("--- EVALUATION REPORT ---")
print(f"Overall Accuracy Score: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")
print("Confusion Matrix Layout:")
print(confusion_matrix(y_test, y_pred))
print("\nDetailed Performance Breakdown:")
print(classification_report(y_test, y_pred, target_names=["Not Readmitted (0)", "Readmitted (1)"]))

# [ENHANCEMENT] Print feature importances to see which factors drive predictions the most
print("\n--- FEATURE IMPORTANCE BREAKDOWN ---")
importances = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)
print(importances)

