import folium
import pandas
import io
import json

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """<h4>Volcano information:</h4>
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_calculator(el):
    if el < 1500:
        return "green"
    elif 1500 <= el < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location = [38.58, -99.89], zoom_start = 5, tiles = "Mapbox Bright")

fg_volcanoes= folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html = html % (nm, nm, el), width=200, height=100)
    fg_volcanoes.add_child(folium.CircleMarker(location = [lt, ln], radius = 6,
    popup = folium.Popup(iframe), fill_color = color_calculator(el), color = 'grey', fill_opacity = 0.7))

fg_population= folium.FeatureGroup(name = "Population")

fg_population.add_child(folium.GeoJson(data = open("world.json", "r", encoding = "utf-8-sig").read(),
style_function = lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else 'red'}))


map.add_child(fg_volcanoes)
map.add_child(fg_population)
map.add_child(folium.LayerControl())

map.save("Population_and_volcanoes_map.html")
