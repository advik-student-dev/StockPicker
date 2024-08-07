import pandas as pd
import json
def standardizeCSV(name, has_date=False, date_name=""):
  data=pd.read_csv(name)
  #prepares the data for display
  data.columns = data.columns.str.strip()
  for iter_name in data.columns:
    data[iter_name] = data[iter_name].str.replace('$','').astype(float)
  #if there is a date column, it will be converted to datetime
  if(has_date):
    data[date_name] = pd.to_datetime(data[date_name])
def standardizeJSONtoCSV(name):
  #Read the JSON file
  with open(name, 'r') as f:
    data = json.load(f)
  #Standardize keys 
  data.keys() = data.keys().tolowerCase()
  data = pd.read_json(name)
  data = pd.to_csv(name)
  
  return data