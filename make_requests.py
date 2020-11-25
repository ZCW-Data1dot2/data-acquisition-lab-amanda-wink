import urllib.request
import json
import time
import os

def make_request():
    offset = 0

    json_num = 0
    count = 1
    while offset < count:
        url_n = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?limit=1000&offset=' + str(offset)
        key='NOAA_TOKEN'
        token=os.getenv(key)
        header = {
            'Content-Type': 'application/json',
            'token': token,
            'Authorization': 'Bearer' + token
        }
        req = urllib.request.Request(url=url_n, headers=header)
        data = urllib.request.urlopen(req)
        final_resp = data.read()
        form = json.loads(final_resp)
        json_file = 'locations_' + str(json_num) + '.json'
        with open(json_file, 'w') as outfile:
            json.dump(form, outfile, sort_keys=True, indent=4)
        count = form['metadata']['resultset']['count']
        offset += 1000
        print("Complete " + str(json_num))
        json_num +=1
        time.sleep(1)

if __name__ == '__main__':
    make_request()

    #default=lambda o: o.__dict__