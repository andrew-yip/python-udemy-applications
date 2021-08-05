import folium
import pandas

#recieving data from the volcanoes txt file
data = pandas.read_csv("/Users/andrewyip/Desktop/udemy/webmap/Volcanoes.txt")

#Loading data for the latitude and longitude
lat = list(data["LAT"]) #retrieved data from dataframe
lon = list(data["LON"])

#Loading elevation data
elev = list(data["ELEV"])

#Function before expressions to return the color based on elevation:
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <=elevation < 3000:
        return 'orange' 
    else:
        return 'red'

#Adding map elements
map = folium.Map(location = [38.58, -99.09], zoom_start = 6, titles = "Stamen Terrain") #this creates a base map/folium gives you a layer thru

#VOLCANOES: Feature (Layer) Group for Volcanoes
fgv = folium.FeatureGroup(name = "Volcanoes")
for lt,ln,el in zip(lat,lon,elev): #ADDING A BUNCH OF CHILDS TO FGV
   fgv.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = "Elevation: "+ str(el)+ " m", fill_color = color_producer(el), color ='grey', fill_opacity = 0.7))


#POPULATION: Feature Layer Group for Population
fgp = folium.FeatureGroup(name = "Population")
#adding geographical features (adding a child layer of geojson on top of it with data from the world json file)
fgp.add_child(folium.GeoJson(data =open('/Users/andrewyip/Desktop/udemy_python/webmap/world.json', 'r', encoding='utf-8-sig').read(), 
    style_function= lambda x: {'fillColor': 'green' if x ['properties']['POP2005'] < 10000000 
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'} ))


#FINAL TOUCHES
#adding the layers onto the original map
map.add_child(fgv)
map.add_child(fgp)

#Layer Control
map.add_child(folium.LayerControl())

#FINAL SAVES
map.save("Map1.html") #saves the map




