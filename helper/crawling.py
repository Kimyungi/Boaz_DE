import requests
from bs4 import BeautifulSoup
from pyspark.sql import SparkSession
from db_helper import DB_HELPER
import os
os.environ["JAVA_HOME"] = "/usr/bin/jvm/java-1.8.0-openjdk-1.8.0.282.b08-2.el8_3.x86_64"

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

class SPARKINPUT:
    def __init__(self):
        self.session = SparkSession.builder.master().getOrCreate()
        self.db = DB_HELPER()

    def __call__(self, data):
        data = self.session.createDataFrame(data, schema=['rt_rank', 'trend'])
        data = data.take(10)
        print(data)
        self.db.update_tables(dbname='testdb', table_name = 'news', data = data)


if __name__== "__main__":
    real = REALTIME()
    crwaled_data = real()
    print(crwaled_data)
    spark = SPARKINPUT()
    spark(crwaled_data)
