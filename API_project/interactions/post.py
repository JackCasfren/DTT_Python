import creds api_key = creds.api_key

import requests
import json

url = f"https://getpantry.cloud/apiv1/pantry/{api_key}"

payload = ""
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
