from flask_blog import app

if __name__=='__main__': #このファイルが直接実行されたかどうかを判別する条件式(このファイルがモジュールとして外部から実行されると__name__の中身が変わる)
    app.run()  