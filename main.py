import tornado.ioloop
import tornado.web
import os

from db import db
from handlers import task_handlers, user_handlers

PORT = 8888

def make_app():
    return tornado.web.Application(
        [
            (r"/", task_handlers.IndexHandler),
            (r"/login", user_handlers.LoginHandler),
            (r"/register", user_handlers.RegisterHandler),
            (r"/logout", user_handlers.LogoutHandler),
            (r"/add_task", task_handlers.AddTaskHandler),
            (r"/edit_task/([0-9]+)", task_handlers.EditTaskHandler),
            (r"/delete_task/([0-9]+)", task_handlers.DeleteTaskHandler),
        ], 
        debug=True, 
        autoreload=True,
        db=db,
        cookie_secret='test',
        login_url='/login',
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    print(f'Server is listening on port {PORT}')
    tornado.ioloop.IOLoop.current().start()