import requests 
from bs4 import BeautifulSoup 
import os
os.system("figlet WendigoScrape")
while True:
    
    url = input(">")
    response = requests.get(url) 
    soup = BeautifulSoup(response.text, 'html.parser') 
    for link in soup.find_all('a'): 
        print(link.get('href'))
