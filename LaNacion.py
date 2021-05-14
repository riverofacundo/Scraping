from bs4 import BeautifulSoup
import requests

url = "https://www.lanacion.com.ar"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

content_titles = soup.find_all('h2',class_='com-title')

for tit in content_titles:
  sub = tit.find_all('a')
  print(sub[0].attrs.get('title'))
  x = sub[0].attrs.get('href')
  print(x)
  response2 = requests.get(x)
  soup2 = BeautifulSoup(response2.text, "html.parser")
  contenido = soup2.find_all('div', class_= 'col-12')
  print("")
  for cont in contenido:
    sub = cont.find_all('p', class_='com-paragraph --s')
    if len(sub) == 0:
        pass
    else:
        for s in sub:
            print(s.getText())
  print("")
  print("")
  


  

