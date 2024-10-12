Excalidraw link: https://excalidraw.com/#json=zifzyRNAJJacAfgJrxCGI,J3gzh6nJLnwZ0sNr_m8ikg


Many files with start with this import, sys and os are used for the creds directory, and the rest are for api + json.

<blockquote>
import sys, os, http.client, json

sys.path.append(os.path.abspath('API_project'))
import creds

api_key = creds.api_key
</blockquote>
