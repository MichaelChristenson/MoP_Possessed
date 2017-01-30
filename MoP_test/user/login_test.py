__author__ = 'Michael Christenson'
__date__ = "12/15/16"
import os
import time

domain_folder = os.path.abspath(__file__).split('flask')[0][:-1]
from seaborn.test.standard_import import *

sys.path.append(os.path.join(domain_folder, 'flask'))
from bindings.python_bindings import Connection
from test.base import BaseTest


class UserLoginTest(BaseTest):

    def test_user_update_email(self, email='new@mechanicsofplay.com'):
        barack = self.test_user_signup()
        user = barack.user.post(email=email)
        assert user['email'] == email
        user = barack.user.get()
        assert user['email'] == email
        barack.user.login.email.post(email, barack._password)


    def test_create_placeholder_users(self):
        if self.SERVER.startswith('http://127.0.0.1:'):
            for i in xrange(100):
                self.test_user_signup('Placeholder_%s'%i,'password')


    def test_user_update_username(self, username='Barack_New'):
        barack = self.test_user_signup()
        user = barack.user.post(username=username)
        assert user['username'] == username
        user = barack.user.get()
        assert user['username'] == username
        barack.user.login.post(username, barack._password)


    def test_user_update_password(self, password='password'):
        barack = self.test_user_signup('PasswordUpdate','old_password')
        user = barack.user.post(email="wth@test.com", password=password)
        barack.user.login.post(user['username'], password)
