import phonenumbers
import opencage
from myphone import number
import folium

from phonenumbers import geocoder

pepnumber =phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print (location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode

key='287a9c25f46a4cb2a5272ae9f069030d'

geocoder =OpenCageGeocode(key)
query =str(location)
results =geocoder.geocode(query)
print(results)

lat= results[0]['geometry']['lat']
lng= results[0]['geometry']['lng']
print(lat, lng)


myMap= folium.Map(location =[lat, lng], zoom_start=12)
folium.Marker([lat, lng], popup= location).add_to(myMap)

# myMap = folium.Map(location=[lat, lng], zoom_start=9)
#
# marker = folium.Marker([lat, lng], popup=location)
# marker.add_to(myMap)  # Correct usage

myMap.save("get_myphone_location.html")




