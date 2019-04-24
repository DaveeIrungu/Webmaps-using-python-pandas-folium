import folium
import pandas

# loading all the data from the predefined list
data = pandas.read_csv("Daystar.txt")

# Create list of latitudes and longitudes
lat = list(data['latitude'])
lon = list(data['longitude'])

# Load the name of the place from the list
name = list(data['name'])

# Load the location from the list. 'off' or 'on' campus
loc = list(data['location'])


# A function that generates color for dynamically marking location points
def color_generator(loc):
    if loc == 'on':
        return 'blue'
    else:
        return 'lightgreen'


# Create a map object and pass a few parameters
map = folium.Map(location=[-1.439515, 37.048486], zoom_start=4, tiles="OpenStreetMap")

# Create feature group to add various features to the Daystar map
fg_Daystar = folium.FeatureGroup(name="Daystar Map")

# Extract exact locations from the lists of longitudes and latitudes by pairing them using zip function
# Icon argument takes output from color_generator function

for latVariable, lonVariable, nameVariable, locVariable in zip(lat, lon, name, loc):
    fg_Daystar.add_child(
        folium.Marker(location=[latVariable, lonVariable], popup=str(nameVariable),
                      icon=folium.Icon(color_generator(locVariable))))

fg_WorldPopulation = folium.FeatureGroup(name="World Population Map")

# Add feature group to use Geo json data located in the world.json file
fg_WorldPopulation.add_child(folium.GeoJson(data=open('world.json', encoding='utf-8-sig').read(),
                                            style_function=lambda x: {
                                                'fillColor': 'red' if x['properties']['POP2005'] < 10000000
                                                else 'blue' if 10000000 <= x['properties'][
                                                    'POP2005'] < 20000000 else 'green'}))

# Add_child method is used to pass 'fg' object to the map object
map.add_child(fg_Daystar)
map.add_child(fg_WorldPopulation)

# Add a control layer to toggle between modes
# Layer control checks for all feature group 'fg' objects and allows the user to toggle between them
map.add_child(folium.LayerControl())

map.save("Map1.html")
