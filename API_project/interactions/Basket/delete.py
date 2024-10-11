import creds 
api_key = creds.api_key

import http.client
import json

conn = http.client.HTTPSConnection("getpantry.cloud")
payload = ''
headers = {
		'Content-Type': 'application/json'
}
conn.request("DELETE", f"/apiv1/pantry/{api_key}/basket/pantry1", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))