__author__ = 'Administrator'
import os
import sys
import My_First_Tornado
class UpdateGit():
    def get(self):
        self.message = My_First_Tornado.MainHandler.get_argument("message")
        while true:
            print self.message


