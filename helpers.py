import os
import datetime
import json
import pandas as pd

basedir = os.path.abspath(os.path.dirname(__file__))

def get_data_from_csv(filename):
  file_path = os.path.join(basedir, "uploads", filename)
  df = pd.read_csv(file_path).drop('Open', axis=1)
  chart_data = df.to_dict(orient='records')
  chart_data = json.dumps(chart_data, indent=2)
  data = {'chart_data': chart_data}
  return data

def delete_csv(filename):
  file_path = os.path.join(basedir, "uploads", filename)
  os.remove(file_path)
  data = {"deleted": True}
  return data
