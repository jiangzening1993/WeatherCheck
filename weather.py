import json
import urllib.request


def getData(url):
    response = urllib.request.urlopen(url)
    html = json.load(response)
    return html


def printData(html):
    print("City:", html["name"])
    print("Country:", html['sys']['country'])
    print("Coordinate: (%f, %f)" % (html['coord']['lon'], html['coord']['lat']))
    for item in html['weather']:
        print("Weather:", item["main"])
    # print(float(html['main']['temp']))
    print("Temperature: %.1f" % ((float(html['main']['temp'])) - 273.15))
    # print("Sunrise:", html['sys']['sunrise'])
    # print("Sunset:",  html['sys']['sunset'])


city_list_file = open("city.list.json", 'rb')
city = input('Enter the city you want to check: ')
country = input('Enter the country: ')
city_list = json.load(city_list_file)
url = r'https://api.openweathermap.org/data/2.5/weather?id=%(id)s&appid=ec1005d1a4a1d28dda1bf31572014fdf'

for each in city_list:
    if city == each['name'] and country == each['country']:
        found = 1
        break
    else:
        found = 0

if found:
    print(each['name'])
    print(each['id'])
    url %= {'id': each['id']}
    printData(getData(url))
elif not found:
    print("Cannot found the city")
