import folium
import pandas

# loading all the data from the predefined list
data = pandas.read_csv("Postcodes.txt")

# Create list of latitudes and longitudes
lat = list(data['latitude'])
lon = list(data['longitude'])

# Load the location data from the list
loc = list(data['location'])

# Create a map object and pass a few parameters
map = folium.Map(location=[-1.439515, 37.048486], zoom_start=16, tiles="OpenStreetMap")

# Create feature group to add various features to the map
fg = folium.FeatureGroup(name="My Map")

# Extract exact locations from the lists of longitudes and latitudes by pairing them using zip function

for latVariable, lonVariable, locVariable in zip(lat, lon, loc):
    fg.add_child(
        folium.Marker(location=[latVariable, lonVariable], popup=str(locVariable),
                      icon=folium.Icon(color="blue")))

# Add_child method is used to pass 'fg' object to the map object
map.add_child(fg)

map.save("Map1.html")
