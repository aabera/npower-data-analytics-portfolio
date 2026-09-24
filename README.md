# Feature Selection Criteria in Machine Learning

When building predictive models, the goal of feature selection is to identify the smallest subset of variables that yields the maximum predictive power. This file outlines the four core pillars of feature selection criteria used in our workflow.

## 📋 The Four Pillars of Feature Selection

### 1. Relevance to the Target (Predictive Power)
A feature must share a meaningful relationship with the variable you are trying to predict.
* **Statistical Significance:** Features should have a measurable statistical relationship with the target (e.g., a high correlation coefficient for linear models, or high mutual information for non-linear models).
* **Variance Threshold:** Features must exhibit variation. If a column contains the identical value for 99% of your rows (near-zero variance), it provides virtually no information for the model to learn from.

### 2. Redundancy & Collinearity
Features should provide entirely *new* information, rather than replicating what another feature has already captured.
* **Low Multicollinearity:** If two features are highly correlated with each other (e.g., `patient_age_in_years` and `patient_birth_year`), one should be omitted. Keeping both introduces noise and destabilizes tree splits or regression coefficients.
* **Information Uniqueness:** Every added feature should explain a distinct dimension of the variance in the dataset.

### 3. Computational Efficiency & Parsimony
Including too many features slows down training, increases inference times, and risks overfitting.
* **The Principle of Parsimony (Occam's Razor):** A simpler model with fewer features is often vastly superior in a production environment due to easier maintenance and faster execution speeds.
* **Curse of Dimensionality:** Keeping feature counts low prevents data from becoming too sparse, allowing models to find genuine, generalizable patterns.

### 4. Data Quality & Operational Constraints
A feature might be statistically valuable but functionally or operationally unusable.
* **Missingness:** If a feature is missing data in a majority of your records, the risk of guessing (imputing) those values often outweighs the benefit of keeping it.
* **Data Leakage:** Features must not contain information that wouldn't actually be available at the exact moment of prediction (e.g., including future discharge data when predicting a current admission).
* **Engineering Cost:** Avoid features that require expensive external API calls, immense computational overhead, or fragile upstream pipelines to calculate in real-time.

---

## 🛠️ Feature Selection Approaches

Depending on the criteria above, features can be filtered out using three main algorithmic strategies:

| Approach | How it Works | Common Examples |
| :--- | :--- | :--- |
| **Filter Methods** | Evaluates features independently of the model based on their intrinsic statistical properties. | Correlation Matrix, Chi-Square Test, Variance Threshold |
| **Wrapper Methods** | Uses a machine learning model to evaluate combinations of features, adding or removing them iteratively. | Forward Selection, Backward Elimination, Recursive Feature Elimination (RFE) |
| **Embedded Methods** | Feature selection happens natively and automatically *during* the model training process. | Lasso (L1) Regression Penalty, **Decision Tree Feature Importances** |

---

## 🚀 Getting Started

To run the machine learning script locally, follow these quick setup steps.

### Prerequisites
Make sure you have Python installed, along with the required libraries. You can install them via terminal/command prompt:
```bash
pip install pandas scikit-learn
```

### Execution
1. Clone this repository or download the files.
2. Place the `diabetic_data.csv` dataset in the same directory as the script.
3. Run the Python model:
```bash
python diabetes_readmission_tree.py
```

---

## 📊 Model Performance & Evaluation

The script evaluates the `DecisionTreeClassifier` (set to a balanced class weight and a max depth of 5) using three core metrics to guarantee transparent evaluation:

### 1. Accuracy Score
Reflects the overall percentage of correct predictions across both classes.

### 2. Confusion Matrix
Breaks down the raw count of predictions vs. actual reality:
* **True Negatives (TN):** Correctly predicted *Not Readmitted*.
* **False Positives (FP):** Incorrectly predicted *Readmitted*.
* **False Negatives (FN):** Incorrectly predicted *Not Readmitted*.
* **True Positives (TP):** Correctly predicted *Readmitted*.

### 3. Classification Report
Provides granular tracking across precision, recall, and f1-score:
* **Precision:** Out of all cases flagged as readmitted, how many were actually readmitted?
* **Recall:** Out of all actual readmissions, how many did the model successfully catch?
* **F1-Score:** The harmonic mean balancing precision and recall together.
## .Ashenafi Abera
