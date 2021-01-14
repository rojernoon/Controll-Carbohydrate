import logging
import os

from lib import carbohydrate
from flask import Flask,render_template 

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/mypage")
def mypage():
    db = carbohydrate.database()
    res = db.search_foods(20)
    message = res
    return render_template("mypage.html", message=message)

@app.route("/food-list", methods=["GET"])
def foodlist():
    db = carbohydrate.database()
    res = db.show_all_foods()
    message = res
    return render_template("foodlist.html", message=message)


def main():
    app.run(host='127.0.0.1', port=5000)


if __name__ == "__main__":
    main()

