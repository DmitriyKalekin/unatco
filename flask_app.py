from flask import Flask, request, jsonify
import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
from config import *
from game import Game

app = Flask(__name__)
game = Game()

# ---------------------------------------------------------  TELEGRAM ----------------------------------------
def tele_send_message(chat_id, text='bla-bla'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()

@app.route('/set_wh', methods=['POST', 'GET'])
def tele_set_wh():
    print("Setting: wh")
    url = URL + "setWebhook?url=" + WH_URL
    print(url)
    r = requests.get(url)
    return str(r.json())

@app.route('/del_wh', methods=['POST', 'GET'])
def tele_del_wh():
    r = requests.get(URL + "deleteWebhook")
    return str(r.json())

@app.route('/wh', methods=['POST', 'GET'])
def web_hook():
    if request.method=='POST':
        try:
            r = request.get_json()
            ans = game.make_move(r["message"]["chat"]["id"], r["message"]["text"])
            if CFG_LOCAL_RUN:
                return jsonify({
                    "answer": ans
                })
            else:
                tele_send_message(r["message"]["chat"]["id"], text=ans)
        except:
            print("ERROR: params wrong")
    return '!',200


# --------------------------------------------------------- ADMIN ---------------------------------------------
@app.route('/off', methods=['POST', 'GET'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

# def write_json(data, filename='answer.json'):
#     with open(filename, 'w') as f:
#         json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
        app.run(host=CFG_LOCALHOST, port=CFG_PORT, debug=CFG_DEBUG, ssl_context=CFG_SSL_CONTEXT)