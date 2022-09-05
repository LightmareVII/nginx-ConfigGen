import os
import json
import shutil

myFolders = os.listdir('/nginx/certs/')

with open('/nginx/nginxData.json', 'r+') as nginxDataFile:
    serviceList = [service['subDomain'] for service in json.load(nginxDataFile)['serviceDetails']]

print('myFolders', myFolders)
print('serviceList', serviceList)

for service in serviceList:
    if service in myFolders:
        pass
    else:
        os.makedirs(f'/nginx/certs/{service}/')
        shutil.copyfile('/nginx/certs/default/cert1.pem', f'/nginx/certs/{service}/cert1.pem')
        shutil.copyfile('/nginx/certs/default/chain1.pem', f'/nginx/certs/{service}/chain1.pem')
        shutil.copyfile('/nginx/certs/default/fullchain1.pem', f'/nginx/certs/{service}/fullchain1.pem')
        shutil.copyfile('/nginx/certs/default/privkey1.pem', f'/nginx/certs/{service}/privkey1.pem')
#