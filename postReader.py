import urllib.request as dw
from bs4 import BeautifulSoup
import sqlite3

db = sqlite3.connect('deps.db')
c = db.cursor()
rootUrl = "http://www.zonaprop.com.ar"

c.execute('SELECT * FROM posts')

for ID, link in c.fetchall():
  if c.execute('SELECT id FROM datos WHERE id={}'.format(ID)).fetchone():
    print("Already did {}".format(ID))
    continue
  url = rootUrl+link
  print("Doanloading {}".format(url))
  soup = BeautifulSoup(dw.urlopen(url), 'html.parser')
  print("Doanload complete — Scanning")
  for div in soup.findAll("div", {'class' : 'card aviso-datos'}):
    for spec in div.findAll('li'):
      c.execute("INSERT INTO datos VALUES ({},'{}')".format(ID, spec.getText()))
      db.commit()
  try:
    location = soup.find(id='map')
    lat = location.find(id='lat').get('value')
    lon = location.find(id='lng').get('value')
    c.execute('INSERT INTO location VALUES ({},{},{})'.format(ID, lon, lat))
    db.commit()
  except:
    continue