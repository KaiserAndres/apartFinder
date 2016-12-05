import urllib.request as dw
from bs4 import BeautifulSoup
import sqlite3

db = sqlite3.connect('deps.db')
c = db.cursor()
rootUrl = "http://www.zonaprop.com.ar"
firstPage = 20
lastPage = 50

for page_num in range(firstPage,lastPage+1):
  if page_num > 1:
    url = rootUrl+"/departamento-cordoba-cb-pagina-{}.html".format(page_num)
  else:
    url = rootUrl+"/departamento-cordoba-cb.html"

  print("Downloading {}".format(url))
  soup = BeautifulSoup(dw.urlopen(url), 'html.parser')
  print("Download coplete.")
  posts = soup.find(id="listadoSection").findAll("li")

  for post in posts:
    secs = post.findAll('h4')
    if secs != []:
      link = secs[0].find('a').get('href')
      c.execute('INSERT INTO posts VALUES ({}, \'{}\')'.format('null' ,link))
      db.commit()

