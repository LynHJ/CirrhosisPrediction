from flask import Flask, render_template, request, url_for, redirect
import datetime as dt
import pymongo 
from bson.objectid import ObjectId
import pandas as pd
import pickle
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    
    return render_template('index.html')


@app.route('/predict')
def predict():
    # Connect to Mongo DB
    load_dotenv() # use dotenv to hide sensitive credential as environment variables
    DATABASE_URL=f'mongodb+srv://cirrhosis:{os.environ.get("password")}'\
              '@cirrhosispred.u8sicly.mongodb.net/database?retryWrites=true&w=majority'

   
    client = pymongo.MongoClient(DATABASE_URL)
   
    db = client.flask_db

    records = db.records
    
    nowDate = dt.datetime.now().strftime("%d/%m/%Y")

    # Pull data from index.html and load into db

    name=request.args['name']

    age=request.args['age']

    ascites=request.args['ascites'].upper()

    hepatomegaly=request.args['hepatomegaly'].upper()

    spiders=request.args['spiders'].upper()

    edema=request.args['edema'].upper()

    bilirubin=request.args['bilirubin']

    albumin=request.args['albumin']

    copper=request.args['copper']

    platelets=request.args['platelets']

    prothrombin=request.args['prothrombin']

    # Preditct the input data is Cirrhosis or not
    # singal row data have to hard coding to dummeid the input data
    if ascites=='Y':
        Ascites_N=0
        Ascites_Y=1
    if ascites=='N':
        Ascites_N=1
        Ascites_Y=0
    if hepatomegaly=='Y':
        Hepatomegaly_N=0
        Hepatomegaly_Y=1
    if hepatomegaly=='N':
        Hepatomegaly_N=1
        Hepatomegaly_Y=0
    if spiders=='Y':
        Spiders_N=0
        Spiders_Y=1
    if spiders=='N':
        Spiders_N=1
        Spiders_Y=0
    if edema=='Y':
        Edema_N=0
        Edema_Y=1
        Edema_S=0
    if edema=='N':
        Edema_N=1
        Edema_Y=0
        Edema_S=0
        
    input = [{'Age':float(age),'Bilirubin':float(bilirubin),'Albumin':float(albumin),'Copper':float(copper),'Platelets':float(platelets),'Prothrombin':float(prothrombin),'Ascites_N':Ascites_N,'Ascites_Y':Ascites_Y,'Hepatomegaly_N':Hepatomegaly_N,'Hepatomegaly_Y':Hepatomegaly_Y,'Spiders_N':Spiders_N,'Spiders_Y':Spiders_Y,'Edema_N':Edema_N,'Edema_S':Edema_S,'Edema_Y':Edema_Y}]

    input_df = pd.DataFrame(input)
    pickled_model = pickle.load(open('Output Data/model.pkl', 'rb'))#load trained model
    pickled_scaler = pickle.load(open('Output Data/scaler.pkl', 'rb'))#load scaler
    scaled = pickled_scaler.transform(input_df)
    ypred = pickled_model.predict(scaled)
    prediction =ypred[0]
    if prediction == 1:
        result = 'Positive'
    if prediction == 0:
        result = 'Negative'


    records.insert_one({'Name': name,'Age':age,'Ascites':ascites,'Hepatomegaly':hepatomegaly,\
            'Spiders':spiders,'Edema':edema,'Bilirubin':bilirubin,'Albumin':albumin,'Copper':copper,\
                'Platelets':platelets,'Prothrombin':prothrombin,'RecordedDate': nowDate,'Result':result})
    
    all_records = records.find()
    
    return render_template('predict.html', records=all_records)

@app.route('/record')

def record():
    # Connect to Mongo DB
    load_dotenv() # use dotenv to hide sensitive credential as environment variables

    DATABASE_URL=f'mongodb+srv://cirrhosis:{os.environ.get("password")}'\
              '@cirrhosispred.u8sicly.mongodb.net/database?retryWrites=true&w=majority'

    client = pymongo.MongoClient(DATABASE_URL)
   
    db = client.flask_db

    records = db.records
    
    all_records = records.find()
    
    return render_template('record.html', records=all_records)
        



@app.post('/<id>/delete/') # Delect stock user not interested
def delete(id):
    # Connect to Mongo DB
    load_dotenv() # use dotenv to hide sensitive credential as environment variables
    DATABASE_URL=f'mongodb+srv://cirrhosis:{os.environ.get("password")}'\
              '@cirrhosispred.u8sicly.mongodb.net/database?retryWrites=true&w=majority'

    client = pymongo.MongoClient(DATABASE_URL)
   
    db = client.flask_db

    records = db.records

    records.delete_one({"_id": ObjectId(id)})
    # stay at the same page

    return redirect(url_for('record'))
        
    
if __name__ == '__main__':
    app.run(debug=True)
