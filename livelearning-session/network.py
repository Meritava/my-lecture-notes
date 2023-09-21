#TUESDAY LECTURE 8th Aug
#type json python package on google
"""
#Dictionary in python
key:value pairs
student = {'name': 'merit', 'age': 25, 'height': 5}
print(student['name'])
len(student)
JSON is different from a dictionary by the quotation that encloses it....
Jsn is a lite way/weigt of transferring data from a clien to a server or between clients, it provide a light/lite weight method of transferring data
import json
json.dumps(student)   #this converts the dictionary to a json file
"""
student = {'name': 'merit', 'age': 25, 'height': 5}
print(student['name'])
len(student)
import json
json.dumps(student)   #this converts the dictionary to a json file
stringified = json.dumps(student)
stringified
stringified['name']  #it will not print, so you have to convert back to object/dictionary before it can print
parsed = json.loads(stringified)   #converters back to dictionary/object
parsed
parsed['name']  #it works
"""
HTTP is a set of rules between two communication parties. It enables you to communicate with client server application
HTTP is the Request and the Response
URL - Uniform Resource Locator: it is use to uniquely identify a resource over the web
URI indentifies a resource on the server
Request have:
-headers
-preview
-text
-content
-status_code
and others
"""
# httpbin.org
#pip allows you to install python packages on your environment. type pip o your terminal and see how it works
#pip install requests, will install request for you
"""
what to do
network > on the header click the first line 
-pip install requests
--import requests
--request = request.get("https://"intranet.alxswe.com)
--dir(request)
check snapped suff
-request.url
-request.status_code
-request.reason
-request.links
-request.text
-request.headers
-request.headers['X-Request-Id']
#search google for starwars api
-after the second snap
--req = requests.get('https://swapi.dev/api/people/1')
--req.status_code
--req json()
--req = requests.get('https://swapi.dev/api/people/45')
-req.json()  - to see the outcome
#after plenty snap
first task
-import requests
-req = requests.get("pass the url here")  the req is a variable you created
-dir(req)   this is to know what is inside the url
-req.text this is to know the type of request that came out
-type(req.text)  to see the type of data that came out
-req.headers - to see the headers
-request.headers['X-Request-Id']
dir(req) - to see the content of the rquest
req.url
"""
