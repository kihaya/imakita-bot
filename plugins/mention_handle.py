#-*- coding:utf-8 -*-

from slackbot.bot import respond_to
from lib.botlogic import ImakitaBotLogic

from pprint import pprint

imakitabotlogic = ImakitaBotLogic()
imakitabotlogic.loadJSON()

#imakitabotlogic.attend_table_dict["attend_table"].append('{"who":"ksugiura"}')
#imakitabotlogic.writeJSON()

#imakitabotlogic.loadJSON()

@respond_to('こんにちは')
def mention_func(message):
    message.reply("構ってくれてありがとう♡")

@respond_to(r"start|end")
def mention_start_cmd(msg):

    if msg.body["user"] == "U0ADXPKLM":

       if msg.body["text"] == "start":
            msg.reply("おはようございます♡" + "今日も１日頑張りましょう！")
       elif msg.body["text"] == "end":
           msg.reply("お疲れ様でした！")

       d = imakitabotlogic.getCurrentUnixTime()
       print(d)
       #date = d[0] + "/" + d[1] + "/" + d[2] + "/" + d[3] + "/" + d[4]
       record = '{"who":"%s","cmd":%s,"date":%s}' % (msg.body["user"] ,msg.body["text"], d)
       print(record)
       imakitabotlogic.attend_table_dict["attend_table"].append(record)

       print(imakitabotlogic.attend_table_dict)

       imakitabotlogic.writeJSON()
       imakitabotlogic.loadJSON()

    else:
       message.reply("あなたは誰...?ごめんね（泣）")

@respond_to("longest")
def mention_show_longest(msg):
   msg.reply("最長労働時間は"+ str(imakitabotlogic.showLongestWork()) + "時間です")
