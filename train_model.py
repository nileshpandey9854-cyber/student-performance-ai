import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

import pickle


# 1. Dataset load karo
df = pd.read_csv("student_data.csv")

print("Dataset:")
print(df.head())


# 2. Input aur target separate karo
X = df.drop("performance", axis=1)
y = df["performance"]


# 3. Training aur testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 4. Model create karo
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# 5. Model train karo
model.fit(X_train, y_train)


# 6. Prediction
y_pred = model.predict(X_test)


# 7. Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)


# 8. Detailed report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# 9. Model save karo
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved as model.pkl")