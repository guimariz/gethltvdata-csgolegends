import requests
from bs4 import BeautifulSoup
import json
import time

def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}

    return BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')


def getPlayer(url, startDate='2022-10-26', endDate='2022-11-02'):
    soup = get_data(
        f'{url}?startDate={startDate}&endDate={endDate}')
    player = soup.find('h1').text

    ratings = [rating.text for rating in soup.find_all(
        'div', {'class': 'summaryStatBreakdownDataValue'})]

    playersStats = {}

    for stat in soup.find_all(
            'div', {'class': 'stats-row'}):
        spans = stat.find_all('span')
        playersStats[spans[0].text] = spans[1].text

    def formatText(i):
        spans = i.find_all('span')
        return {'pais': i.find('img')[
            'title'], 'nome': spans[0].text, 'rating': spans[1].text}

    teams = [formatText(team) for team in soup.find_all(
        'div', {'class': 'teammate-info'})]

    print(f'{player} success.')

    time.sleep(3)
    return {'player': player, 'ratings': ratings, 'playersStats': playersStats, 'teams': teams}

players = ["https://www.hltv.org/stats/players/11893/zywoo",
          "https://www.hltv.org/stats/players/7998/s1mple",
          "https://www.hltv.org/stats/players/16920/sh1ro",
          "https://www.hltv.org/stats/players/9216/coldzera",
           "https://www.hltv.org/stats/players/2023/fallen",
          "https://www.hltv.org/stats/players/15631/kscerato"
         ]

playersStats = [getPlayer(p) for p in players]

def write_file(file_name, todos):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(todos)
    file.close()

write_file('playersStats.json', json.dumps(playersStats))
