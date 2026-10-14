
from pathlib import Path

import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "cleaned_training_data.csv"
MODEL_PATH = BASE_DIR / "best_model.pkl"

# Load dataset
df = pd.read_csv(DATA_PATH)
df = df.drop_duplicates().copy()

target = "outcome_variable"

# Remove rows without a target
df = df.dropna(subset=[target])

# Separate features and target
X = df.drop(columns=[target])
y = df[target].astype(str).str.strip()

# Identify numeric and categorical columns
numeric_columns = X.select_dtypes(include="number").columns.tolist()
categorical_columns = X.select_dtypes(
    exclude="number"
).columns.tolist()

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore")),
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_columns),
    ("categorical", categorical_pipeline, categorical_columns),
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced",
    )),
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Model training completed.")
print(f"Training rows: {len(X_train)}")
print(f"Testing rows: {len(X_test)}")
print(f"Accuracy: {accuracy_score(y_test, predictions):.3f}")

print("\nClassification report:")
print(classification_report(y_test, predictions, zero_division=0))

print("\nConfusion matrix:")
print(confusion_matrix(y_test, predictions))

joblib.dump(model, MODEL_PATH)
print(f"\nModel saved to: {MODEL_PATH}")
