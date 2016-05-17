import csv

def print_record_count():
	with open('static/data/inspections.csv', 'r') as csvin:
		reader = list(csv.DictReader(csvin))
	print(len(reader))
  return len(reader)
