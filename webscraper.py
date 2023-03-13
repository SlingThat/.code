import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 

url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"

results = requests.get(url)

soup = BeautifulSoup(results.text, "html.parser")

titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')

for container in movie_div:

    #Name
    name = container.h3.a.text
    titles.append(name)

    #year
    year = container.h3.find('span', class_='lister-item-year').text
    years.append(year)

    #time
    runtime = container.p.find('span', class_='runtime').text if container.p.find('span', class_='runtime').text else '-'
    time.append(runtime)
    
#building out Pandas dataframe
movies = pd.DataFrame({
    'movie': titles,
    'year' : years,
    'timeMin' : time,
})

#Cleaning data with Pandas
movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
movies['timeMin'] = movies['timeMin'].str.extract('(\d+)').astype(int)


movies.to_csv('movies.csv')