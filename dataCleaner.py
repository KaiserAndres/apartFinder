import re
import sqlite3

db = sqlite3.connect('deps.db')
c = db.cursor()

numberFinder = re.compile(r'\d+(\.|\d)*')
categoryFinder = re.compile(r'([a-z]|ñ|á|é|í|ó|ú|ü)+\s*([a-z]|ñ|á|é|í|ó|ú|ü)+')

c.execute('SELECT * FROM datos')

for ID, data in c.fetchall():
  if c.execute('SELECT id FROM descriptions') != ():
    continue
  data = data.lower()

  numRes = numberFinder.search(data)
  catRes = categoryFinder.search(data)

  try:
    value = numRes.group()
  except:
    value = 0
  try:
    catego = catRes.group()
  except:
    catego = ""

  try:
    c.execute('INSERT INTO descriptions VALUES ({}, "{}", "{}")'.format(ID,
                                                                        catego,
                                                                        value))
  except:
    print(ID, category, value)
    break
  db.commit()
