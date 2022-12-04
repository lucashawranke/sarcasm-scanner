import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
filename= "mnb.pkl"

with open(filename, 'rb') as file:
    model = joblib.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    X_test_new = [x for x in request.form.values()]
    prediction = model.predict(X_test_new)
    output = prediction[0]
    return render_template('index.html', prediction_text='This headline is most likely from a {} news source.'.format(output))


if __name__ == "__main__":
    app.run(debug=True)