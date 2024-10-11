import creds 
api_key = creds.api_key

import http.client
import json

pantry = "pantry1"


conn = http.client.HTTPSConnection("getpantry.cloud")
payload = json.dumps({
  "newKey": "newValue"
})
headers = {
		'Content-Type': 'application/json'
}
conn.request("PUT", f"/apiv1/pantry/{api_key}/basket/YOUR_BASKET_NAME", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))