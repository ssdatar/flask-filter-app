import csv

def get_data():
  with open('static/data/inspections.csv', 'r') as csvin:
    datarows = list(csv.DictReader(csvin))
  return datarows

def print_record_count():
  with open('static/data/inspections.csv', 'r') as csvin:
    reader = list(csv.DictReader(csvin))
  print(len(reader))
  return len(reader)

def filter_by_score(score, datarows):
  if score == 'ninety':
    datarows = [d for d in datarows if len(d['inspection_score']) >= 2 
                and int(d['inspection_score']) > 90]
  elif score == 'seventy':
    datarows = [d for d in datarows if len(d['inspection_score']) >= 2 and 
                int(d['inspection_score']) > 70 and int(d['inspection_score']) <= 90]
  elif score == 'sixty':
    datarows = [d for d in datarows if len(d['inspection_score']) >= 2 and 
                int(d['inspection_score']) > 60 and int(d['inspection_score']) <= 80]
  elif score == 'least':
    datarows = [d for d in datarows if len(d['inspection_score']) >= 2 and 
                int(d['inspection_score']) <= 60]
  return datarows

def filter_by_risk(risk, datarows):
  datarows = [d for d in datarows if risk in d['risk_category']]
  return datarows

def filter_by_name(name, datarows):
  datarows = [d for d in datarows if name in d['business_name']]
  return datarows



def filter_func(score="", risk="", name=""):
  matched_rows = []
  datarows = get_data()

  if score:
    filteredrows = filter_by_score(score, datarows)

  elif risk:
    filteredrows = filter_by_risk(risk, datarows)

  return filteredrows
