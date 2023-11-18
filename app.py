import pickle
import flask 
from flask import Flask, render_template, url_for, request
from numpy.random import randint, choice
import pandas as pd
import numpy as np
import os

#load saved model
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
model_url = os.path.join(SITE_ROOT, 'model.pkl')
def load_pkl(fname):
    with open(fname, 'rb') as f:
        obj = pickle.load(f)
    return obj
model = load_pkl(model_url)

result = {'PHASE 1': ['Breathing Exercise', 'Breathing Exercise', 'Breathing Exercise', 'Breathing Exercise', 'Breathing Exercise'],
 'PHASE 2': ['Light Exercise', 'Light Exercise', 'Light Exercise', 'Light Exercise', 'Light Exercise'],
 'PHASE 3': ['Everyday Activities (Balance while Sitting)', 'Everyday Activities (Balance while Sitting)', 'Everyday Activities (Balance while Sitting)', 'Everyday Activities (Balance while Sitting)', 'Everyday Activities (Balance while Sitting)'],
 'PHASE 4': ['Everyday Activities (Exercises while Sitting)', 'Everyday Activities (Give Support to your Weak Side)', 'Everyday Activities (Muscles Lengthening hand, arm and leg )', 'Everyday Activities (Exercises while Sitting)', 'Everyday Activities (Give Support to your Weak Side)'],
 'PHASE 5': ['Everyday Activities (Muscles Lengthening hand, arm and leg )', 'Everyday Activities (Muscles Lengthening hand, arm and leg )', 'Everyday Activities (Exercises while Sitting)', 'Everyday Activities (Muscles Lengthening hand, arm and leg )', 'Everyday Activities (Muscles Lengthening hand, arm and leg )'],
 'PHASE 6': ['Everyday Activities (Give Support to your Weak Side)', 'Everyday Activities (Strengthening your Arm, Hand and Legs)', 'Everyday Activities (Strengthening your Arm, Hand and Legs)', 'Everyday Activities (Give Support to your Weak Side)', 'Everyday Activities (Strengthening your Arm, Hand and Legs)'],
 'PHASE 7': ['Everyday Activities (Strengthening your Arm, Hand and Legs)', 'Everyday Activities (Exercises while Sitting)', 'Everyday Activities (Give Support to your Weak Side)', 'Everyday Activities (Strengthening your Arm, Hand and Legs)', 'Everyday Activities (Exercises while Sitting)'],
 'PHASE 8': ['Everyday Activities (Functional Hand and Finger Activities)', 'Everyday Activities (Functional Hand and Finger Activities)', 'Everyday Activities (Functional Hand and Finger Activities)', 'Everyday Activities (Functional Hand and Finger Activities)', 'Everyday Activities (Functional Hand and Finger Activities)'],
 'PHASE 9': ['Everyday Activities (Stand up and Getting up from fall)', 'Everyday Activities (Bed moving, transferring and rolling)', 'Everyday Activities (Bed moving, transferring and rolling)', 'Everyday Activities (Stand up and Getting up from fall)', 'Everyday Activities (Stand up and Getting up from fall)'],
 'PHASE 10':['Everyday Activities (Bed moving, transferring and rolling)', 'Everyday Activities (Stand up and Getting up from fall)', 'Everyday Activities (Stand up and Getting up from fall)', 'Everyday Activities (Bed moving, transferring and rolling)', 'Everyday Activities (Bed moving, transferring and rolling)'],
 'PHASE 11':['Standing and Walking (Exercise for a very weak leg -wearing brace or gaiter)', 'Standing and Walking (Exercise for a very weak leg -wearing brace or gaiter)', 'Standing and Walking (Exercise for a very weak leg -wearing brace or gaiter)', 'Standing and Walking (Exercise for a very weak leg -wearing brace or gaiter)', 'Standing and Walking (Exercise for a very weak leg -wearing brace or gaiter)'],
 'PHASE 12':['Standing and Walking (exercises without a knee support)', 'Standing and Walking (standing)', 'Standing and Walking (exercises without a knee support)', 'Standing and Walking (exercises without a knee support)', 'Standing and Walking (standing)'],
 'PHASE 13':['Standing and Walking (walking)', 'Standing and Walking (exercises without a knee support)', 'Standing and Walking (exercises without a knee support)', 'Standing and Walking (walking)', 'Standing and Walking (exercises without a knee support)'],
 'PHASE 14':['Strength and Control (Movement in your Arm and Hand)', 'Standing and Walking (walking)', 'Strength and Control (Movement in your Arm and Hand)', 'Strength and Control (Movement in your Arm and Hand)', 'Standing and Walking (walking)'],
 'PHASE 15':['Strength and Control (Strengthen your Back and Stomach Muscles)', 'Strength and Control (Movement in your Arm and Hand)', 'Strength and Control (Strengthen your Back and Stomach Muscles)', 'Strength and Control (Strengthen your Back and Stomach Muscles)', 'Strength and Control (Movement in your Arm and Hand)'],
 'PHASE 16':['Strength and Control (Strengthen  Hip)', 'Strength and Control (Strengthen your Back and Stomach Muscles)', 'Strength and Control (Strengthen  Hip)', 'Strength and Control (Strengthen  Hip)', 'Strength and Control (Strengthen your Back and Stomach Muscles)'],
 'PHASE 17':['Strength and Control (Strengthen Ankle)', 'Strength and Control (Strengthen  Hip)', 'Strength and Control (Strengthen Ankle)', 'Strength and Control (Strengthen Ankle)', 'Strength and Control (Strengthen  Hip)'],
 'PHASE 18':['Strength and Control (Strengthen  Knee)', 'Strength and Control (Strengthen Ankle)', 'Strength and Control (Strengthen  Knee)', 'Strength and Control (Strengthen  Knee)', 'Strength and Control (Strengthen Ankle)'],
 'PHASE 19':['Facial Exercise (Smiling and talking)', 'Strength and Control (Strengthen  Knee)', 'Facial Exercise (Smiling and talking)', 'Facial Exercise (Smiling and talking)', 'Strength and Control (Strengthen  Knee)'],
 'PHASE 20':['Speech Training Exercises (Lip Buzing , Vowal and consonant sounds exercises)', 'Facial Exercise (Smiling and talking)', 'Speech Training Exercises (Lip Buzing , Vowal and consonant sounds exercises)', 'Speech Training Exercises (Lip Buzing , Vowal and consonant sounds exercises)', 'Facial Exercise (Smiling and talking)'],
 'PHASE 21':['Return to work assistant', 'Speech Training Exercises (Lip Buzing , Vowal and consonant sounds exercises)', 'Return to work assistant', 'Return to work assistant', 'Speech Training Exercises (Lip Buzing , Vowal and consonant sounds exercises)'],
 'PHASE 22':['Rest', 'Return to work assistant', 'Rest', 'Rest', 'Return to work assistant']}


num_disease = []
app = Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html", judul="Home")

@app.route("/predict", methods=["POST"])
def predict():
    disease = []
    smoke = request.form["smoke"]
    if smoke == "smokes":
        disease.append("SMOKER")
        num_disease.append(0)
        
    obey = int(request.form["bmi"])
    if obey > 30 and obey < 35:
        disease.append("OBESITY I")
        num_disease.append(1)
    elif obey > 35 and obey < 40:
        disease.append("OBESITY II")
        num_disease.append(1)
    elif obey > 40:
        disease.append("OBESITY III")
        num_disease.append(1)
        
    heart = request.form["heart"]
    if heart == 'yes':
        disease.append('HEART DISEASE')  
        num_disease.append(2)
        
    hyper = request.form["hypertension"]
    if hyper == "yes":
        disease.append("HYPERTENSION")
        num_disease.append(3)
        
    diabetes = int(request.form["glucose"])
    if diabetes > 199:
        disease.append("DIABETES")
        num_disease.append(4)

    pred = 1#randint(0,5)
    return render_template('index.html',prediction_text=pred, dis=",".join(disease))

@app.route("/expert")
def expert():
    return render_template("expert-review.html", judul="Expert Review")

@app.route("/expert_review", methods=["POST"])
def expert_review():
    PHASE,HEALTH,EXERCISE = "","",""
    FASE = request.form["phase"]
    PROGRESS =  int(request.form.get("proses", False))
    if PROGRESS > 70 :
        PHASE = FASE.split(' ')[0] +" "+str(int(FASE.split(" ")[1])+1)
    else:
        PHASE = FASE
    HEALTH = choice([str(x)+"%" for x in range(30,90,10)])
    EXERCISE = [result[PHASE][x] for x in list(set(num_disease))]
    return render_template("expert-review.html", judul="Expert Review", ph=PHASE, health=HEALTH, exe=EXERCISE)

@app.route("/exercise")
def exercise():
    return render_template("Exercise.html", judul="Exercise")
    
@app.route("/health")
def health():
    return render_template("Health.html", judul="Health")
    
@app.route("/module")
def module():
    return render_template("Module.html", judul="Module")
    
if __name__ == '__main__':
    app.run(debug=True)
