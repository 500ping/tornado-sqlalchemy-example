import tornado.ioloop
import tornado.web

from db import db
from handlers import IndexHandler, AddTaskHandler, EditTaskHandler, DeleteTaskHandler

PORT = 8888

def make_app():
    return tornado.web.Application(
        [
            (r"/", IndexHandler),
            (r"/add_task", AddTaskHandler),
            (r"/edit_task/([0-9]+)", EditTaskHandler),
            (r"/delete_task/([0-9]+)", DeleteTaskHandler),
        ], 
        debug=True, 
        autoreload=True,
        db=db,
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    print(f'Server is listening on port {PORT}')
    tornado.ioloop.IOLoop.current().start()