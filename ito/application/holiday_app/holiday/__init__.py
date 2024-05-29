from flask import Flask

app = Flask(__name__)
app.config.from_object('holiday.config')

import holiday.views