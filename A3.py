#!/usr/bin/env python
# coding: utf-8

# In[12]:


from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()
X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.svm import SVC
clf = SVC(kernel='linear', C = 1)
print(clf.fit(X_train, y_train))

from sklearn.metrics import accuracy_score
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")


# In[4]:





# In[5]:





# In[10]:





# In[8]:





# In[ ]:




