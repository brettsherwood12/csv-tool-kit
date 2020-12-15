# start virtual env with ". venv/bin/activate"
# tell flask to debug with "export FLASK_ENV=development"
from flask import Flask, render_template, redirect, request, jsonify
from flask_dropzone import Dropzone
import pandas as pd
import os, json

from helpers import get_data_from_csv, delete_csv

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
dropzone = Dropzone(app)

@app.before_request
def log_request_info():
    app.logger.debug('Body: %s', request.get_data())

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/upload", methods=["POST"])
def upload():
  f = request.files.get("file")
  f.save(os.path.join(basedir, "uploads", filename))
  print(request.form)
  return "OK"

@app.route("/visualizer", methods=["GET"])
def visualizer():
  return render_template("visualizer.html")

@app.route("/processor", methods=["GET"])
def processor():
  return render_template("processor.html")

@app.route("/visualizer-results/<filename>", methods=["GET"])
def visualizer_results(filename):
  data = get_data_from_csv(filename)
  return render_template("visualizerresults.html", data=data)

@app.route("/processor-results/<filename>", methods=["GET"])
def processor_results(filename):
  data = get_data_from_csv(filename)
  return render_template("processorresults.html", data=data)

@app.route("/about", methods=["GET"])
def about():
  return render_template("about.html")

if __name__ == "main":
  app.run(debug=true)
