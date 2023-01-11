from flask_sqlalchemy import SQLAlchemy
from multiprocessing.util import debug
from flask import Flask
from markupsafe import escape
from winmagic import magic
import threading, random, datetime
from paho.mqtt import client as mqtt_client
import sub



app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = "a csrf secret key"


if __name__ == "__main__":
    mqtt_thread = threading.Thread(target=sub.run)
    mqtt_thread.daemon = True
    mqtt_thread.start()
    app.run(host="0.0.0.0", port="7000", debug=False)