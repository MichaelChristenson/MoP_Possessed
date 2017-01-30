__author__ = 'Ben Christenson'
__date__ = "10/5/15"
from seaborn.test.standard_import import *

domain_folder = os.path.abspath(__file__).split('flask')[0][:-1]
sys.path.append(os.path.join(domain_folder, 'flask'))
from bindings.python_bindings import Connection
from settings import config
from test.base import BaseTest

class PasswordSmokeTest(BaseTest):
    def test_login(self):
        """ This will test logging in """
        ben = Connection('Ben', self.local_data.ben_password, 'user/login', base_uri=self.SERVER, timeout=self.TIMEOUT)

    @skip_if_already_done
    def test_load_game_words(self):
        """ This will test loading a few game words """
        ben = Connection('Ben', self.local_data.ben_password, 'user/login', base_uri=self.SERVER, timeout=self.TIMEOUT)
        ben.password.word.post('hello', 7, 'A pleasant greeting', 'Mary says hello to her neighbor in the morning.',
                               'smoke-test')
        ben.password.word.post('world', 7, 'The current planet, or everything', 'The world is a big place.',
                               'smoke-test')
        gevent.sleep(1)

    @skip_if_already_done
    def test_load_spelling_words(self):
        """ This will test loading a few game words """
        ben = Connection('Ben', self.local_data.ben_password, 'user/login', base_uri=self.SERVER, timeout=self.TIMEOUT)
        ben.spelling.put('first second third fourth fifth sixth random_test bad'.split(), 0, 'smoke-test', 'smoke-test')

    @skip_if_already_done
    def test_get_spelling_words(self):
        """ This will test loading a few game words """
        ben = Connection('Ben', self.local_data.ben_password, 'user/login', base_uri=self.SERVER, timeout=self.TIMEOUT)
        self.test_load_spelling_words()
        assert ben.spelling.get('firstd') == False, 'Failed to spot spelling error'
        assert ben.spelling.get('first') == True, 'Failed to spot word that is spelled correctly'

    @skip_if_already_done
    def test_create_user(self):
        """ This will test creating users and having them make friends """

        ben = Connection('Ben', self.local_data.ben_password, 'user/login', base_uri=self.SERVER, timeout=self.TIMEOUT)

        ali = Connection('Ali', self.local_data.ali_password, base_uri=self.SERVER, timeout=self.TIMEOUT)
        ali_user = ali.user.signup.put('Ali', 'Alice@BenChristenson.com', 'Alice', 'ALI', self.local_data.ali_password,
                                       self.local_data.ali_password)

        ben.user.admin.put('Cal', 'Cal@BenChristenson.com', 'Cal', 'CAL', self.local_data.cal_password, 'Patron')
        ben.user.admin.post('Ali', _type='Patron')

        cal = Connection('Cal', self.local_data.cal_password, 'user/login', base_uri=self.SERVER, timeout=self.TIMEOUT)

        dan = Connection('Dan', self.local_data.dan_password, base_uri=self.SERVER, timeout=self.TIMEOUT)
        dan.user.signup.put('Dan', 'Dan@BenChristenson.com', 'Dan', 'DAN', self.local_data.ali_password,
                            self.local_data.ali_password)

        ben.user.friend.name.put(usernames=['Cal', 'Ali', 'Dan'])
        ali.user.friend.name.put(usernames=['Cal', 'Ben', 'Dan'])
        cal.user.friend.name.put(usernames=['Ben', 'Ali'])
        dan.user.friend.name.put(usernames=['Cal'])

        ben_friends = sorted([user['username'] for user in ben.user.friend.accepts.get()])
        ali_request = sorted([user['username'] for user in ali.user.friend.requests.get()])
        cal_friends = sorted([user['username'] for user in cal.user.friend.accepts.get()])

        self.assertListEqual(ben_friends, ['Ali', 'Cal', 'Dan'])
        self.assertListEqual(ali_request, ['Ben', 'Cal'])
        self.assertListEqual(cal_friends, ['Ali', 'Ben'])

        dan.user.friend.name.put(usernames=['Ali', 'Ben'])
        cal.user.friend.name.put(usernames='Dan')

        return ali, ben, cal, dan

    @skip_if_already_done
    def test_creating_a_game(self):
        """ This will test creating a game, finding a friendly game, join the game, and configuring the settings """
        self.test_load_game_words()
        self.test_load_spelling_words()
        ali, ben, cal, dan = self.test_create_user()
        game = ali.password.game.put('Room_1', rounds_per_team=4)
        self.assert_(game, "This should be a dictionary of the game")

        games = ben.password.game.friendly.get(game_status_filter='Setup')
        self.assert_(games, 'Games should have the Room_1 game')

        ben.password.game.player.put(games[0]['game_id'], ready=True, team_index=0,
                                     team_color='Green')  # later changed to Red
        dan.password.game.player.put(games[0]['game_id'], ready=True, team_index=1, team_color='Blue')
        ali.password.game.player.post(game['game_id'], team_index=0, team_color='Red', index=0)
        cal.password.game.player.put(games[0]['game_id'])
        players = dict([(player['username'], player['user_id'])
                        for player in ali.password.game.player.all.get(game['game_id'])])
        self.assertListEqual(sorted(players.keys()), ['Ali', 'Ben', 'Cal', 'Dan'])

        # game owner setting other player's settings
        ali.password.game.player.post(game['game_id'], user_id=players['Cal'], team_index=2)

        game = ali.password.game.start.put(game['game_id'], is_ready_check=False, is_auto_setup=True)

        self.assertTrue(isinstance(game, dict) and game['name'] == 'Room_1', "There were problems of %s" % game)

        active_games = ali.password.game.get()
        self.assertEqual(active_games[0]['name'], 'Room_1')

        answer = ali.password.game.round.answer.get(game['game_id'], round_index=0)
        self.assertEqual(answer, 'hello')

        return game['game_id'], ali, ben, cal, dan, answer

    @skip_if_already_done
    def test_chat(self):
        """ This will test player's chatting in a game room """
        game_id, ali, ben, cal, dan, answer = self.test_creating_a_game()
        ben.password.game.chat.post(game_id=game_id, message='Hello')
        ben.password.game.chat.put(game_id=game_id, message='World')
        chats = [chat['message'] for chat in
                 ali.password.game.chat.put(game_id=game_id, message='My turn', chat_index=0)]
        self.assertListEqual(chats, ['Hello', 'World', 'My turn'], 'Failed to receive chats after putting a chat')

        chats = cal.password.game.chat.get(game_id=game_id, chat_index=0)
        self.assertEqual(chats[0]['username'], 'Ben')
        self.assertEqual(chats[0]['message'], 'Hello')
        self.assertEqual(chats[1]['username'], 'Ben')
        self.assertEqual(chats[1]['message'], 'World')
        self.assertEqual(chats[2]['username'], 'Ali')
        self.assertEqual(chats[2]['message'], 'My turn')

        chats = ben.password.game.chat.get(game_id=game_id, chat_index=2)
        self.assertEqual(chats[0]['username'], 'Ali')
        self.assertEqual(chats[0]['message'], 'My turn')

    def test_chat_censor(self):
        """ This will test player's chatting in a game room """
        game_id, ali, ben, cal, dan, answer = self.test_creating_a_game()
        ben.password.game.chat.post(game_id=game_id, message='message to test -1 index')
        ben.password.game.chat.post(game_id=game_id, message='Shit crape ass')
        chats = cal.password.game.chat.get(game_id=game_id, chat_index=-1)
        log.debug("Message:: %s" % chats[0]['message'])
        self.assertEqual(chats[0]['message'], 'S*** crape a**')

    @skip_if_already_done
    def test_making_move(self):
        game_id, ali, ben, cal, dan, answer = self.test_creating_a_game()
        self.test_load_game_words()
        self.test_load_spelling_words()

        moves = ali.password.game.round.move.get(game_id=game_id, round_index=0)
        self.assertEqual(len(moves), 1)

        # try:    ali.password.game.round.answer(game_id, round_index=0)
        # except ForbiddenException as e: pass # ali is a guesser and isn't allowed the answer
        assert isinstance(ali[-1].error, ForbiddenException)

        try:
            ali.password.game.round.move.put(moves[0]['move_id'], 'firstd', 'Done')
        except BadRequestException as e:
            pass

        ali.password.game.round.move.put(moves[0]['move_id'], 'first', 'Done')

        moves = ali.password.game.round.move.get(game_id=game_id, round_index=0)
        self.assertEqual(moves[0]['answer'], 'first')

        ben.password.game.round.move.put(moves[1]['move_id'], answer, 'Done')  # good guess :)
        moves = ben.password.game.round.move.get(game_id=game_id, round_index=0)
        self.assertEqual(moves[-1]['status'], 'Correct')

    def test_making_tentative_move(self, round_index=1):
        game_id, h2, g2, h1, g1, answer = self.test_creating_a_game()
        answer = h1.password.game.round.answer.get(game_id, round_index=round_index)
        moves = h1.password.game.round.move.get(game_id, round_index=round_index)
        h1.password.game.round.move.put(moves[-1]['move_id'], 'first', 'Done')

        moves = g1.password.game.round.move.get(game_id, round_index=round_index)
        g1.password.game.round.move.put(moves[-1]['move_id'], 'second', 'Scratch')

        moves = h2.password.game.round.move.get(game_id, round_index=round_index)
        self.assertNotEqual(moves[1]['answer'], 'second')  # because it is tentative
        h2.password.game.round.move.put(moves[-1]['move_id'], 'third', 'Tentative')

        moves = h1.password.game.round.move.get(game_id, round_index=round_index)
        h1.password.game.round.move.put(moves[-1]['move_id'], 'fifth', 'Scratch')

        moves = g2.password.game.round.move.get(game_id, round_index=round_index)
        self.assertEqual(''.join([move['answer'] for move in moves]), 'first')  # one first answer
        g2.password.game.round.move.put(moves[-1]['move_id'], 'fourth', 'Scratch')

        g1.password.game.round.move.put(moves[1]['move_id'], 'second', 'Tentative')  # this will actually make it done

        moves = g1.password.game.round.move.get(game_id, round_index=round_index)
        g1.password.game.round.move.put(moves[-1]['move_id'], 'sixth', 'Done')  # this should cascade third to done

        moves = g2.password.game.round.move.get(game_id, round_index=round_index)
        self.assertEqual([moves[-1]['status'], moves[-1]['answer']], ['Scratch', 'fourth'])
        self.assertEqual([moves[-2]['status'], moves[-2]['answer']], ['Done', 'third'])
        self.assertEqual([moves[-3]['status'], moves[-3]['answer']], ['Done', 'second'])

        moves = g2.password.game.round.move.get(game_id, round_index=round_index)
        g2.password.game.round.move.put(moves[-1]['move_id'], answer, 'Done')

    def test_everyone_losing(self, round_index=2):
        game_id, ali, ben, cal, dan, answer = self.test_creating_a_game()
        players = [ben, ali, dan, cal]
        move_index = 0
        moves = ben.password.game.round.move.get(game_id=game_id, round_index=round_index)
        while moves[-1]['status'] not in ['Done']:
            for player in players:
                player.password.game.round.move.index.post(game_id, round_index, move_index, 'bad', 'Done')
                move_index += 1
            moves = ben.password.game.round.move.get(game_id=game_id, round_index=round_index)
        games = ben.password.game.get(game_id=game_id)
        self.assertEqual(games[0]['guesses_per_team'] * 4, move_index)

    def test_making_random_round(self, guesses=4, round_index=3):
        """ This will test random play doing random thing
            :param guesses:      int of the number of bad guesses before giving the right answer 
            :param round_index:  int the round index number
            :return:             list of moves
            """
        seed(guesses + round_index * 100)
        game_id, ali, ben, cal, dan, answer = self.test_creating_a_game()
        players = [ali, ben, cal, dan]
        options = ['Scratch', 'Tentative', 'Pass', 'Done']
        game = ben.password.game.get(game_id=game_id)[0]
        guesses = guesses < game['guesses_per_team'] and guesses or game['guesses_per_team']

        def is_moves_done(moves):
            return sum([move['is_guesser'] and move['status'] == 'Done' and 1 or 0 for move in moves]) == guesses

        moves = ali.password.game.round.move.get(game_id, round_index=round_index)
        while True:
            player = players[int(random() * len(players))]
            option = options[int(random() * len(options))]

            moves = player.password.game.round.move.get(game_id, round_index)
            if is_moves_done(moves):
                break
            elif moves[-1]['status'] != 'Done':
                player.password.game.round.move.post(moves[-1]['move_id'], 'random_test', 'Done')

        try:
            answer = ali.password.game.round.answer.get(game_id, round_index)
        except:  # one of these two knows the answer
            answer = ben.password.game.round.answer.get(game_id, round_index)

        for i in range(20):
            player = players[i % len(players)]
            moves = player.password.game.round.move.get(game_id, round_index)
            if moves[-1]['username'] == player[0].data['username']:
                move = player.password.game.round.move.post(moves[-1]['move_id'], answer, 'Done')
                if move['status'] == 'Correct':
                    break

    def test_making_random_rounds(self):
        game_id, ali, ben, cal, dan, answer = self.test_creating_a_game()
        game = ben.password.game.get(game_id=game_id)[0]
        players = ben.password.game.player.all.get(game_id=game_id)
        players = [player for player in players if not player['observing']]
        for i in range(4, game['rounds_per_team'] * len(players) / 2):
            game = ben.password.game.get(game_id=game_id)[0]
            if game['status'] != 'Active': break
            self.test_making_random_round(i, i)


if __name__ == '__main__':
    unittest.main()
