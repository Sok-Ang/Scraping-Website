import requests
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen

url = 'https://www.scrapethissite.com/pages/simple/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

countries = soup.find_all('div', class_='col-md-4 country')

with open('country_data.csv', 'w', newline='') as csv_file:
    fieldnames = ['Name', 'Capital', 'Population', 'Area']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for c in countries:
        c_name = c.find('h3', class_='country-name').text.strip()
        c_capt = c.find('span', class_='country-capital').text
        c_popl = c.find('span', class_='country-population').text
        c_area = c.find('span', class_='country-area').text

        writer.writerow({'Name': c_name, 'Capital': c_capt, 'Population':c_popl, 'Area':c_area})

