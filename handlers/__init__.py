import tornado.web
from tornado_sqlalchemy import SessionMixin

from models.user import User


class BaseHandler(tornado.web.RequestHandler, SessionMixin):
    def get_current_user(self):
        username = self.get_secure_cookie("username")
        with self.make_session() as session:
            user = session.query(User).filter(User.username == username).first()
            session.expunge_all()
        return user