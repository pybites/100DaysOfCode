import csv
from pprint import pprint as pp

import folium

cities = ['Amsterdam', 'Paris', 'Madrid', 'Barcelona', 'København', 'Berlin', 
	  'Seville', 'Marseille', 'Lyon', 'London', 'Nottingham', 'Brussels',
	  'Rome', 'Florence', 'Naples', 'Bucharest', 'Verona', 'Valencia', 
          'Palermo', 'Edinburgh', 'Biarritz']
CENTER = 'Berlin'

longlat = {}

with open('simplemaps-worldcities-basic.csv') as csvfile:
    rows = csv.DictReader(csvfile)
    for r in rows:
        city = r['city']
        if city in cities:
            longlat[city] = [r['lat'], r['lng']]

#pp(longlat)

map_1 = folium.Map(location=longlat[CENTER], zoom_start=4,
                   tiles='Stamen Terrain')

for city, coords in longlat.items():
    folium.Marker(coords, popup=city).add_to(map_1)

# TODO: some cities don't show up (BCN, London)

map_1.save('cities.html')
