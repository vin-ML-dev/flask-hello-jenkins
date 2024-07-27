from flask import Flask,render_template,jsonify,request
import os
import pickle
import numpy as np


app = Flask(__name__)

def make_predict(sample):
   with open('iris_model.pkl', 'rb') as f:
       model = pickle.load(f)
       
   prediction = model.predict(sample)

   return prediction
   
   
@app.route("/")
def hello():
   return render_template('home.html')

@app.route("/predict/",methods=['POST'])
def predict():

   print(request)
   t = request.get_json['test_data']
   print(t,type(t))
   sample = np.array([t])
   pred = make_predict(sample)

   return jsonify({'response':pred})
   
   
   


if __name__ == "__main__":
   
   app.run(host='0.0.0.0', port="5000")
