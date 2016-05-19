__author__ = 'Administrator'
import os
import sys
import time
import My_First_Tornado
class UpdateGit(My_First_Tornado):
    def getupdate(self):
        self.message = My_First_Tornado.MainHandler.get_argument("message")
        while 1:
            print self.message
            time.sleep(5)


if __name__ == "__main__":
    UpdateGit.getupdate()