#-*- coding: utf-8 -*-　　
#-*- coding: cp950 -*-　
import sys
# 引入 ChatBot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class KantaiBOT:
    print ('static')
    # 建立一個 ChatBot
    chatbot = ChatBot(
        # 這個 ChatBot 的名字叫做 KantaiBOT
        "KantaiBOT",
        storage_adapter = "chatterbot.storage.JsonFileStorageAdapter",
        # 設定訓練的資料庫輸出於根目錄，並命名為 KantaiBOT_DB.json
        database = "./KantaiBOT_DB.json"
    )

    def __init__(self):
        print ('__init__')

        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        # self.chatbot.train("chatterbot.corpus.custom")
        self.chatbot.train("./achinese/")

    def getResponse(self, message=""):
        return self.chatbot.get_response(message)

if __name__ == "__main__":
    print ('__name__')
    bot = KantaiBOT()
    print(bot.getResponse(sys.argv[1]))