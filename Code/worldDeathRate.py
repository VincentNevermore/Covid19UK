import pycountry
import requests
import json
from datetime import date
today = date.today()
countries_info ={'items':[]}

for i in range(len (pycountry.countries)):
    country_name =list(pycountry.countries)[i].name
    country_name_alpha3Code = list(pycountry.countries)[i].alpha_3
    # Call OxfordUni api to get death and confirmed case data
    res = requests.get('https://covidtrackerapi.bsg.ox.ac.uk/api/stringency/actions/'+ country_name_alpha3Code +'/'+today.strftime("%Y-%m-%d"))
    # Ignore no data countries in the word
    if 'deaths' not in res.json()["stringencyData"]:
        continue
    if res.json()["stringencyData"]['deaths'] is None:
        continue

    country_info = {
        'Country': country_name,
        'Alpha3Code': country_name_alpha3Code,
        'Death': res.json()["stringencyData"]['deaths'],
        'Confirmed': res.json()["stringencyData"]['confirmed'],
        'DeathRate': "%.2f%%" % (res.json()["stringencyData"]['deaths']/res.json()["stringencyData"]['confirmed'] * 100)
    }
    countries_info['items'].append(country_info)

with open('../Data/worldwideData.json', 'w') as json_file:
    json.dump(countries_info, json_file)

