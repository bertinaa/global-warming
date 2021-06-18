from flask import Flask, render_template, request
import random
import json
import yfinance as yf
import datetime
import math

app = Flask(__name__)
PORT = 3009


@app.route("/", methods=["GET", "POST"])
def startpy():

    return render_template("index.html")


@app.route("/get/output", methods=["GET", "POST"])
def get_profit_by_price():

    ticker = request.values.get("ticker")
    price = request.values.get("amount")

    stock = yf.Ticker(ticker)
    price = int(price)
    start = datetime.datetime(2021, 1, 4)
    end = datetime.datetime(2021, 1, 17)

    history = stock.history(start=start, end=end)

    history.reset_index(drop=True, inplace=True)

    start_price = history['Close'].iloc[0]
    end_price = history['Close'].iloc[-1]

    if(start_price > price):
        return None

    units = price // start_price

    # print("No of shares ",units)

    profit = end_price-start_price

    total_profit = profit * units

    # return total_profit
    return render_template("index.html", result=total_profit)


@app.route("/game", methods=["GET", "POST"])
def startpy2():

    return render_template("game.html")


@app.route("/game/output", methods=["GET", "POST"])
def get_profit_by_price_2():

    ticker1 = request.values.get("ticker1")
    price1 = request.values.get("amount1")
    ticker2 = request.values.get("ticker2")
    price2 = request.values.get("amount2")

    profit1 = get_profit(ticker1, price1)
    profit2 = get_profit(ticker2, price2)

    total_profit = profit1 + profit2

    # result = {
    #     'profit 1' : profit1,
    #     'profit 2' : profit2
    # }

    # return total_profit
    return render_template("game.html", result=total_profit)


def get_profit(ticker, price):

    stock = yf.Ticker(ticker)
    price = int(price)

    start = datetime.datetime(2021, 1, 4)
    end = datetime.datetime(2021, 1, 17)

    history = stock.history(start=start, end=end)

    history.reset_index(drop=True, inplace=True)

    start_price = history['Close'].iloc[0]
    end_price = history['Close'].iloc[-1]

    if(start_price > price):
        return None

    units = price // start_price

    # print("No of shares ",units)

    profit = end_price-start_price

    total_profit = profit * units

    return total_profit


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
