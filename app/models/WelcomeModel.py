""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    """

    def get_course(self, id):
        query = "SELECT * from courses where id = :id"
        data = {'id': id}
        return self.db.query_db(query, data)


    def get_courses(self):
        query = "SELECT * FROM courses"
        return self.db.query_db(query)

    def add_course(self, data):
        sql = "INSERT into courses (title, descr, created_at, updated_at) values(:title, :descr, NOW(), NOW())"
        values = {"title": data["title"], "descr": data["descr"]}
        self.db.query_db(sql, values)
        return True

    def delete(self, id):
        query = "DELETE FROM courses WHERE id= :id"
        data = { 'id': id }
        self.db.query_db(query, data)
        return True
    """
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """