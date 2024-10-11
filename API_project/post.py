import http.client
import json

import creds
api_key = creds.api_key

conn = http.client.HTTPSConnection("getpantry.cloud")
payload = json.dumps({
  "name": "Postman_Account_Updated",
  "description": "Postman test account updated"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("PUT", f"/apiv1/pantry/{api_key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))