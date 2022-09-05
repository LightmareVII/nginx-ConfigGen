import jinja2
import json

myLoader = jinja2.FileSystemLoader(searchpath='./')
myEnv = jinja2.Environment(loader=myLoader)
myTemplate = myEnv.get_template('nginx-template.config')

with open('/nginx/nginxData.json', 'r+') as nginxDataFile:
    myServiceDetails = json.load(nginxDataFile)['serviceDetails']


nginxConfig = myTemplate.render(serviceDetails=myServiceDetails)

with open('/nginx/nginx.conf', 'w') as nginxConfigFile:
    nginxConfigFile.write(nginxConfig)
