import httpx
from bs4 import BeautifulSoup
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"
response = httpx.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
jobs = []

divcon = soup.find('div', class_='columns')
title = divcon.find_all(class_='card-content')

for titles in title:
    job = titles.find(class_='title').text
    subtitle = titles.find(class_='subtitle').text
    place = titles.find(class_='location').text

    # titles.writerow({'Job-Name': titles, 'HR': subtitle, 'Location': place})
    jobs.append([job, subtitle, place])

df = pd.DataFrame(jobs, columns=['Title', 'HR', 'Location'])
df.to_csv('jobs.csv')