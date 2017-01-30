"""
    This will test basic rest call of various types
"""
__author__ = 'Ben Christenson'
__date__ = "10/5/15"
from seaborn.test.standard_import import *
from seaborn.calling_function import function_info
from pprint import pprint

domain_folder = os.path.abspath(__file__).split('flask')[0][:-1]
sys.path.append(os.path.join(domain_folder, 'flask'))
from bindings.python_bindings import Connection

DEBUG_SERVER = 'http://127.0.0.1:4999'
LOCAL_SERVER = 'http://local.api.mechanicsofplay.com'
AWS_SERVER   = 'http://api.mechanicsofplay.com'

class ApiEdgeTest(unittest.TestCase):
    thread = None
    SERVER = AWS_SERVER
    TIMEOUT = 20

    @classmethod
    def setUpClass(cls):
        global local_data
        local_data = LocalData('../_passwords.json', no_question=True)

        traceback_skip_path('/bindings/')

        if cls.SERVER == DEBUG_SERVER:
            from settings.config import TestConfig
            os.environ['flask_config'] = TestConfig.__name__
            from settings.setup_app import setup_flask
            run = setup_flask()
            sigquit = getattr(signal, 'SIGQUIT', "Windows_Problem")
            if sigquit != "Windows_Problem":
                gevent.signal(sigquit, gevent.kill)
            cls.thread = gevent.spawn(run)
            cls.thread.start()
            gevent.sleep(0)
        cls.conn = Connection('Ben', local_data.ben_password, 'user/login', base_uri=cls.SERVER, timeout=cls.TIMEOUT)

        if cls.SERVER == DEBUG_SERVER:
            cls.conn.setup.database.reinitialize.post()


    @classmethod
    def tearDownClass(cls):
        print "That's All Folks"

    def test_echo(self):
        ret = self.conn.get('test/echo', message='Hello World!')
        assert ret == 'ECHO: Hello World!'

    def test_server_default(self):
        assert self.conn.test.get() == 'Hello World!'
        assert self.conn.test.echo.get(None) == 'ECHO: hello'
        assert self.conn.test.wait.get(None) == 'Waited: 2 seconds'
        assert self.conn.test.int.get(None) == 5
        assert self.conn.test.float.get(None) == 1.23
        assert self.conn.test.array.string.get(None) == ['a', 'b', 'c']
        assert self.conn.test.array.int.get(None) == [1, 2, 3]
        assert self.conn.test.array.string2.get() == ['a', 'b', 'c']
        assert self.conn.test.array.int2.get() == [0, 1, 2]
        assert self.conn.test.array.float.get(None) == [1.1, 2.2, 3.3]
        assert self.conn.test.array.float2.get() == [1.1, 2.2, 3.3]
        assert self.conn.test.key.post(None, None) == {'key': 'hello', 'value': 'world'}
        assert self.conn.test.key.put(None, None) == {'key': 'hello', 'value': 'world'}
        assert self.conn.test.key.get(None) == {'key': 'hello', 'value': 'world'}

    def test_client_default(self):
        assert self.conn.test.get() == 'Hello World!'
        assert self.conn.test.echo.get() == 'ECHO: hello'
        assert self.conn.test.wait.get() == 'Waited: 2 seconds'
        assert self.conn.test.int.get() == 5
        assert self.conn.test.float.get() == 1.23
        assert self.conn.test.array.string.get() == ['a', 'b', 'c']
        assert self.conn.test.array.int.get() == [1, 2, 3]
        assert self.conn.test.key.post() == {'key': 'hello', 'value': 'world'}
        assert self.conn.test.key.put() == {'key': 'hello', 'value': 'world'}
        assert self.conn.test.key.get() == {'key': 'hello', 'value': 'world'}

    def test_arguments(self, wait_time=1):
        assert self.conn.test.string.post("Hello") == 'Hello'
        assert self.conn.test.string.put("Hello") == 'Hello'
        assert self.conn.test.echo.get('echo') == 'ECHO: echo'
        assert self.conn.test.wait.get(wait_time) == 'Waited: %s seconds' % wait_time
        assert self.conn.test.int.get(2) == 2
        assert self.conn.test.float.get(3.21) == 3.21
        assert self.conn.test.array.string.get(['c', 'b', 'a']) == ['c', 'b', 'a']
        assert self.conn.test.array.int.get([1,2,3]) == [1, 2, 3]
        assert self.conn.test.array.float.get([1.1,2.2,3.3]) == [1.1,2.2,3.3]
        assert self.conn.test.key.post('world', 'hello') == {'key': 'world', 'value': 'hello'}
        assert self.conn.test.key.put('world2', 'hell') == {'key': 'world2', 'value': 'hell'}
        assert self.conn.test.key.get('world') == {'key': 'world', 'value': 'hello'}

    def test_sending_array(self):
        assert self.conn.test.array.string.get(['c', 'b', 'a']) == ['c', 'b', 'a']
        assert self.conn.test.array.int.get([1,2,3]) == [1, 2, 3]
        assert self.conn.test.array.float.get([1.1,2.2,3.3]) == [1.1,2.2,3.3]

    def test_repeat(self):
        for i in xrange(100):
            self.test_arguments(0)

    def test_repeat_get(self):
        for i in xrange(100):
            assert self.conn.test.int.get(2) == 2

if __name__ == '__main__':
    unittest.main()
