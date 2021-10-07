import tornado.web

from . import BaseHandler


class LoginHandler(BaseHandler):
    def get(self):
        self.render('../templates/login.html')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect("/")


class LogoutHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        self.clear_cookie('user')
        self.redirect("/")