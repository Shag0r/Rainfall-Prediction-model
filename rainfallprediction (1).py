# -*- coding: utf-8 -*-
"""RainfallPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IMmtvZSNP8F5Zu0kXuwiTXF0EfECdZbu
"""

import pandas as pd
from google.colab import files
uploaded = files.upload()
full_data = pd.read_csv('/content/data.csv')
full_data.head()

full_data.shape

full_data.info()

full_data['RainToday'].replace({'No': 0, 'Yes': 1},inplace = True)
full_data['RainTomorrow'].replace({'No': 0, 'Yes': 1},inplace = True)

import matplotlib.pyplot as plt

# Plot bar plot of 'RainToday'
rain_today_counts = full_data['RainToday'].value_counts()
rain_today_counts.plot(kind='bar')
plt.xlabel('RainToday')
plt.ylabel('Count')
plt.title('Bar plot: RainToday')
plt.show()

# Plot bar plot of 'RainTomorrow'
rain_tomorrow_counts = full_data['RainTomorrow'].value_counts()
rain_tomorrow_counts.plot(kind='bar')
plt.xlabel('RainTomorrow')
plt.ylabel('Count')
plt.title('Bar plot: RainTomorrow')
plt.show()

fig = plt.figure(figsize = (8,5))
full_data.RainTomorrow.value_counts(normalize = True).plot(kind='bar', color= ['skyblue','navy'], alpha = 0.9, rot=0)
plt.title('RainTomorrow Indicator No(0) and Yes(1) in the Imbalanced Dataset')
plt.show()

from sklearn.utils import resample

no = full_data[full_data.RainTomorrow == 0]
yes = full_data[full_data.RainTomorrow == 1]
yes_oversampled = resample(yes, replace=True, n_samples=len(no), random_state=123)
oversampled = pd.concat([no, yes_oversampled])

fig = plt.figure(figsize = (8,5))
oversampled.RainTomorrow.value_counts(normalize = True).plot(kind='bar', color= ['skyblue','navy'], alpha = 0.9, rot=0)
plt.title('RainTomorrow Indicator No(0) and Yes(1) after Oversampling (Balanced Dataset)')
plt.show()

missing_data = full_data.isnull().sum()
print(missing_data)

import seaborn as sns
sns.heatmap(oversampled.isnull(), cbar=False, cmap='PuBu')

total = oversampled.isnull().sum().sort_values(ascending=False)
percent = (oversampled.isnull().sum()/oversampled.isnull().count()).sort_values(ascending=False)
missing = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing.head(4)

import matplotlib.pyplot as plt

# Plot the top N columns with the highest percentage of missing values
n = 4  # Number of columns to plot
top_missing = missing.head(n)

plt.figure(figsize=(8, 6))
plt.barh(top_missing.index, top_missing['Percent'], color='skyblue')
plt.xlabel('Percentage of Missing Values')
plt.ylabel('Columns')
plt.title(f'Top {n} Columns with Highest Missing Values')
plt.show()

for column, percent in missing.iterrows():
    print(f"{column}: {percent['Percent']*100:.2f}%")

import matplotlib.pyplot as plt

# Plot the percentage of missing data
plt.figure(figsize=(8, 6))
plt.barh(missing.index, missing['Percent'], color='purple')
plt.xlabel('Percentage of Missing Values')
plt.ylabel('Columns')
plt.title('Percentage of Missing Data')
plt.show()

for column, percent in missing.iterrows():
    print(f"{column}: {percent['Percent']*100:.2f}%")

oversampled.select_dtypes(include=['object']).columns

oversampled['Date'] = oversampled['Date'].fillna(oversampled['Date'].mode()[0])
oversampled['Location'] = oversampled['Location'].fillna(oversampled['Location'].mode()[0])
oversampled['WindGustDir'] = oversampled['WindGustDir'].fillna(oversampled['WindGustDir'].mode()[0])
oversampled['WindDir9am'] = oversampled['WindDir9am'].fillna(oversampled['WindDir9am'].mode()[0])
oversampled['WindDir3pm'] = oversampled['WindDir3pm'].fillna(oversampled['WindDir3pm'].mode()[0])

from sklearn.preprocessing import LabelEncoder
lencoders = {}
for col in oversampled.select_dtypes(include=['object']).columns:
    lencoders[col] = LabelEncoder()
    oversampled[col] = lencoders[col].fit_transform(oversampled[col])

import warnings
warnings.filterwarnings("ignore")
# Multiple Imputation by Chained Equations
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
MiceImputed = oversampled.copy(deep=True)
mice_imputer = IterativeImputer()
MiceImputed.iloc[:, :] = mice_imputer.fit_transform(oversampled)

# Calculate the IQR for each numeric column
Q1 = MiceImputed.quantile(0.25)
Q3 = MiceImputed.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

# Define the threshold for outliers
threshold = 1.5

# Identify rows with outliers
outliers = ((MiceImputed < (Q1 - threshold * IQR)) | (MiceImputed > (Q3 + threshold * IQR))).any(axis=1)

# Remove or handle outliers
MiceImputed_no_outliers = MiceImputed[~outliers]

MiceImputed.shape

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.boxplot(MiceImputed_no_outliers.values)
plt.title('Box Plot - After Removing Outliers')
plt.xticks(range(1, len(MiceImputed_no_outliers.columns) + 1), MiceImputed_no_outliers.columns, rotation=90)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
corr = MiceImputed.corr()
mask = np.triu(np.ones_like(corr, dtype=np.bool))
f, ax = plt.subplots(figsize=(20, 20))
cmap = sns.diverging_palette(250, 25, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=None, center=0,square=True, annot=True, linewidths=.5, cbar_kws={"shrink": .9})

sns.pairplot( data=MiceImputed, vars=('MaxTemp','MinTemp','Pressure9am','Pressure3pm', 'Temp9am', 'Temp3pm', 'Evaporation'), hue='RainTomorrow' )

# Standardizing data
from sklearn import preprocessing
r_scaler = preprocessing.MinMaxScaler()
r_scaler.fit(MiceImputed)
modified_data = pd.DataFrame(r_scaler.transform(MiceImputed), index=MiceImputed.index, columns=MiceImputed.columns)

from sklearn.feature_selection import SelectKBest, chi2
X = modified_data.loc[:,modified_data.columns!='RainTomorrow']
y = modified_data[['RainTomorrow']]
selector = SelectKBest(chi2, k=10)
selector.fit(X, y)
X_new = selector.transform(X)
print(X.columns[selector.get_support(indices=True)])

import matplotlib.pyplot as plt

# Get the scores/importance values from the feature selection
scores = selector.scores_

# Get the selected feature names
selected_features = X.columns[selector.get_support(indices=True)]

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(range(len(selected_features)), scores[selector.get_support()])
plt.title('Feature Importance')
plt.xlabel('Features')
plt.ylabel('Importance')
plt.xticks(range(len(selected_features)), selected_features, rotation=90)
plt.show()

from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier as rf

X = MiceImputed.drop('RainTomorrow', axis=1)
y = MiceImputed['RainTomorrow']
selector = SelectFromModel(rf(n_estimators=100, random_state=0))
selector.fit(X, y)
support = selector.get_support()
features = X.loc[:,support].columns.tolist()
print(features)
print(rf(n_estimators=100, random_state=0).fit(X,y).feature_importances_)

features = MiceImputed[['Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 'WindGustDir',
                       'WindGustSpeed', 'WindDir9am', 'WindDir3pm', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
                       'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 'Temp3pm',
                       'RainToday']]
target = MiceImputed['RainTomorrow']

# Split into test and train
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.25, random_state=12345)

# Normalize Features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

def plot_roc_cur(fper, tper):
    plt.plot(fper, tper, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()

from sklearn.metrics import roc_curve, auc
from sklearn.linear_model import LogisticRegression  # Example classifier, replace with your choice

# Train a classification model
model = LogisticRegression()  # Replace with your chosen classifier
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred_prob = model.predict_proba(X_test)[:, 1]

# Calculate the false positive rate and true positive rate
fper, tper, _ = roc_curve(y_test, y_pred_prob)
roc_auc = auc(fper, tper)

# Plot the ROC curve
plot_roc_cur(fper, tper)



import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, roc_auc_score, cohen_kappa_score, roc_curve, classification_report, confusion_matrix
import time
import itertools
import numpy as np

def run_model(model, X_train, y_train, X_test, y_test, verbose=True):
    t0 = time.time()
    if not verbose:
        model.fit(X_train, y_train, verbose=0)
    else:
        model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)
    coh_kap = cohen_kappa_score(y_test, y_pred)
    time_taken = time.time() - t0
    print("Accuracy = {}".format(accuracy))
    print("ROC Area under Curve = {}".format(roc_auc))
    print("Cohen's Kappa = {}".format(coh_kap))
    print("Time taken = {}".format(time_taken))
    print(classification_report(y_test, y_pred, digits=5))

    probs = model.predict_proba(X_test)
    probs = probs[:, 1]
    fper, tper, thresholds = roc_curve(y_test, probs)
    plt.figure()
    plt.plot(fper, tper)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.show()

    cm = confusion_matrix(y_test, y_pred)
    plot_confusion_matrix(cm, classes=model.classes_)

    return model, accuracy, roc_auc, coh_kap, time_taken


def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion Matrix', cmap=plt.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

# Logistic Regression
from sklearn.linear_model import LogisticRegression

params_lr = {'penalty': 'l1', 'solver': 'liblinear'}

model_lr = LogisticRegression(**params_lr)
model_lr, accuracy_lr, roc_auc_lr, coh_kap_lr, tt_lr = run_model(model_lr, X_train, y_train, X_test, y_test)

# Decision Tree
from sklearn.tree import DecisionTreeClassifier

params_dt = {'max_depth': 16,
             'max_features': "sqrt"}

model_dt = DecisionTreeClassifier(**params_dt)
model_dt, accuracy_dt, roc_auc_dt, coh_kap_dt, tt_dt = run_model(model_dt, X_train, y_train, X_test, y_test)

# Neural Network
from sklearn.neural_network import MLPClassifier

params_nn = {'hidden_layer_sizes': (30, 30, 30),
             'activation': 'logistic',
             'solver': 'lbfgs',
             'max_iter': 500}

model_nn = MLPClassifier(**params_nn)
model_nn, accuracy_nn, roc_auc_nn, coh_kap_nn, tt_nn = run_model(model_nn, X_train, y_train, X_test, y_test)

# Random Forest
from sklearn.ensemble import RandomForestClassifier

params_rf = {'max_depth': 16,
             'min_samples_leaf': 1,
             'min_samples_split': 2,
             'n_estimators': 100,
             'random_state': 12345}

model_rf = RandomForestClassifier(**params_rf)
model_rf, accuracy_rf, roc_auc_rf, coh_kap_rf, tt_rf = run_model(model_rf, X_train, y_train, X_test, y_test)

# Light GBM
import lightgbm as lgb

params_lgb = {'colsample_bytree': 0.95,
              'max_depth': 16,
              'min_split_gain': 0.1,
              'n_estimators': 200,
              'num_leaves': 50,
              'reg_alpha': 1.2,
              'reg_lambda': 1.2,
              'subsample': 0.95,
              'subsample_freq': 20}

model_lgb = lgb.LGBMClassifier(**params_lgb)
model_lgb, accuracy_lgb, roc_auc_lgb, coh_kap_lgb, tt_lgb = run_model(model_lgb, X_train, y_train, X_test, y_test)

# Create a list of accuracies
accuracies = [accuracy_lr, accuracy_dt, accuracy_nn, accuracy_rf, accuracy_lgb]

# Get the index of the model with the highest accuracy
best_model_index = np.argmax(accuracies)

# Get the corresponding model
best_model = [model_lr, model_dt, model_nn, model_rf, model_lgb][best_model_index]

# Predict using the best model
final_prediction = best_model.predict(X_test)

# Convert the prediction to integers
final_prediction = final_prediction.astype(int)

# Convert the prediction to "Rain" or "No Rain"
prediction_labels = ["No Rain", "Rain"]
final_output = np.take(prediction_labels, final_prediction)

# Print the final output
print("Final Output: ", final_output)

from scipy.stats import mode

# Create an array of model predictions
predictions = np.array([model_lr.predict(X_test), model_dt.predict(X_test),
                        model_nn.predict(X_test), model_rf.predict(X_test),
                        model_lgb.predict(X_test)])

# Calculate the mode of the predictions
final_prediction, _ = mode(predictions)

# Convert the mode prediction to "Rain" or "No Rain"
final_output = np.take(prediction_labels, final_prediction.astype(int))

# Print the final output
print("Final Output: ", final_output)

# Create a list of accuracies
accuracies = [accuracy_lr, accuracy_dt, accuracy_nn, accuracy_rf, accuracy_lgb]

# Create a list of model names
model_names = ['Logistic Regression', 'Decision Tree', 'Neural Network', 'Random Forest', 'LightGBM']

# Get the index of the model with the highest accuracy
best_model_index = np.argmax(accuracies)

# Get the corresponding model name and accuracy
best_model_name = model_names[best_model_index]
best_accuracy = accuracies[best_model_index]

# Print the final decision
print("Best Model: ", best_model_name)
print("Accuracy: ", best_accuracy)

import matplotlib.pyplot as plt

# Create a list of accuracies
accuracies = [accuracy_lr, accuracy_dt, accuracy_nn, accuracy_rf, accuracy_lgb]

# Create a list of model names
model_names = ['Logistic Regression', 'Decision Tree', 'Neural Network', 'Random Forest', 'LightGBM']

# Plot the accuracies
plt.figure(figsize=(8, 6))
plt.bar(model_names, accuracies)
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.title('Model Accuracies')
plt.ylim([0, 1])  # Set the y-axis limits
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.show()

# Predict using the best model
final_prediction = best_model.predict_proba(X_test)[:, 1]  # Get the probabilities for the "Rain" class

# Threshold the probabilities to make a binary decision
threshold = 0.5  # Adjust this threshold based on your preference
binary_prediction = (final_prediction > threshold).astype(int)

# Convert the binary prediction to "Rain" or "No Rain"
final_output = np.take(prediction_labels, binary_prediction)

# Print the final output
print("Final Output: ", final_output)

# Create a list of accuracies
accuracies = [accuracy_lr, accuracy_dt, accuracy_nn, accuracy_rf, accuracy_lgb]

# Get the index of the model with the highest accuracy
best_model_index = np.argmax(accuracies)

# Get the corresponding model
best_model = [model_lr, model_dt, model_nn, model_rf, model_lgb][best_model_index]

# Predict using the best model
final_prediction = best_model.predict(X_test)

# Convert the prediction to integers
final_prediction = final_prediction.astype(int)

# Convert the prediction to "Rain" or "No Rain"
prediction_labels = ["No Rain", "Rain"]
final_output = np.take(prediction_labels, final_prediction)

# Print the final output
print("Final Output: ", final_output)

# Get the predicted probabilities for the "Rain" class
final_probabilities = best_model.predict_proba(X_test)[:, 1]

# Threshold the probabilities to make a binary decision
threshold = 0.5  # Adjust this threshold based on your preference
binary_prediction = (final_probabilities > threshold).astype(int)

# Convert the binary prediction to "Rain" or "No Rain"
binary_output = np.take(prediction_labels, binary_prediction)

# Print the binary output
print("Binary Output: ", binary_output)

# Determine the majority vote
majority_vote = np.bincount(final_prediction).argmax()
majority_output = prediction_labels[majority_vote]

# Print the majority vote
print("Majority Vote: ", majority_output)