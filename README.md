# Predicting Cirrhosis

![](https://img.shields.io/badge/Flask-2.1.3-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/matplotlib-3.6.2-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/numpy-1.23.4-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/pandas-1.5.2-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/pymongo-4.3.3-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/scikit-learn-1.0.1-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/seaborn-0.12.1-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/tensorflow-2.11.0-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/gunicorn-20.0.4-informational?style=plastic&logo=appveyor)

![alt text](https://github.com/LynHJ/CirrhosisPrediction/blob/ba70f04e40881b02c19140f62bc12cd3d91a151a/static/images/cirrhosis.jpg)

## Background

  

## Data Processing

1. Load data  
2. Clean data(dropna,drop_duplicates) 
3. Fill null values 
3. Scale data  
4. Split data  
5. Find out the best classifier models  
6. Output findings
7. Apply to Flask-Heroku-MongoDB
   
### Summary:

##### <ins> Predicting</ins>:  


##### <ins>Conclusion</ins>:  




## Content:
```
Project  
├── CirrhosisPrediction.ipynb
├── Output Data
│   ├── Bar_Categors.png
│   ├── Classifier.png
│   ├── Classifier_Results.png
│   ├── Data_Structure.png
│   ├── FinalModel.png
│   ├── NNM.png
│   ├── NNM_Results.png
│   ├── NNResult.csv
│   ├── Regplot.png
│   ├── Stage1.png
│   ├── Stage2.png
│   ├── Stage3.png
│   ├── Stage4.png
│   ├── cleaned.csv
│   ├── clfTestResult.csv
│   ├── model.pkl
│   ├── predmodel.joblib
│   └── scaler.pkl
├── Procfile
├── README.md
├── Resources
│   └── cirrhosis.csv
├── app.py
├── requirements.txt
├── runtime.txt
├── static
│   ├── css
│   │   └── style.css
│   ├── images
│   │   ├── blur-hospital.jpg
│   │   └── cirrhosis.jpg
│   └── js
│       ├── anime.js
│       └── app.js
└── templates
    ├── base.html
    ├── error.html
    ├── index.html
    ├── predict.html
    └── record.html
```

## Installation

pip install -r requirements.txt


## References
1. https://www.mayoclinic.org/tests-procedures/bilirubin/about/pac-20393041  
2. https://www.mayoclinic.org/diseases-conditions/high-blood-cholesterol/symptoms-causes/syc-20350800  
3. https://medlineplus.gov/lab-tests/albumin-blood-test/#:~:text=Albumin%20is%20a%20protein%20made,and%20enzymes%20throughout%20your%20body.  
4. https://medlineplus.gov/lab-tests/ceruloplasmin-test/#:~:text=What%20is%20a%20ceruloplasmin%20test,your%20body%20that%20need%20it.  
5. https://medlineplus.gov/lab-tests/alkaline-phosphatase/  
6. https://www.healthline.com/health/sgot-test  
7. https://www.mayoclinic.org/diseases-conditions/high-blood-cholesterol/in-depth/triglycerides/art-20048186#:~:text=Triglycerides%20are%20a%20type%20of,triglycerides%20for%20energy%20between%20meals.  
8. https://www.urmc.rochester.edu/encyclopedia/content.aspx?ContentTypeID=160&ContentID=36  
9. https://medlineplus.gov/lab-tests/prothrombin-time-test-and-inr-ptinr/#:~:text=Prothrombin%20is%20a%20protein%20made,to%20form%20a%20blood%20clot.  
10. https://dev.to/vulcanwm/environment-variables-in-heroku-python-385o
11. https://www.freecodecamp.org/news/how-to-deploy-an-application-to-heroku/  
12. https://www.fosslinux.com/50303/deploy-mongodb-on-heroku.htm  
13. https://www.kaggle.com/code/yashnegi01/78-accuracy-gradientboost-rf-xgb  
14. http://www.learningaboutelectronics.com/Articles/How-to-specify-the-Python-runtime-version-in-heroku.php  
15. https://coding-boot-camp.github.io/full-stack/mongodb/deploy-with-heroku-and-mongodb-atlas  











 
