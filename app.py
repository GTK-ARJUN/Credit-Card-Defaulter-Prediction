#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


# In[2]:


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    for rendering results on HTML
    '''
    features = [int(x) for x in request.form.values()]

    # re-arranging the list as per data set
    feature_list = [features[4]] + features[:4] + features[5:11][::-1] + features[11:17][::-1] + features[17:][::-1]
    features_arr = [np.array(feature_list)]

    prediction = model.predict(features_arr)

    print(features_arr)
    print("prediction value: ", prediction)

    result = ""
    if prediction == 1:
        result = "The credit card holder will be Defaulter in the next month"
    else:
        result = "The Credit card holder will not be Defaulter in the next month"

    return render_template('index.html', prediction_text = result)


if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




