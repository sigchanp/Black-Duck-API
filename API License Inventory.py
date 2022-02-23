#!/usr/bin/env python
# coding: utf-8

# https://github.com/blackducksoftware/hub-rest-api-python
# pip3 install blackduck

from blackduck import Client
import logging
import os
import csv

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(module)s:%(lineno)d} %(levelname)s - %(message)s"
)

bd = Client(
    token=os.environ.get('blackduck_token'),
    base_url="https://localhost",
    verify=False  # TLS certificate verification
)

params = {
    'filter': ["inUse:true"], # show only licenses that are found in scan
    'limit' : 1000 # max license number in a single download
}

# Connect to the license dashboard endpoint
print("Processing licenses...")
items = bd.get_json("/api/license-dashboard",params=params)['items']
print("Detected",len(items),"licenses...")
results = []

# iterate all licenses
for item in items:
    licenseTerms = bd.get_json(item['_meta']['href']+'/license-terms')['items']
    LT = []
    # iterate all license terms
    for licenseTerm in licenseTerms:
        LT.append(licenseTerm['name']+"="+licenseTerm['responsibility'])
    results.append([item['name'], item['bomComponentCount'], LT])

with open('licenses.csv', 'w', newline='') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(['License','Component Count','License Terms'])
    write.writerows(results)
f.close()

print("All Done, exported",len(results),"licenses")

