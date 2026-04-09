import pandas as pd
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

data = pd.read_csv("diabetes.csv")
target = "Outcome"
# profile = ProfileReport(data, title="Diabetes report", explorative=True)
# profile.to_file("diabetes_report.html")
x = data.drop(target, axis=1)
y = data[target]

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100991)

# Preprocess data
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Pick up a model
model = RandomForestClassifier()

# Train the selected model
model.fit(x_train, y_train)

y_predict = model.predict_proba(x_test)
print(y_predict)

# print("Accuracy: {}".format(accuracy_score(y_test, y_predict)))
# print("Precision: {}".format(precision_score(y_test, y_predict)))
# print("Recall: {}".format(recall_score(y_test, y_predict)))
# print("F1: {}".format(f1_score(y_test, y_predict)))
# print(confusion_matrix(y_test, y_predict))
