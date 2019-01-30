import requests
import csv
import re

user_name = 'Maurice Yap'
sheet_url = 'https://docs.google.com/spreadsheet/ccc?key=1kFRfM5-l3IEKTxf0w5iVRkTPLb4dT5LNcK9dxWZucJ0&output=csv'
date_line = 0
role_column = 0
date_cell_regex = r'.*(\d\d)/(\d\d)/(20\d\d).*'
day_match_group = 1
month_match_group = 2
year_match_group = 3

reader = csv.reader([l.decode() for l in requests.get(sheet_url).iter_lines()])
data = [row for row in reader]
dates = data[date_line]
for names_row in data[date_line + 1:]:
  for i, name in enumerate(names_row):
    if name == user_name:
      date_cell = dates[i]
      date_match = re.match(date_cell_regex, date_cell)
      print(date_match.group(1))
      print(date_match.group(2))
      print(date_match.group(3))
      print(names_row[role_column])

def lambda_handler(event, context):
  return {'statusCode': '400', 'headers': {
            'Content-Type': 'text/html',
}, 'body': 'hello hello hello'}
