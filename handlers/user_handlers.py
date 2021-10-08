import tornado.web
import bcrypt

from . import BaseHandler
from models.user import User


class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")

        if not username or not password:
            self.redirect("/login")

        with self.make_session() as session:
            user = session.query(User).filter(User.username == username).first()
            if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                self.redirect("/login")
            else:
                self.set_secure_cookie("username", user.username)
                self.redirect("/")


class RegisterHandler(BaseHandler):
    def get(self):
        self.render('register.html')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        re_password = self.get_argument("re-password")

        if not username or not password or not re_password or password != re_password:
            self.redirect("/register")

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        with self.make_session() as session:
            user = User(username=username, password=hashed_password)
            session.add(user)
            session.commit()
        self.redirect("/login")


class LogoutHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        self.clear_cookie('username')
        self.redirect("/")