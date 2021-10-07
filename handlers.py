import tornado.web
from tornado_sqlalchemy import SessionMixin, as_future

from models import Task


class IndexHandler(tornado.web.RequestHandler, SessionMixin):
    async def get(self):
        with self.make_session() as session:
            tasks = await as_future(session.query(Task).order_by(Task.id.desc()).all)
            session.expunge_all()

        context = {
            'title': 'Todo App',
            'tasks': tasks,
        }

        self.render('templates/index.html', **context)


class AddTaskHandler(tornado.web.RequestHandler, SessionMixin):
    def get(self):
        context = {
            'title': 'App Task',
            'task': Task(name=''),
        }

        self.render('templates/task_form.html', **context)

    def post(self):
        with self.make_session() as session:
            name = self.get_argument('name')
            status = True if self.get_argument('status', None) else False
            task = Task(name=name, status=status)
            session.add(task)
            session.commit()
        self.redirect('/')


class EditTaskHandler(tornado.web.RequestHandler, SessionMixin):
    def get(self, task_id):
        with self.make_session() as session:
            task = session.query(Task).get(int(task_id))
            session.expunge_all()

        context = {
            'title': 'Edit Task',
            'task': task,
        }

        self.render('templates/task_form.html', **context)

    def post(self, task_id):
        with self.make_session() as session:
            name = self.get_argument('name')
            status = True if self.get_argument('status', None) else False
            task = session.query(Task).get(int(task_id))
            task.name = name
            task.status = status
            session.commit()
        self.redirect('/')


class DeleteTaskHandler(tornado.web.RequestHandler, SessionMixin):
    def get(self, task_id):
        with self.make_session() as session:
            task = session.query(Task).get(int(task_id))
            session.delete(task)
            session.commit()
        self.redirect('/')