from flask import Flask, render_template
import sys
sys.path.insert(0, "../helper/")
sys.path.insert(0, '/var/www/flaskapp/helper')
sys.path.insert(0, "../templates/")
from db_helper import DB_HELPER
import time

now = time.gmtime(time.time())
db = DB_HELPER()
app = Flask(__name__) ## 플라스크를 생성하고 app 변수에 flask 초기화 하여 실행

@app.route("/") # 사용자에게 ( ) 에 있는 경로를 안내 해준다고 생각하면 쉬움
def show():
    try:
        db.create_tables()
    except:
        pass
    db.update_tables()
    while 1:
        min = now.tm_min
        if min != min:
            db.update_tables()
        result = {}
        for i in range(1, 21):
            result[i] = db.read_tables()[i-1]['trend']
        
        return render_template("index.html", result = result)
