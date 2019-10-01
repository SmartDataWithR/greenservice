from geopy.geocoders import Nominatim
import folium

adresse = input('Enter your adress: ')
tooltip = 'Click me!'

def geo():
    data = []
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.geocode(adresse)
    data.append((location.latitude)) 
    data.append((location.longitude))
    return data
    
m = folium.Map(location=geo(), zoom_start=20)

folium.Marker(geo(), popup='<i>hat geklappt</i>', tooltip=tooltip).add_to(m)

m.save('map.html')