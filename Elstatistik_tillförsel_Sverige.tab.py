import csv
from datetime import datetime, timedelta
boundary = datetime(2024,1,2,0,0,0)
res = []
accum = []
# file fetched from https://www.svk.se/om-kraftsystemet/kraftsystemdata/elstatistik/
# and columns removed in libreoffice
with open("n_fot2024-01-12.csv",'r') as f:
    c = csv.reader(f)
    for row in c:
      dt = datetime.strptime(row[0], '%d-%m-%Y %H:%M:%S')
      if dt < boundary:
          res.append(float(row[1].replace(',','.')))
      else:
          boundary = dt + timedelta(days=1)
          accum.append((dt,res))
          res = [float(row[1].replace(',', '.'))]

assert 24 == len(accum[0][1]), len(accum[0][1])
assert 365 == len(accum)

print("date,mwh_produced")
total=0.0
for (boundary, hour_values) in accum:
   print(f"{boundary.date()},{sum(hour_values)}")
   total += sum(hour_values)

