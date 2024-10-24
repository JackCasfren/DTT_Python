import sys, os, http.client, json
sys.path.append(os.path.abspath('API_project'))
import creds
api_key = creds.api_key
"""
conn = http.client.HTTPSConnection("getpantry.cloud")
payload = ''
headers = {
		'Content-Type': 'application/json'
}
conn.request("GET", f"/apiv1/pantry/{api_key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
"""

def get_pantry_data():
    #print("get_pantry_data called")
    conn = http.client.HTTPSConnection("getpantry.cloud")
    payload = "" 
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("GET", f"/apiv1/pantry/{api_key}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    return data.decode("utf-8")

# Usage
# result = get_pantry_data("your_api_key_here")
# print(result)


def update_pantry_account( name, description):
    conn = http.client.HTTPSConnection("getpantry.cloud")
    payload = json.dumps({
        "name": name,
        "description": description
    })
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("PUT", f"/apiv1/pantry/{api_key}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

# Example usage:
# result = update_pantry_account("Name of the pantry", "Description")
# print(result)


def list_all_baskets():
    print("The baskets are:")
    data = json.loads(get_pantry_data())
    baskets = data['baskets']
    for basket in baskets:
                    print(basket)
