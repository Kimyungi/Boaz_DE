import pymysql
from crawling import REALTIME

class DB_HELPER():
    def __init__(self, host = '13.209.6.72', user = 'test', passwd = 'qkqhdi12', db = 'testdb'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.data = REALTIME()

    def read_tables(self, dbname='testdb', table_name = 'soo2'):
        connection = pymysql.connect(
                    host = self.host,
                    user = self.user,
                    passwd = self.passwd,
                    db= self.db,
                    charset = 'utf8'
                )        
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM {};".format(table_name)
        cursor.execute(sql)
        result = cursor.fetchall()
        connection.close()

        return result
    
    def update_tables(self, dbname='testdb', table_name = 'news'):
        connection = pymysql.connect(
                    host = self.host,
                    user = self.user,
                    passwd = self.passwd,
                    db= self.db,
                    charset = 'utf8'
                )
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "DELETE FROM soo2;"
        cursor.execute(sql)

        sql = "INSERT INTO soo2 (rt_rank, trend) Values (%s, %s)"
        val = [(int(key), value) for key, value in self.data()]

        cursor.executemany(sql, val)

        connection.commit()
        connection.close()