import folium
from folium.plugins import MarkerCluster
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create a map of Europe
Travel_Map = folium.Map(location=[50.5, 10], zoom_start=4, tiles='cartodbpositron')

# Add markers for the towns in the specified order
towns = {'Split': [43.5081, 16.4402],
         'Pilsen': [49.7475, 13.3776],
         'Liege': [50.6439, 5.5718],
         'Prague': [50.0755, 14.4378],
         'Paris': [48.8566, 2.3522],
         'Monaco': [43.7384, 7.4246],
         'Brno': [49.1951, 16.6068],
         'Ostrava': [49.8209, 18.2625],
         'London': [51.5074, -0.1278],
         'Malta': [35.8989, 14.5146],
         'Bruxxelles': [50.8503, 4.3517],
         'Warsaw': [52.2297, 21.0122],
         'Krakow': [50.0647, 19.9450],
         'Kielce': [50.8661, 20.6286],
         'Marseille': [43.2965, 5.3698],
         'Verona': [45.4384, 10.9916],
         'Milan': [45.4642, 9.1900],
         'Kyiv': [50.4501, 30.5234],
         'Minsk': [53.9045, 27.5615],
         'Jindřichův Hradec': [49.1458, 15.0031],
         'Bratislva': [48.1486, 17.1077],
         'Zurich': [47.3769, 8.5417],
         'Nice': [43.7102, 7.2620],
         'Cannes': [43.5528, 7.0174],
         'Zadar': [44.1194, 15.2313],
         'Zagreb': [45.8150, 15.9819],
         'Kupres': [43.9064, 17.3728],
         'Barcelona': [41.3851, 2.1734],
         'Amsterdam': [52.3676, 4.9041],
         'Luxembourg': [49.6116, 6.1319],
         'Vienna': [48.2082, 16.3738],
         'Zhytomyr': [50.2649, 28.6767],
         'Karlovy Vary': [50.2329, 12.8710],
         'České Budějovice': [48.9759, 14.4805],
         'Hradec Králové': [50.2092, 15.8327],
         'Budapest': [47.4979, 19.0402]}

for i, (town, coordinates) in enumerate(towns.items(), 1):
    folium.Marker(location=coordinates, 
                  popup=f"{i}. {town}",
                  icon=folium.Icon(icon='circle', prefix='fa', color='green')).add_to(Travel_Map)

# Save the map as an HTML file
Travel_Map.save('travel_map.html')
