import requests
from bs4 import BeautifulSoup
import pandas as pd

team = []
for i in (1,5):
    url = f"https://www.scrapethissite.com/pages/forms/?page_name={i}.html"
    soup = requests.get(url)
    hockey = BeautifulSoup(soup.content, 'html.parser')
    tr = hockey.find('table')
    hockeyname = tr.find_all('tr', class_='team')

    for hockeynames in hockeyname:
        name = hockeynames.find('td', class_='name').text
        year = hockeynames.find('td', class_='year').text
        win = hockeynames.find('td', class_='wins').text
        lose = hockeynames.find('td', class_='losses').text
        team.append([name, year, win, lose])
df = pd.DataFrame(team, columns=['Name', 'Year', 'Win', 'Lose'])
df.to_csv('Hockey-Team.csv')
    