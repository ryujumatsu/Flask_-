#本体ファイル(Flaskのインポート、アプリケーション本体の作成)
from flask import Flask
app=Flask(__name__)

#ビューファイル(中身を書くもの)
@app.route('/')
def hello_world(): #サーバーサイドに実行させたい処理の関数
    return "Hello World!"

#起動ファイル
if __name__=='__main__':
    app.run()
