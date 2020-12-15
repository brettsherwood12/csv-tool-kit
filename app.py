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

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/visualizer", methods=["GET", "POST"])
def visualizer():
  if request.method == "POST":
    f = request.files.get("file")
    filename = request.form["filename"]
    f.save(os.path.join(basedir, "uploads", filename))
    return redirect('/visualizer/' + filename)
  else:
    return render_template("visualizer.html")

@app.route("/processor", methods=["GET", "POST"])
def processor():
  if request.method == "POST":
    f = request.files.get("file")
    filename = request.form["filename"]
    f.save(os.path.join(basedir, "uploads", filename))
    return redirect('/processor/' + filename)
  else:
    return render_template("processor.html")

@app.route("/viewer", methods=["GET", "POST"])
def viewer():
  if request.method == "POST":
    f = request.files.get("file")
    filename = request.form["filename"]
    f.save(os.path.join(basedir, "uploads", filename))
    return redirect('/viewer/' + filename)
  else:
    return render_template("viewer.html")

@app.route("/visualizer/<filename>")
def visualizer_results(filename):
  data = get_data_from_csv(filename)
  return render_template("graph.html", data=data)

@app.route("/processor/<filename>")
def processor_results(filename):
  data = get_data_from_csv(filename)
  return render_template("analysis.html", data=data)

@app.route("/viewer/<filename>")
def viewer_results(filename):
  data = get_data_from_csv(filename)
  return render_template("table.html", data=data)

@app.route("/about")
def about():
  return render_template("about.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('notfound.html'), 404
