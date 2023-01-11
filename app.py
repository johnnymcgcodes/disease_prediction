import flask
from flask import Flask, send_file, redirect, render_template
from flask_bootstrap import Bootstrap

import pickle
from flask import request, jsonify
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)
Bootstrap(app)

# Load machine learning model
model = pickle.load(open("diabetes_classifier.pkl", "rb"))

# Create app
@app.route('/')
def IndexPage():  # put application's code here
    return render_template("index.html")


@app.route('/classify', methods=["POST"])
def classify():
    number_features = [float(x) for x in request.form.values()]
    features = [np.array(number_features)]
    print(features)
    pred = model.predict(features)
    pred_prob = model.predict_proba(features)

    plt.pie(pred_prob[0])
    plt.title("Prediction probability")
    plt.xlabel("0: No disease indicated, 1: pre-diabetic indicated")
    plt.ylabel("Percent")
    plt.legend(["No disease", "pre-diabetic"])
    plt.savefig('plot.png')
    plt.close()
    pred = pred[0]
    pred_text = ""
    if pred == 1:
        pred_text = "Pre-diabetic indicated"
    else:
        pred_text = "Pre-diabetic not indicated"

    return render_template("results.html", pred_text=f"Diagnosis: {pred_text}",
                           graph1='my_plot.png')


@app.route('/classify')
def submit():
    # button action to return to home page
    return redirect('/')


def show_chart():
    # Load matplotlib chart from the pickle file
    with open('chart.pickle', 'rb') as f:
        chart = pickle.load(f)

    # Generate  image of  chart
    chart.savefig('chart.png')

    return send_file('chart.png', mimetype='image/png')


@app.route('/image0')
def serve_image_pie():
    return send_file(f'plot.png')


@app.route('/image1')
def serve_image_feature():
    return send_file(f'./charts/featureImpact.png')


@app.route('/image2')
def serve_image_scatter():
    return send_file(f'./charts/scatter.png')


@app.route('/image3')
def serve_image_roc():
    return send_file(f'./charts/roc_curve.png')


if __name__ == '__main__':
    app.run()
