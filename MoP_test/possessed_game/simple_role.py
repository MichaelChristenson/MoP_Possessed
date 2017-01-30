__author__ = "Michael Christenson's simple_gen"
import os

domain_folder = os.path.abspath(__file__).split('flask')[0][:-1]

from test.possessed_game.simple_automated import PossessedSimpleAutomated
from seaborn.test.standard_import import *


class PossessedRoleTest(PossessedSimpleAutomated):

    def test_role_silencer(self):
        self.automated_game_against_file("answers/test_file_silencer.md")

    def test_role_reporter(self):
        self.automated_game_against_file("answers/test_file_reporter.md")

    def test_role_spy(self):
        self.automated_game_against_file("answers/test_file_spy.md")

    def test_role_trader(self):
        self.automated_game_against_file("answers/test_file_trader.md")

    def test_role_priest(self):
        self.automated_game_against_file("answers/test_file_priest.md")

    def test_role_psychic(self):
        self.automated_game_against_file("answers/test_file_psychic.md")

    def test_role_jailer(self):
        self.automated_game_against_file("answers/test_file_jailer.md")

    def test_role_prophet(self):
        self.automated_game_against_file("answers/test_file_prophet.md")

    def test_role_assassin(self):
        self.automated_game_against_file("answers/test_file_assassin.md")

    def test_role_medic(self):
        self.automated_game_against_file("answers/test_file_medic.md")

    
if __name__ == '__main__':
     unittest.main()