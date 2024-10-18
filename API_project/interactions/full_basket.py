import sys, os, http.client, json
sys.path.append(os.path.abspath('API_project'))
import creds
api_key = creds.api_key




def get_basket_data(basket_name):
    conn = http.client.HTTPSConnection("getpantry.cloud")
    payload = "" 
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("GET", f"/apiv1/pantry/{api_key}/basket/{basket_name}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    #print(data.decode("utf-8"))
    return data.decode("utf-8")
    
# To use the function:
# result = get_basket_data()
# print(result)



#insert data in to basket
def make_pantry_insert(sel_pantry, new_data):
    conn = http.client.HTTPSConnection("getpantry.cloud")
    payload = json.dumps(new_data)
    # it was originaly like this, i think its going to give some errors, so just in case im storing it.
    """ 
    payload = json.dumps({
        "derp": "flerp123",
        "testPayload": True,
        "keysLength": 3
    })
    """
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("POST", f"/apiv1/pantry/{api_key}/basket/{sel_pantry}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    return data.decode("utf-8")


def update_pantry_basket( basket_name, new_data):
    conn = http.client.HTTPSConnection("getpantry.cloud")
    payload = json.dumps(new_data)
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("PUT", f"/apiv1/pantry/{api_key}/basket/{basket_name}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

# Example usage:
# basket_name = "YOUR_BASKET_NAME"
# new_data = {"newKey": "newValue"}
# response = update_pantry_basket(api_key, basket_name, new_data)
# print(response)


# deletes entire basket
def delete_pantry_basket(basket_name):
    conn = http.client.HTTPSConnection("getpantry.cloud")
    payload = ''
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("DELETE", f"/apiv1/pantry/{api_key}/basket/{basket_name}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

