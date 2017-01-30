__author__ = 'Bob Christenson'
__date__ = "10/5/15"
import os

domain_folder = os.path.abspath(__file__).split('flask')[0][:-1]
from seaborn.test.standard_import import *
from test.base import BaseTest

sys.path.append(os.path.join(domain_folder, 'flask'))


class UserTransactionTest(BaseTest):
    pass

    def test_google_access(self):
        access_token = self.conn.user.sale.transaction.access.post()
        assert access_token, 'Failed to get new google access token'


