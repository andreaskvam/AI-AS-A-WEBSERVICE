
import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# used to scale the data to fit the logistic algorithm
sc = StandardScaler()

# random_state=0 means that we don't shuffle the dataset
classifier = LogisticRegression(random_state=0)

def train_model():
  con = sqlite3.connect('ads_dataset.db')
  # df = dataframe
  df = pd.read_sql_query('SELECT * FROM dataset', con)

  # Independent values, the input data to analyse
  X = df.iloc[:, :-1].values

  # Dependent values, the target data of the process
  y = df.iloc[:, -1].values

  # split the dataset into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

  # scale data to fit the training algorithm
  X_train = sc.fit_transform(X_train)
  X_test = sc.transform(X_test)

  # training the model
  classifier.fit(X_train, y_train)

  # close connection to database when training is done
  con.close()


def predict(age, income):

  probability_of_click = classifier.predict_proba(sc.transform([[age, income]]))

  # [[will-not-click, will-click]]
  # [[0.11090976     0.890967985]]
  probability = probability_of_click[0, 1]

  # classifier.predict() == probability > 0.5
  prediction = True if probability > 0.5 else False

  # return a dict with predicted values
  return { "willClick": prediction, "probability": probability }
