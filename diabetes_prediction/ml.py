import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
warnings.filterwarnings("ignore")

data=pd.read_csv('c:\Users\devas\OneDrive\Desktop\diabetes_prediction_dataset.csv')
data=np.array(data)

X=data[:,:-1]
y=data[:,-1:]
y=y.astype('int')
X=X.astype('int')
X_train,X_test,y_train,y_test=train_test_split(X,y,test_test_split=0.3,random_state=0);
log_reg=LogisticRegression()

log_reg.fit(X_train,y_train)

pickle.dump(log_reg.open('samples.pkl','wb'))