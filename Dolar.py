from bs4 import BeautifulSoup
import requests

url = "https://www.dolarhoy.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

div = soup.find_all('div',class_='val')

print('::::::DOLAR HOY::::::')
print('DÓLAR BLUE')
print(f"Compra: {div[0].getText()} Venta: {div[1].getText()}")
print("----------------------------------------------------")
print('DÓLAR OFICIAL PROMEDIO')
print(f"Compra: {div[4].getText()} Venta: {div[5].getText()}")
print("----------------------------------------------------")
print('DÓLAR BOLSA')
print(f"Compra: {div[6].getText()} Venta: {div[7].getText()}")
print("----------------------------------------------------")
print('CONTADO CON LIQUI')
print(f"Compra: {div[8].getText()} Venta: {div[9].getText()}")
print("----------------------------------------------------")
print('DÓLAR SOLIDARIO')
print(f"Venta: {div[10].getText()}")