'''アプリケーション本体ファイルの作成'''
#Flask事態のインポート
from flask import Flask
#Flaskアプリケーション本体を作成
app = Flask(__name__)
app.config.from_object('salary.config')
#viewsファイルのインポート
import salary.views
