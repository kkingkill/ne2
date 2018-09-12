import requests
import json

ip = "10.39.6.220"
baseurl = "http://" + ip


### Get all ports
portsurl= baseurl + "/api/hw/Ports"
portsResp = requests.get(portsurl, auth=('admin', 'admin'))
print("All ports information:")
print(json.dumps(json.loads(portsResp.text), indent=4))



### Get Port 1 information
porturl =  baseurl + "/api/hw/Port/1"
portResp = requests.get(porturl, auth=('admin', 'admin'))
print("The Port 1 information: ")
print(json.dumps(json.loads((portResp.text)), indent=4))



### Get Hardware information
hdInfo= baseurl + "/api/actions/hwInfo"
hdResp = requests.get(hdInfo, auth=('admin', 'admin'))
print("The NE2 hardware inforamtion:")
print(json.dumps(json.loads((hdResp.text)), indent=4))


### Set Port 1 new profile and set policer
porturl = baseurl + "/api/hw/Port/1"
with open("policer.json", "r") as f:
    data = json.load(f)
print(data)
port_setResp = requests.put(porturl, auth=('admin', 'admin'), data=json.dumps(data))
print(port_setResp.status_code, port_setResp.text)





