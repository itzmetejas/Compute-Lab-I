#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("car_evaluation.csv", header=None)
columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
data.columns = columns
data_encoded = pd.get_dummies(data, columns=columns[:-1], drop_first=True)
X = data_encoded.drop('class', axis=1) 
y = data_encoded['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train, y_train)

y_pred = rf_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

class_report = classification_report(y_test, y_pred, target_names=data['class'].unique())
print("Classification Report:\n", class_report)


# In[ ]:




