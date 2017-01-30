#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 78   | 9       | 2       |

#### Roles
| Role         |
| :----------- |
| Medic        |
| Demagog      |
| Executioner  |
| Priest       |
| Judge        |
| Spy          |
| Trader       |
| Thief        |
| Reporter     |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Spy         | role change | Your Role is Spy          |
| 0           | NPC Ann | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Trader      | role change | Your Role is Trader       |
| 0           | NPC Bob | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Cal | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Dan | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Ed  | Judge       | possessed   | You are Possessed         |
| 0           | NPC Fae | Medic       | role change | Your Role is Medic        |
| 0           | NPC Fae | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Gia | Thief       | role change | Your Role is Thief        |
| 0           | NPC Gia | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Han | Priest      | role change | Your Role is Priest       |
| 0           | NPC Han | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Igi | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Igi | Executioner | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action   | Target 1 | Target 2 | status                         |
| :-----------| :-------| :--------| :--------| :--------| :----------------------------- |
| 1           | NPC Ann | Spy      |          |          | successful                     |
| 1           | NPC Bob | Trader   | NPC Fae  | NPC Han  | failed because not vulnerable  |
| 1           | NPC Cal | Demagog  | Trader   |          | voting in progress             |
| 1           | NPC Dan | Reporter | NPC Han  |          | successful                     |
| 1           | NPC Ed  | Judge    | Thief    |          | successful                     |
| 1           | NPC Fae | Medic    | NPC Igi  |          | successful                     |
| 1           | NPC Gia | Thief    | NPC Cal  |          | successful                     |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Demagog     | False      | False     | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Igi | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Gia | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Spy         | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Priest        |
| 1           | NPC Ann | Spy         | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ann | Spy         | reveal    | NPC Ed is targeting NPC Gia                                  |
| 1           | NPC Ann | Spy         | reveal    | NPC Gia is targeting NPC Cal                                 |
| 1           | NPC Ann | Spy         | reveal    | NPC Dan is targeting NPC Han                                 |
| 1           | NPC Ann | Spy         | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Bob | Trader      | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Priest        |
| 1           | NPC Bob | Trader      | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Bob | Trader      | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Cal | Demagog     | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Priest        |
| 1           | NPC Cal | Demagog     | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Cal | Demagog     | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Dan | Reporter    | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Priest        |
| 1           | NPC Dan | Reporter    | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Dan | Reporter    | reveal    | NPC Han is Priest                                            |
| 1           | NPC Dan | Reporter    | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Ed  | Judge       | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Priest        |
| 1           | NPC Ed  | Judge       | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ed  | Judge       | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Priest        |
| 1           | NPC Fae | Medic       | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Fae | Medic       | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Gia | Thief       | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Priest        |
| 1           | NPC Gia | Thief       | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Gia | Thief       | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Han | Priest      | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Priest        |
| 1           | NPC Han | Priest      | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Han | Priest      | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Igi | Executioner | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Priest        |
| 1           | NPC Igi | Executioner | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Igi | Executioner | vote      | Demagog has initiated a vote on eliminating Trader           |

#### Actions Round 2
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 2           | NPC Ann | Spy    |          |          | successful  |
| 2           | NPC Ed  | Judge  | Demagog  |          | successful  |
| 2           | NPC Fae | Medic  | NPC Han  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Demagog     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Igi | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Gia | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 2           | NPC Ann | Spy         | broadcast | I (NPC Ann) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Ann | Spy         | broadcast | I (NPC Ann) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Ann | Spy         | broadcast | I (NPC Ann) am the Spy and NPC Ed is targeting NPC Gia   |
| 2           | NPC Ann | Spy         | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Ann | Spy         | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Ann | Spy         | broadcast | I (NPC Ann) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Ann | Spy         | broadcast | I (NPC Ann) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Ann | Spy         | reveal    | NPC Fae is targeting NPC Igi                             |
| 2           | NPC Ann | Spy         | reveal    | NPC Cal is targeting NPC Bob                             |
| 2           | NPC Ann | Spy         | reveal    | NPC Ed is targeting NPC Cal                              |
| 2           | NPC Ann | Spy         | reveal    | NPC Bob is targeting NPC Fae                             |
| 2           | NPC Ann | Spy         | reveal    | NPC Bob is targeting NPC Fae                             |
| 2           | NPC Ann | Spy         | reveal    | NPC Gia is targeting NPC Cal                             |
| 2           | NPC Ann | Spy         | reveal    | NPC Dan is targeting NPC Han                             |
| 2           | NPC Bob | Trader      | broadcast | I (NPC Ann) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Bob | Trader      | broadcast | I (NPC Ann) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Bob | Trader      | broadcast | I (NPC Ann) am the Spy and NPC Ed is targeting NPC Gia   |
| 2           | NPC Bob | Trader      | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Bob | Trader      | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Bob | Trader      | broadcast | I (NPC Ann) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Bob | Trader      | broadcast | I (NPC Ann) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Cal | Demagog     | broadcast | I (NPC Ann) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Cal | Demagog     | broadcast | I (NPC Ann) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Cal | Demagog     | broadcast | I (NPC Ann) am the Spy and NPC Ed is targeting NPC Gia   |
| 2           | NPC Cal | Demagog     | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Cal | Demagog     | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Cal | Demagog     | broadcast | I (NPC Ann) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Cal | Demagog     | broadcast | I (NPC Ann) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Dan | Reporter    | broadcast | I (NPC Ann) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Dan | Reporter    | broadcast | I (NPC Ann) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Dan | Reporter    | broadcast | I (NPC Ann) am the Spy and NPC Ed is targeting NPC Gia   |
| 2           | NPC Dan | Reporter    | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Dan | Reporter    | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Dan | Reporter    | broadcast | I (NPC Ann) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Dan | Reporter    | broadcast | I (NPC Ann) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Ed  | Judge       | broadcast | I (NPC Ann) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Ed  | Judge       | broadcast | I (NPC Ann) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Ed  | Judge       | broadcast | I (NPC Ann) am the Spy and NPC Ed is targeting NPC Gia   |
| 2           | NPC Ed  | Judge       | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Ed  | Judge       | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Ed  | Judge       | broadcast | I (NPC Ann) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Ed  | Judge       | broadcast | I (NPC Ann) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Fae | Medic       | broadcast | I (NPC Ann) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Fae | Medic       | broadcast | I (NPC Ann) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Fae | Medic       | broadcast | I (NPC Ann) am the Spy and NPC Ed is targeting NPC Gia   |
| 2           | NPC Fae | Medic       | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Fae | Medic       | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Fae | Medic       | broadcast | I (NPC Ann) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Fae | Medic       | broadcast | I (NPC Ann) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Gia | Thief       | broadcast | I (NPC Ann) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Gia | Thief       | broadcast | I (NPC Ann) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Gia | Thief       | broadcast | I (NPC Ann) am the Spy and NPC Ed is targeting NPC Gia   |
| 2           | NPC Gia | Thief       | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Gia | Thief       | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Gia | Thief       | broadcast | I (NPC Ann) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Gia | Thief       | broadcast | I (NPC Ann) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Han | Priest      | broadcast | I (NPC Ann) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Han | Priest      | broadcast | I (NPC Ann) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Han | Priest      | broadcast | I (NPC Ann) am the Spy and NPC Ed is targeting NPC Gia   |
| 2           | NPC Han | Priest      | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Han | Priest      | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Han | Priest      | broadcast | I (NPC Ann) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Han | Priest      | broadcast | I (NPC Ann) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Igi | Executioner | broadcast | I (NPC Ann) am the Spy and NPC Fae is targeting NPC Igi  |
| 2           | NPC Igi | Executioner | broadcast | I (NPC Ann) am the Spy and NPC Cal is targeting NPC Bob  |
| 2           | NPC Igi | Executioner | broadcast | I (NPC Ann) am the Spy and NPC Ed is targeting NPC Gia   |
| 2           | NPC Igi | Executioner | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Igi | Executioner | broadcast | I (NPC Ann) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Igi | Executioner | broadcast | I (NPC Ann) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Igi | Executioner | broadcast | I (NPC Ann) am the Spy and NPC Dan is targeting NPC Han  |