import numpy as np
from flask import Flask, render_template, request 

import pickle
app=Flask(__name__)

model = pickle.load(open('wqi.pkl','rb')) 
@app.route('/')
def home():
    return render_template("login.html")

@app.route('/')
def home():
    return render_template("signup.html")


@app.route('/')
def home():
    return render_template("home.html")

@app.route("/login",methods = ['POST'])
def login():
    temp=request.form["temp"]
    do=request.form["do"]
    ph =request.form["ph"] 
    co=request.form["co"] 
    bod = request.form["bod"] 
    na=request.form["na"]
    tcrequest.form["tc"]
    total =[[float(temp), float (do), float (ph), float (co), float (bod), float (na), float(tc)]] 
    y_pred=model.predict(total)
    y_pred=y_pred[[0]]
    if(y_pred >= 95 and y_pred <= 100): 
        s='Excellent'
        return render_template("home.html",showcase = 'Excellent, The predicted value is'+ str(y_pred)) 
    elif(y_pred >= 89 and y_pred<=94):
        s='Very good'
        return render_template("home.html",showcase = 'Very good, The predicted value is' + str(y_pred)) 
    elif(y_pred >= 80 and y_pred<=88):
        s='Good'
        return render_template("home.html",showcase = 'Good, The predicted value is' + str(y_pred))
    elif(y_pred >= 65 and y_pred<=79):
        s='Fair'
        return render_template("home.html",showcase = 'Fair, The predicted value is ' + str(y_pred))
    elif(y_pred >= 45 and y_pred<=64):
        s='Marginal'
        return render_template("home.html",showcase = 'Marginal, The predicted value is ' + str(y_pred))
    else:
        s='Poor'
        return render_template("home.html",showcase = 'Poor, The predicted value is ' + str(y_pred))


if __name__=='__main__':
    app.run()
Footer