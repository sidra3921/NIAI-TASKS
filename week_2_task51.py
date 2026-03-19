"""
Week 2 - Task 51: Linear Regression in Python (Scikit-Learn)

This script demonstrates a full beginner ML pipeline:
1) Load an hours->scores dataset (from CSV if provided; otherwise use sample data)
2) Simple EDA: head/shape/correlation
3) Train/test split
4) Train a LinearRegression model
5) Inspect intercept + slope (coef)
6) Predict on test set and on a new value (e.g., 9.5 hours)
7) Evaluate with MAE, MSE, RMSE
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split


SEED = 42


def load_dataset(csv_path: str | None) -> pd.DataFrame:
    """
    If csv_path is provided and exists, load it.
    Otherwise, use a small built-in dataset similar to the common 'student_scores' example.
    """
    if csv_path:
        p = Path(csv_path)
        if p.exists() and p.is_file():
            df = pd.read_csv(p)
            # Expect columns like Hours, Scores (case-sensitive in many CSVs)
            if "Hours" not in df.columns or "Scores" not in df.columns:
                raise ValueError("CSV must contain columns named 'Hours' and 'Scores'.")
            return df[["Hours", "Scores"]]

        print(f"[Info] CSV not found at: {csv_path}. Using built-in sample data instead.\n")

    # Built-in sample dataset (Hours, Scores)
    data = {
        "Hours": [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7],
        "Scores": [21, 47, 27, 75, 30, 20, 88, 60, 81, 25],
    }
    return pd.DataFrame(data)


def main():
    # Optional: python week_2_task51.py path/to/student_scores.csv
    csv_path = sys.argv[1] if len(sys.argv) > 1 else None
    df = load_dataset(csv_path)

    print("=== Dataset preview ===")
    print(df.head())
    print("\nShape:", df.shape)

    print("\n=== Correlation (Hours vs Scores) ===")
    # corr() works on numeric columns
    print(df.corr(numeric_only=True))

    # Prepare X and y
    # scikit-learn expects 2D arrays for X
    X = df["Hours"].values.reshape(-1, 1)
    y = df["Scores"].values.reshape(-1, 1)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=SEED
    )

    # Train model
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    intercept = float(regressor.intercept_[0])
    slope = float(regressor.coef_[0][0])

    print("\n=== Trained Model ===")
    print(f"Intercept (b): {intercept:.4f}")
    print(f"Slope (a)    : {slope:.4f}")
    print(f"Line equation: score = {slope:.4f} * hours + {intercept:.4f}")

    # Predict on test set
    y_pred = regressor.predict(X_test)

    results = pd.DataFrame(
        {
            "Hours": X_test.squeeze(),
            "Actual": y_test.squeeze(),
            "Predicted": y_pred.squeeze(),
        }
    ).sort_values("Hours")
    print("\n=== Test Predictions (Actual vs Predicted) ===")
    print(results.to_string(index=False))

    # Predict a new value (example: 9.5 hours)
    new_hours = 9.5
    predicted_score = float(regressor.predict([[new_hours]])[0][0])
    print(f"\nPredicted score for {new_hours} hours: {predicted_score:.2f}")

    # Evaluate
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    print("\n=== Evaluation Metrics (Test Set) ===")
    print(f"MAE : {mae:.2f}")
    print(f"MSE : {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")


if __name__ == "__main__":
    main()
