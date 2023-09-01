# Rainfall Prediction Model With Machine Learning
This project focuses on the development of machine learning models for rainfall prediction in major cities across Australia.
![image](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/11f5a230-586f-45c9-a098-a70c21927a2d)


Project Objective: Develop machine learning models for rainfall prediction in major cities to enhance timely forecasting and reduce human and financial losses from extreme weather events.

Data and Methods: Utilize diverse weather data, including temperature, humidity, wind speed, atmospheric pressure, and historical precipitation records, to train and evaluate machine learning algorithms such as regression, decision trees, random forests, and ensemble methods.

Evaluation Metrics: Rigorous statistical analysis and performance metrics (accuracy, precision, recall, F1-score) assess model effectiveness in predicting rain occurrence, enabling tailored approaches for different cities.

Implications: Improved rainfall prediction benefits agriculture, water resource management, disaster preparedness, and urban planning, aiding farmers, water authorities, and emergency management agencies in optimizing resources and responding to extreme weather events proactively.

Objective: Develop accurate machine learning models for rainfall prediction, addressing class imbalance, missing data, outliers, and feature selection in major cities.

Aim: Enhance forecasting by preprocessing data and comparing models like Logistic Regression, Decision Trees, Neural Networks, Random Forest, and LightGBM.

Motivation: Timely and precise rainfall forecasts reduce losses in extreme weather events, benefitting agriculture, water management, and emergency planning in Australia.

Techniques

Class Imbalance: Addressed with minority class oversampling.
![download (2)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/f4a8431f-f341-4017-9cd0-df27683f6093)
![download (3)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/96c77d0d-97ca-4f2c-8ca7-708d000e9f5a)
![download (4)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/c4a24180-b937-4592-bfbf-4718249e1067)
![download (5)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/0f2b4851-a92b-45f2-9946-af30d6e08821)


Missing Data: Imputed using Multiple Imputation by Chained Equations (MICE).
![download (6)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/a58b0735-81da-46c1-a074-2a18eeed6f86)
![download (7)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/9f956752-b349-4220-b437-0b927be112ae)

Outlier Detection: Identified outliers using the Interquartile Range (IQR) method.
![download (8)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/8abb8627-ed95-487c-9b6e-d981156ea358)
![download (9)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/abc8aa27-62a8-4248-9e9e-8459f125c29b)

![download (10)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/a5f3bf9e-3624-45cb-836f-ca830abb1099)


Feature Selection: Used filter and wrapper methods for selecting relevant features.
![download (11)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/2d394c07-041a-4f8f-9084-217e9073e3cc)



Machine Learning Models: Employed models like Logistic Regression, Decision Trees, Neural Networks, and Random Forest.
![download (12)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/292688b3-f8a3-44da-944f-97dbf4fa1e96)

Accuracy = 0.8050146850864789
ROC Area under Curve = 0.805039737453916
Cohen's Kappa = 0.6100470056991374
Time taken = 4.293061256408691
              precision    recall  f1-score   support

         0.0    0.79882   0.81390   0.80629     27501
         1.0    0.81141   0.79618   0.80372     27657

    accuracy                        0.80501     55158
   macro avg    0.80512   0.80504   0.80501     55158
weighted avg    0.80513   0.80501   0.80500     55158
![download (13)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/235a3b73-d548-4068-a51a-d7fd5f7260bf)

Confusion matrix, without normalization
Accuracy = 0.8666195293520432
ROC Area under Curve = 0.8665334987138236
Cohen's Kappa = 0.733191586808682
Time taken = 0.7531166076660156
              precision    recall  f1-score   support

         0.0    0.88972   0.83612   0.86209     27501
         1.0    0.84625   0.89695   0.87086     27657

    accuracy                        0.86662     55158
   macro avg    0.86799   0.86653   0.86648     55158
weighted avg    0.86793   0.86662   0.86649     55158
![download (14)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/966639b4-3fe0-4198-b31d-8dc514d88df8)
![download (15)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/a9982777-256d-46ca-8de7-7ad2fac94013)

Confusion matrix, without normalization
Accuracy = 0.8937053555241307
ROC Area under Curve = 0.8936717401423054
Cohen's Kappa = 0.7873950784904907
Time taken = 484.4572079181671
              precision    recall  f1-score   support

         0.0    0.90276   0.88179   0.89215     27501
         1.0    0.88511   0.90556   0.89522     27657

    accuracy                        0.89371     55158
   macro avg    0.89393   0.89367   0.89368     55158
weighted avg    0.89391   0.89371   0.89369     55158
![download (16)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/2aa85191-ca89-4f47-82d1-2ea981d5a7f7)
![download (17)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/d3fb1f56-97b8-4d70-a689-d9ec5e5d717c)

Confusion matrix, without normalization
Accuracy = 0.9234562529460821
ROC Area under Curve = 0.9233814961038466
Cohen's Kappa = 0.8468885765844757
Time taken = 48.85527777671814
              precision    recall  f1-score   support

         0.0    0.94673   0.89695   0.92117     27501
         1.0    0.90262   0.94981   0.92562     27657

    accuracy                        0.92346     55158
   macro avg    0.92467   0.92338   0.92339     55158
weighted avg    0.92461   0.92346   0.92340     55158
![download (18)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/0a73aafb-a5de-445e-aa86-b98de567ccf1)
![download (19)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/490cda5c-919a-44b5-97b1-eb481684176c)

Confusion matrix, without normalization
Accuracy = 0.8728017694622721
ROC Area under Curve = 0.8727177880255684
Cohen's Kappa = 0.7455592851796542
Time taken = 9.703380107879639
              precision    recall  f1-score   support

         0.0    0.89572   0.84302   0.86857     27501
         1.0    0.85254   0.90241   0.87677     27657

    accuracy                        0.87280     55158
   macro avg    0.87413   0.87272   0.87267     55158
weighted avg    0.87407   0.87280   0.87268     55158
![download (20)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/337b4ee3-8e6d-436e-917e-0f79b055f8d6)
![download (21)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/478f471e-d93a-420a-940e-f72555d4975c)



Evaluation: Assessed performance with metrics like accuracy, ROC-AUC, and Cohen’s Kappa.
![download (22)](https://github.com/Shag0r/Rainfall-Prediction-model/assets/101504353/7ea39c66-6d42-4246-b3e3-3ca6a7a063d0)
Final Output:  ['Rain' 'No Rain' 'Rain' ... 'No Rain' 'No Rain' 'Rain']
Binary Output:  ['Rain' 'No Rain' 'Rain' ... 'No Rain' 'No Rain' 'Rain']
Majority Vote:  Rain

