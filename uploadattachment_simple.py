from requests_toolbelt import MultipartEncoder
import requests

filepath    = '/Users/taylorhanson/Desktop/screenshot.png'
filetype    = 'image/png'
roomId      = 'SOME ROOM'
token       = 'YOUR ACCOUNT BEARER TOKEN'
url         = "https://api.ciscospark.com/v1/messages"

my_fields={'roomId': roomId, 
           'text': 'Hello World',
           'files': (filepath, open(filepath, 'rb'), filetype)
           }
m = MultipartEncoder(fields=my_fields)
r = requests.post(url, data=m,
                  headers={'Content-Type': m.content_type,
                           'Authorization': 'Bearer ' + token})
print r.json()
