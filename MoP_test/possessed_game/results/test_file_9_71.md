#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 71   | 9       | 4       |

#### Roles
| Role         |
| :----------- |
| Prophet      |
| Medic        |
| Silencer     |
| Judge        |
| Spy          |
| Executioner  |
| Inspector    |
| Assassin     |
| Thief        |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Fae | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ann | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Bob | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Medic       | role change | Your Role is Medic        |
| 0           | NPC Cal | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Thief       | role change | Your Role is Thief        |
| 0           | NPC Dan | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Ed  | Spy         | possessed   | You are Possessed         |
| 0           | NPC Fae | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Fae | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Gia | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Gia | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Han | Judge       | role change | Your Role is Judge        |
| 0           | NPC Han | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Igi | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Igi | Silencer    | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Bob | Inspector | NPC Fae  |          | successful  |
| 1           | NPC Cal | Medic     | NPC Igi  |          | successful  |
| 1           | NPC Dan | Thief     | NPC Han  |          | successful  |
| 1           | NPC Ed  | Spy       |          |          | successful  |
| 1           | NPC Fae | Prophet   | NPC Bob  |          | successful  |
| 1           | NPC Gia | Assassin  | Judge    |          | successful  |
| 1           | NPC Han | Judge     | Assassin |          | successful  |
| 1           | NPC Igi | Silencer  | NPC Cal  |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Fae | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Igi | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Gia | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Executioner | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed     |
| 1           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Thief and I have made NPC Han vulnerable  |
| 1           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed     |
| 1           | NPC Bob | Inspector   | broadcast | I (NPC Dan) am the Thief and I have made NPC Han vulnerable  |
| 1           | NPC Bob | Inspector   | reveal    | Prophet is Innocent                                          |
| 1           | NPC Cal | Medic       | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed     |
| 1           | NPC Cal | Medic       | broadcast | I (NPC Dan) am the Thief and I have made NPC Han vulnerable  |
| 1           | NPC Cal | Medic       | silenced  | You have been silenced                                       |
| 1           | NPC Dan | Thief       | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed     |
| 1           | NPC Dan | Thief       | broadcast | I (NPC Dan) am the Thief and I have made NPC Han vulnerable  |
| 1           | NPC Ed  | Spy         | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed     |
| 1           | NPC Ed  | Spy         | broadcast | I (NPC Dan) am the Thief and I have made NPC Han vulnerable  |
| 1           | NPC Ed  | Spy         | reveal    | NPC Igi is targeting NPC Cal                                 |
| 1           | NPC Ed  | Spy         | reveal    | NPC Han is targeting NPC Gia                                 |
| 1           | NPC Ed  | Spy         | reveal    | NPC Bob is targeting NPC Fae                                 |
| 1           | NPC Ed  | Spy         | reveal    | NPC Dan is targeting NPC Han                                 |
| 1           | NPC Fae | Prophet     | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed     |
| 1           | NPC Fae | Prophet     | broadcast | I (NPC Dan) am the Thief and I have made NPC Han vulnerable  |
| 1           | NPC Gia | Assassin    | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed     |
| 1           | NPC Gia | Assassin    | broadcast | I (NPC Dan) am the Thief and I have made NPC Han vulnerable  |
| 1           | NPC Han | Judge       | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed     |
| 1           | NPC Han | Judge       | broadcast | I (NPC Dan) am the Thief and I have made NPC Han vulnerable  |
| 1           | NPC Igi | Silencer    | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed     |
| 1           | NPC Igi | Silencer    | broadcast | I (NPC Dan) am the Thief and I have made NPC Han vulnerable  |

#### Actions Round 2
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 2           | NPC Cal | Medic    | NPC Han  |          | successful  |
| 2           | NPC Ed  | Spy      |          |          | successful  |
| 2           | NPC Fae | Prophet  | NPC Igi  |          | successful  |
| 2           | NPC Han | Judge    | Prophet  |          | successful  |
| 2           | NPC Igi | Silencer | NPC Ed   |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Fae | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Igi | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Han | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                 |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------ |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi  |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Cal  |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi  |
| 2           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Cal  |
| 2           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 2           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 2           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Cal  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi  |
| 2           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Cal  |
| 2           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 2           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 2           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi  |
| 2           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Cal  |
| 2           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 2           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 2           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Ed  | Spy         | silenced  | You have been silenced                                  |
| 2           | NPC Ed  | Spy         | reveal    | NPC Fae is targeting NPC Bob                            |
| 2           | NPC Ed  | Spy         | reveal    | NPC Cal is targeting NPC Igi                            |
| 2           | NPC Ed  | Spy         | reveal    | NPC Igi is targeting NPC Ed                             |
| 2           | NPC Ed  | Spy         | reveal    | NPC Han is targeting NPC Fae                            |
| 2           | NPC Ed  | Spy         | reveal    | NPC Bob is targeting NPC Fae                            |
| 2           | NPC Ed  | Spy         | reveal    | NPC Gia is targeting NPC Han                            |
| 2           | NPC Ed  | Spy         | reveal    | NPC Dan is targeting NPC Han                            |
| 2           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi  |
| 2           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Cal  |
| 2           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 2           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 2           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi  |
| 2           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Cal  |
| 2           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 2           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 2           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi  |
| 2           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Cal  |
| 2           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 2           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 2           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi  |
| 2           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Cal  |
| 2           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 2           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 2           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Han  |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 3           | NPC Bob | Inspector | NPC Dan  |          | successful  |
| 3           | NPC Cal | Medic     | NPC Ed   |          | successful  |
| 3           | NPC Dan | Thief     | NPC Ann  |          | successful  |
| 3           | NPC Ed  | Spy       |          |          | successful  |
| 3           | NPC Fae | Prophet   | NPC Gia  |          | successful  |
| 3           | NPC Gia | Assassin  | Judge    |          | successful  |
| 3           | NPC Han | Judge     | Assassin |          | successful  |
| 3           | NPC Igi | Silencer  | NPC Fae  |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Fae | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Igi | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Han | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Bob | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Gia | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann | Executioner | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed     |
| 3           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed     |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Bob | Inspector   | reveal    | Thief is Innocent                                            |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed     |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Dan | Thief       | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed     |
| 3           | NPC Dan | Thief       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Ed  | Spy         | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed     |
| 3           | NPC Ed  | Spy         | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Ed  | Spy         | reveal    | NPC Fae is targeting NPC Igi                                 |
| 3           | NPC Ed  | Spy         | reveal    | NPC Cal is targeting NPC Han                                 |
| 3           | NPC Ed  | Spy         | reveal    | NPC Igi is targeting NPC Fae                                 |
| 3           | NPC Ed  | Spy         | reveal    | NPC Han is targeting NPC Gia                                 |
| 3           | NPC Ed  | Spy         | reveal    | NPC Bob is targeting NPC Dan                                 |
| 3           | NPC Ed  | Spy         | reveal    | NPC Gia is targeting NPC Han                                 |
| 3           | NPC Ed  | Spy         | reveal    | NPC Dan is targeting NPC Ann                                 |
| 3           | NPC Fae | Prophet     | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed     |
| 3           | NPC Fae | Prophet     | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Fae | Prophet     | silenced  | You have been silenced                                       |
| 3           | NPC Gia | Assassin    | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed     |
| 3           | NPC Gia | Assassin    | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Han | Judge       | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed     |
| 3           | NPC Han | Judge       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Igi | Silencer    | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed     |
| 3           | NPC Igi | Silencer    | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |

#### Actions Round 4
| round_index | Player  | action   | Target 1  | Target 2 | status      |
| :-----------| :-------| :--------| :---------| :--------| :---------- |
| 4           | NPC Cal | Medic    | NPC Ann   |          | successful  |
| 4           | NPC Ed  | Spy      |           |          | successful  |
| 4           | NPC Fae | Prophet  | NPC Han   |          | successful  |
| 4           | NPC Han | Judge    | Inspector |          | successful  |
| 4           | NPC Igi | Silencer | NPC Bob   |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Fae | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Igi | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Han | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Bob | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Gia | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                 |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------ |
| 4           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia  |
| 4           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae  |
| 4           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 4           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Dan  |
| 4           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 4           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann  |
| 4           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia  |
| 4           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae  |
| 4           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 4           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Dan  |
| 4           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 4           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann  |
| 4           | NPC Bob | Inspector   | silenced  | You have been silenced                                  |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia  |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae  |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Dan  |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann  |
| 4           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia  |
| 4           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae  |
| 4           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 4           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Dan  |
| 4           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 4           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann  |
| 4           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia  |
| 4           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae  |
| 4           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 4           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Dan  |
| 4           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 4           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann  |
| 4           | NPC Ed  | Spy         | reveal    | NPC Fae is targeting NPC Gia                            |
| 4           | NPC Ed  | Spy         | reveal    | NPC Cal is targeting NPC Ed                             |
| 4           | NPC Ed  | Spy         | reveal    | NPC Igi is targeting NPC Bob                            |
| 4           | NPC Ed  | Spy         | reveal    | NPC Han is targeting NPC Bob                            |
| 4           | NPC Ed  | Spy         | reveal    | NPC Bob is targeting NPC Dan                            |
| 4           | NPC Ed  | Spy         | reveal    | NPC Gia is targeting NPC Han                            |
| 4           | NPC Ed  | Spy         | reveal    | NPC Dan is targeting NPC Ann                            |
| 4           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia  |
| 4           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae  |
| 4           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 4           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Dan  |
| 4           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 4           | NPC Fae | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann  |
| 4           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia  |
| 4           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae  |
| 4           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 4           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Dan  |
| 4           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 4           | NPC Gia | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann  |
| 4           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia  |
| 4           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae  |
| 4           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 4           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Dan  |
| 4           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 4           | NPC Han | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann  |
| 4           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia  |
| 4           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae  |
| 4           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Gia  |
| 4           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Dan  |
| 4           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han  |
| 4           | NPC Igi | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann  |