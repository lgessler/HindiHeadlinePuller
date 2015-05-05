import requests
from bs4 import BeautifulSoup as BS

url = "http://www.bbc.co.uk"

r = requests.get(url + '/hindi')
soup = BS(r.text)

#divs = soup.find_all('div', {'class':'hard-news-unit__body'})
divs = soup.find_all('h3', {'class':'hard-news-unit__headline'})

#`print divs[0],type(divs)


for div in divs:
    article = div.find_all('a')[0]['href']
    link = url + article 
    print(("<a href=%s><h1>" + div.find_all('a')[0].contents[0].strip() + "</h1></a>") % link)

