
import pandas as pd 
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

#
# Data From UCI Repo
# https://archive.ics.uci.edu/ml/datasets/Student+Performance
#
data_location = "data/student/student-mat.csv"
data = pd.read_csv(data_location, sep=";")
data = data[["G1","G2","G3","studytime","failures","absences"]]

# What would you like to predict?
predict = "G3"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

# Splitting Vars - 4 Different arrays
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y, test_size=0.1)

# Linear Regression - y = mx + b
# Slope = y2 - y1 / x2 - x1
linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)

# 83 Percent Accurate
acc_score = linear.score(x_test, y_test)
print("Accurate: ",acc_score)

print("Co: ", linear.coef_)
print("Intercept: ", linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x],y_test[x])


