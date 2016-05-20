__author__ = 'Administrator'
import tornado.ioloop
import tornado.web
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="file" name="filename">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')
    def post(self):
        self.set_header("Content-Type","text/plain")
        self.write("git reset --hard " + self.get_argument("message"))
        self.message = self.get_argument("message")
        if self.message == "":
            print "nothing"
        else:
            cmd = "cd /root/github/My_Repo/My_Tornado && git reset --hard %s " % self.get_argument("message")
            print cmd
            #os.popen(cmd)

class UploadFile(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="file" enctype="multipart/for-data" method="post">'
                   '<input type="file" name="file"/><br/>'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')
    def post(self):
         self.file_meta = self.request.files["file"]
         for meta in self.filen_meta:
            filename =  meta["filename"]
            print filename
            self.write(filename)

class StoryHandle(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/story/([0-9]+)",StoryHandle),
    (r"/file",UploadFile),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()