#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 5    | 6       | 4       |

#### Roles
| Role         |
| :----------- |
| Thief        |
| Executioner  |
| Psychic      |
| Priest       |
| Assassin     |
| Prophet      |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Assassin    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Thief       | role change | Your Role is Thief        |
| 0           | NPC Ann | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Bob | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Cal | Assassin    | possessed   | You are Possessed         |
| 0           | NPC Dan | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Dan | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ed  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Priest      | role change | Your Role is Priest       |
| 0           | NPC Fae | Priest      | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 1           | NPC Ann | Thief    | NPC Cal  |          | successful  |
| 1           | NPC Bob | Psychic  |          |          | successful  |
| 1           | NPC Cal | Assassin | Prophet  |          | successful  |
| 1           | NPC Dan | Prophet  | NPC Fae  |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Fae | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Assassin    | False      | True      | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Thief       | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ann | Thief       | broadcast | I (NPC Bob) am the Psychic and the Prophet is not possessed  |
| 1           | NPC Ann | Thief       | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed    |
| 1           | NPC Bob | Psychic     | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Prophet is not possessed  |
| 1           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed    |
| 1           | NPC Bob | Psychic     | reveal    | Player: NPC Fae is not possessed                             |
| 1           | NPC Bob | Psychic     | reveal    | Player: NPC Dan is not possessed                             |
| 1           | NPC Cal | Assassin    | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Cal | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Prophet is not possessed  |
| 1           | NPC Cal | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed    |
| 1           | NPC Dan | Prophet     | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Dan | Prophet     | broadcast | I (NPC Bob) am the Psychic and the Prophet is not possessed  |
| 1           | NPC Dan | Prophet     | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed    |
| 1           | NPC Ed  | Executioner | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ed  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Prophet is not possessed  |
| 1           | NPC Ed  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed    |
| 1           | NPC Fae | Priest      | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Fae | Priest      | broadcast | I (NPC Bob) am the Psychic and the Prophet is not possessed  |
| 1           | NPC Fae | Priest      | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed    |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Bob | Psychic |          |          | successful  |
| 2           | NPC Dan | Prophet | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ann | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Fae | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Assassin    | False      | True      | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 2           | NPC Ann | Thief       | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed   |
| 2           | NPC Ann | Thief       | broadcast | I (NPC Bob) am the Psychic and the Prophet is not possessed  |
| 2           | NPC Ann | Thief       | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed    |
| 2           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed   |
| 2           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Prophet is not possessed  |
| 2           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed    |
| 2           | NPC Bob | Psychic     | reveal    | Player: NPC Ann is not possessed                             |
| 2           | NPC Bob | Psychic     | reveal    | Player: NPC Dan is not possessed                             |
| 2           | NPC Cal | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed   |
| 2           | NPC Cal | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Prophet is not possessed  |
| 2           | NPC Cal | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed    |
| 2           | NPC Dan | Prophet     | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed   |
| 2           | NPC Dan | Prophet     | broadcast | I (NPC Bob) am the Psychic and the Prophet is not possessed  |
| 2           | NPC Dan | Prophet     | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed    |
| 2           | NPC Ed  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed   |
| 2           | NPC Ed  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Prophet is not possessed  |
| 2           | NPC Ed  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed    |
| 2           | NPC Fae | Priest      | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed   |
| 2           | NPC Fae | Priest      | broadcast | I (NPC Bob) am the Psychic and the Prophet is not possessed  |
| 2           | NPC Fae | Priest      | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed    |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 3           | NPC Ann | Thief    | NPC Dan  |          | successful  |
| 3           | NPC Bob | Psychic  |          |          | successful  |
| 3           | NPC Cal | Assassin | Prophet  |          | successful  |
| 3           | NPC Dan | Prophet  | NPC Cal  |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ann | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Fae | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Assassin    | False      | True      | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Prophet     | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 3           | NPC Ann | Thief       | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable      |
| 3           | NPC Ann | Thief       | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed        |
| 3           | NPC Ann | Thief       | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed       |
| 3           | NPC Ann | Thief       | broadcast | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Bob | Psychic     | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable      |
| 3           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed        |
| 3           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed       |
| 3           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Bob | Psychic     | reveal    | Player: NPC Ann is not possessed                                 |
| 3           | NPC Bob | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 3           | NPC Cal | Assassin    | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable      |
| 3           | NPC Cal | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed        |
| 3           | NPC Cal | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed       |
| 3           | NPC Cal | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Dan | Prophet     | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable      |
| 3           | NPC Dan | Prophet     | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed        |
| 3           | NPC Dan | Prophet     | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed       |
| 3           | NPC Dan | Prophet     | broadcast | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Ed  | Executioner | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable      |
| 3           | NPC Ed  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed        |
| 3           | NPC Ed  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed       |
| 3           | NPC Ed  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Fae | Priest      | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable      |
| 3           | NPC Fae | Priest      | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed        |
| 3           | NPC Fae | Priest      | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed       |
| 3           | NPC Fae | Priest      | broadcast | I (NPC Bob) am the Psychic and the Executioner is not possessed  |

#### Actions Round 4
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 4           | NPC Bob | Psychic |          |          | successful  |
| 4           | NPC Dan | Prophet | NPC Cal  |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ann | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Fae | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Assassin    | False      | True      | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Prophet     | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 4           | NPC Ann | Thief       | broadcast | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ann | Thief       | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed       |
| 4           | NPC Ann | Thief       | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed        |
| 4           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed       |
| 4           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed        |
| 4           | NPC Bob | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 4           | NPC Bob | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 4           | NPC Cal | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Cal | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed       |
| 4           | NPC Cal | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed        |
| 4           | NPC Dan | Prophet     | broadcast | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Dan | Prophet     | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed       |
| 4           | NPC Dan | Prophet     | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed        |
| 4           | NPC Ed  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ed  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed       |
| 4           | NPC Ed  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed        |
| 4           | NPC Fae | Priest      | broadcast | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Fae | Priest      | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed       |
| 4           | NPC Fae | Priest      | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed        |