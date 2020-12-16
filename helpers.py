import os
import datetime
import json
import pandas as pd

basedir = os.path.abspath(os.path.dirname(__file__))

def get_dict_from_csv(filename):
  file_path = os.path.join(basedir, "uploads", filename)
  df = pd.read_csv(file_path).drop('Open', axis=1)
  data = df.to_dict(orient='records')
  return data

def delete_csv(filename):
  file_path = os.path.join(basedir, "uploads", filename)
  os.remove(file_path)
  data = {"deleted": True}
  return data
