__author__ = 'Michael Christenson'
__date__ = "12/22/16"
import os

domain_folder = os.path.abspath(__file__).split('flask')[0][:-1]
from seaborn.test.standard_import import *
from collections import OrderedDict

sys.path.append(os.path.join(domain_folder, 'flask'))
from bindings.python_bindings import Connection
from test.base import BaseTest

NAMES = ['Ann', 'Bob', 'Cal', 'Dan', 'Ed', 'Fae', 'Gia', 'Han', 'Igi', 'Jeff', 'Ken', 'Lee', 'Mark', 'Norm',
         'Ozie', 'Paul', 'Quin', 'Rick', 'Sam', 'Tom', 'Umar', 'Vic', 'Wick']


class PossessedSmokeTest(BaseTest):
    def test_get_role_array(self):
        """
        Creates a game and tests the role call
        :return: the array of roles
        """
        ann = self.test_user_signup(username="Ann", delete_if_exists=True)
        roles = ann.possessed.role.array.get()
        self.assertIsNotNone(roles)  # todo not good, you need to assert not empty
        roles = ann.possessed.role.array.get()
        roles2 = ann.possessed.role.array.post(status_list=['active'])
        self.assertGreater(len(roles), 0)
        self.assertEqual(roles, roles2)
        return ann, roles

    def test_creating_a_game(self, number_of_players=None):
        """
        Creates a game that is capable of hosting a number of players
        :param number_of_players: the number of players to host.
        :return: the host of the game and the game itself
        """
        ann, roles = self.test_get_role_array()
        number_of_players = number_of_players or len(roles)
        game = ann.possessed.game.put(number_of_players=number_of_players,
                                      group="test")
        return ann, roles, game

    def test_getting_a_game(self):
        """
        Tests the game's get call
        :return: None
        """
        ann, roles, game = self.test_creating_a_game()
        get_game = ann.possessed.game.get(game_id=game['game_id'])
        self.assertEqual(game, get_game)

    def test_getting_game_role_array(self):
        """
        Creates a game and tests the role call
        :return: the array of roles
        """
        ann, roles, game = self.test_creating_a_game()
        game_roles = ann.possessed.game.role.array.get(game["game_id"])
        roles_priority = {role['priority']: role for role in roles}
        game_roles_priority = {role['priority']: role for role in game_roles}
        self.assertEquals(roles_priority, game_roles_priority)
        return game_roles

    def test_getting_array_of_games(self):
        """
        Tests retrieval of game array
        :return: host of one game and the game itself
        """
        ann, roles, game = self.test_creating_a_game()
        ann_games = ann.possessed.game.array.get(status='setup', group='test')
        self.assertGreater(len(ann_games), 0)
        self.assertIn(game, ann_games)

        bob = self.test_user_signup("Bob", delete_if_exists=True)
        bob_games = bob.possessed.game.array.get(status='setup', group='test')
        self.assertEqual(ann_games, bob_games)
        return bob_games

    def test_adding_player_to_game(self):
        """
        places the player into a game
        :return: game
        """
        ann, roles, game = self.test_creating_a_game()
        player = ann.possessed.game.player.put(game_id=game["game_id"])
        self.assertEqual(ann.user_id, player['user_id'])
        return ann, player, game

    def test_get_player(self):
        """
        retrieves a given player's role
        :return: player object
        """
        ann, player, game = self.test_adding_player_to_game()
        get_player = ann.possessed.game.player.get(game_id=game['game_id'])
        self.assertEqual(get_player, player)

    def test_adding_players_to_game(self):
        """
        This will populate a game and have the host steal from the first generated player
        :return: game object
        """
        ann, roles, game = self.test_creating_a_game()
        game = self.test_getting_array_of_games()[0]
        ann, player, game = self.test_adding_player_to_game()

        players = OrderedDict()
        players[ann] = player

        for i in xrange(1, game["number_of_players"]):
            user = self.test_user_signup(username=NAMES[i], delete_if_exists=True)
            player = user.possessed.game.player.put(game_id=game["game_id"],
                                                    role_id=roles[i]['role_id'])
            self.assertEqual(player['user_id'], user.user_id)
            players[user] = player
        return players

    def test_getting_players_in_game(self):
        players = self.test_adding_players_to_game()
        ann, bob = list(players.keys())[:2]
        ann_players = ann.possessed.game.player.array.get(game_id=players[ann]['game_id'])
        bob_players = bob.possessed.game.player.array.get(game_id=players[bob]['game_id'])

        self.assertEqual(ann_players, bob_players)
        self.assertEqual(ann_players, list(players.values()))

    def test_getting_notification_before_game_start(self):
        players = self.test_adding_players_to_game()
        for user, player in players.items():
            notifications = user.possessed.game.notification.array.get(game_id=player['game_id'])
            self.assertEqual(len(notifications), 0)

    def test_starting_game(self):
        """
        This will create and start a game
        :return: None
        """
        ann, roles, game = self.test_creating_a_game()
        self.test_getting_a_game()
        self.test_getting_notification_before_game_start()  # just to make sure it happens first
        players = self.test_adding_players_to_game()
        game = ann.possessed.game.start.put(game_id=game["game_id"])
        self.assertEqual(game['status'], 'active')
        return game, players

    def test_getting_notification_after_game_start(self):
        """
        Tests capability of retrieving notices
        :return: notice instance
        """
        ann, roles = self.test_get_role_array()
        game, players = self.test_starting_game()
        player_notifications = []
        for user, player in players.items():
            notifications = user.possessed.game.notification.array.get(game_id=game['game_id'], offset=0, limit=10)
            player_notifications.append(notifications)
            self.assertGreater(len(notifications), 0)
            for notification in notifications:
                self.assertEqual(notification['round_index'], 0)

        for i in range(len(player_notifications)):
            self.assertEqual(player_notifications[1][0]['message'], 'role change')
            self.assertIn(roles[1]['name'],player_notifications[1][0]['details'])
        return player_notifications

    def test_creating_game_steal_action(self):
        """
        Tests to determine if "steal" action's put call functions
        :return: action
        """
        game_roles = self.test_getting_game_role_array()
        game, players = self.test_starting_game()
        user, player = list(players.items())[0]
        target_player = list(players.items())[1][1]
        action = user.possessed.game.action.put(game_id=game["game_id"],
                                                action="Steal",
                                                target_player1=target_player['player_id'],
                                                target_role2=game_roles[0]['role_id'])
        self.assertEqual(action['action'], 'Steal')
        self.assertEqual(action['player_id'], player['player_id'])
        self.assertEqual(action['game_id'], game['game_id'])
        return action

    def test_getting_game_steal_action(self):
        """
        Tests to determine if "steal" action's get call functions
        :return: action
        """
        action = self.test_creating_game_steal_action()
        get_action = self.conn.possessed.game.action.get(action_id=action["action_id"])
        self.assertEqual(action, get_action)

    def test_creating_game_role_action(self, action="Judge"):
        """
        Tests to determine if "judge" action's put call functions
        :return: action
        """
        game, players = self.test_starting_game()
        player_notifications = self.test_getting_notification_after_game_start()

        player_id = [n['player_id'] for n, p in player_notifications
                     if n['message'] == 'role change' and action in n['details']][0]

        user = [user for user, player in players.items() if player['player_id'] == player_id][0]
        action = user.possessed.game.action.put(game_id=game["game_id"], action="Judge")
        self.assertEqual(action['action'], 'Judge')
        self.assertEqual(action['player_id'], player_id)
        self.assertEqual(action['game_id'], game['game_id'])
        return action

    def test_getting_game_role_action(self):
        """
        Tests to determine if "judge" action's get call functions
        :return: action
        """
        action = self.test_creating_game_role_action()
        get_action = self.conn.possessed.game.action.get(action_id=action["action_id"])
        self.assertEqual(action, get_action)
        return get_action

    def test_ending_a_games_round(self):
        ann, roles, game = self.test_creating_a_game()
        self.test_getting_game_role_action()
        self.test_getting_game_steal_action()
        self.test_starting_game()
        new_game = ann.possessed.post(game_id=game['game_id'],
                                      round_index=1)
        self.assertEqual(new_game['round_index'],2)
        return game

    def test_getting_notification_after_game_round(self):
        """
        Tests capability of retrieving notices
        :return: notice instance
        """
        game, players = self.test_starting_game()
        game = self.test_ending_a_games_round()
        player_notifications = self.test_getting_notification_after_game_start()
        for user, player in players.items():
            old_notifications = player_notifications.pop(0)
            notifications = user.possessed.game.notification.array.get(game_id=game['game_id'],
                                                                       offset=len(old_notifications),
                                                                       limit=10)
            if notifications:
                self.assertEqual(notifications[0]['round_index'], 1)
                self.assertNotIn(old_notifications[0], notifications)
                self.assertEqual(old_notifications[0]['player_id'], notifications[0]['player_id'])

    def test_state_get_array(self):
        """
        Creates a game and retrieves all possible states
        :return: states
        """
        game = self.test_ending_a_games_round()
        states = self.conn.possessed.game.state.array.get(game_id=game["game_id"])
        self.assertIsNotNone(states)
        return states

    def test_state_get(self):
        """
        tests the get call
        :return: state of game
        """
        states = self.test_state_get_array()
        state = self.conn.possessed.game.state.get(states[0]["state_id"])
        return state


if __name__ == "__main__":
    unittest.main()
