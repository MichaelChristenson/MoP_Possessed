__author__ = 'Michael Christenson'
__date__ = "12/16/16"
import os
import time

domain_folder = os.path.abspath(__file__).split('flask')[0][:-1]
from seaborn.test.standard_import import *

sys.path.append(os.path.join(domain_folder, 'flask'))
from bindings.python_bindings import Connection
from test.base import BaseTest


class UserScoreTest(BaseTest):


    def test_user_score_put(self, name="test0"):
        public_rank, private_rank = self.conn.user.score.post(name,100, max_amount=1)
        assert public_rank == 1 and private_rank == 1

        barack = self.test_user_signup()
        public_rank, private_rank = barack.user.score.post(name=name, score=0, description='description',
                                                           expiration_days_from_now=1, max_amount=1)
        assert public_rank == 2 and private_rank == 1

        public_rank, private_rank = barack.user.score.post(name,99, expiration_days_from_now=1, max_amount=4,
                                                           description='description')
        assert public_rank == 2 and private_rank == 1

        public_rank, private_rank = barack.user.score.post(name,50, expiration_days_from_now=1, max_amount=3,
                                                           description='description')
        assert public_rank == 3 and private_rank == 2

        public_rank, private_rank = barack.user.score.post(name,25, expiration_days_from_now=1, max_amount=3,
                                                           description='description')
        assert public_rank == 4 and private_rank == 3


    def test_user_score_put2(self):
        self.test_user_score_put()
        self.test_user_score_put('test1')
        self.test_user_score_put('test2')


    def test_user_score_get_array(self):
        self.test_user_score_put2()
        barack = self.test_user_signup()

        scores = barack.user.score.array.get(limit=4, name='test0')
        assert(scores[0]['score'] == 100)
        assert(scores[1]['score'] == 99)
        assert(scores[2]['score'] == 50)
        assert(scores[3]['score'] == 25)
        assert(scores[0]['name'] == 'test0')
        assert(len(scores) < 5)

        scores = barack.user.score.array.get(limit=4, name='test1', group='Barak')
        for i in range(3):
            assert(scores[i]['user_id'] == barack.user_id)
            assert(scores[i]['description'] == 'description')
            assert(scores[i]['initials'] == "BAR")
        assert scores[0]['score'] == 99
        assert scores[1]['score'] == 50
        assert scores[2]['score'] == 25


    def test_user_score_get(self):
        score = self.test_user_score_put()
        barack = self.test_user_signup()
        get_score = barack.user.score.get('test0')
        assert(score == score)





