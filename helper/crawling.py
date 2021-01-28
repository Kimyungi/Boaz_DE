import requests
from bs4 import BeautifulSoup

class REALTIME:
    def __init__(self):
        self.url = "https://datalab.naver.com/keyword/realtimeList.naver"
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'} #http://www.useragentstring.com/

    def __call__(self):
        response = requests.get(self.url, headers = self.header)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html,'html.parser')
            rank = soup.select('span.item_num')
            trend = soup.select('span.item_title')
            data = []
            for i, j in zip(rank, trend):
                data.append([i.get_text(), j.get_text()])
        else:
            data = []
            print("ERROR!!")

        return data