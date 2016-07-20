"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')

    def index(self):
        data = self.models['WelcomeModel'].get_courses()
        return self.load_view('index.html', data=data)

    def add_submit(self):
        data = request.form
        self.models["WelcomeModel"].add_course(data)
        return redirect("/")
    
    def edit_submit(self, id):
        data = request.form
        self.models['WelcomeModel'].edit(id, data)
        print 'here'
        return redirect("/")

    def edit(self, id):
        data = self.models['WelcomeModel'].get_user(id)
        return self.load_view("edit.html", data=data, id=id)

    def show(self, id):
        data = self.models['WelcomeModel'].get_user(id)
        return self.load_view("show.html", data=data)

    def delete(self, id):
        data = self.models['WelcomeModel'].get_course(id)
        return self.load_view("delete_conf.html", data=data, id=id)

    def delete_submit(self, id):
        data = self.models['WelcomeModel'].delete(id)
        return redirect("/")

