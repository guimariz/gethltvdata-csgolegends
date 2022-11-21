import requests
from bs4 import BeautifulSoup
import json
import time

def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}

    return BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

def getPlayer(url, startDate='2021-04-12', endDate='2021-05-08'):

    soup = get_data(f'{url}?startDate={startDate}&endDate={endDate}')    

    print(url)

    nomeJogador = soup.find("img",{"class":"summaryBodyshot"})  
    teamLogo = soup.find('img',{"class":"team-logo"})
    playerImg = soup.find("img",{"class":"summaryBodyshot"})

    if nomeJogador:
        nomeJogador = nomeJogador["title"]
    elif soup.find("img",{"class":"summaryBodyshotContainer"}):
        nomeJogador = soup.find("img",{"class":"summaryBodyshotContainer"})["title"]
    else:
        nomeJogador = soup.find("img",{"class":"summarySquare"})["title"]
    
    if teamLogo:
        teamLogo = teamLogo["src"]
    else:
        teamLogo = "Sem time"
        print("Não tem time!")

    if playerImg:
        playerImg = playerImg["src"]
    elif soup.find("img",{"class":"summaryBodyshotContainer"}):
        playerImg = soup.find("img",{"class":"summaryBodyshotContainer"})["src"]        
    else:
        print(nomeJogador)
        playerImg = "nao tem foto"
        print("nao achou nada!")

    return {'nomeJogador': nomeJogador, 'teamLogo': teamLogo, 'playerImg': playerImg}

player = ["https://www.hltv.org/stats/players/11893/zywoo",
          "https://www.hltv.org/stats/players/7998/s1mple",
          "https://www.hltv.org/stats/players/16920/sh1ro",
          "https://www.hltv.org/stats/players/9216/coldzera",
           "https://www.hltv.org/stats/players/2023/fallen",
          "https://www.hltv.org/stats/players/15631/kscerato"]

todos = [getPlayer(play) for play in player]

def write_file(file_name, todos):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(todos)
    file.close()

write_file('fotosJogador.json', json.dumps(todos))
