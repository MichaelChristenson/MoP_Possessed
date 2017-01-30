#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 77   | 9       | 7       |

#### Roles
| Role       |
| :--------- |
| Reporter   |
| Demagog    |
| Silencer   |
| Spy        |
| Trader     |
| Inspector  |
| Assassin   |
| Thief      |
| Judge      |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Fae | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Demagog   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi | Silencer  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Trader    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Assassin  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Ann | Inspector | possessed   | You are Not Possessed   |
| 0           | NPC Bob | Assassin  | role change | Your Role is Assassin   |
| 0           | NPC Bob | Assassin  | possessed   | You are Not Possessed   |
| 0           | NPC Cal | Demagog   | role change | Your Role is Demagog    |
| 0           | NPC Cal | Demagog   | possessed   | You are Not Possessed   |
| 0           | NPC Dan | Judge     | role change | Your Role is Judge      |
| 0           | NPC Dan | Judge     | possessed   | You are Not Possessed   |
| 0           | NPC Ed  | Trader    | role change | Your Role is Trader     |
| 0           | NPC Ed  | Trader    | possessed   | You are Possessed       |
| 0           | NPC Fae | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Fae | Reporter  | possessed   | You are Not Possessed   |
| 0           | NPC Gia | Thief     | role change | Your Role is Thief      |
| 0           | NPC Gia | Thief     | possessed   | You are Not Possessed   |
| 0           | NPC Han | Spy       | role change | Your Role is Spy        |
| 0           | NPC Han | Spy       | possessed   | You are Not Possessed   |
| 0           | NPC Igi | Silencer  | role change | Your Role is Silencer   |
| 0           | NPC Igi | Silencer  | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status                         |
| :-----------| :-------| :---------| :--------| :--------| :----------------------------- |
| 1           | NPC Ann | Inspector | NPC Fae  |          | successful                     |
| 1           | NPC Bob | Assassin  | Spy      |          | successful                     |
| 1           | NPC Cal | Demagog   | Assassin |          | voting in progress             |
| 1           | NPC Dan | Judge     | Spy      |          | successful                     |
| 1           | NPC Ed  | Trader    | NPC Bob  | NPC Cal  | failed because not vulnerable  |
| 1           | NPC Fae | Reporter  | NPC Igi  |          | successful                     |
| 1           | NPC Gia | Thief     | NPC Fae  |          | successful                     |
| 1           | NPC Han | Spy       |          |          | successful                     |
| 1           | NPC Igi | Silencer  | NPC Ed   |          | successful                     |

#### States Round 1
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Fae | Reporter  | False      | False     | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Cal | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Igi | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Han | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Trader    | False      | True      | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Ann | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Gia | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Inspector | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 1           | NPC Ann | Inspector | broadcast | I (NPC Fae) am the Reporter and NPC Igi is the Silencer      |
| 1           | NPC Ann | Inspector | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Ann | Inspector | reveal    | Reporter is Innocent                                         |
| 1           | NPC Ann | Inspector | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 1           | NPC Bob | Assassin  | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 1           | NPC Bob | Assassin  | broadcast | I (NPC Fae) am the Reporter and NPC Igi is the Silencer      |
| 1           | NPC Bob | Assassin  | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Bob | Assassin  | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 1           | NPC Cal | Demagog   | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 1           | NPC Cal | Demagog   | broadcast | I (NPC Fae) am the Reporter and NPC Igi is the Silencer      |
| 1           | NPC Cal | Demagog   | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Cal | Demagog   | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 1           | NPC Dan | Judge     | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 1           | NPC Dan | Judge     | broadcast | I (NPC Fae) am the Reporter and NPC Igi is the Silencer      |
| 1           | NPC Dan | Judge     | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Dan | Judge     | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 1           | NPC Ed  | Trader    | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 1           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Reporter and NPC Igi is the Silencer      |
| 1           | NPC Ed  | Trader    | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Ed  | Trader    | silenced  | You have been silenced                                       |
| 1           | NPC Ed  | Trader    | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 1           | NPC Fae | Reporter  | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 1           | NPC Fae | Reporter  | broadcast | I (NPC Fae) am the Reporter and NPC Igi is the Silencer      |
| 1           | NPC Fae | Reporter  | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Fae | Reporter  | reveal    | NPC Igi is Silencer                                          |
| 1           | NPC Fae | Reporter  | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 1           | NPC Gia | Thief     | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 1           | NPC Gia | Thief     | broadcast | I (NPC Fae) am the Reporter and NPC Igi is the Silencer      |
| 1           | NPC Gia | Thief     | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Gia | Thief     | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 1           | NPC Han | Spy       | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 1           | NPC Han | Spy       | broadcast | I (NPC Fae) am the Reporter and NPC Igi is the Silencer      |
| 1           | NPC Han | Spy       | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Han | Spy       | reveal    | NPC Fae is targeting NPC Igi                                 |
| 1           | NPC Han | Spy       | reveal    | NPC Igi is targeting NPC Ed                                  |
| 1           | NPC Han | Spy       | reveal    | NPC Ann is targeting NPC Fae                                 |
| 1           | NPC Han | Spy       | reveal    | NPC Gia is targeting NPC Fae                                 |
| 1           | NPC Han | Spy       | reveal    | NPC Dan is targeting NPC Han                                 |
| 1           | NPC Han | Spy       | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 1           | NPC Igi | Silencer  | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 1           | NPC Igi | Silencer  | broadcast | I (NPC Fae) am the Reporter and NPC Igi is the Silencer      |
| 1           | NPC Igi | Silencer  | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Igi | Silencer  | vote      | Demagog has initiated a vote on eliminating Assassin         |

#### Actions Round 2
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 2           | NPC Dan | Judge    | Thief    |          | successful  |
| 2           | NPC Han | Spy      |          |          | successful  |
| 2           | NPC Igi | Silencer | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Fae | Reporter  | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Cal | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Igi | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Han | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Trader    | False      | True      | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Ann | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Bob | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role      | message   | details                                                  |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------- |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ed   |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae  |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Ann | Inspector | silenced  | You have been silenced                                   |
| 2           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ed   |
| 2           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae  |
| 2           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 2           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ed   |
| 2           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae  |
| 2           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 2           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ed   |
| 2           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae  |
| 2           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 2           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ed   |
| 2           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae  |
| 2           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 2           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ed   |
| 2           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae  |
| 2           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 2           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ed   |
| 2           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae  |
| 2           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 2           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ed   |
| 2           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae  |
| 2           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 2           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Han | Spy       | reveal    | NPC Fae is targeting NPC Igi                             |
| 2           | NPC Han | Spy       | reveal    | NPC Cal is targeting NPC Bob                             |
| 2           | NPC Han | Spy       | reveal    | NPC Igi is targeting NPC Ann                             |
| 2           | NPC Han | Spy       | reveal    | NPC Ed is targeting NPC Bob                              |
| 2           | NPC Han | Spy       | reveal    | NPC Ed is targeting NPC Bob                              |
| 2           | NPC Han | Spy       | reveal    | NPC Ann is targeting NPC Fae                             |
| 2           | NPC Han | Spy       | reveal    | NPC Bob is targeting NPC Han                             |
| 2           | NPC Han | Spy       | reveal    | NPC Gia is targeting NPC Fae                             |
| 2           | NPC Han | Spy       | reveal    | NPC Dan is targeting NPC Gia                             |
| 2           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ed   |
| 2           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae  |
| 2           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 2           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han  |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status              |
| :-----------| :-------| :---------| :--------| :--------| :------------------ |
| 3           | NPC Ann | Inspector | NPC Gia  |          | successful          |
| 3           | NPC Bob | Assassin  | Spy      |          | successful          |
| 3           | NPC Cal | Demagog   | Assassin |          | voting in progress  |
| 3           | NPC Dan | Judge     | Reporter |          | successful          |
| 3           | NPC Fae | Reporter  | NPC Ed   |          | successful          |
| 3           | NPC Gia | Thief     | NPC Ann  |          | successful          |
| 3           | NPC Han | Spy       |          |          | successful          |
| 3           | NPC Igi | Silencer  | NPC Bob  |          | successful          |

#### States Round 3
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Fae | Reporter  | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Cal | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Igi | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Han | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Trader    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann | Inspector | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Bob | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Gia | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader         |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi      |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ann      |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae      |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Gia      |
| 3           | NPC Ann | Inspector | reveal    | Thief is Innocent                                            |
| 3           | NPC Ann | Inspector | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Bob | Assassin  | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader         |
| 3           | NPC Bob | Assassin  | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi      |
| 3           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 3           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ann      |
| 3           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae      |
| 3           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Gia      |
| 3           | NPC Bob | Assassin  | silenced  | You have been silenced                                       |
| 3           | NPC Bob | Assassin  | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Cal | Demagog   | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader         |
| 3           | NPC Cal | Demagog   | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi      |
| 3           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 3           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ann      |
| 3           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae      |
| 3           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Gia      |
| 3           | NPC Cal | Demagog   | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader         |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi      |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ann      |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae      |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Gia      |
| 3           | NPC Dan | Judge     | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader         |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi      |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ann      |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae      |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Gia      |
| 3           | NPC Ed  | Trader    | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Fae | Reporter  | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader         |
| 3           | NPC Fae | Reporter  | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi      |
| 3           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 3           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ann      |
| 3           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae      |
| 3           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Gia      |
| 3           | NPC Fae | Reporter  | reveal    | NPC Ed is Trader                                             |
| 3           | NPC Fae | Reporter  | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Gia | Thief     | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader         |
| 3           | NPC Gia | Thief     | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi      |
| 3           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 3           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ann      |
| 3           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae      |
| 3           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Gia      |
| 3           | NPC Gia | Thief     | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Han | Spy       | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader         |
| 3           | NPC Han | Spy       | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi      |
| 3           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 3           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ann      |
| 3           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae      |
| 3           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Gia      |
| 3           | NPC Han | Spy       | reveal    | NPC Fae is targeting NPC Ed                                  |
| 3           | NPC Han | Spy       | reveal    | NPC Cal is targeting NPC Bob                                 |
| 3           | NPC Han | Spy       | reveal    | NPC Igi is targeting NPC Bob                                 |
| 3           | NPC Han | Spy       | reveal    | NPC Ed is targeting NPC Bob                                  |
| 3           | NPC Han | Spy       | reveal    | NPC Ed is targeting NPC Bob                                  |
| 3           | NPC Han | Spy       | reveal    | NPC Ann is targeting NPC Gia                                 |
| 3           | NPC Han | Spy       | reveal    | NPC Bob is targeting NPC Han                                 |
| 3           | NPC Han | Spy       | reveal    | NPC Gia is targeting NPC Ann                                 |
| 3           | NPC Han | Spy       | reveal    | NPC Dan is targeting NPC Fae                                 |
| 3           | NPC Han | Spy       | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Igi | Silencer  | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader         |
| 3           | NPC Igi | Silencer  | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Igi      |
| 3           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 3           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Ann      |
| 3           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 3           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Fae      |
| 3           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Gia      |
| 3           | NPC Igi | Silencer  | vote      | Demagog has initiated a vote on eliminating Assassin         |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 4           | NPC Dan | Judge    | Spy      |          | successful  |
| 4           | NPC Han | Spy      |          |          | successful  |
| 4           | NPC Igi | Silencer | NPC Fae  |          | successful  |

#### States Round 4
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Fae | Reporter  | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Cal | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Igi | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Han | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Trader    | False      | True      | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann | Inspector | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Bob | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Gia | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role      | message   | details                                                  |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------- |
| 4           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed   |
| 4           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 4           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Bob  |
| 4           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia  |
| 4           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 4           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann  |
| 4           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Fae  |
| 4           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed   |
| 4           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 4           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Bob  |
| 4           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia  |
| 4           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 4           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann  |
| 4           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Fae  |
| 4           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed   |
| 4           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 4           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Bob  |
| 4           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia  |
| 4           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 4           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann  |
| 4           | NPC Cal | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Fae  |
| 4           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed   |
| 4           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 4           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Bob  |
| 4           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia  |
| 4           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 4           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann  |
| 4           | NPC Dan | Judge     | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Fae  |
| 4           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed   |
| 4           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 4           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Bob  |
| 4           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia  |
| 4           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 4           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann  |
| 4           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Fae  |
| 4           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed   |
| 4           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 4           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Bob  |
| 4           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia  |
| 4           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 4           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann  |
| 4           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Fae  |
| 4           | NPC Fae | Reporter  | silenced  | You have been silenced                                   |
| 4           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed   |
| 4           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 4           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Bob  |
| 4           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia  |
| 4           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 4           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann  |
| 4           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Fae  |
| 4           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed   |
| 4           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 4           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Bob  |
| 4           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia  |
| 4           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 4           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann  |
| 4           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Fae  |
| 4           | NPC Han | Spy       | reveal    | NPC Fae is targeting NPC Ed                              |
| 4           | NPC Han | Spy       | reveal    | NPC Cal is targeting NPC Bob                             |
| 4           | NPC Han | Spy       | reveal    | NPC Igi is targeting NPC Fae                             |
| 4           | NPC Han | Spy       | reveal    | NPC Ed is targeting NPC Bob                              |
| 4           | NPC Han | Spy       | reveal    | NPC Ed is targeting NPC Bob                              |
| 4           | NPC Han | Spy       | reveal    | NPC Ann is targeting NPC Gia                             |
| 4           | NPC Han | Spy       | reveal    | NPC Bob is targeting NPC Han                             |
| 4           | NPC Han | Spy       | reveal    | NPC Gia is targeting NPC Ann                             |
| 4           | NPC Han | Spy       | reveal    | NPC Dan is targeting NPC Han                             |
| 4           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed   |
| 4           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob  |
| 4           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Bob  |
| 4           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia  |
| 4           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han  |
| 4           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann  |
| 4           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Fae  |

#### Actions Round 5
| round_index | Player  | action    | Target 1 | Target 2 | status              |
| :-----------| :-------| :---------| :--------| :--------| :------------------ |
| 5           | NPC Ann | Inspector | NPC Igi  |          | successful          |
| 5           | NPC Bob | Assassin  | Demagog  |          | successful          |
| 5           | NPC Cal | Demagog   | Spy      |          | voting in progress  |
| 5           | NPC Dan | Judge     | Assassin |          | successful          |
| 5           | NPC Ed  | Trader    | NPC Cal  | NPC Dan  | successful          |
| 5           | NPC Fae | Reporter  | NPC Dan  |          | successful          |
| 5           | NPC Gia | Thief     | NPC Cal  |          | successful          |
| 5           | NPC Han | Spy       |          |          | successful          |
| 5           | NPC Igi | Silencer  | NPC Han  |          | successful          |

#### States Round 5
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Fae | Reporter  | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Cal | Judge     | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Igi | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Han | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Trader    | False      | True      | False      | 4         | True   | 0              | 0                  |
| 5           | NPC Ann | Inspector | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Bob | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Gia | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Dan | Demagog   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Ann) inspected NPC Igi and they are not possessed     |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed       |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia      |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann      |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 5           | NPC Ann | Inspector | reveal    | Silencer is Innocent                                         |
| 5           | NPC Ann | Inspector | vote      | Demagog has initiated a vote on eliminating Spy              |
| 5           | NPC Bob | Assassin  | broadcast | I (NPC Ann) inspected NPC Igi and they are not possessed     |
| 5           | NPC Bob | Assassin  | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 5           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed       |
| 5           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 5           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 5           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia      |
| 5           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 5           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann      |
| 5           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 5           | NPC Bob | Assassin  | vote      | Demagog has initiated a vote on eliminating Spy              |
| 5           | NPC Cal | Judge     | broadcast | I (NPC Ann) inspected NPC Igi and they are not possessed     |
| 5           | NPC Cal | Judge     | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 5           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed       |
| 5           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 5           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 5           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia      |
| 5           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 5           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann      |
| 5           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 5           | NPC Cal | Judge     | vote      | Demagog has initiated a vote on eliminating Spy              |
| 5           | NPC Dan | Demagog   | broadcast | I (NPC Ann) inspected NPC Igi and they are not possessed     |
| 5           | NPC Dan | Demagog   | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 5           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed       |
| 5           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 5           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 5           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia      |
| 5           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 5           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann      |
| 5           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 5           | NPC Dan | Demagog   | vote      | Demagog has initiated a vote on eliminating Spy              |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Ann) inspected NPC Igi and they are not possessed     |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed       |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia      |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann      |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 5           | NPC Ed  | Trader    | vote      | Demagog has initiated a vote on eliminating Spy              |
| 5           | NPC Fae | Reporter  | broadcast | I (NPC Ann) inspected NPC Igi and they are not possessed     |
| 5           | NPC Fae | Reporter  | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 5           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed       |
| 5           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 5           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 5           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia      |
| 5           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 5           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann      |
| 5           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 5           | NPC Fae | Reporter  | reveal    | NPC Dan is Judge                                             |
| 5           | NPC Fae | Reporter  | vote      | Demagog has initiated a vote on eliminating Spy              |
| 5           | NPC Gia | Thief     | broadcast | I (NPC Ann) inspected NPC Igi and they are not possessed     |
| 5           | NPC Gia | Thief     | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 5           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed       |
| 5           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 5           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 5           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia      |
| 5           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 5           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann      |
| 5           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 5           | NPC Gia | Thief     | vote      | Demagog has initiated a vote on eliminating Spy              |
| 5           | NPC Han | Spy       | broadcast | I (NPC Ann) inspected NPC Igi and they are not possessed     |
| 5           | NPC Han | Spy       | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 5           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed       |
| 5           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 5           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 5           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia      |
| 5           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 5           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann      |
| 5           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 5           | NPC Han | Spy       | silenced  | You have been silenced                                       |
| 5           | NPC Han | Spy       | reveal    | NPC Fae is targeting NPC Dan                                 |
| 5           | NPC Han | Spy       | reveal    | NPC Cal is targeting NPC Bob                                 |
| 5           | NPC Han | Spy       | reveal    | NPC Igi is targeting NPC Han                                 |
| 5           | NPC Han | Spy       | reveal    | NPC Ed is targeting NPC Bob                                  |
| 5           | NPC Han | Spy       | reveal    | NPC Ed is targeting NPC Bob                                  |
| 5           | NPC Han | Spy       | reveal    | NPC Ann is targeting NPC Igi                                 |
| 5           | NPC Han | Spy       | reveal    | NPC Bob is targeting NPC Han                                 |
| 5           | NPC Han | Spy       | reveal    | NPC Gia is targeting NPC Cal                                 |
| 5           | NPC Han | Spy       | reveal    | NPC Dan is targeting NPC Bob                                 |
| 5           | NPC Han | Spy       | vote      | Demagog has initiated a vote on eliminating Spy              |
| 5           | NPC Igi | Silencer  | broadcast | I (NPC Ann) inspected NPC Igi and they are not possessed     |
| 5           | NPC Igi | Silencer  | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 5           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Ed       |
| 5           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Bob      |
| 5           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 5           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Bob       |
| 5           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Gia      |
| 5           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Han      |
| 5           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Ann      |
| 5           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 5           | NPC Igi | Silencer  | vote      | Demagog has initiated a vote on eliminating Spy              |

#### Actions Round 6
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 6           | NPC Dan | Demagog  | Spy      |          | voting in progress  |
| 6           | NPC Han | Spy      |          |          | successful          |
| 6           | NPC Igi | Silencer | NPC Fae  |          | successful          |

#### States Round 6
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Fae | Reporter  | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Cal | Judge     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Igi | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Han | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ed  | Trader    | False      | True      | False      | 3         | True   | 0              | 0                  |
| 6           | NPC Ann | Inspector | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Bob | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Gia | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Dan | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role      | message  | details                                          |
| :-----------| :-------| :---------| :--------| :----------------------------------------------- |
| 6           | NPC Ann | Inspector | vote     | Demagog has initiated a vote on eliminating Spy  |
| 6           | NPC Bob | Assassin  | vote     | Demagog has initiated a vote on eliminating Spy  |
| 6           | NPC Cal | Judge     | vote     | Demagog has initiated a vote on eliminating Spy  |
| 6           | NPC Dan | Demagog   | vote     | Demagog has initiated a vote on eliminating Spy  |
| 6           | NPC Ed  | Trader    | vote     | Demagog has initiated a vote on eliminating Spy  |
| 6           | NPC Fae | Reporter  | silenced | You have been silenced                           |
| 6           | NPC Fae | Reporter  | vote     | Demagog has initiated a vote on eliminating Spy  |
| 6           | NPC Gia | Thief     | vote     | Demagog has initiated a vote on eliminating Spy  |
| 6           | NPC Han | Spy       | reveal   | NPC Fae is targeting NPC Dan                     |
| 6           | NPC Han | Spy       | reveal   | NPC Cal is targeting NPC Han                     |
| 6           | NPC Han | Spy       | reveal   | NPC Igi is targeting NPC Fae                     |
| 6           | NPC Han | Spy       | reveal   | NPC Ed is targeting NPC Cal                      |
| 6           | NPC Han | Spy       | reveal   | NPC Ed is targeting NPC Cal                      |
| 6           | NPC Han | Spy       | reveal   | NPC Ann is targeting NPC Igi                     |
| 6           | NPC Han | Spy       | reveal   | NPC Bob is targeting NPC Dan                     |
| 6           | NPC Han | Spy       | reveal   | NPC Gia is targeting NPC Cal                     |
| 6           | NPC Han | Spy       | vote     | Demagog has initiated a vote on eliminating Spy  |
| 6           | NPC Igi | Silencer  | vote     | Demagog has initiated a vote on eliminating Spy  |

#### Actions Round 7
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 7           | NPC Ann | Inspector | NPC Han  |          | successful  |
| 7           | NPC Bob | Assassin  | Demagog  |          | successful  |
| 7           | NPC Cal | Judge     | Reporter |          | successful  |
| 7           | NPC Fae | Reporter  | NPC Ann  |          | successful  |
| 7           | NPC Gia | Thief     | NPC Igi  |          | successful  |
| 7           | NPC Han | Spy       |          |          | successful  |
| 7           | NPC Igi | Silencer  | NPC Ann  |          | successful  |

#### States Round 7
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Fae | Reporter  | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Cal | Judge     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Igi | Silencer  | False      | False     | True       | 1         | True   | 0              | 0                  |
| 7           | NPC Han | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Ed  | Trader    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Ann | Inspector | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Bob | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Gia | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Dan | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Ann) inspected NPC Han and they are not possessed     |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Gia) am the Thief and I have made NPC Igi vulnerable  |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Dan      |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Han      |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Igi      |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Dan      |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Cal      |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 7           | NPC Ann | Inspector | reveal    | Spy is Innocent                                              |
| 7           | NPC Ann | Inspector | silenced  | You have been silenced                                       |
| 7           | NPC Bob | Assassin  | broadcast | I (NPC Ann) inspected NPC Han and they are not possessed     |
| 7           | NPC Bob | Assassin  | broadcast | I (NPC Gia) am the Thief and I have made NPC Igi vulnerable  |
| 7           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Dan      |
| 7           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Han      |
| 7           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 7           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Igi      |
| 7           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Dan      |
| 7           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Cal      |
| 7           | NPC Bob | Assassin  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 7           | NPC Cal | Judge     | broadcast | I (NPC Ann) inspected NPC Han and they are not possessed     |
| 7           | NPC Cal | Judge     | broadcast | I (NPC Gia) am the Thief and I have made NPC Igi vulnerable  |
| 7           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Dan      |
| 7           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Han      |
| 7           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 7           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Igi      |
| 7           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Dan      |
| 7           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Cal      |
| 7           | NPC Cal | Judge     | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 7           | NPC Dan | Demagog   | broadcast | I (NPC Ann) inspected NPC Han and they are not possessed     |
| 7           | NPC Dan | Demagog   | broadcast | I (NPC Gia) am the Thief and I have made NPC Igi vulnerable  |
| 7           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Dan      |
| 7           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Han      |
| 7           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 7           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Igi      |
| 7           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Dan      |
| 7           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Cal      |
| 7           | NPC Dan | Demagog   | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Ann) inspected NPC Han and they are not possessed     |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Gia) am the Thief and I have made NPC Igi vulnerable  |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Dan      |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Han      |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Igi      |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Dan      |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Cal      |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 7           | NPC Fae | Reporter  | broadcast | I (NPC Ann) inspected NPC Han and they are not possessed     |
| 7           | NPC Fae | Reporter  | broadcast | I (NPC Gia) am the Thief and I have made NPC Igi vulnerable  |
| 7           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Dan      |
| 7           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Han      |
| 7           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 7           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Igi      |
| 7           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Dan      |
| 7           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Cal      |
| 7           | NPC Fae | Reporter  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 7           | NPC Fae | Reporter  | reveal    | NPC Ann is Inspector                                         |
| 7           | NPC Gia | Thief     | broadcast | I (NPC Ann) inspected NPC Han and they are not possessed     |
| 7           | NPC Gia | Thief     | broadcast | I (NPC Gia) am the Thief and I have made NPC Igi vulnerable  |
| 7           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Dan      |
| 7           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Han      |
| 7           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 7           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Igi      |
| 7           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Dan      |
| 7           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Cal      |
| 7           | NPC Gia | Thief     | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 7           | NPC Han | Spy       | broadcast | I (NPC Ann) inspected NPC Han and they are not possessed     |
| 7           | NPC Han | Spy       | broadcast | I (NPC Gia) am the Thief and I have made NPC Igi vulnerable  |
| 7           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Dan      |
| 7           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Han      |
| 7           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 7           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Igi      |
| 7           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Dan      |
| 7           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Cal      |
| 7           | NPC Han | Spy       | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |
| 7           | NPC Han | Spy       | reveal    | NPC Fae is targeting NPC Ann                                 |
| 7           | NPC Han | Spy       | reveal    | NPC Cal is targeting NPC Fae                                 |
| 7           | NPC Han | Spy       | reveal    | NPC Igi is targeting NPC Ann                                 |
| 7           | NPC Han | Spy       | reveal    | NPC Ed is targeting NPC Cal                                  |
| 7           | NPC Han | Spy       | reveal    | NPC Ed is targeting NPC Cal                                  |
| 7           | NPC Han | Spy       | reveal    | NPC Ann is targeting NPC Han                                 |
| 7           | NPC Han | Spy       | reveal    | NPC Bob is targeting NPC Dan                                 |
| 7           | NPC Han | Spy       | reveal    | NPC Gia is targeting NPC Igi                                 |
| 7           | NPC Han | Spy       | reveal    | NPC Dan is targeting NPC Han                                 |
| 7           | NPC Igi | Silencer  | broadcast | I (NPC Ann) inspected NPC Han and they are not possessed     |
| 7           | NPC Igi | Silencer  | broadcast | I (NPC Gia) am the Thief and I have made NPC Igi vulnerable  |
| 7           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Fae is targeting NPC Dan      |
| 7           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Cal is targeting NPC Han      |
| 7           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Igi is targeting NPC Fae      |
| 7           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Ann is targeting NPC Igi      |
| 7           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Bob is targeting NPC Dan      |
| 7           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Gia is targeting NPC Cal      |
| 7           | NPC Igi | Silencer  | broadcast | I (NPC Han) am the Spy and NPC Dan is targeting NPC Han      |