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
                   '<input type="file" name="postfile"><br/>'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')
    def post(self):
         file_meta = self.request.files['postfile']
         for meta in file_meta:
            filename = meta['filename']
            print filename
            self.write(filename)

class StoryHandle(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)

class ProfileHandle(tornado.web.RequestHandler):
    def initialize(self,database):
        self.database = database
    def get(self,username):
        self.username = username
class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("Hello, " + name)

class LoginHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect("/")


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/story/([0-9]+)",StoryHandle),
    (r"/file",UploadFile),
    (r"/user",ProfileHandle),
    (r"/login", LoginHandler),
], cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=")

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()