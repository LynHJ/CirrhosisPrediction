# Predicting Credit Risk

![](https://img.shields.io/badge/matplotlib-3.5.3-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/numpy-1.21.5-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/pandas-1.3.5-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/scikit_learn-1.0.2-informational?style=plastic&logo=appveyor)


## Background-Supervised Machine Learning

```
Supervised Machine Learning
└── sklearn
    ├── .datasets
    |    ├── lending_data.csv
    |    ├── make_blobs
    |    ├── load_iris
    |    └── make_swiss_roll
    ├── .neighbors      
    |    └──KNeighborsClaassifier
    ├── .linear_model
    |    ├── LogisticRegression
    |    ├── LinearRegression
    |    ├── Ridge
    |    ├── Lasso       
    |    └── ElasticNet   
    ├── .model_selection
    |    ├── train_test_split 
    |    └──GridSearchCV 
    ├── .preprocessing
    |    ├── StandardScaler
    |    ├── MinMaxScaler
    |    ├── Normalize     
    |    └── LabelEcoder  
    ├── .feature_selection     
    |    └── SelectFromModel
    ├── .metircs
    |    ├── auc
    |    ├── roc_curve
    |    ├── classification_report
    |    ├── mean_squared_error
    |    ├── r2_score
    |    ├── confusion_matrix             
    |    └── accuracy_score 
    ├── .tree            
    |    └── DecisionTreeClassifier
    ├── .ensemble
    |    ├── RandomForestClassifier
    |    ├── ExtraTreeClassifier             
    |    └── AdaBoostClassifier 
    └── .svm
         └── svc(kernel='linear')  
```

## Data Processing

1. Load data  
2. Clean data(dropna,drop_duplicates)  
3. Scale data  
4. Split data  
5. Train models(Logistic Regression & RandomForestClassifier)  
6. Output classification_report(check accuracy rate)  
   
### Summary:

##### <ins> Predicting</ins>:  

This process will run two models on this data: a Logistic Regression, and a Random Forests Classifier.   

At first glance, the data has 6 features, all data types are numeric. However some columns have a linear relationship between them(`['debt_to_income']=['total_debt']/['borrower_income']`) and also `['number_of_accounts']` seems not a factor to verify a person's payback ability. Therefore, the number of explanatory variables is 4 ,and the number of noise variables is 2.  

In my opinion, the performance of Logistic Regression's prediction could be better as Random Forest Classifier would performance better when the data set has many variables.  

##### <ins>Conclusion</ins>:  

Compared to two results from two different classifiers, the output is the same as my prediction.  The Logistic Regression model had a higher accuracy score 0.92 while the Random Forest Classifier model had 0.86.  



## Content:
```
Project  
├── Credit Risk Evaluator.ipynb
├── README.md
├── Resources
    └── lending_data.csv
```

## Installation

pip install -r requirements.txt














 
