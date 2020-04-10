import requests
import json

def get_all_borough_pos_data(url):
    res = requests.get(url)
    return res.json()["data"]

def get_local_authorities_data(loc, all_data):
    area_data = json.loads(all_data[0]["area"])
    print(json.loads(all_data[0]["area"])[0])


if __name__ == '__main__':
    url = 'https://api.covid19uk.live/'
    res = get_all_borough_pos_data(url)
    get_local_authorities_data('',res)