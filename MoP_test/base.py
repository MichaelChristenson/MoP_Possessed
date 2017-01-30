__author__ = "Michael Christenson"
__date__ = "12/21/17"

import os
import time

domain_folder = os.path.abspath(__file__).split('flask')[0][:-1]
from seaborn.test.standard_import import *
# Game specific import

from seaborn.file import relative_path

sys.path.append(os.path.join(domain_folder, 'flask'))
from bindings.python_bindings import Connection
from test_chain import TestChain

DEBUG_SERVER = 'http://127.0.0.1:4999'
LOCAL_SERVER = 'http://local.api.mechanicsofplay.com'
AWS_SERVER = 'http://api.mechanicsofplay.com'
PROXY_DEBUG_SERVER = 'http://127.0.0.1:4777'
PROXY_AWS_SERVER = 'http://127.0.0.1:4888'
PROXIES = None  # {'http': 'http://127.0.0.1:4666', 'https': 'https://127.0.0.1:4665'}


class BaseTest(TestChain):
    thread = None
    SERVER = DEBUG_SERVER
    TIMEOUT = 20
    START_TIME = time.time()
    local_data = LocalData(relative_path('_test.json'), no_question=True)

    @classmethod
    def setUpClass(cls):
        traceback_skip_path('/bindings/')
        if cls.SERVER is DEBUG_SERVER:
            if sys.version_info[0] == 2:
                cls._spawn_gevent_flask()
            else:
                cls._spawn_thread_flask()

        admin_password = cls.local_data.admin_password
        cls.conn = Connection('Admin-User', admin_password, 'user/login', base_uri=cls.SERVER,
                              proxies=PROXIES if cls.SERVER not in [PROXY_DEBUG_SERVER, PROXY_AWS_SERVER] else None)

        cls.ann = Connection("Ann",cls.local_data.user_password, base_uri=cls.SERVER, timeout=cls.TIMEOUT,
                             proxies=PROXIES if cls.SERVER not in [PROXY_DEBUG_SERVER, PROXY_AWS_SERVER] else None)
        cls.ann.user.signup.put(username="Ann", password=cls.local_data.user_password)

    @classmethod
    def _get_flask_run(cls):
        from settings.config import TestConfig
        os.environ['flask_config'] = TestConfig.__name__
        from settings.setup_app import setup_flask, log, initialize_database
        return setup_flask()

    @classmethod
    def _spawn_gevent_flask(cls):
        run = cls._get_flask_run()
        sigquit = getattr(signal, 'SIGQUIT', "Windows_Problem")
        if sigquit != "Windows_Problem":
            gevent.signal(sigquit, gevent.kill)
        cls.thread = gevent.spawn(run)
        cls.thread.start()
        gevent.sleep(0)

    @classmethod
    def _spawn_thread_flask(cls):
        import _thread
        run = cls._get_flask_run()
        _thread.start_new_thread(run,())

    @classmethod
    def tearDownClass(cls):
        print("\n\nThat's All Folks in %s seconds" % round(time.time() - cls.START_TIME, 2))

    def test_login(self, name='Fire-Fly', password = None):
        user = Connection(name, password or self.local_data.user_password, 'user/login', base_uri=self.SERVER, timeout=self.TIMEOUT,
                         proxies=PROXIES if self.SERVER not in [PROXY_DEBUG_SERVER, PROXY_AWS_SERVER] else None)
        return user
		
    def test_user_signup(self, username="Barack", password=None, email=None, initials=None, group=None,
                         delete_if_exists=True):
        if password is None:
            password = self.local_data.user_password

        initials = initials or (username+"AAA")[:3].upper()
        if delete_if_exists:
            try:
                old = self.conn.user.get(username=username)
                self.conn.user.delete(old['user_id'])
            except Exception as e:
                pass
        group = group or username
        user_conn = Connection(username, password, base_uri=self.SERVER, timeout=self.TIMEOUT,
                               proxies=PROXIES if self.SERVER not in [PROXY_DEBUG_SERVER, PROXY_AWS_SERVER] else None)
        ret = user_conn.user.signup.put(username=username, password=password, confirm_password=password,
                                        initials=initials, group=group)
        user_conn.user_id = ret['user_id']
        user_conn._status = "logged in from signup"
        return user_conn

