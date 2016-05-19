__author__ = 'Administrator'
import tornado.ioloop
import tornado.web
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="text" name="message1">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')
    def post(self):
        self.set_header("Content-Type","text/plain")
        self.write("git reset --hard " + self.get_argument("message") + self.get_argument("message1"))
    def getupdate(self):
        self.message = self.get_argument("message")
        while 1:
            if self.message == "":
                print "nothing"
                time.sleep(3)
            else:
                print self.message
                time.sleep(5)



class StoryHandle(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/story/([0-9]+)",StoryHandle),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()