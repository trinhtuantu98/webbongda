from flask import Flask, render_template
from datetime import datetime,timedelta
import pymongo
from models.db import client
from models.db import get_all,match_this_week
thisweek=match_this_week()

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('bongda.html',thisweek=thisweek)

@app.route('/lineup/<tendoi>')
def lineup(tendoi):
  data = {}
  db = client.Allteam
  p = db.lineup.find()
  for v in p:
    if v['Đội'] == tendoi:
          data = v
  return render_template('lineup.html',data=data)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=False)
