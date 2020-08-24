""" Astrological Sign Prediction
API View

By Broken
August 2020 """
from flask import Flask, jsonify
from dmvc.controller import Bot


__all__ = ('API',)
API = Flask(__name__)
API.bot = Bot()


@API.route('/')
def index():
    """ Returns a random astrological sign """
    return jsonify(API.bot.random())


@API.route('/<user_input>')
def search(user_input: str):
    """ Predicts astrological sign based on natural language input """
    return jsonify(API.bot.search(user_input))


@API.route('/sign/<user_input>')
def sign(user_input: str):
    """ Returns the details for a given astrology sign """
    return jsonify(API.bot.sign_lookup(user_input))


if __name__ == '__main__':
    API.run(debug=True)
