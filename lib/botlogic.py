#-*-coding:utf-8

import datetime
import json

class ImakitaBotLogic(object):

    def __init__(self):
        self.JSON_PATH = "data/attend_log.json"
        self.attend_table_dict = None
        self.loadJSON()

    def loadJSON(self):
        f = open(self.JSON_PATH, "r")
        self.attend_table_dict = json.load(f)
        #print(self.attend_table_dict["attend_table"])
        f.close()

    def writeJSON(self):
        f = open(self.JSON_PATH, "w")
        json.dump(self.attend_table_dict, f)
        f.close()

    def getCurrentUnixTime(self):
        # Current time tuple (year,month,day,hour,min,sec)
        current_date = datetime.datetime.now()
        return current_date.strftime('%s')

    def showLongestWork(self):
        return 8
