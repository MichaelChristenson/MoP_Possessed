__author__ = 'Michael Christenson'
__date__ = "01/12/25"
import os

domain_folder = os.path.abspath(__file__).split('flask')[0][:-1]
from seaborn.table.seaborn_table import *

from copy import deepcopy
from seaborn.test.standard_import import *
sys.path.append(os.path.join(domain_folder, 'flask'))

from bindings.python_bindings import Connection
from seaborn.file import relative_path
from collections import OrderedDict
from seaborn.calling_function import function_info

sys.path.append(os.path.join(domain_folder, 'flask'))
from test.base import BaseTest
from random import random, seed

DEBUG_SERVER = 'http://127.0.0.1:4999'
LOCAL_SERVER = 'http://local.api.mechanicsofplay.com'
AWS_SERVER = 'http://api.mechanicsofplay.com'
PROXY_DEBUG_SERVER = 'http://127.0.0.1:4777'
PROXY_AWS_SERVER = 'http://127.0.0.1:4888'
PROXIES = None  # {'http': 'http://127.0.0.1:4666', 'https': 'https://127.0.0.1:4665'}
ROLE_STATUS_ENUM = ['is vulnerable not implemented','perform action not implemented',
                    'npc action not implemented','active','probation','quarantined',
                    'abandoned']
ROLES_TABLE = ['Role']
SETUP_TABLE = ['Seed', 'Players', 'Rounds']

MANUAL_SETUP_TABLE = ['Seed','Rounds']
INITIAL_TABLE = ['Player','Role','Password']
COLUMNS = {'actions':['round_index','Player','Role','action','Target 1','Target 2','status'],
           'states':['round_index','Player','Role','eliminated','possessed','vulnerable',
                     'cool_down','active','cleansed_index','last_action_index'],
           'notifications':['Player','Role','round_index','message','details']}

ROLES = ['Judge', 'Executioner', 'Inspector', 'Silencer', 'Thief', 'Reporter', 'Spy',
         'Trader', 'Priest', 'Psychic', 'Jailer', 'Prophet', 'Assassin', 'Demagog', 'Medic',
         'Changeling', 'Bodyguard', 'Police']
EXCLUDE = ['Changeling', 'Bodyguard', 'Police', 'Demagog']
SAFE = ['Thief', 'Inspector', 'Judge', 'Executioner']
PARTNERS = {'Judge': 'Executioner', 'Executioner': 'Judge'}


class PossessedBaseTest(BaseTest):
    offset = {}

    @classmethod
    def generate_test_files(cls, roles=None, max_players=None, min_players=4, testing=False):
        """
        Generates a single file containing drafted roles that are not excluded from testing.
        :param roles: roles to be included, if a particular configuration is preferred
        :param max_players: maximum players preferred
        :param min_players: minimum players preferred
        :param testing: boolean for the current execution under test. If True, no file is produced
        :return: the name of the file that has been created
        """
        roles = roles or ROLES
        available = []
        taken = []
        for i in roles:
            if i not in EXCLUDE:
                available += [i]
        max_players = min(max_players, len(available)) if max_players else len(available)
        players = int((max_players - min_players + 1) * random() + min_players)
        tables = {}
        roles = []
        while len(roles) < players:
            index = int(random() * (len(available)))
            if available[index] not in taken:
                if (available[index] in PARTNERS.keys()):
                    if roles + 1 == players:
                        taken += [available[index]]
                        taken += [PARTNERS[available[index]]]
                    else:
                        roles += [[available[index]]]
                        roles += [PARTNERS[available[index]]]
                    available = available[:index]+available[index+1:]
                else:
                    roles += [[available[index]]]
                    available = available[:index]+available[index+1:]

        seed = int(100 * random())
        tables['Roles'] = SeabornTable(table = roles, columns = ROLES_TABLE)
        tables['Setup'] = SeabornTable(table = [[seed, players, int(8 * random() + 2)]],
                                       columns = SETUP_TABLE)
        file = 'test_file_%s_%s.md'%(players, seed)
        print("Creating %s"%file)
        if testing:
            for i in tables.keys():
                print(tables[i])
        else:
            open('answers/' + file, 'w').write(SeabornTable.objs_to_mark_down(tables))
        return file

    @classmethod
    def generate_role_tests(cls,  testing=False):
        """
        Generates tests for each role that isn't safe or excluded, adding the safe roles to populate the games
        :param testing: boolean for the current execution under test. If True, no files are produced
        :return: None
        """
        header_template = """
__author__ = "Michael Christenson's simple_gen"
import os

domain_folder = os.path.abspath(__file__).split('flask')[0][:-1]

from test.possessed_game.simple_automated import PossessedSimpleAutomated
from seaborn.test.standard_import import *


class PossessedRoleTest(PossessedSimpleAutomated):

    {funcs}
if __name__ == '__main__':
                unittest.main()
            """.strip().replace('\n           ','\n')

        function_template = """
def test_role_{role}(self):
                self.automated_game_against_file("answers/test_file_{role}.md")

            """.split('\n',1)[-1].replace('\n        ','\n')

        conn = Connection('Admin-User', cls.local_data.admin_password, 'user/login', base_uri = cls.SERVER,
                          proxies = PROXIES if cls.SERVER not in [PROXY_DEBUG_SERVER, PROXY_AWS_SERVER] else None)
        source = conn.possessed.role.array.get(ROLE_STATUS_ENUM)
        extract = []
        taken = []
        partner = {}
        name = 'test_file_%s'
        funcs = ''
        for item in source:
            extract += [item['name']]
            if item['partner']:
                partner[item['name']]=item['partner']
        for subject in extract:
            if subject in EXCLUDE + SAFE + taken:
                continue
            roles = [subject] + SAFE
            players = len(roles)
            tables = OrderedDict()
            report = []
            title = subject
            if subject in partner.keys():
                roles += [partner[subject]]
                title += '_'+partner[subject]
                taken += [partner[subject]]
            seed = len(''.join(roles))+players**players % 23
            for i in roles:
                report += [[i]]
            tables['Setup'] = SeabornTable(table = [[seed, players, 10]],
                                       columns = SETUP_TABLE)
            tables['Roles'] = SeabornTable(table = report, columns = ROLES_TABLE)
            if testing:
                for i in tables.keys():
                    print(tables[i])
            else:
                file_path = 'answers/' + name%title.lower()+'.md'
                if not os.path.isfile(file_path):
                    open(file_path, 'w').write(SeabornTable.objs_to_mark_down(tables))
                funcs += function_template.format(role = title.lower())
        open('simple_role.py', 'w').write(header_template.format(funcs = funcs))

    def import_from_id(self,game_id):
        """
        Pulls information from a given game_id and generates a .md
        file that expresses the data sufficiently to be read by simple_*
        :param game_id: the database ID that represents the game to be generated
        :return: None
        """
        self.generate_role_tests()
        conn = Connection('Admin-User', self.local_data.admin_password, 'user/login', base_uri=self.SERVER,
                          proxies=PROXIES if self.SERVER not in [PROXY_DEBUG_SERVER, PROXY_AWS_SERVER] else None)
        source = conn.possessed.role.array.get(ROLE_STATUS_ENUM)
        targets = {'actions':['Target 1','Target 2','Player'],
                   'notifications':['Player','Role'],
                   'states':['Player','Role']}
        designates = {'Target 1':'target_1','Target 2':'target_2','Player':'player_id','Role':'role_id'}
        subdiv = ['roles','players','states','actions','notifications']
        data = {}
        tables = {}
        roster = {}
        classes = {}
        register = {}
        rounds = 0
        file = 'test_game_id_%s.md'%game_id
        dict_dir = {'target_1':[classes,roster,{None:None}],
                    'target_2':[classes,roster,{None:None}],
                    'player_id':roster,'role_id':[classes,{None:None}]}
        for item in source:
            classes[item['role_id']]=item['name']
        by_player=['notifications']
        by_round=['actions','states','notifications']
        for subject in subdiv:
            kwargs = {'game_id':game_id}
            if subject in by_player:
                data[subject]=[]
                for item in data['players']:
                    kwargs['player_id']=item['player_id']
                    data[subject] += [getattr(conn.possessed.game,subject[:-1]).array.get(**kwargs)]
            else:
                data[subject] = getattr(conn.possessed.game, subject[:-1]).array.get(**kwargs)
            if subject == 'players':
                for item in data['players']:
                    roster[item['player_id']]=item['username']
            if subject in by_round:
                rounds_max = 0
                rounds_min = None
                comp = 'comp_'+subject
                data[comp] = {}
                checklist = {}
                for item in data[subject]:
                    if subject == 'states':
                        if item['round_index'] not in register.keys():
                            register[item['round_index']]={}
                        register[item['round_index']][item['player_id']]=item['role_id']
                    if type(item) == list:
                        for sub in item:
                            if sub['round_index'] not in data[comp].keys():
                                data[comp][sub['round_index']]=[]
                                checklist[sub['round_index']] = []
                            if sub['message']=='broadcast':
                                if sub['details'] not in checklist[sub['round_index']]:
                                    checklist[sub['round_index']] += [sub['details']]
                                    for ident in roster.keys():
                                        ret = deepcopy(sub)
                                        data[comp][sub['round_index']]+=[ret]
                                        data[comp][sub['round_index']][-1]['player_id']=ident
                                        data[comp][sub['round_index']][-1]['role_id']=\
                                            register[sub['round_index']][ident]
                                continue
                            data[comp][sub['round_index']] += [sub]
                            data[comp][sub['round_index']][-1]['role_id']=register[sub['round_index']][sub['player_id']]
                            rounds_max = max(sub['round_index'], rounds_max)
                            rounds_min = min(sub['round_index'],
                                             rounds_min if rounds_min != None else sub['round_index'])
                    else:
                        if item['round_index'] not in data[comp].keys():
                            data[comp][item['round_index']]=[]
                        data[comp][item['round_index']] += [item]
                        rounds_max = max(item['round_index'], rounds_max)
                        rounds_min = min(item['round_index'], rounds_min if rounds_min != None else item['round_index'])
                for i in sorted(data[comp].keys()):
                    key = subject[0].upper()+subject[1:]+' Round %s'%i
                    tables[key]=SeabornTable(
                        columns=slip(COLUMNS[subject],targets[subject],[designates[j] for j in targets[subject]]),
                        table=data[comp][i])
                    for j in targets[subject]:
                        oper = {}
                        temp = dict_dir[designates[j]]
                        if type(temp) == list:
                            for k in temp:
                                oper.update(k)
                        else:
                            oper.update(temp)
                        tables[key].insert(0, j, compute_value_func=lambda row: oper[row[designates[j]]])
                rounds = max(rounds,rounds_max)
        report = OrderedDict()
        for turn in range(rounds+1):
            for subject in by_round:
                key = subject[0].upper()+subject[1:]+' Round %s'%turn
                report[key]=SeabornTable(columns=COLUMNS[subject])
                if key in tables.keys():
                    report[key]=SeabornTable(columns=COLUMNS[subject],table=tables[key].table)
        open('answers/' + file, 'w').write(SeabornTable.objs_to_mark_down(report))

    def generate_many(cls):
        """
        Generates 10 random test games, then prints out the functions necessary to run them
        :return: None
        """
        test = []
        for i in range(10):
            test += [cls.generate_test_files().replace('.md', '')]
        for i in range(10):
            print("""\tdef %s(self):\n\t\tself.automated_game_against_file(self.get_file_from_test_name())""" % test[i])

    def automated_game_against_file(self, filename):
        """
        Reads in the file and executes the game represented by that file.
        :param filename: file in question, with the path relative to execution
        :return: None
        """
        print('\n\n'+filename.replace('answers/','')+'\n\n')
        result_file = relative_path(filename.replace('answers', 'results'))

        tables = SeabornTable.mark_down_to_dict_of_obj(relative_path(filename))
        tables.columns = ['round_index','Player','Role','message','details']
        role_list = list(tables['Roles'].get_column('Role'))
        roles = {role['role_id']: role['name'] for role in self.ann.possessed.role.array.get()}
        game = self.ann.possessed.game.put(number_of_players=tables['Setup'][0]['Players'],
                                           role_list=role_list,
                                           seed=tables['Setup'][0]['Players'])
        self.ann.possessed.game.start.put(game_id=game['game_id'])
        players = {player['player_id']: player['username']
                   for player in self.ann.possessed.game.player.array.get(game_id=game['game_id'])}
        self.offset = {player['player_id']: 0
                       for player in self.ann.possessed.game.player.array.get(game_id=game['game_id'])}
        result_tables = OrderedDict()
        result_tables['Setup'] = tables['Setup']
        result_tables['Roles'] = tables['Roles']
        result_tables["States Round %s" % 0] = self.get_states(game['game_id'], 0, players, roles)
        result_tables["Notifications Round %s" % 0] = self.get_notifications(
            game['game_id'], 0, players, roles, list(result_tables.values())[-1])

        for round_index in range(1, tables['Setup'][0]['Rounds'] + 1):
            try:
                self.ann.possessed.post(game_id=game['game_id'],
                                        round_index=round_index)
                result_tables["Actions Round %s" % (round_index)] = \
                    self.get_actions(game['game_id'], round_index, players, roles)
                result_tables["States Round %s" % round_index] = \
                    self.get_states(game['game_id'], round_index, players, roles)
                result_tables["Notifications Round %s" % round_index] = \
                    self.get_notifications(game['game_id'], round_index, players, roles,
                                           list(result_tables.values())[-1])
            except Exception as e:
                open(result_file, 'w').write(SeabornTable.objs_to_mark_down(result_tables))
                raise

        open(result_file, 'w').write(SeabornTable.objs_to_mark_down(result_tables))

        for key in tables.keys():
            if str(tables.get(key, '')) != str(result_tables.get(key, '')):
                raise Exception("Table %s don't match\n\n%s\n\n%s" % (key,
                                                                      str(tables.get(key, '')),
                                                                      str(result_tables.get(key, ''))))

    def get_actions(self, game_id, round_index, players, roles):
        actions = self.conn.possessed.game.action.array.get(game_id=game_id, round_index=round_index)
        actions = SeabornTable(actions)

        actions.insert(0, 'Player', compute_value_func=lambda row: players[row['player_id']])
        actions.insert(0, 'Target 1', compute_key='target_1',
                       compute_value_func= lambda target: roles.get(target, players.get(target,target)))
        actions.insert(0, 'Target 2', compute_key='target_2',
                       compute_value_func= lambda target: roles.get(target, players.get(target,target)))
        actions.columns = ['round_index', 'Player', 'action', 'Target 1', 'Target 2', 'status']
        return actions

    def get_states(self, game_id, round_index, players, roles):
        states = self.conn.possessed.game.state.array.get(game_id=game_id, round_index=round_index)
        states = SeabornTable(states)
        states.insert(0, 'Role', compute_value_func=lambda row: roles[row['role_id']])
        states.insert(0, 'Player', compute_value_func=lambda row: players[row['player_id']])
        states.columns = ['round_index', 'Player', 'Role', 'eliminated', 'possessed', 'vulnerable', 'cool_down',
                          'active', 'cleansed_index', 'last_action_index']
        return states

    def get_notifications(self, game_id, round_index, players, roles, states):
        table = SeabornTable(columns=['round_index', 'Player', 'Role', 'message', 'details'])
        player_role = {state['Player']: state['Role'] for state in states}

        for player_id in sorted(players.keys()):
            notifications = self.conn.possessed.game.notification.array.get(game_id=game_id,
                                                                            player_id=player_id,
                                                                            offset=self.offset[player_id])
            self.offset[player_id] += len(notifications)
            notifications = SeabornTable(notifications)
            notifications.insert(0, 'Player', players[player_id])
            notifications.insert(0, 'Role', player_role[players[player_id]])
            table += notifications
        return table

    def get_file_from_test_name(self):
        test_function = function_info(2)['function_name']
        return 'answers/%s.md'%test_function

    def generate_test_based_on_game_id(self, game_id=1):
        self.import_from_id(game_id)

def slip(roster, target, designate):
    if type(target)==list:
        temp = roster
        for i in range(len(target)):
            temp = slip(temp, target[i], designate[i])
        return temp
    else:
        return '!'.join(roster).replace(target, designate).split('!')

if __name__ == '__main__':
    mode = (os.sys.argv+['role'])[1]
    if mode == 'role':
        PossessedBaseTest.test_role_test_generation()
    else:
        PossessedBaseTest.generate_test_based_on_game_id(eval(mode))
