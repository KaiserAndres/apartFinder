import sqlite3
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

uniLat = -64.192241
uniLng = -31.438921
db = sqlite3.connect('deps.db')
c = db.cursor()

c.execute('SELECT * FROM location')
for ID, lat, lng in c.fetchall():
    if c.execute('SELECT id FROM distance WHERE id={}'.format(ID)).fetchone():
        print("Already did {}".format(ID))
        continue
    dist = haversine(uniLng, uniLat, lng, lat)
    print(ID, dist)
    c.execute('INSERT INTO distance VALUES ({},{})'.format(ID, dist))
    db.commit()
