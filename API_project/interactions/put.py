import creds 
api_key = creds.api_key

import http.client
import json

conn = http.client.HTTPSConnection("getpantry.cloud")
payload = json.dumps({
  "name": "basket_name",
  "description": "bascket_description"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("PUT", f"https://getpantry.cloud/apiv1/pantry/{api_key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
