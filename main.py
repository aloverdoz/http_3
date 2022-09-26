import requests
from bs4 import BeautifulSoup

perem = []
date_up = []
count = True
while count:
    url = f'https://stackoverflow.com/questions/tagged/python?tab=newest&page={count}&pagesize=15'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('a', class_='s-link')
    a = str(quotes)
    start = a.split('<a class="s-link"')
    start.remove(start[0])
    for i in start:
        aa = i.split('">')
        for ii in aa:
            if '</a>, ' in ii:
                god = ii.replace('</a>, ', '')
                perem.append(god)
    quotes2 = soup.find_all('span', class_='relativetime')
    a2 = str(quotes2).split('</span>')
    for i in a2:
        up = i.split('">')
        for i in up:
            if 'ago' in i:
                date_up.append(i)
    if '2 days ago' in date_up:
        count = False

print(perem)
print(date_up)
