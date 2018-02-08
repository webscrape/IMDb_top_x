import requests
from bs4 import BeautifulSoup
import sys
import csv

url = 'http://www.imdb.com/chart/top'
x = int(sys.argv[1]) if len(sys.argv) == 2 else 10
if x<=0 or x>250:
    x = 10

response = requests.get('http://www.imdb.com/chart/top')
if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_list = soup.find('tbody', attrs={'class':'lister-list'}).find_all('tr')
    data = [['Title', 'Year', 'Rating']]
    for movie in movie_list[:x]:
        title = movie.find('td', attrs={'class': 'titleColumn'}).find('a').text
        year = movie.find('td', attrs={'class': 'titleColumn'}).find('span').text.strip('(').strip(')')
        rating = movie.find('td', attrs={'class':'imdbRating'}).text.strip()
        data.append([title, year, rating])
        print('{}, {}, {}'.format(title, year, rating))

    with open('top.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
else:
    print('Error Occurred while fetching {}'.format(url))