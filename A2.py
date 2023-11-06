#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('diabetes.csv')
data.head()
data.info()
data.isnull().values.any()
data.mean()
data.median()
data.mode()
data.var()
data.std()
data.skew()
data.kurtosis()

(data.Pregnancies==0).sum(),(data.Glucose==0).sum(),(data.BloodPressure==0).sum(),(data.SkinThickness==0).sum(),(data.Insulin==0).sum(),(data.BMI==0).sum()

drop_preg = data.index[data.Pregnancies==0].tolist()
drop_gluc = data.index[data.Glucose==0].tolist()
drop_BP = data.index[data.BloodPressure==0].tolist()
drop_SkinTh = data.index[data.SkinThickness==0].tolist()
drop_Ins = data.index[data.Insulin==0].tolist()
drop_bmi = data.index[data.BMI==0].tolist()
drop_total = drop_preg + drop_gluc + drop_BP + drop_SkinTh + drop_Ins + drop_bmi
diab = data.drop(data.index[drop_total])

diab.head(),diab.info()

dia0 = diab[diab.Outcome==0]
dia1 = diab[diab.Outcome==1]

out0 = len(diab[diab.Outcome==0])
out1 = len(diab[diab.Outcome==1])

sns.countplot(x=diab.Outcome)
plt.title("Count Plot for Outcome")

Total = out0+out1
P_out0 = out0*100/Total
P_out1 = out1*100/Total
P_out0,P_out1

sns.pairplot(diab, vars=["Pregnancies", "Glucose","BloodPressure","SkinThickness","Insulin", "BMI","DiabetesPedigreeFunction", "Age"],hue="Outcome")
plt.title("Pairplot of Variables by Outcome")

cor = diab.corr(method ='pearson')
cor

sns.heatmap(cor)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




