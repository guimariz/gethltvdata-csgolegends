import requests
from bs4 import BeautifulSoup
import json
import time


def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}

    return BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

def getPlayer(url, startDate='2022-10-26', endDate='2022-11-02'):
    soup = get_data(f'{url}?startDate={startDate}&endDate={endDate}')    

    print(url)

    teamLogo = soup.find("img",{"class":"context-item-image"})["src"]

    players = [i["title"] for i in soup.find_all("img",{"class":"container-width teammate-player-image"})]
    playerImg = [i["src"] for i in soup.find_all("img",{"class":"container-width teammate-player-image"})]
    
    print(players)
    
    return {'players': players, 'playerImg': playerImg, 'teamLogo': teamLogo}

player = ["https://www.hltv.org/stats/teams/8297/furia",
"https://www.hltv.org/stats/teams/5995/g2",
"https://www.hltv.org/stats/teams/6667/faze",
"https://www.hltv.org/stats/teams/4608/natus-vincere",
"https://www.hltv.org/stats/teams/9455/imperial",
"https://www.hltv.org/stats/teams/11309/00nation"]

todos = [getPlayer(play) for play in player]

def write_file(file_name, todos):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(todos)
    file.close()

write_file('allTeams.json', json.dumps(todos))
