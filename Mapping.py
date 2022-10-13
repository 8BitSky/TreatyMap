import folium
import pandas

#https://native-land.ca/

data = pandas.read_csv("Towns.txt")
town_name = list(data["TOWN"])
town_lat = list(data["LAT"])
town_lon = list(data["LON"])
town_pop = list(data["POP"])

def color_producer(population):
    if population < 1000:
        return "blue"
    elif 1000 <= population < 5000:
        return "green"
    else:
        return "black"
    return "green"

style_function = lambda x: {"fillColor":x["properties"]["color"]}

map1 = folium.Map(location=[55.113437681629975,-105.28932028344423], zoom_start=10, tiles="Stamen Watercolor")

fgv = folium.FeatureGroup(name="Towns")
for nm, lt, ln, p in zip(town_name, town_lat, town_lon, town_pop):
    fgv.add_child(folium.Marker(location=[lt,ln], popup=nm, icon=folium.Icon(color=color_producer(p))))

#Treaties
json_treaties=folium.GeoJson(data=open("indigenousTreaties.json","r", encoding="utf-8-sig").read(),
style_function=style_function)
folium.GeoJsonTooltip(fields=["Name","description"],).add_to(json_treaties)
fgtreaties = folium.FeatureGroup(name="Treaties")
fgtreaties.add_child(json_treaties)

#LANGUAGES
json_languages = folium.GeoJson(data=open("indigenousLanguages.json","r", encoding="utf-8-sig").read(),
style_function=style_function)
folium.GeoJsonTooltip(fields=["Name"]).add_to(json_languages)
fglanguages = folium.FeatureGroup(name="Languages", show=False)
fglanguages.add_child(json_languages)

#Territories
json_territories = folium.GeoJson(data=open("indigenousTerritories.json","r", encoding="utf-8-sig").read(),style_function=style_function)
folium.GeoJsonTooltip(fields=["Name"]).add_to(json_territories)
fgterritories = folium.FeatureGroup(name="Territories",show=False)
fgterritories.add_child(json_territories)

#Add Feature Groups (layers) to Map
map1.add_child(fgv)
map1.add_child(fgtreaties)
map1.add_child(fglanguages)
map1.add_child(fgterritories)

#Add Layer Control to Map
folium.LayerControl().add_to(map1)

map1.save("Index.html")



#For testing, import pandas, create "data" variable, store read_csv("file")
#Use type(data) to show dataframe 
#Use data.columns to get header returned as list/array