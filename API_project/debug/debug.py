import sys, os, http.client, json
sys.path.append(os.path.abspath('API_project'))
import creds
api_key = creds.api_key

try:
    # Create a connection to a website
    connection = http.client.HTTPConnection("www.example.com")
    
    # Send a GET request
    connection.request("GET", "/")
    
    # Get the response
    response = connection.getresponse()
    
    # Print the response status and reason
    print("Status:", response.status)
    print("Reason:", response.reason)
    
    # Close the connection
    connection.close()

    print("http.client works!")
except Exception as e:
    print("Error:", e)
