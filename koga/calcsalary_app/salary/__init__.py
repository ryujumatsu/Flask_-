from flask import Flask

app=Flask(__name__)
app.config.from_object('salary.config') #コンフィグの有効化

import salary.views
