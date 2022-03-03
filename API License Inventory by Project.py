from blackduck import Client
import logging
import re
from collections import Counter
import csv

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(module)s:%(lineno)d} %(levelname)s - %(message)s"
)

# Please modify the token and base_url
bd = Client(
    token="MTNmNDY0NzItNGVjNS00Yzg0LgE5NWEtOWRaYzg3fzRjMjQtOmY1ZjRhMjM0LWZlZDUtNDliNC05NzkxLWUyY2JiNTk0Y2UyOA==",
    base_url="https://localhost",
    verify=False  # TLS certificate verification
)

lic_list = []

# Get license and ID
def extract_details(lic_item):
    lic_ID = re.findall(r"licenses\/(.*$)",lic_item['license'])
    return (lic_item['licenseDisplay'],  lic_ID[0])

# Query projects
for project in bd.get_resource(name='projects'):
    prj_name = project.get('name')
    # Please modify project names
    if prj_name in ["chanp_JavaSecCode","chanp_insecure_bank"]:
        print("Processing Project:",prj_name)
        for version in bd.get_resource('versions', project):
            print("Processing Version:",version['versionName'])
            for component in bd.get_resource('components', version):
                for license in component['licenses']:
                    # If there is dual or multi licenses
                    if len(license['licenses'])>0:
                        for multi_lic in license['licenses']:
                            lic_list.append(extract_details(multi_lic))
                    # Otherwise
                    else:
                        lic_list.append(extract_details(license))

lic_cnt = Counter(lic_list)
results = {}

print("Outputing",len(lic_cnt),"licenses")

# Get license terms
for (key, value) in lic_cnt.items():
    licenseTerms = bd.get_json(bd.base_url+'/api/licenses/'+key[1]+'/license-terms')['items']
    LT = []
    for licenseTerm in licenseTerms:
        LT.append(licenseTerm['name']+"="+licenseTerm['responsibility'])
    results[(key[0],' '.join([str(elem) for elem in LT]))] = value

# Output as CSV             
with open('license_inventory.csv','w', newline='') as csvfile:
    fieldnames=['License','License Terms','count']
    writer=csv.writer(csvfile)
    writer.writerow(fieldnames)
    for key, value in sorted(results.items(), key=lambda x: x[1], reverse=True):
        writer.writerow(list(key) + [value]) 
print("All done")