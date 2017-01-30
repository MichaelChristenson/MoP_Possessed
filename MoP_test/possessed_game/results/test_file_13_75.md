#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 75   | 13      | 4       |

#### Roles
| Role         |
| :----------- |
| Executioner  |
| Prophet      |
| Silencer     |
| Trader       |
| Jailer       |
| Priest       |
| Reporter     |
| Demagog      |
| Thief        |
| Spy          |
| Medic        |
| Inspector    |
| Judge        |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Trader      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Mark | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Ann  | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Bob  | Trader      | role change | Your Role is Trader       |
| 0           | NPC Bob  | Trader      | possessed   | You are Possessed         |
| 0           | NPC Cal  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Cal  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Dan  | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Ed   | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Fae  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Thief       | role change | Your Role is Thief        |
| 0           | NPC Gia  | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Han  | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Igi  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Jeff | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Ken  | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Lee  | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Mark | Priest      | role change | Your Role is Priest       |
| 0           | NPC Mark | Priest      | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status                         |
| :-----------| :-------| :---------| :--------| :--------| :----------------------------- |
| 1           | NPC Ann | Silencer  | NPC Dan  |          | successful                     |
| 1           | NPC Bob | Trader    | NPC Gia  | NPC Cal  | failed because not vulnerable  |
| 1           | NPC Dan | Medic     | NPC Han  |          | successful                     |
| 1           | NPC Ed  | Demagog   | Trader   |          | voting in progress             |
| 1           | NPC Fae | Inspector | NPC Han  |          | successful                     |
| 1           | NPC Gia | Thief     | NPC Fae  |          | successful                     |
| 1           | NPC Han | Prophet   | NPC Dan  |          | successful                     |
| 1           | NPC Igi | Judge     | Spy      |          | successful                     |
| 1           | NPC Ken | Spy       |          |          | successful                     |
| 1           | NPC Lee | Reporter  | NPC Dan  |          | successful                     |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Bob  | Trader      | False      | True      | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Jeff | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Mark | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Lee  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed   | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Gia  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ken  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                      |
| :-----------| :--------| :-----------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann  | Silencer    | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed     |
| 1           | NPC Ann  | Silencer    | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Ann  | Silencer    | broadcast | I (NPC Lee) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Ann  | Silencer    | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Bob  | Trader      | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed     |
| 1           | NPC Bob  | Trader      | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Bob  | Trader      | broadcast | I (NPC Lee) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Bob  | Trader      | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed     |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Lee) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Cal  | Executioner | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Dan  | Medic       | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed     |
| 1           | NPC Dan  | Medic       | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Dan  | Medic       | broadcast | I (NPC Lee) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Dan  | Medic       | silenced  | You have been silenced                                       |
| 1           | NPC Dan  | Medic       | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed     |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Ed   | Demagog     | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Fae  | Inspector   | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed     |
| 1           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Fae  | Inspector   | broadcast | I (NPC Lee) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Fae  | Inspector   | reveal    | Prophet is Innocent                                          |
| 1           | NPC Fae  | Inspector   | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Gia  | Thief       | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed     |
| 1           | NPC Gia  | Thief       | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Gia  | Thief       | broadcast | I (NPC Lee) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Gia  | Thief       | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed     |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Lee) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Han  | Prophet     | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed     |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Lee) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Igi  | Judge       | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed     |
| 1           | NPC Jeff | Jailer      | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Jeff | Jailer      | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Ken  | Spy         | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed     |
| 1           | NPC Ken  | Spy         | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Ken  | Spy         | broadcast | I (NPC Lee) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Ken  | Spy         | reveal    | NPC Ann is targeting NPC Dan                                 |
| 1           | NPC Ken  | Spy         | reveal    | NPC Lee is targeting NPC Dan                                 |
| 1           | NPC Ken  | Spy         | reveal    | NPC Gia is targeting NPC Fae                                 |
| 1           | NPC Ken  | Spy         | reveal    | NPC Fae is targeting NPC Han                                 |
| 1           | NPC Ken  | Spy         | reveal    | NPC Igi is targeting NPC Ken                                 |
| 1           | NPC Ken  | Spy         | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Lee  | Reporter    | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed     |
| 1           | NPC Lee  | Reporter    | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Lee  | Reporter    | broadcast | I (NPC Lee) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Lee  | Reporter    | reveal    | NPC Dan is Medic                                             |
| 1           | NPC Lee  | Reporter    | vote      | Demagog has initiated a vote on eliminating Trader           |
| 1           | NPC Mark | Priest      | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed     |
| 1           | NPC Mark | Priest      | broadcast | I (NPC Gia) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Mark | Priest      | broadcast | I (NPC Lee) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Mark | Priest      | vote      | Demagog has initiated a vote on eliminating Trader           |

#### Actions Round 2
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 2           | NPC Ann | Silencer | NPC Ken  |          | successful  |
| 2           | NPC Dan | Medic    | NPC Ann  |          | successful  |
| 2           | NPC Han | Prophet  | NPC Igi  |          | successful  |
| 2           | NPC Igi | Judge    | Spy      |          | successful  |
| 2           | NPC Ken | Spy      |          |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob  | Trader      | False      | True      | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Jeff | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Mark | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Lee  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed   | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ken  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae  | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                  |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------- |
| 2           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan  |
| 2           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Dan  |
| 2           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Dan  |
| 2           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han  |
| 2           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Ken  |
| 2           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan  |
| 2           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Dan  |
| 2           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Dan  |
| 2           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han  |
| 2           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Ken  |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan  |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Dan  |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Dan  |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han  |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Ken  |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan  |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Dan  |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Dan  |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han  |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Ken  |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan  |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Dan  |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Dan  |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han  |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Ken  |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan  |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Dan  |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Dan  |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han  |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Ken  |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan  |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Dan  |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Dan  |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han  |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Ken  |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan  |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Dan  |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Dan  |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han  |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Ken  |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan  |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Dan  |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Dan  |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han  |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Ken  |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan  |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Dan  |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Dan  |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han  |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Ken  |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan  |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Dan  |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Dan  |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han  |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Ken  |
| 2           | NPC Ken  | Spy         | silenced  | You have been silenced                                   |
| 2           | NPC Ken  | Spy         | reveal    | NPC Han is targeting NPC Dan                             |
| 2           | NPC Ken  | Spy         | reveal    | NPC Ann is targeting NPC Ken                             |
| 2           | NPC Ken  | Spy         | reveal    | NPC Bob is targeting NPC Gia                             |
| 2           | NPC Ken  | Spy         | reveal    | NPC Bob is targeting NPC Gia                             |
| 2           | NPC Ken  | Spy         | reveal    | NPC Lee is targeting NPC Dan                             |
| 2           | NPC Ken  | Spy         | reveal    | NPC Ed is targeting NPC Bob                              |
| 2           | NPC Ken  | Spy         | reveal    | NPC Gia is targeting NPC Fae                             |
| 2           | NPC Ken  | Spy         | reveal    | NPC Dan is targeting NPC Han                             |
| 2           | NPC Ken  | Spy         | reveal    | NPC Fae is targeting NPC Han                             |
| 2           | NPC Ken  | Spy         | reveal    | NPC Igi is targeting NPC Ken                             |
| 2           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan  |
| 2           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Dan  |
| 2           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Dan  |
| 2           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han  |
| 2           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Ken  |
| 2           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan  |
| 2           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Dan  |
| 2           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia  |
| 2           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Dan  |
| 2           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Bob   |
| 2           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Han  |
| 2           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han  |
| 2           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Ken  |

#### Actions Round 3
| round_index | Player  | action    | Target 1  | Target 2 | status              |
| :-----------| :-------| :---------| :---------| :--------| :------------------ |
| 3           | NPC Ann | Silencer  | NPC Bob   |          | successful          |
| 3           | NPC Dan | Medic     | NPC Bob   |          | successful          |
| 3           | NPC Ed  | Demagog   | Inspector |          | voting in progress  |
| 3           | NPC Fae | Inspector | NPC Mark  |          | successful          |
| 3           | NPC Gia | Thief     | NPC Ken   |          | successful          |
| 3           | NPC Han | Prophet   | NPC Ed    |          | successful          |
| 3           | NPC Igi | Judge     | Priest    |          | successful          |
| 3           | NPC Ken | Spy       |           |          | successful          |
| 3           | NPC Lee | Reporter  | NPC Jeff  |          | successful          |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Bob  | Trader      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Jeff | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Mark | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Lee  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ed   | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Gia  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ken  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Dan  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Fae  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message   | details                                                      |
| :-----------| :--------| :-----------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann  | Silencer    | broadcast | I (NPC Fae) inspected NPC Mark and they are not possessed    |
| 3           | NPC Ann  | Silencer    | broadcast | I (NPC Gia) am the Thief and I have made NPC Ken vulnerable  |
| 3           | NPC Ann  | Silencer    | broadcast | I (NPC Lee) am the Reporter and NPC Jeff is the Jailer       |
| 3           | NPC Ann  | Silencer    | vote      | Demagog has initiated a vote on eliminating Inspector        |
| 3           | NPC Bob  | Trader      | broadcast | I (NPC Fae) inspected NPC Mark and they are not possessed    |
| 3           | NPC Bob  | Trader      | broadcast | I (NPC Gia) am the Thief and I have made NPC Ken vulnerable  |
| 3           | NPC Bob  | Trader      | broadcast | I (NPC Lee) am the Reporter and NPC Jeff is the Jailer       |
| 3           | NPC Bob  | Trader      | silenced  | You have been silenced                                       |
| 3           | NPC Bob  | Trader      | vote      | Demagog has initiated a vote on eliminating Inspector        |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Fae) inspected NPC Mark and they are not possessed    |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Gia) am the Thief and I have made NPC Ken vulnerable  |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Lee) am the Reporter and NPC Jeff is the Jailer       |
| 3           | NPC Cal  | Executioner | vote      | Demagog has initiated a vote on eliminating Inspector        |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Fae) inspected NPC Mark and they are not possessed    |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Gia) am the Thief and I have made NPC Ken vulnerable  |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Lee) am the Reporter and NPC Jeff is the Jailer       |
| 3           | NPC Dan  | Medic       | vote      | Demagog has initiated a vote on eliminating Inspector        |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Fae) inspected NPC Mark and they are not possessed    |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Thief and I have made NPC Ken vulnerable  |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Reporter and NPC Jeff is the Jailer       |
| 3           | NPC Ed   | Demagog     | vote      | Demagog has initiated a vote on eliminating Inspector        |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Fae) inspected NPC Mark and they are not possessed    |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Thief and I have made NPC Ken vulnerable  |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Lee) am the Reporter and NPC Jeff is the Jailer       |
| 3           | NPC Fae  | Inspector   | reveal    | Priest is Innocent                                           |
| 3           | NPC Fae  | Inspector   | vote      | Demagog has initiated a vote on eliminating Inspector        |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Fae) inspected NPC Mark and they are not possessed    |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Gia) am the Thief and I have made NPC Ken vulnerable  |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Lee) am the Reporter and NPC Jeff is the Jailer       |
| 3           | NPC Gia  | Thief       | vote      | Demagog has initiated a vote on eliminating Inspector        |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Fae) inspected NPC Mark and they are not possessed    |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Gia) am the Thief and I have made NPC Ken vulnerable  |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Lee) am the Reporter and NPC Jeff is the Jailer       |
| 3           | NPC Han  | Prophet     | vote      | Demagog has initiated a vote on eliminating Inspector        |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) inspected NPC Mark and they are not possessed    |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Gia) am the Thief and I have made NPC Ken vulnerable  |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Lee) am the Reporter and NPC Jeff is the Jailer       |
| 3           | NPC Igi  | Judge       | vote      | Demagog has initiated a vote on eliminating Inspector        |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) inspected NPC Mark and they are not possessed    |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Gia) am the Thief and I have made NPC Ken vulnerable  |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Reporter and NPC Jeff is the Jailer       |
| 3           | NPC Jeff | Jailer      | vote      | Demagog has initiated a vote on eliminating Inspector        |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Fae) inspected NPC Mark and they are not possessed    |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Gia) am the Thief and I have made NPC Ken vulnerable  |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Lee) am the Reporter and NPC Jeff is the Jailer       |
| 3           | NPC Ken  | Spy         | reveal    | NPC Han is targeting NPC Igi                                 |
| 3           | NPC Ken  | Spy         | reveal    | NPC Ann is targeting NPC Bob                                 |
| 3           | NPC Ken  | Spy         | reveal    | NPC Bob is targeting NPC Gia                                 |
| 3           | NPC Ken  | Spy         | reveal    | NPC Bob is targeting NPC Gia                                 |
| 3           | NPC Ken  | Spy         | reveal    | NPC Lee is targeting NPC Jeff                                |
| 3           | NPC Ken  | Spy         | reveal    | NPC Ed is targeting NPC Bob                                  |
| 3           | NPC Ken  | Spy         | reveal    | NPC Gia is targeting NPC Ken                                 |
| 3           | NPC Ken  | Spy         | reveal    | NPC Dan is targeting NPC Ann                                 |
| 3           | NPC Ken  | Spy         | reveal    | NPC Fae is targeting NPC Mark                                |
| 3           | NPC Ken  | Spy         | reveal    | NPC Igi is targeting NPC Mark                                |
| 3           | NPC Ken  | Spy         | vote      | Demagog has initiated a vote on eliminating Inspector        |
| 3           | NPC Lee  | Reporter    | broadcast | I (NPC Fae) inspected NPC Mark and they are not possessed    |
| 3           | NPC Lee  | Reporter    | broadcast | I (NPC Gia) am the Thief and I have made NPC Ken vulnerable  |
| 3           | NPC Lee  | Reporter    | broadcast | I (NPC Lee) am the Reporter and NPC Jeff is the Jailer       |
| 3           | NPC Lee  | Reporter    | reveal    | NPC Jeff is Jailer                                           |
| 3           | NPC Lee  | Reporter    | vote      | Demagog has initiated a vote on eliminating Inspector        |
| 3           | NPC Mark | Priest      | broadcast | I (NPC Fae) inspected NPC Mark and they are not possessed    |
| 3           | NPC Mark | Priest      | broadcast | I (NPC Gia) am the Thief and I have made NPC Ken vulnerable  |
| 3           | NPC Mark | Priest      | broadcast | I (NPC Lee) am the Reporter and NPC Jeff is the Jailer       |
| 3           | NPC Mark | Priest      | vote      | Demagog has initiated a vote on eliminating Inspector        |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status                         |
| :-----------| :-------| :--------| :--------| :--------| :----------------------------- |
| 4           | NPC Ann | Silencer | NPC Mark |          | successful                     |
| 4           | NPC Bob | Trader   | NPC Jeff | NPC Han  | failed because not vulnerable  |
| 4           | NPC Dan | Medic    | NPC Jeff |          | successful                     |
| 4           | NPC Han | Prophet  | NPC Dan  |          | successful                     |
| 4           | NPC Igi | Judge    | Spy      |          | successful                     |
| 4           | NPC Ken | Spy      |          |          | successful                     |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Bob  | Trader      | False      | True      | False      | 4         | True   | 0              | 0                  |
| 4           | NPC Jeff | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Mark | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Lee  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed   | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Gia  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ken  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Dan  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae  | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                   |
| :-----------| :--------| :-----------| :---------| :-------------------------------------------------------- |
| 4           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ed    |
| 4           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Bob   |
| 4           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Jeff  |
| 4           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Fae    |
| 4           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken   |
| 4           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Bob   |
| 4           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Mark  |
| 4           | NPC Ann  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Mark  |
| 4           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ed    |
| 4           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Bob   |
| 4           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Jeff  |
| 4           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Fae    |
| 4           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken   |
| 4           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Bob   |
| 4           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Mark  |
| 4           | NPC Bob  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Mark  |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ed    |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Bob   |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Jeff  |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Fae    |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken   |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Bob   |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Mark  |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Mark  |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ed    |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Bob   |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Jeff  |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Fae    |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken   |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Bob   |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Mark  |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Mark  |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ed    |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Bob   |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Jeff  |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Fae    |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken   |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Bob   |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Mark  |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Mark  |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ed    |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Bob   |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Jeff  |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Fae    |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken   |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Bob   |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Mark  |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Mark  |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ed    |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Bob   |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Jeff  |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Fae    |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken   |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Bob   |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Mark  |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Mark  |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ed    |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Bob   |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Jeff  |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Fae    |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken   |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Bob   |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Mark  |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Mark  |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ed    |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Bob   |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Jeff  |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Fae    |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken   |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Bob   |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Mark  |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Mark  |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ed    |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Bob   |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Jeff  |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Fae    |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken   |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Bob   |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Mark  |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Mark  |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ed    |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Bob   |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Jeff  |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Fae    |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken   |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Bob   |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Mark  |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Mark  |
| 4           | NPC Ken  | Spy         | reveal    | NPC Han is targeting NPC Ed                               |
| 4           | NPC Ken  | Spy         | reveal    | NPC Ann is targeting NPC Mark                             |
| 4           | NPC Ken  | Spy         | reveal    | NPC Bob is targeting NPC Gia                              |
| 4           | NPC Ken  | Spy         | reveal    | NPC Bob is targeting NPC Gia                              |
| 4           | NPC Ken  | Spy         | reveal    | NPC Lee is targeting NPC Jeff                             |
| 4           | NPC Ken  | Spy         | reveal    | NPC Ed is targeting NPC Fae                               |
| 4           | NPC Ken  | Spy         | reveal    | NPC Gia is targeting NPC Ken                              |
| 4           | NPC Ken  | Spy         | reveal    | NPC Dan is targeting NPC Bob                              |
| 4           | NPC Ken  | Spy         | reveal    | NPC Fae is targeting NPC Mark                             |
| 4           | NPC Ken  | Spy         | reveal    | NPC Igi is targeting NPC Ken                              |
| 4           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ed    |
| 4           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Bob   |
| 4           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Jeff  |
| 4           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Fae    |
| 4           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken   |
| 4           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Bob   |
| 4           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Mark  |
| 4           | NPC Lee  | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Mark  |
| 4           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ed    |
| 4           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Bob   |
| 4           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Gia   |
| 4           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Lee is targeting NPC Jeff  |
| 4           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Fae    |
| 4           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken   |
| 4           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Bob   |
| 4           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Mark  |
| 4           | NPC Mark | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Igi is targeting NPC Mark  |
| 4           | NPC Mark | Priest      | silenced  | You have been silenced                                    |