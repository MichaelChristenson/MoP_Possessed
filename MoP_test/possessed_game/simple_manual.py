__author__ = 'Michael Christenson'
__date__ = "12/31/16"
import os

domain_folder = os.path.abspath(__file__).split('flask')[0][:-1]
from seaborn.test.standard_import import *
from seaborn.table.seaborn_table import SeabornTable
from seaborn.file import relative_path
from collections import OrderedDict

sys.path.append(os.path.join(domain_folder, 'flask'))
from test.base import BaseTest
from random import random, seed
from test.possessed_game.simple_gen import PossessedBaseTest


class PossessedSimpleManual(PossessedBaseTest):
    TIMEOUT = 2000
    FILE = relative_path('answers/simple_manual_5.md')
    RESULT_FILE = relative_path('results/simple_manual_5.md')
    results = OrderedDict()
    players = OrderedDict()
    game = {}
    roles = {}
    player_id = {}
    tables = OrderedDict()
    roster = {}
    role_roster = {}
    rounds = 0
    formatting = OrderedDict({'Actions': ['round_index','Player','action','Target 1','Target 2','status'],
                              'States': ['round_index','Player','Role','eliminated','possessed','vulnerable',
                                         'cool_down','active','cleansed_index','last_action_index'],
                              'Notifications': ['Player','Role','round_index','message','details']})

    def test_read_table(self):
        self.tables.update(SeabornTable.mark_down_to_dict_of_obj(self.FILE))
        seed(self.tables['Setup'].get_column('Seed')[0])
        #self.assertEqual(sorted(list(self.tables.keys())),
        #                 sorted(['Setup', 'Initial State', 'Actions', 'States', 'Notifications']))

        players = self.tables['Initial State'].get_column('Player')
        roles = self.tables['Initial State'].get_column('Role')
        self.rounds = self.tables['Setup'].get_column('Rounds')[0]

        for table in self.tables.keys():
            if 'Actions' in table:
                for item in self.tables[table].get_column('Player'):
                    self.assertIn(item,players)
                for row in self.tables[table]:
                    for i in [1, 2]:
                        self.assertIn(row['Target %d' % i], roles + players + [None,''])
            if 'States' in table:
                for item in self.tables[table].get_column('Role'):
                    self.assertIn(item,roles)
            if 'Notifications' in table:
                for item in self.tables[table].get_column('Player'):
                    self.assertIn(item,players)

        self.results['Setup'] = self.tables['Setup']
        self.results['Initial State'] = self.tables['Initial State']
        for i in range(1,self.rounds+1):
            self.results["Actions Round %d" % i] = self.tables["Actions Round %d" % i]
        for i in ['States','Notifications']:
            if i != 'Actions':
                for j in range(self.rounds+1):
                    print("Creating %s Round %d"%(i,j))
                    key = "%s Round %d"%(i,j)
                    if not key in self.tables.keys():
                        self.tables[key] = SeabornTable(columns = self.formatting[i])
                    self.results[key] = SeabornTable(columns = self.formatting[i])

    def test_signup_users_in_table(self):
        """
        This will dynamically signup the users from the table
        :return: OrderedDict {str <name>: Connection}
        """
        self.test_login()
        self.test_read_table()
        for row in self.tables['Initial State']:
            self.players[row['Player']] = self.test_user_signup.original_func(
                self,
                username=row['Player'],
                password=row['Password'],
                delete_if_exists=False)
        self.host = list(self.players.values())[0]

    def test_initiate_game(self):
        """
        This will create a game with the number of players in the table and the roles in the table.
        Then it will add the users to the game and start it.
        :return: game, players
        """
        self.test_signup_users_in_table()
        roles = sorted(list(set(self.tables['Initial State'].get_column('Role'))))
        self.assertEqual(len(roles), len(self.players))

        game = self.host.possessed.game.put(number_of_players=len(roles),
                                            role_list=roles,
                                            seed=self.tables['Setup'][0]['Seed'])

        self.game.update(game)
        roles = self.host.possessed.game.role.array.get(game_id=self.game['game_id'])
        self.roles.update({role['name']: role['role_id'] for role in roles})
        self.role_roster.update({role['role_id']: role['name'] for role in roles})
        for row in self.tables['Initial State']:
            conn = self.players[row[0]]
            player = conn.possessed.game.player.put(game_id=self.game['game_id'],
                                                    role_id=self.roles[row[1]])
            conn.player_id = player['player_id']
            self.roster[conn.player_id] = row[0]
            conn.notification_offset = 0
            self.player_id[conn.player_id] = row["Player"]
        self.host.possessed.game.start.put(game_id=self.game['game_id'])

    def test_review_state_0(self):
        if self.rounds >= 0:
            self.review_state(0)

    def test_getting_notification_0(self):
        if self.rounds >= 0:
            self.getting_notification(0)

    def test_submit_action_1(self):
        if self.rounds >= 1:
            self.submit_action(1)

    def test_end_round_1(self):
        if self.rounds >= 1:
            self.end_round(1)

    def test_review_state_1(self):
        if self.rounds >= 1:
            self.review_state(1)

    def test_getting_notification_1(self):
        if self.rounds >= 1:
            self.getting_notification(1)

    def test_submit_action_2(self):
        if self.rounds >= 2:
            self.submit_action(2)

    def test_end_round_2(self):
        if self.rounds >= 2:
            self.end_round(2)

    def test_review_state_2(self):
        if self.rounds >= 2:
            self.review_state(2)

    def test_getting_notification_2(self):
        if self.rounds >= 2:
            self.getting_notification(2)

    def test_submit_action_3(self):
        if self.rounds >= 3:
            self.submit_action(3)

    def test_end_round_3(self):
        if self.rounds >= 3:
            self.end_round(3)

    def test_review_state_3(self):
        if self.rounds >= 3:
            self.review_state(3)

    def test_getting_notification_3(self):
        if self.rounds >= 3:
            self.getting_notification(3)

    def test_submit_action_4(self):
        if self.rounds >= 4:
            self.submit_action(4)

    def test_end_round_4(self):
        if self.rounds >= 4:
            self.end_round(4)

    def test_review_state_4(self):
        if self.rounds >= 4:
            self.review_state(4)

    def test_getting_notification_4(self):
        if self.rounds >= 4:
            self.getting_notification(4)

    def test_submit_action_5(self):
        if self.rounds >= 5:
            self.submit_action(5)

    def test_end_round_5(self):
        if self.rounds >= 5:
            self.end_round(5)

    def test_review_state_5(self):
        if self.rounds >= 5:
            self.review_state(5)

    def test_getting_notification_5(self):
        if self.rounds >= 5:
            self.getting_notification(5)

    def test_submit_action_6(self):
        if self.rounds >= 6:
            self.submit_action(6)

    def test_end_round_6(self):
        if self.rounds >= 6:
            self.end_round(6)

    def test_review_state_6(self):
        if self.rounds >= 6:
            self.review_state(6)

    def test_getting_notification_6(self):
        if self.rounds >= 6:
            self.getting_notification(6)

    def test_submit_action_7(self):
        if self.rounds >= 7:
            self.submit_action(7)

    def test_end_round_7(self):
        if self.rounds >= 7:
            self.end_round(7)

    def test_review_state_7(self):
        if self.rounds >= 7:
            self.review_state(7)

    def test_getting_notification_7(self):
        if self.rounds >= 7:
            self.getting_notification(7)


    def review_state(self, round_index):
        if round_index:
            getattr(self, 'test_end_round_%s' % (round_index))()
        else:
            self.test_initiate_game()
        if round_index > self.tables['Setup'][0]['Rounds']:
            return

        print("starting review state %s" % round_index)
        states = self.conn.possessed.game.state.array.get(game_id=self.game['game_id'],
                                                          round_index=round_index)

        # columns=['round_index', 'Player', 'Role', 'eliminated', 'possessed', 'vulnerable',
        #         'cool_down', 'active', 'cleansed_index', 'last_action_index'])

        new_states = SeabornTable(states)
        new_states.insert(0, 'Role', compute_value_func=lambda row: self.role_roster[row['role_id']])
        new_states.insert(0, 'Player', compute_value_func=lambda row: self.roster[row['player_id']])
        new_states = SeabornTable(table=new_states.table,
                                  columns=self.formatting['States'])
        self.save_intermediate_results(new_state_rows=new_states, round_index = round_index)
        empty_table = new_states.filter('round_index', '!=', round_index)
        self.assertEqual(len(empty_table), 0)
        self.assertGreater(len(new_states), 0)

        answer = self.tables['States Round %d'%round_index]
        #for row in new_states:
        #    self.assertIn(row, answer)
        self.assertEqual(len(new_states), len(answer))

    def getting_notification(self, round_index):
        getattr(self, 'test_review_state_%s' % round_index)()
        if round_index > self.tables['Setup'][0]['Rounds']:
            return
        print("starting get notifications %s" % round_index)

        state = self.tables['States Round %d'%round_index]
        answer = self.tables['Notifications Round %d'%round_index]
        new_notifications = SeabornTable(columns=self.formatting['Notifications'])
        for player, conn in self.players.items():
            notification = conn.possessed.game.notification.array.get(game_id=self.game['game_id'],
                                                                      offset=conn.notification_offset)
            conn.notification_offset += len(notification)
            player_notifications = SeabornTable(notification)
            player_notifications.insert(1, 'Role',
                                        state.get_column('Role')[max(
                                            [(i if row == player else -1) for i, row in
                                             enumerate(state.get_column('Player'))])])
            player_notifications.insert(0, 'Player', player)
            new_notifications += player_notifications

        self.save_intermediate_results(new_notification_rows=new_notifications, round_index=round_index)
        #for i in range(len(new_notifications)):
        #    for j in new_notifications[i]._columns:
        #        if not player_notifications[j][i]:
        #            player_notifications[i][j] = ''


        #for row in new_notifications:
        #    self.assertIn(row, answer)
        self.assertEqual(len(new_notifications), len(answer))

    def submit_action(self, round_index):
        """
        new_moves declaration returns an empty list:
            List is of length 950+ before game_id filter, length 1 after
            List is empty after round_index filter
        :param round_index:
        :return:
        """
        getattr(self, 'test_getting_notification_%s' % (round_index - 1))()
        if round_index > self.tables['Setup'][0]['Rounds']:
            return
        print("starting submit action %s" % round_index)
        moves = self.tables['Actions Round %d'%round_index].filter('action', '!=', '')
        self.assertGreater(len(moves), 0)
        for row in moves:
            player1 = player2 = role1 = role2 = None
            player_id = self.players[row["Player"]].player_id

            action = row['action'] if row['action'] != 'Class' else row['Role']
            if row['Target 1'] in self.roles:
                role1 = self.roles[row['Target 1']]
            elif row['Target 1'] in self.players:
                player1 = self.players[row['Target 1']].player_id

            if row['Target 2'] in self.roles:
                role2 = self.roles[row['Target 2']]
            elif row['Target 2'] in self.players:
                player2 = self.players[row['Target 2']].player_id

            action = self.players[row["Player"]].possessed.game.action.put(
                game_id=self.game["game_id"],
                action=action,
                round_index=round_index,
                player_id=player_id,
                target_player1=player1,
                target_role1=role1,
                target_player2=player2,
                target_role2=role2)
            print(action)
        new_moves = self.conn.possessed.game.action.array.get(game_id=self.game["game_id"],
                                                              round_index=round_index)
        for move in new_moves:
            self.assertEqual(move['status'], 'not resolved', '%s %s to %s' % (
                self.roster[move['player_id']], move['status'], move['action']))
        self.assertEqual(len(moves), len(new_moves))

    def end_round(self, round_index):
        getattr(self, 'test_submit_action_%s' % round_index)()
        print("starting end round %s" % round_index)
        self.players["Ann"].possessed.put(game_id=self.game["game_id"], round_index=round_index)

    def save_intermediate_results(self, new_state_rows=None, new_notification_rows=None, round_index=0):
        if not self.RESULT_FILE:
            return
        if new_state_rows:
            key = 'States Round %d'%round_index
            self.results[key] += new_state_rows
            self.results[key].sort_by_key(['round_index', 'Player'])
        if new_notification_rows:
            key = 'Notifications Round %d'%round_index
            self.results[key] += new_notification_rows
        open(self.RESULT_FILE, 'w').write(SeabornTable.objs_to_mark_down(self.results, self.results.keys()))


class PossessedSimpleManual_2(PossessedSimpleManual):
    """
    Trader doesn't work when specifying players instead of roles
    """
    FILE = relative_path('answers/simple_manual_2.md')
    RESULT_FILE = relative_path('results/simple_manual_2.md')


class PossessedSimpleManual_3(PossessedSimpleManual):
    """
    Trader doesn't work when specifying players instead of roles
    """
    FILE = relative_path('answers/simple_manual_3.md')
    RESULT_FILE = relative_path('results/simple_manual_3.md')


class PossessedSimpleManual_5(PossessedSimpleManual):
    FILE = relative_path('answers/simple_manual_5.md')
    RESULT_FILE = relative_path('results/simple_manual_5.md')

if __name__ == "__main__":
    unittest.main()
