Excalidraw link: https://excalidraw.com/#json=zifzyRNAJJacAfgJrxCGI,J3gzh6nJLnwZ0sNr_m8ikg


Many files with start with this import, sys and os are used for the creds directory, and the rest are for api + json.

<blockquote>
import sys, os, http.client, json

sys.path.append(os.path.abspath('API_project'))
import creds

api_key = creds.api_key
</blockquote>


This is what the json now looks like, previous versions might be diferent.
But thanks to the non relatable nature of json we can afford to make multiple diferent iterations.
<blockquote>
{
  "company": {
    "name": "Microsoft",
    "product": "Windows10",
    "logo": {
      "main_color": "blue",
      "Logo_shape": "window"
    },
    "industry": "Software",
    "usage": "Cloud",
    "additional_features": []
  }
}
</blockquote>


