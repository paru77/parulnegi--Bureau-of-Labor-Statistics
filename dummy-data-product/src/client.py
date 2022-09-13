import pandas as pd
from bs4 import BeautifulSoup as bs

import requests as r

data = r.get("https://www.bls.gov/")
# url of data
print(data.url)
a = data.content

# parsing html
par = bs(a, "html.parser")
print(par.prettify())

s = par.find('body')
# printing all anchor tags
for i in s.find_all('a'):
    print(i.get('href'))

# scrapping history page
par1 = r.get('https://www.bls.gov/bls/history/home.htm')
print(par1.url)
s = bs(par1.content, 'html.parser')
his = s.find('div', class_='bls--history')
p = his.find_all('p')
# history of the US labor statistics website
print("History")
for i in p:
    print(i.text)

# scraping leadership page

leader = r.get('https://www.bls.gov/bls/senior_staff/home.htm')
print("The URL of Leadership Website Is : ", leader.url)

n = bs(leader.content, 'html.parser')
de = n.find('div', class_='bls--senior-staff')
print("Names of leaders")
for i in de.find_all('span', class_='orgname'):
    print(i.text)
