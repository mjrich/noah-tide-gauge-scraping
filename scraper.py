#!/usr/bin/env python
import httplib2
import json
import csv



data = []
station_list = []
with open('station_all.json') as f:
    for line in f:
        data.append(json.loads(line))

for item in data[0]['td']:
    station_list += [(item)]

print station_list

def write_to_file(full_data):
    with open("output.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(full_data)


def parse_results(content):
    full_data = []
    td_data = json.loads(content)
    #print td_data
    #full_data = [(td_data['station']['lat']),(td_data['station']['lng']),(td_data['station']['verbose_name']),(td_data['station']['station_id'])]
    for i,item in enumerate(td_data['time']):
        full_data += [[td_data['station']['lat'],td_data['station']['lng'],td_data['station']['verbose_name'],td_data['station']['station_id'],item, td_data['series'][0]['values'][i]]]
    #print full_data
    return write_to_file(full_data)


def page_load(url): #function to scrape websites
    h = httplib2.Http(".cache")

    response, content = h.request(url, "GET")
    return parse_results(content)

url = 'http://noah.dost.gov.ph/td/campomanesbay_td/'

page_load(url)
 


