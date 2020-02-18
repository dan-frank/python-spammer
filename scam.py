import requests
import os
import random
import string
import json

random.seed = (os.urandom(1024))

url = 'http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php'

names = json.loads(open('names.json').read())
lastnames = json.loads(open('lastnames.json').read())
emaildomains = json.loads(open('emails.json').read())

def getFirstName():
    i = random.randint(0, (len(names) - 1))
    return names[i].lower()

def getLastName():
    i = random.randint(0, (len(lastnames) - 1))
    return lastnames[i].lower()

def getEmailDomain():
    i = random.randint(0, (len(emaildomains) - 1))
    return '@' + emaildomains[i].lower()

def getDigits(amountOf):
    digits = ''

    for i in range(0, amountOf):
        digit = ''.join(random.choice(string.digits))
        digits = digits + digit

    return digits

def getUsername():
    username = ''
    i = random.randint(0, 7)

    # selects random character combination
    if i == 0:
        username = getFirstName() + getLastName()
    elif i == 1:
        username = getFirstName() + '.' + getLastName()
    elif i == 2:
        username = getFirstName() + "_" + getLastName()
    elif i == 3:
        username = getLastName() + "-" + getLastName()
    elif i == 4:
        username = getLastName() + getFirstName()
    elif i == 5:
        username = getLastName() + "." + getFirstName()
    elif i == 6:
        username = getLastName() + "_" + getLastName()
    elif i == 7:
        username = getLastName() + "-" + getLastName()

    digits = random.randint(0, 3)
    username = username + getDigits(digits)

    username = username + getEmailDomain()
    return username

def main():
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    
    for name in names:
    	username = getUsername()

    	password = ''.join(random.choice(chars) for i in range(8))

    	requests.post(url, allow_redirects=False, data={
    		'auid2yjauysd2uasdasdasd': username,
    		'kjauysd6sAJSDhyui2yasd': password
    	})

    	print ("sending username {un} and password {pw}".format(un=username, pw=password))

main()