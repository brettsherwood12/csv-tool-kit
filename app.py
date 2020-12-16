# start virtual env with ". venv/bin/activate"
# tell flask to debug with "export FLASK_ENV=development"
from flask import Flask, request, url_for, render_template, redirect, jsonify
from flask_dropzone import Dropzone
import os, json

from helpers import get_dict_from_csv, delete_csv

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
dropzone = Dropzone(app)

@app.route("/")
def home():
  return render_template("views/home.html")

@app.route("/visualizer", methods=["GET", "POST"])
def visualizer():
  if request.method == "POST":
    f = request.files.get("file")
    filename = request.form["filename"]
    f.save(os.path.join(basedir, "uploads", filename))
    return redirect('/visualizer/' + filename)
  else:
    return render_template("views/visualizer.html")

@app.route("/processor", methods=["GET", "POST"])
def processor():
  if request.method == "POST":
    f = request.files.get("file")
    filename = request.form["filename"]
    f.save(os.path.join(basedir, "uploads", filename))
    return redirect('/processor/' + filename)
  else:
    return render_template("views/processor.html")

@app.route("/viewer", methods=["GET", "POST"])
def viewer():
  if request.method == "POST":
    f = request.files.get("file")
    filename = request.form["filename"]
    f.save(os.path.join(basedir, "uploads", filename))
    return redirect('/viewer/' + filename)
  else:
    return render_template("views/viewer.html")

@app.route("/visualizer/<path:filename>")
def visualizer_results(filename):
  data = get_dict_from_csv(filename)
  delete_csv(filename)
  return render_template("views/table.html", data=data)
  # render graph once functionality implemented

@app.route("/processor/<path:filename>")
def processor_results(filename):
  data = get_dict_from_csv(filename)
  delete_csv(filename)
  return render_template("views/table.html", data=data)
  # render analysis once functionality implemented

@app.route("/viewer/<filename>")
def viewer_results(filename):
  data = get_dict_from_csv(filename)
  delete_csv(filename)
  return render_template("views/table.html", data=data)

@app.route("/about")
def about():
  return render_template("views/about.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("views/notfound.html"), 404

if __name__ == '__main__':
    app.run(debug=True)
