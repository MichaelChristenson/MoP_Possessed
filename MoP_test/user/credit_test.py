__author__ = 'Michael Christenson'
__date__ = "1/6/2017"
import os
from seaborn.test.standard_import import *
from test.base import BaseTest
import unittest
from seaborn.table.seaborn_table import *
from seaborn.file import relative_path

START_TIME = "2016-09-18 00:00:00"


class CreditSmokeTest(BaseTest):
    def setUp(self):
        self.ann = self.test_user_signup(username="Ann", password=self.local_data.user_password,
                                         delete_if_exists=True)
        self.set_ann_credit_state(user_id=self.ann.user_id,
                                  count=0,
                                  funds=0,
                                  status="good",
                                  failed_attempts=0,
                                  daily_count=0,
                                  timestamp=START_TIME)

    def set_ann_credit_state(self, user_id=None, funds=None, count=None, status=None, failed_attempts=None,
                             timestamp=None, daily_count=None):
        return self.conn.user.credit.admin.post(user_id=user_id or self.ann.user_id,
                                                funds=funds,
                                                count=count,
                                                timestamp=timestamp,
                                                status=status,
                                                daily_count=daily_count,
                                                failed_attempts=failed_attempts)

    def test_admin_get_settings(self):
        settings = self.conn.user.credit.settings.get()
        settings['validation_function'] = eval(settings['validation_function'])
        return settings

    def test_getting_credit(self):
        settings = self.test_admin_get_settings()
        bob = self.test_user_signup('Bob', delete_if_exists=True)
        credit = bob.user.credit.get()
        self.assert_credit(credit, funds=0, count=0, status='good', remaining=settings['max_per_day'],
                           timestamp=settings['today'])
        return credit

    def test_admin_update_credit(self):
        settings = self.test_admin_get_settings()
        values = dict(count=2,
                      timestamp="2015-09-06 00:00:00",
                      status="good")

        supplement = dict(user_id=self.ann.user_id,
                          failed_attempts=3)
        supplement.update(values)
        credit = self.conn.user.credit.admin.post(**supplement)
        self.assert_credit(credit, **values)

    def test_user_update_credit(self):
        settings = self.test_admin_get_settings()
        credit = self.ann.user.credit.post(0, 3, settings['validation_function'](0, 3))
        self.assert_credit(credit, funds=3, count=3, status="good", remaining=settings['max_per_day'] - 3)

    def assert_credit(self, credit, funds=None, count=None, status=None, remaining=None, timestamp=None):
        if count is not None:
            self.assertEqual(count, credit["count"])
        if status is not None:
            self.assertEqual(status, credit["status"])
        if timestamp is not None:
            self.assertEqual(timestamp, credit["timestamp"])
        if remaining is not None:
            self.assertEqual(remaining, credit["remaining"])
        if funds is not None:
            self.assertEqual(funds, credit['funds'])

    def test_validation(self):
        settings = self.test_admin_get_settings()
        credit = self.ann.user.credit.post(0, 3, 5)  # 5 is wrong
        self.assert_credit(credit, funds=0, count=3, status='suspect', remaining=settings['max_per_day'] - 3)


class CreditEdgeTest(CreditSmokeTest):
    def get_table(self, name, settings):
        text = open(relative_path('credit_test_%s.md'%name), 'r').read().replace('today',
                                                                         settings['today'])  # todo double check
        table = SeabornTable.mark_down_to_obj(text=text)
        open(relative_path('credit_test_%s.csv'%name),'w').write(table.obj_to_csv(space_columns=True))

        def replace_max_with_setting(cell):
            return int(eval(cell.replace('max', str(settings['max_per_day'])))) if 'max' in str(cell) else cell

        table.map(replace_max_with_setting)
        return table

    def test_good_updates(self):
        settings = self.test_admin_get_settings()
        table = self.get_table('good', settings)
        for row in table:
            print(row)#todo delete
            credit = self.conn.user.credit.admin.post(user_id=self.ann.user_id,
                                             status=row['previous status'],
                                             funds=int(row['previous funds']),
                                             count=int(row['previous count']),
                                             daily_count=int(row['previous daily count']),
                                             failed_attempts=int(row['previous failed attempts']),
                                             timestamp=row['previous timestamp'])
            get_credit = self.ann.user.credit.get()
            self.assertEqual(credit, get_credit)

            validation = settings['validation_function'](row['client start'], row['client end'])
            credit = self.ann.user.credit.post(row['client start'], row['client end'], validation)

            self.assert_credit(credit, funds=row['new funds'],
                               count=int(row['new count']),
                               status=row['new status'],
                               timestamp=settings['today'],
                               remaining=int(row['remaining']))

    def test_bad_updates(self):
        settings = self.test_admin_get_settings()
        table = self.get_table('bad', settings)
        for row in table:
            print(row)#todo delete
            credit = self.conn.user.credit.admin.post(user_id=self.ann.user_id,
                                                      status=row['previous status'],
                                                      funds=int(row['previous funds']),
                                                      count=int(row['previous count']),
                                                      daily_count=int(row['previous daily count']),
                                                      failed_attempts=int(row['previous failed attempts']),
                                                      timestamp=row['previous timestamp'])
            start = int(row['client start'])
            end = int(row['client end'])
            validation = settings['validation_function'](start, end)
            credit = self.conn.user.credit.post(start=row['client start'], end=row['client end'],
                                               validation=validation)

            self.assert_credit(credit, funds=int(row['previous funds']),
                               count=int(row['previous count']),
                               status=row['new status'],
                               timestamp=settings['today'],
                               remaining=int(row['previous daily count']))

