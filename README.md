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
Cirrhosis is a late stage of scarring (fibrosis) of the liver caused by many forms of liver diseases and conditions, such as hepatitis and chronic alcoholism. The following data contains the information collected from the Mayo Clinic trial in primary biliary cirrhosis (PBC) of the liver conducted between 1974 and 1984. A description of the clinical background for the trial and the covariates recorded here is in Chapter 0, especially Section 0.2 of Fleming and Harrington, Counting
Processes and Survival Analysis, Wiley, 1991. A more extended discussion can be found in Dickson, et al., Hepatology 10:1-7 (1989) and in Markus, et al., N Eng J of Med 320:1709-13 (1989).  

A total of 424 PBC patients, referred to Mayo Clinic during that ten-year interval, met eligibility criteria for the randomized placebo-controlled trial of the drug D-penicillamine. The first 312 cases in the dataset participated in the randomized trial and contain largely complete data. The additional 112 cases did not participate in the clinical trial but consented to have basic measurements recorded and to be followed for survival. Six of those cases were lost to follow-up shortly after diagnosis, so the data here are on an additional 106 cases as well as the 312 randomized participants. 

 Click [here](http://www.diva-portal.org/smash/get/diva2:769192/FULLTEXT01.pdf) to go to original research paper. Based on that research, Stage4 is Cirrhosis.  
 ```
 Stage 1 shows a florid, asymmetric destruction of the septal and interlobular bile ducts and what are typically surrounded by dense infiltrates of mononuclear cells, especially T lympocytes. Hepatic granuloma can be seen in all stages but are most common in stage 1. The presence of granuloma has been proposed to be of prognostic importance (Lee et al 1981). However, this observation has not be confirmed (Roll et al 1983).   
In stage 2 there are more widespread lesions with a reduction of normal bile ducts and increased numbers of atypical, poorly formed bile ducts. Diffuse portal fibrosis is seen and as in stage 1 periportal cholestasis is conspicuous.  
Stage 3 displays more progressive lesions with fibrous septa forming bridges.   
Stage 4 represents the end stage with clear cirrhosis and may be difficult to distinguish from other types of cirrhosis.   
```
  

## Data Processing

#### 1. Load data    
<img src='https://github.com/LynHJ/CirrhosisPrediction/blob/cceee5a8e90e4cf4b7a98ef354b45f1b2abf33bf/Output%20Data/Data_Structure.png' width= 30% ><img src='https://github.com/LynHJ/CirrhosisPrediction/blob/cceee5a8e90e4cf4b7a98ef354b45f1b2abf33bf/Output%20Data/Info.png' width= 50% >  

 Brief: The data has only 418 data points and almost 1/3 of rows contain null values. Using <code>dropna()</code> methods is not a good way for this small data set.  

#### 2. Process data   

##### 2.1 Fill null values  

<img src='https://github.com/LynHJ/CirrhosisPrediction/blob/cceee5a8e90e4cf4b7a98ef354b45f1b2abf33bf/Output%20Data/Stage1.png' width= 40% ><img src='https://github.com/LynHJ/CirrhosisPrediction/blob/cceee5a8e90e4cf4b7a98ef354b45f1b2abf33bf/Output%20Data/Stage2.png' width= 40% >  
<img src='https://github.com/LynHJ/CirrhosisPrediction/blob/cceee5a8e90e4cf4b7a98ef354b45f1b2abf33bf/Output%20Data/Stage3.png' width= 40% ><img 'https://github.com/LynHJ/CirrhosisPrediction/blob/cceee5a8e90e4cf4b7a98ef354b45f1b2abf33bf/Output%20Data/Stage4.png' width= 40% >  

Brief: As each stage's features have their own distributions, if I simply use the whole data's mean,mode,median to fill the null value, the data might have severe bias. To do so, I filtered each stage to make sure the null values have been filled in proper data. Furthermore, using this way to fill in null values could help classifier models achieve higher accuracy.  
 
##### 2.2 Choose Featrues  
<img src='https://github.com/LynHJ/CirrhosisPrediction/blob/cceee5a8e90e4cf4b7a98ef354b45f1b2abf33bf/Output%20Data/Bar_Categors.png' width= 50% ><img 'https://github.com/LynHJ/CirrhosisPrediction/blob/cceee5a8e90e4cf4b7a98ef354b45f1b2abf33bf/Output%20Data/Regplot.png' width= 50% >    

#### 3. Find out the best classifier models  
 
![alt text](https://github.com/LynHJ/CirrhosisPrediction/blob/cceee5a8e90e4cf4b7a98ef354b45f1b2abf33bf/Output%20Data/Classifier.png)
![alt text](https://github.com/LynHJ/CirrhosisPrediction/blob/cceee5a8e90e4cf4b7a98ef354b45f1b2abf33bf/Output%20Data/NNM.png)  

#### 4. Output findings  

[Classifier Models Results ](https://github.com/LynHJ/CirrhosisPrediction/blob/4dab69dc8036c7b19b3bf8439703019c4682a523/Output%20Data/clfTestResult.csv)  
[NNM Results ](https://github.com/LynHJ/CirrhosisPrediction/blob/4dab69dc8036c7b19b3bf8439703019c4682a523/Output%20Data/NNResult.csv)     

![alt text](https://github.com/LynHJ/CirrhosisPrediction/blob/cceee5a8e90e4cf4b7a98ef354b45f1b2abf33bf/Output%20Data/FinalModel.png) 
 
#### 5. Apply to Flask-Heroku-MongoDB  

Click [here](https://cirrhosisprediction.herokuapp.com) to go to my deplyed Falsk app.
   
### Summary:
<img src='' width= 51% ><img src='' width= 51% >
<img src='' width= 51% ><img src='' width= 51% >
<img src='' width= 51% ><img src='' width= 51% >
<img src='' width= 51% ><img src='' width= 51% >
<img src='' width= 51% ><img src='' width= 51% >
<img src='' width= 51% ><img src='' width= 51% >
<img src='' width= 51% ><img src='' width= 51% ><img src='' width= 51% ><img src='' width= 51% >
<img src='' width= 51% ><img src='' width= 51% >


## Content:
```
Project  
├── CirrhosisPrediction.ipynb
├── Cirrhosis Prediction.pptx
├── Output Data
│   ├── Bar_Categors.png
│   ├── Classifier.png
│   ├── Classifier_Results.png
│   ├── Data_Structure.png
│   ├── FinalModel.png
│   ├── Info.png
│   ├── NNM.png
│   ├── NNM_Results.png
│   ├── NNResult.csv
│   ├── Regplot.png
│   ├── Stage1.png
│   ├── Stage2.png
│   ├── Stage3.png
│   ├── Stage4.png
│   ├── clfTestResult.csv
│   ├── model.pkl
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
16. https://www.kaggle.com/datasets/fedesoriano/cirrhosis-prediction-dataset  
17. http://www.diva-portal.org/smash/get/diva2:769192/FULLTEXT01.pdf  
18. https://www.freepik.com/  











 
