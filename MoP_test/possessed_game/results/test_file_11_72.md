#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 72   | 11      | 4       |

#### Roles
| Role         |
| :----------- |
| Prophet      |
| Jailer       |
| Executioner  |
| Inspector    |
| Assassin     |
| Judge        |
| Trader       |
| Thief        |
| Demagog      |
| Spy          |
| Priest       |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Assassin    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Ann  | Assassin    | possessed   | You are Possessed         |
| 0           | NPC Bob  | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Bob  | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Cal  | Thief       | role change | Your Role is Thief        |
| 0           | NPC Cal  | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Trader      | role change | Your Role is Trader       |
| 0           | NPC Dan  | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Ed   | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Fae  | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Gia  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Han  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Igi  | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Priest      | role change | Your Role is Priest       |
| 0           | NPC Jeff | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Ken  | Demagog     | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status                         |
| :-----------| :-------| :---------| :--------| :--------| :----------------------------- |
| 1           | NPC Ann | Assassin  | Prophet  |          | successful                     |
| 1           | NPC Bob | Prophet   | NPC Fae  |          | successful                     |
| 1           | NPC Cal | Thief     | NPC Dan  |          | successful                     |
| 1           | NPC Dan | Trader    | NPC Bob  | NPC Jeff | failed because not vulnerable  |
| 1           | NPC Ed  | Inspector | NPC Jeff |          | successful                     |
| 1           | NPC Fae | Spy       |          |          | successful                     |
| 1           | NPC Gia | Judge     | Thief    |          | successful                     |
| 1           | NPC Ken | Demagog   | Trader   |          | voting in progress             |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed   | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann  | Assassin    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Trader      | False      | False     | True       | 4         | True   | 0              | 0                  |
| 1           | NPC Cal  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ken  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                      |
| :-----------| :--------| :-----------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann  | Assassin    | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Ann  | Assassin    | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed     |
| 1           | NPC Ann  | Assassin    | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Bob  | Prophet     | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Bob  | Prophet     | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed     |
| 1           | NPC Bob  | Prophet     | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Cal  | Thief       | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Cal  | Thief       | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed     |
| 1           | NPC Cal  | Thief       | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed     |
| 1           | NPC Dan  | Trader      | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Ed   | Inspector   | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Ed   | Inspector   | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed     |
| 1           | NPC Ed   | Inspector   | reveal    | Priest is Innocent                                           |
| 1           | NPC Ed   | Inspector   | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed     |
| 1           | NPC Fae  | Spy         | reveal    | NPC Ed is targeting NPC Jeff                                 |
| 1           | NPC Fae  | Spy         | reveal    | NPC Gia is targeting NPC Cal                                 |
| 1           | NPC Fae  | Spy         | reveal    | NPC Cal is targeting NPC Dan                                 |
| 1           | NPC Fae  | Spy         | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Gia  | Judge       | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed     |
| 1           | NPC Gia  | Judge       | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Han  | Executioner | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Han  | Executioner | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed     |
| 1           | NPC Han  | Executioner | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed     |
| 1           | NPC Igi  | Jailer      | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed     |
| 1           | NPC Jeff | Priest      | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Ken  | Demagog     | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Ken  | Demagog     | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed     |
| 1           | NPC Ken  | Demagog     | vote      | Demagog has initiated a vote on eliminating Trader           |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Bob | Prophet | NPC Han  |          | successful  |
| 2           | NPC Fae | Spy     |          |          | successful  |
| 2           | NPC Gia | Judge   | Prophet  |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed   | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann  | Assassin    | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Trader      | False      | False     | True       | 3         | True   | 0              | 0                  |
| 2           | NPC Cal  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ken  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                  |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------- |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff  |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob  |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan  |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan  |
| 2           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff  |
| 2           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob  |
| 2           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan  |
| 2           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan  |
| 2           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff  |
| 2           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob  |
| 2           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan  |
| 2           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan  |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff  |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob  |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan  |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan  |
| 2           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff  |
| 2           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob  |
| 2           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan  |
| 2           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan  |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff  |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob  |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan  |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan  |
| 2           | NPC Fae  | Spy         | reveal    | NPC Bob is targeting NPC Fae                             |
| 2           | NPC Fae  | Spy         | reveal    | NPC Ed is targeting NPC Jeff                             |
| 2           | NPC Fae  | Spy         | reveal    | NPC Ann is targeting NPC Bob                             |
| 2           | NPC Fae  | Spy         | reveal    | NPC Gia is targeting NPC Bob                             |
| 2           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Bob                             |
| 2           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Bob                             |
| 2           | NPC Fae  | Spy         | reveal    | NPC Cal is targeting NPC Dan                             |
| 2           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Dan                             |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff  |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob  |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan  |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan  |
| 2           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff  |
| 2           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob  |
| 2           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan  |
| 2           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan  |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff  |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob  |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan  |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan  |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff  |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob  |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan  |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan  |
| 2           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae  |
| 2           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff  |
| 2           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob  |
| 2           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Cal  |
| 2           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 2           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan  |
| 2           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan  |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status              |
| :-----------| :-------| :---------| :--------| :--------| :------------------ |
| 3           | NPC Ann | Assassin  | Trader   |          | successful          |
| 3           | NPC Bob | Prophet   | NPC Igi  |          | successful          |
| 3           | NPC Cal | Thief     | NPC Igi  |          | successful          |
| 3           | NPC Ed  | Inspector | NPC Han  |          | successful          |
| 3           | NPC Fae | Spy       |          |          | successful          |
| 3           | NPC Gia | Judge     | Prophet  |          | successful          |
| 3           | NPC Ken | Demagog   | Assassin |          | voting in progress  |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Igi  | Jailer      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Han  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed   | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann  | Assassin    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan  | Trader      | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Cal  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ken  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message   | details                                                      |
| :-----------| :--------| :-----------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Cal) am the Thief and I have made NPC Igi vulnerable  |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed      |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff      |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob      |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan      |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan      |
| 3           | NPC Ann  | Assassin    | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Bob  | Prophet     | broadcast | I (NPC Cal) am the Thief and I have made NPC Igi vulnerable  |
| 3           | NPC Bob  | Prophet     | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed      |
| 3           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff      |
| 3           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob      |
| 3           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan      |
| 3           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan      |
| 3           | NPC Bob  | Prophet     | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Cal  | Thief       | broadcast | I (NPC Cal) am the Thief and I have made NPC Igi vulnerable  |
| 3           | NPC Cal  | Thief       | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed      |
| 3           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff      |
| 3           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob      |
| 3           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan      |
| 3           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan      |
| 3           | NPC Cal  | Thief       | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Cal) am the Thief and I have made NPC Igi vulnerable  |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan      |
| 3           | NPC Dan  | Trader      | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Ed   | Inspector   | broadcast | I (NPC Cal) am the Thief and I have made NPC Igi vulnerable  |
| 3           | NPC Ed   | Inspector   | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed      |
| 3           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff      |
| 3           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob      |
| 3           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan      |
| 3           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan      |
| 3           | NPC Ed   | Inspector   | reveal    | Executioner is Innocent                                      |
| 3           | NPC Ed   | Inspector   | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Thief and I have made NPC Igi vulnerable  |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed      |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff      |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob      |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan      |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan      |
| 3           | NPC Fae  | Spy         | reveal    | NPC Bob is targeting NPC Han                                 |
| 3           | NPC Fae  | Spy         | reveal    | NPC Ed is targeting NPC Han                                  |
| 3           | NPC Fae  | Spy         | reveal    | NPC Ann is targeting NPC Bob                                 |
| 3           | NPC Fae  | Spy         | reveal    | NPC Gia is targeting NPC Bob                                 |
| 3           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Bob                                 |
| 3           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Bob                                 |
| 3           | NPC Fae  | Spy         | reveal    | NPC Cal is targeting NPC Igi                                 |
| 3           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Dan                                 |
| 3           | NPC Fae  | Spy         | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Thief and I have made NPC Igi vulnerable  |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan      |
| 3           | NPC Gia  | Judge       | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Cal) am the Thief and I have made NPC Igi vulnerable  |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed      |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff      |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob      |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan      |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan      |
| 3           | NPC Han  | Executioner | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Cal) am the Thief and I have made NPC Igi vulnerable  |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed      |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff      |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob      |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan      |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan      |
| 3           | NPC Igi  | Jailer      | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Thief and I have made NPC Igi vulnerable  |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed      |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff      |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob      |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan      |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan      |
| 3           | NPC Jeff | Priest      | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Ken  | Demagog     | broadcast | I (NPC Cal) am the Thief and I have made NPC Igi vulnerable  |
| 3           | NPC Ken  | Demagog     | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed      |
| 3           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Han      |
| 3           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff      |
| 3           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Bob      |
| 3           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob      |
| 3           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan      |
| 3           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Dan      |
| 3           | NPC Ken  | Demagog     | vote      | Demagog has initiated a vote on eliminating Assassin         |

#### Actions Round 4
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 4           | NPC Bob | Prophet | NPC Gia  |          | successful  |
| 4           | NPC Fae | Spy     |          |          | successful  |
| 4           | NPC Gia | Judge   | Spy      |          | successful  |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Bob  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Igi  | Jailer      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Han  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed   | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann  | Assassin    | False      | True      | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan  | Trader      | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Cal  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ken  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                  |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------- |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Igi  |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Dan  |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob  |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Igi  |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann  |
| 4           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Igi  |
| 4           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Dan  |
| 4           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob  |
| 4           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Igi  |
| 4           | NPC Bob  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann  |
| 4           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Igi  |
| 4           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Dan  |
| 4           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob  |
| 4           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Igi  |
| 4           | NPC Cal  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann  |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Igi  |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Dan  |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob  |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Igi  |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann  |
| 4           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Igi  |
| 4           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Dan  |
| 4           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob  |
| 4           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Igi  |
| 4           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann  |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Igi  |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Dan  |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob  |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Igi  |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann  |
| 4           | NPC Fae  | Spy         | reveal    | NPC Bob is targeting NPC Igi                             |
| 4           | NPC Fae  | Spy         | reveal    | NPC Ed is targeting NPC Han                              |
| 4           | NPC Fae  | Spy         | reveal    | NPC Ann is targeting NPC Dan                             |
| 4           | NPC Fae  | Spy         | reveal    | NPC Gia is targeting NPC Fae                             |
| 4           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Bob                             |
| 4           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Bob                             |
| 4           | NPC Fae  | Spy         | reveal    | NPC Cal is targeting NPC Igi                             |
| 4           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Ann                             |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Igi  |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Dan  |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob  |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Igi  |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann  |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Igi  |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Dan  |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob  |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Igi  |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann  |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Igi  |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Dan  |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob  |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Igi  |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann  |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Igi  |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Dan  |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob  |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Igi  |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann  |
| 4           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Igi  |
| 4           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Dan  |
| 4           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob  |
| 4           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Igi  |
| 4           | NPC Ken  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann  |