import requests
from bs4 import BeautifulSoup
url ='https://www.infomoney.com.br/cotacoes/ibovespa/'


request = requests.get(url).content
soup = BeautifulSoup(request,'html.parser')
table = soup.find_all('table',class_='default-table')
positive = soup.find_all('td')

print()
#links = soup.find_all('table', id='low')

for i in positive:
     print(i)
