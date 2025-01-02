import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Model designing----------------------------------------------------------------------
datax = pd.read_csv('lifestyledatasets.csv')  # Renamed 'data' to 'datax'
le_disease = LabelEncoder()
datax['Disease'] = le_disease.fit_transform(datax['Disease'])

# Inputs
le = LabelEncoder()
datax['Fever'] = le.fit_transform(datax['Fever'])
datax['Cough'] = le.fit_transform(datax['Cough'])
datax['Fatigue'] = le.fit_transform(datax['Fatigue'])
datax['Difficulty Breathing'] = le.fit_transform(datax['Difficulty Breathing'])
datax['Gender'] = le.fit_transform(datax['Gender'])
datax['Blood Pressure'] = le.fit_transform(datax['Blood Pressure'])
datax['Cholesterol Level'] = le.fit_transform(datax['Cholesterol Level'])

# print(datax.head())
x = datax.drop(['Disease'], axis=1)
y = datax['Disease'].values.ravel()
print("before:", y.shape)

# Splitting data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("after:", y.shape)

# Train the model
models = RandomForestClassifier(random_state=42)
models.fit(x_train, y_train)

# Saving the model
joblib.dump(models, 'models.pkl')
joblib.dump(le_disease, 'le_disease.pkl')
print("Label and encoder saved")
