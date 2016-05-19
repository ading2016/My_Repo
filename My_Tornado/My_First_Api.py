__author__ = 'Administrator'
import os
import sys
import time
import My_First_Tornado
class UpdateGit(My_First_Tornado.MainHandler):
    def getupdate(self):
        self.message = self.get_argument("message")
        while 1:
            if self.message == "":
                print "nothing"
                time.sleep(3)
            else:
                print self.message
                time.sleep(5)


if __name__ == "__main__":
    UpdateGit.getupdate()
