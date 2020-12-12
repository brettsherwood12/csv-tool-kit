# activate virtual env with command ". venv/bin/activate"
# tell flask to debug with "export FLASK_ENV=development"
from flask import Flask, render_template, redirect, request, jsonify
from flask_dropzone import Dropzone
import os

app = Flask(__name__)
dropzone = Dropzone(app)
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
  if request.method == "POST":
    f = request.files.get("file")
    print(request)
    f.save(os.path.join(basedir, "uploads", "file.csv"))
    return render_template("upload.html", data=["data", "data", "datathree"])
  if request.method == "GET":
    return render_template("upload.html", no_data=True)

@app.route("/about")
def about():
  return render_template("about.html")

if __name__ == "main":
  app.run(debug=True)
