'''アプリケーション本体ファイルの作成'''
from flask_sqlalchemy import SQLAlchemy
#Flask事態のインポート
from flask import Flask
#Flaskアプリケーション本体を作成
app = Flask(__name__)
app.config.from_object('holiday.config')

#db変数の設定
db = SQLAlchemy(app)

#viewsファイルのインポート
from holiday.views import input,list,maintenance_date