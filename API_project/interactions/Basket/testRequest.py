import sys, os, http.client, json
sys.path.append(os.path.abspath('API_project'))
import creds
api_key = creds.api_key


import requests
import json

url = f"https://getpantry.cloud/apiv1/pantry/{api_key}"

payload = ""
headers = {
  'Content-Type': 'application/json'
}