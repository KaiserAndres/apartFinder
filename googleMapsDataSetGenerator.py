import sqlite3
import csv

db = sqlite3.connect('deps.db')
c = db.cursor()

with open('dataset.csv', 'w', newline='') as dataset:
  dataWriter = csv.writer(dataset,
                          delimiter=' ',
                          quotechar='|',
                          quoting=csv.QUOTE_MINIMAL)
  c.execute('SELECT id FROM descriptions WHERE cat="dormitorio" OR cat="dormitorios" AND val=1')
  for depId in c.fetchall():
    c.execute('SELECT * FROM location WHERE id={}'.format(depId[0]))

    for loc in c.fetchall():
      ID, lng, lat = loc
      dataWriter.writerow([lat, lng])
