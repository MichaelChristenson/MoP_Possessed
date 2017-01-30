__author__ = 'Ben Christenson'
__date__ = "10/5/15"
from seaborn.test.standard_import import *

domain_folder = os.path.abspath(__file__).split('flask')[0][:-1]
sys.path.append(os.path.join(domain_folder, 'flask'))
from bindings.python_bindings import Connection

DEBUG_SERVER = 'http://127.0.0.1:4999'
LOCAL_SERVER = 'http://local.api.mechanicsofplay.com'
AWS_SERVER = 'http://api.mechanicsofplay.com'

class ApiSetupTest(unittest.TestCase):
    thread = None
    SERVER = DEBUG_SERVER
    TIMEOUT = 20

    @classmethod
    def setUpClass(cls):
        global local_data
        local_data = LocalData('../_passwords.json', no_question=True)

        traceback_skip_path('/bindings/')

        if cls.SERVER == DEBUG_SERVER:
            from settings.config import LocalDebugConfig
            os.environ['flask_config'] = LocalDebugConfig.__name__
            from settings.setup_app import setup_flask, log
            run = setup_flask()
            sigquit = getattr(signal, 'SIGQUIT', "Windows_Problem")
            if sigquit != "Windows_Problem":
                gevent.signal(sigquit, gevent.kill)
            cls.thread = gevent.spawn(run)
            cls.thread.start()
            gevent.sleep(0)
        else:
            setup_stdout_logging()

    @classmethod
    def tearDownClass(cls):
        log.info("That's All Folks")

    def test_chat_setup(self):
        """ This will test settingup a chat session"""
        ben = Connection('Ben', local_data.ben_password, 'user/login', base_uri=self.SERVER, timeout=self.TIMEOUT)
        report = ben.setup.chat.post()
        log.info('\n    %s' % '\n    '.join(report) + '\n')
        games = ben.password.game.get('Setup')
        self.assertEqual(games[0]['name'], 'Chat Room', "Couldn't find the game 'Chat Room'")
        log.info('\n    %s' % '\n    '.join('%s %s' % (k.ljust(20), v) for k, v in games[0].items()))
        chats = ben.password.game.chat.get(games[0]['game_id'])
        self.assertEqual(chats[0]['message'], 'Hello World!', "Couldn't find the first chat in Chat Room")
        players = ben.password.game.player.all.get(game_id=games[0]['game_id'])
        self.assertEqual(players[0]['username'], 'Ben', 'Player Ben not accounted for')
        self.assertEqual(players[1]['username'], 'Patrick', 'Player Patrick not accounted for')


if __name__ == '__main__':
    unittest.main()
