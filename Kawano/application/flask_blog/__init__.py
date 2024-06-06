'''アプリケーション本体ファイルの作成'''
#Flask事態のインポート
from flask import Flask
#SQLアルケミーのインポート
from flask_sqlalchemy import SQLAlchemy

#Flaskアプリケーション本体を作成
app = Flask(__name__)
app.config.from_object('flask_blog.config')

#db変数の設定
db = SQLAlchemy(app)

#viewsファイルのインポート
from flask_blog.views import views,entries,comments
