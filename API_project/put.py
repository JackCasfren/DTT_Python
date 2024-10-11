import creds api_key = creds.api_key

import requests
import json

url = f"https://getpantry.cloud/apiv1/pantry/{api_key}"

payload = json.dumps({
  "name": "Postman_Account_Updated",
  "description": "Postman test account updated"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
