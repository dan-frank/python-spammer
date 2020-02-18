import requests
import os
import random
import string
import json

random.seed = (os.urandom(1024))

names = json.loads(open('json/names.json').read())
lastnames = json.loads(open('json/lastnames.json').read())
emaildomains = json.loads(open('json/emails.json').read())
nouns = json.loads(open('json/nouns.json'). read())

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

def getNoun():
    i = random.randint(0, (len(nouns) - 1))
    return nouns[i].lower()

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

    # add digits to end of username
    digits = random.randint(0, 3)
    username = username + getDigits(digits)

    username = username + getEmailDomain()
    return username

def getPassword():
    password = ''
    option = random.randint(0, 3)

    chars = string.ascii_letters + string.digits + '!@#$%^&*()'

    # generates random string 
    if option == 0:
        password = ''.join(random.choice(chars) for i in range(14))
    # generates realistic password from top 100 most common nouns
    else:
        amountOf = random.randint(1,3)
        for i in range(0, amountOf):  
            password = password + getNoun()
        password.capitalize()

    # add digits to end of password
    digits = random.randint(1, 4)
    password = password + getDigits(digits)

    return password

def main():
    url = 'http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php'

    for name in names:
    	username = getUsername()
    	password = getPassword()

    	requests.post(url, allow_redirects=False, data={
    		'auid2yjauysd2uasdasdasd': username,
    		'kjauysd6sAJSDhyui2yasd': password
    	})

    	print ("sending username {un} and password {pw}".format(un=username, pw=password))

main()
