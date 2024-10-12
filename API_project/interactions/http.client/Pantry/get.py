import sys, os, http.client, json
sys.path.append(os.path.abspath('API_project'))
import creds
api_key = creds.api_key

conn = http.client.HTTPSConnection("getpantry.cloud")
payload = ''
headers = {
  'Content-Type': 'application/json'
}
conn.request("GET", f"https://getpantry.cloud/apiv1/pantry/{api_key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))