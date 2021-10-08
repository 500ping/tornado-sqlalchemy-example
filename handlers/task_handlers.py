import tornado.web

from . import BaseHandler
from models.task import Task


class IndexHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        with self.make_session() as session:
            tasks = session.query(Task).filter(Task.user_id == self.current_user.id).order_by(Task.id.desc()).all()
            session.expunge_all()

        context = {
            'title': 'Todo App',
            'tasks': tasks,
        }

        self.render('index.html', **context)


class AddTaskHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        context = {
            'title': 'App Task',
            'task': Task(name=''),
        }

        self.render('task_form.html', **context)

    @tornado.web.authenticated
    def post(self):
        name = self.get_argument('name')
        status = True if self.get_argument('status', None) else False
        with self.make_session() as session:
            task = Task(name=name, status=status, user_id=self.current_user.id)
            session.add(task)
            session.commit()
        self.redirect('/')


class EditTaskHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, task_id):
        with self.make_session() as session:
            task = session.query(Task).get(int(task_id))
            session.expunge_all()

        context = {
            'title': 'Edit Task',
            'task': task,
        }

        self.render('task_form.html', **context)

    @tornado.web.authenticated
    def post(self, task_id):
        name = self.get_argument('name')
        status = True if self.get_argument('status', None) else False
        with self.make_session() as session:
            task = session.query(Task).get(int(task_id))
            task.name = name
            task.status = status
            session.commit()
        self.redirect('/')


class DeleteTaskHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, task_id):
        with self.make_session() as session:
            task = session.query(Task).get(int(task_id))
            session.delete(task)
            session.commit()
        self.redirect('/')