import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php'

names = json.loads(open('names.json').read())
lastnames = json.loads(open('lastnames.json').read())
emaildomains = json.loads(open('emails.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + lastnames[random.randint(0,1000)].lower() + name_extra + '@' + emaildomains[random.randint(0,100)].lower()
	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects=False, data={
		'auid2yjauysd2uasdasdasd': username,
		'kjauysd6sAJSDhyui2yasd': password
	})

	print ("sending username {un} and password {pw}".format(un=username, pw=password))
