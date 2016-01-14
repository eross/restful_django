import requests
from time import sleep

selector = 0
payloads=[]
payloads.append({"username":"ericr3e", "email": "eric.ross@hp.com"})
payloads.append({"username":"ericr3x", "email": "ericr@hp.com"})
for x in xrange(0,4):

	r = requests.put('http://localhost:8000/sas/users/4/',json=payloads[selector])
	if r.status_code == 200:
		print r.status_code
		print r.text
	else:
		print "status: ",r.status_code
		print "Could not update record"
		print r.text
	if selector==1:
		selector = 0
	else:
		selector = 1	
	sleep(1)
	
	
## list all users
	
r = requests.get('http://localhost:8000/sas/users/?format=json')

print "Now enumerate all the records in the database"
if r.status_code == 200:
	print r.text
	val = r.json()
	index = 0
	for rec in val:
		index = index + 1
		print rec['username'],': ',rec['email'],': ',rec['groups'],': ',rec['url']
 