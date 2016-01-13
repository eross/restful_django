import requests

r = requests.get('http://localhost:8000/sas/users/?format=json')
if r.status_code == 200:
	print r.text
	val = r.json()
	index = 0
	for rec in val:
		index = index + 1
		print rec['username'],': ',rec['email'],': ',rec['url']
 
payload = {'username':'ericr3', 'email': 'xyz@contosu.com', 'groups': [u'http://localhost:8000/sas/groups/1/?format=json']}

#r = requests.post('http://localhost:8000/sas/users/',json=payload)
#print r.status_code
#print r.text

payload = {
    "url": "http://localhost:8000/sas/users/4/",
    "username": "ericr3",
    "email": "xyz@contosu.com",
    "groups": [
        "http://localhost:8000/sas/groups/1/"
    ]
}
#payload = {"username":"ericr3b"}
r = requests.put('http://localhost:8000/sas/users/4',json=payload)
print r.status_code
print r.text