# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

import os
import sys
import logging

from argparse import ArgumentParser

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from flask import Flask, request, abort
# from flask_sslify import SSLify

import ssl

from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)
# sslify = SSLify(app)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', '1a2da7b8ab4436320d9e589df476e72f')
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', 'Fjxj5it/OvSgCJiMh3ixzU5J02mlR0lWx772P+oGRX/VKoA216Q5dCi9JG/ZgBAW2TTgFhfRkQ6iV/yfLk//m5L21UnGBVfxdaz53RdWGXOUsBC4i3ydFV7eU8G2ayBpzzJfidCr4osmyiXrNpk5RgdB04t89/1O/w1cDnyilFU=')
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi('Fjxj5it/OvSgCJiMh3ixzU5J02mlR0lWx772P+oGRX/VKoA216Q5dCi9JG/ZgBAW2TTgFhfRkQ6iV/yfLk//m5L21UnGBVfxdaz53RdWGXOUsBC4i3ydFV7eU8G2ayBpzzJfidCr4osmyiXrNpk5RgdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser('1a2da7b8ab4436320d9e589df476e72f')


@app.route("/callback", methods=['POST'])
def callback():

    print(" =========== Start Callback =============")
    # print(request)
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)
    # print(body);
    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        logging.error("Catch an exception.", exc_info=True)
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
 #       print('Input = ' + event.message.text)
        result = bot.getResponse(event.message.text)
        line_bot_api.reply_message(
            event.reply_token,
            # TextSendMessage(text=event.message.text)
            TextSendMessage(text=result.text)
        )
#        print('Output= ' + result.text)

    return 'OK'

class KantaiBOT:
    print('static')
    # 建立一個 ChatBot
    chatbot = ChatBot(
        # 這個 ChatBot 的名字叫做 KantaiBOT
        "KantaiBOT",
        storage_adapter = "chatterbot.storage.JsonFileStorageAdapter",
        # 設定訓練的資料庫輸出於根目錄，並命名為 KantaiBOT_DB.json
        database = "./KantaiBOT_DB.json"
    )

    def __init__(self):
        print ('KantaiBOT, __init__')

        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        self.chatbot.train("customize/")
        # self.chatbot.train("chatterbot.corpus.custom")

    def getResponse(self, message=""):
        return self.chatbot.get_response(message)

if __name__ == "__main__":
    bot = KantaiBOT();
    # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    # context.load_cert_chain('ca.crt', 'ca.key')

    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=1299, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    arg_parser.add_argument('--host', default="localhost", help='set host location')

    options = arg_parser.parse_args()

    # ssl_context='adhoc'
    # context = ('ca.crt', 'ca.key')
    # app.run(host='127.0.0.1', port=1299, ssl_context=context, threaded=True, debug=False)
    app.run(host=options.host, debug=options.debug, port=options.port);
