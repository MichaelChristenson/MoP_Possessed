#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 90   | 12      | 6       |

#### Roles
| Role         |
| :----------- |
| Judge        |
| Executioner  |
| Assassin     |
| Inspector    |
| Thief        |
| Demagog      |
| Prophet      |
| Spy          |
| Trader       |
| Psychic      |
| Jailer       |
| Silencer     |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Demagog     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Thief       | role change | Your Role is Thief        |
| 0           | NPC Ann  | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Bob  | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Bob  | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Cal  | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Cal  | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Dan  | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Spy         | role change | Your Role is Spy          |
| 0           | NPC Ed   | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Trader      | role change | Your Role is Trader       |
| 0           | NPC Fae  | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Gia  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Han  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Igi  | Demagog     | possessed   | You are Possessed         |
| 0           | NPC Jeff | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Jeff | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Ken  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Lee  | Psychic     | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player   | action    | Target 1    | Target 2 | status              |
| :-----------| :--------| :---------| :-----------| :--------| :------------------ |
| 1           | NPC Ann  | Thief     | NPC Igi     |          | successful          |
| 1           | NPC Bob  | Assassin  | Executioner |          | successful          |
| 1           | NPC Dan  | Silencer  | NPC Cal     |          | successful          |
| 1           | NPC Ed   | Spy       |             |          | successful          |
| 1           | NPC Fae  | Trader    | NPC Gia     | NPC Cal  | successful          |
| 1           | NPC Gia  | Judge     | Assassin    |          | successful          |
| 1           | NPC Igi  | Demagog   | Trader      |          | voting in progress  |
| 1           | NPC Jeff | Prophet   | NPC Ken     |          | successful          |
| 1           | NPC Ken  | Inspector | NPC Igi     |          | successful          |
| 1           | NPC Lee  | Psychic   |             |          | successful          |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Gia  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ken  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Igi  | Demagog     | False      | True      | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Jeff | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Lee  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Cal  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 1           | NPC Ann  | Thief       | broadcast | I (NPC Ann) am the Thief and I have made NPC Igi vulnerable      |
| 1           | NPC Ann  | Thief       | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed             |
| 1           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 1           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Ann  | Thief       | vote      | Demagog has initiated a vote on eliminating Trader               |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Ann) am the Thief and I have made NPC Igi vulnerable      |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed             |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Bob  | Assassin    | vote      | Demagog has initiated a vote on eliminating Trader               |
| 1           | NPC Cal  | Judge       | broadcast | I (NPC Ann) am the Thief and I have made NPC Igi vulnerable      |
| 1           | NPC Cal  | Judge       | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed             |
| 1           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 1           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Cal  | Judge       | silenced  | You have been silenced                                           |
| 1           | NPC Cal  | Judge       | vote      | Demagog has initiated a vote on eliminating Trader               |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Ann) am the Thief and I have made NPC Igi vulnerable      |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed             |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Dan  | Silencer    | vote      | Demagog has initiated a vote on eliminating Trader               |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Ann) am the Thief and I have made NPC Igi vulnerable      |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed             |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Ed   | Spy         | reveal    | NPC Gia is targeting NPC Bob                                     |
| 1           | NPC Ed   | Spy         | reveal    | NPC Ken is targeting NPC Igi                                     |
| 1           | NPC Ed   | Spy         | reveal    | NPC Ann is targeting NPC Igi                                     |
| 1           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Cal                                     |
| 1           | NPC Ed   | Spy         | vote      | Demagog has initiated a vote on eliminating Trader               |
| 1           | NPC Fae  | Trader      | broadcast | I (NPC Ann) am the Thief and I have made NPC Igi vulnerable      |
| 1           | NPC Fae  | Trader      | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed             |
| 1           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 1           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Fae  | Trader      | vote      | Demagog has initiated a vote on eliminating Trader               |
| 1           | NPC Gia  | Jailer      | broadcast | I (NPC Ann) am the Thief and I have made NPC Igi vulnerable      |
| 1           | NPC Gia  | Jailer      | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed             |
| 1           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 1           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Gia  | Jailer      | vote      | Demagog has initiated a vote on eliminating Trader               |
| 1           | NPC Han  | Executioner | broadcast | I (NPC Ann) am the Thief and I have made NPC Igi vulnerable      |
| 1           | NPC Han  | Executioner | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed             |
| 1           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 1           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Han  | Executioner | vote      | Demagog has initiated a vote on eliminating Trader               |
| 1           | NPC Igi  | Demagog     | broadcast | I (NPC Ann) am the Thief and I have made NPC Igi vulnerable      |
| 1           | NPC Igi  | Demagog     | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed             |
| 1           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 1           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Igi  | Demagog     | vote      | Demagog has initiated a vote on eliminating Trader               |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Ann) am the Thief and I have made NPC Igi vulnerable      |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed             |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Jeff | Prophet     | vote      | Demagog has initiated a vote on eliminating Trader               |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Ann) am the Thief and I have made NPC Igi vulnerable      |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed             |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Ken  | Inspector   | reveal    | Demagog is Possessed                                             |
| 1           | NPC Ken  | Inspector   | vote      | Demagog has initiated a vote on eliminating Trader               |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Ann) am the Thief and I have made NPC Igi vulnerable      |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed             |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Lee  | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 1           | NPC Lee  | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 1           | NPC Lee  | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 1           | NPC Lee  | Psychic     | reveal    | Player: NPC Ann is not possessed                                 |
| 1           | NPC Lee  | Psychic     | reveal    | Player: NPC Ken is not possessed                                 |
| 1           | NPC Lee  | Psychic     | vote      | Demagog has initiated a vote on eliminating Trader               |

#### Actions Round 2
| round_index | Player   | action      | Target 1 | Target 2 | status                        |
| :-----------| :--------| :-----------| :--------| :--------| :---------------------------- |
| 2           | NPC Cal  | Judge       | Jailer   |          | successful                    |
| 2           | NPC Dan  | Silencer    | NPC Fae  |          | successful                    |
| 2           | NPC Ed   | Spy         |          |          | successful                    |
| 2           | NPC Han  | Executioner | NPC Igi  |          | failed because of no support  |
| 2           | NPC Jeff | Prophet     | NPC Dan  |          | successful                    |
| 2           | NPC Lee  | Psychic     |          |          | successful                    |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Gia  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Executioner | False      | False     | False      | 4         | True   | 0              | 0                  |
| 2           | NPC Bob  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ken  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Igi  | Demagog     | False      | True      | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Jeff | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Lee  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message       | details                                                        |
| :-----------| :--------| :-----------| :-------------| :------------------------------------------------------------- |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han         |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Lee) am the Psychic and the Judge is not possessed      |
| 2           | NPC Ann  | Thief       | broadcast     | I (NPC Lee) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han         |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Lee) am the Psychic and the Judge is not possessed      |
| 2           | NPC Bob  | Assassin    | broadcast     | I (NPC Lee) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han         |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Lee) am the Psychic and the Judge is not possessed      |
| 2           | NPC Cal  | Judge       | broadcast     | I (NPC Lee) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han         |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Lee) am the Psychic and the Judge is not possessed      |
| 2           | NPC Dan  | Silencer    | broadcast     | I (NPC Lee) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han         |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Lee) am the Psychic and the Judge is not possessed      |
| 2           | NPC Ed   | Spy         | broadcast     | I (NPC Lee) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Ed   | Spy         | reveal        | NPC Han is targeting NPC Igi                                   |
| 2           | NPC Ed   | Spy         | reveal        | NPC Bob is targeting NPC Han                                   |
| 2           | NPC Ed   | Spy         | reveal        | NPC Ken is targeting NPC Igi                                   |
| 2           | NPC Ed   | Spy         | reveal        | NPC Ann is targeting NPC Igi                                   |
| 2           | NPC Ed   | Spy         | reveal        | NPC Igi is targeting NPC Fae                                   |
| 2           | NPC Ed   | Spy         | reveal        | NPC Jeff is targeting NPC Ken                                  |
| 2           | NPC Ed   | Spy         | reveal        | NPC Fae is targeting NPC Gia                                   |
| 2           | NPC Ed   | Spy         | reveal        | NPC Fae is targeting NPC Gia                                   |
| 2           | NPC Ed   | Spy         | reveal        | NPC Cal is targeting NPC Gia                                   |
| 2           | NPC Ed   | Spy         | reveal        | NPC Dan is targeting NPC Fae                                   |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han         |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Lee) am the Psychic and the Judge is not possessed      |
| 2           | NPC Fae  | Trader      | broadcast     | I (NPC Lee) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Fae  | Trader      | silenced      | You have been silenced                                         |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han         |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Lee) am the Psychic and the Judge is not possessed      |
| 2           | NPC Gia  | Jailer      | broadcast     | I (NPC Lee) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han         |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Lee) am the Psychic and the Judge is not possessed      |
| 2           | NPC Han  | Executioner | broadcast     | I (NPC Lee) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Han  | Executioner | action failed |                                                                |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han         |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Lee) am the Psychic and the Judge is not possessed      |
| 2           | NPC Igi  | Demagog     | broadcast     | I (NPC Lee) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han         |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Lee) am the Psychic and the Judge is not possessed      |
| 2           | NPC Jeff | Prophet     | broadcast     | I (NPC Lee) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han         |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Lee) am the Psychic and the Judge is not possessed      |
| 2           | NPC Ken  | Inspector   | broadcast     | I (NPC Lee) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han         |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Lee) am the Psychic and the Judge is not possessed      |
| 2           | NPC Lee  | Psychic     | broadcast     | I (NPC Lee) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Lee  | Psychic     | reveal        | Player: NPC Han is not possessed                               |
| 2           | NPC Lee  | Psychic     | reveal        | Player: NPC Cal is not possessed                               |
| 2           | NPC Lee  | Psychic     | reveal        | Player: NPC Jeff is not possessed                              |
| 2           | NPC Lee  | Psychic     | reveal        | Player: NPC Ann is not possessed                               |
| 2           | NPC Lee  | Psychic     | reveal        | Player: NPC Gia is not possessed                               |

#### Actions Round 3
| round_index | Player   | action    | Target 1  | Target 2 | status              |
| :-----------| :--------| :---------| :---------| :--------| :------------------ |
| 3           | NPC Ann  | Thief     | NPC Fae   |          | successful          |
| 3           | NPC Bob  | Assassin  | Jailer    |          | successful          |
| 3           | NPC Cal  | Judge     | Inspector |          | successful          |
| 3           | NPC Dan  | Silencer  | NPC Ann   |          | successful          |
| 3           | NPC Ed   | Spy       |           |          | successful          |
| 3           | NPC Igi  | Demagog   | Trader    |          | voting in progress  |
| 3           | NPC Jeff | Prophet   | NPC Gia   |          | successful          |
| 3           | NPC Ken  | Inspector | NPC Igi   |          | successful          |
| 3           | NPC Lee  | Psychic   |           |          | successful          |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Gia  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Han  | Executioner | False      | False     | False      | 3         | True   | 0              | 0                  |
| 3           | NPC Bob  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ken  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Igi  | Demagog     | False      | True      | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Jeff | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Fae  | Trader      | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Lee  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Cal  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable   |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi        |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han        |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi        |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae        |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Fae        |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed          |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 3           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed     |
| 3           | NPC Ann  | Thief       | silenced  | You have been silenced                                        |
| 3           | NPC Ann  | Thief       | vote      | Demagog has initiated a vote on eliminating Trader            |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable   |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi        |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han        |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi        |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae        |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Fae        |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed          |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed     |
| 3           | NPC Bob  | Assassin    | vote      | Demagog has initiated a vote on eliminating Trader            |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable   |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi        |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han        |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi        |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae        |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Fae        |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed          |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 3           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed     |
| 3           | NPC Cal  | Judge       | vote      | Demagog has initiated a vote on eliminating Trader            |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable   |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi        |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han        |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi        |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae        |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Fae        |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed          |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed     |
| 3           | NPC Dan  | Silencer    | vote      | Demagog has initiated a vote on eliminating Trader            |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable   |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi        |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han        |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi        |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae        |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Fae        |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed          |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed     |
| 3           | NPC Ed   | Spy         | reveal    | NPC Han is targeting NPC Igi                                  |
| 3           | NPC Ed   | Spy         | reveal    | NPC Bob is targeting NPC Han                                  |
| 3           | NPC Ed   | Spy         | reveal    | NPC Ken is targeting NPC Igi                                  |
| 3           | NPC Ed   | Spy         | reveal    | NPC Ann is targeting NPC Fae                                  |
| 3           | NPC Ed   | Spy         | reveal    | NPC Igi is targeting NPC Fae                                  |
| 3           | NPC Ed   | Spy         | reveal    | NPC Jeff is targeting NPC Dan                                 |
| 3           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Gia                                  |
| 3           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Gia                                  |
| 3           | NPC Ed   | Spy         | reveal    | NPC Cal is targeting NPC Ken                                  |
| 3           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Ann                                  |
| 3           | NPC Ed   | Spy         | vote      | Demagog has initiated a vote on eliminating Trader            |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable   |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi        |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han        |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi        |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae        |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Fae        |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed          |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 3           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed     |
| 3           | NPC Fae  | Trader      | vote      | Demagog has initiated a vote on eliminating Trader            |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable   |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi        |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han        |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi        |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae        |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Fae        |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed          |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 3           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed     |
| 3           | NPC Gia  | Jailer      | vote      | Demagog has initiated a vote on eliminating Trader            |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable   |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi        |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han        |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi        |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae        |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Fae        |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed          |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 3           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed     |
| 3           | NPC Han  | Executioner | vote      | Demagog has initiated a vote on eliminating Trader            |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable   |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi        |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han        |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi        |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae        |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Fae        |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed          |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 3           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed     |
| 3           | NPC Igi  | Demagog     | vote      | Demagog has initiated a vote on eliminating Trader            |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable   |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi        |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han        |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi        |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae        |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Fae        |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed          |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed     |
| 3           | NPC Jeff | Prophet     | vote      | Demagog has initiated a vote on eliminating Trader            |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable   |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi        |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han        |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi        |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae        |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Fae        |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed          |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed     |
| 3           | NPC Ken  | Inspector   | reveal    | Demagog is Possessed                                          |
| 3           | NPC Ken  | Inspector   | vote      | Demagog has initiated a vote on eliminating Trader            |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable   |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi        |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Han        |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi        |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae        |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia        |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Fae        |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Ken) inspected NPC Igi and they are possessed          |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed     |
| 3           | NPC Lee  | Psychic     | reveal    | Player: NPC Ed is not possessed                               |
| 3           | NPC Lee  | Psychic     | reveal    | Player: NPC Gia is not possessed                              |
| 3           | NPC Lee  | Psychic     | reveal    | Player: NPC Ann is not possessed                              |
| 3           | NPC Lee  | Psychic     | reveal    | Player: NPC Han is not possessed                              |
| 3           | NPC Lee  | Psychic     | reveal    | Player: NPC Jeff is not possessed                             |
| 3           | NPC Lee  | Psychic     | vote      | Demagog has initiated a vote on eliminating Trader            |

#### Actions Round 4
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 4           | NPC Cal  | Judge    | Prophet  |          | successful  |
| 4           | NPC Dan  | Silencer | NPC Gia  |          | successful  |
| 4           | NPC Ed   | Spy      |          |          | successful  |
| 4           | NPC Jeff | Prophet  | NPC Ken  |          | successful  |
| 4           | NPC Lee  | Psychic  |          |          | successful  |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Gia  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Han  | Executioner | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Bob  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ken  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Igi  | Demagog     | False      | True      | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Jeff | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae  | Trader      | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Lee  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Cal  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia           |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi           |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae           |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae           |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Gia          |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ken           |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann           |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed        |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia           |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi           |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae           |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae           |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Gia          |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ken           |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann           |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed        |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia           |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi           |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae           |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae           |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Gia          |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ken           |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann           |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed        |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia           |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi           |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae           |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae           |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Gia          |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ken           |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann           |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed        |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia           |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi           |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae           |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae           |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Gia          |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ken           |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann           |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed        |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 4           | NPC Ed   | Spy         | reveal    | NPC Han is targeting NPC Igi                                     |
| 4           | NPC Ed   | Spy         | reveal    | NPC Bob is targeting NPC Gia                                     |
| 4           | NPC Ed   | Spy         | reveal    | NPC Ken is targeting NPC Igi                                     |
| 4           | NPC Ed   | Spy         | reveal    | NPC Ann is targeting NPC Fae                                     |
| 4           | NPC Ed   | Spy         | reveal    | NPC Igi is targeting NPC Fae                                     |
| 4           | NPC Ed   | Spy         | reveal    | NPC Jeff is targeting NPC Gia                                    |
| 4           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Gia                                     |
| 4           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Gia                                     |
| 4           | NPC Ed   | Spy         | reveal    | NPC Cal is targeting NPC Jeff                                    |
| 4           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Gia                                     |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia           |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi           |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae           |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae           |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Gia          |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ken           |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann           |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed        |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia           |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi           |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae           |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae           |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Gia          |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ken           |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann           |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed        |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 4           | NPC Gia  | Jailer      | silenced  | You have been silenced                                           |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia           |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi           |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae           |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae           |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Gia          |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ken           |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann           |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed        |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia           |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi           |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae           |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae           |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Gia          |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ken           |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann           |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed        |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia           |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi           |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae           |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae           |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Gia          |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ken           |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann           |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed        |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia           |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi           |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae           |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae           |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Gia          |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ken           |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann           |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed        |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia           |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi           |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae           |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae           |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Gia          |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia           |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Ken           |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ann           |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Judge is not possessed        |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed        |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 4           | NPC Lee  | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 4           | NPC Lee  | Psychic     | reveal    | Player: NPC Ann is not possessed                                 |
| 4           | NPC Lee  | Psychic     | reveal    | Player: NPC Cal is not possessed                                 |
| 4           | NPC Lee  | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 4           | NPC Lee  | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |

#### Actions Round 5
| round_index | Player   | action    | Target 1 | Target 2 | status                         |
| :-----------| :--------| :---------| :--------| :--------| :----------------------------- |
| 5           | NPC Ann  | Thief     | NPC Han  |          | successful                     |
| 5           | NPC Bob  | Assassin  | Judge    |          | successful                     |
| 5           | NPC Cal  | Judge     | Demagog  |          | successful                     |
| 5           | NPC Dan  | Silencer  | NPC Bob  |          | successful                     |
| 5           | NPC Ed   | Spy       |          |          | successful                     |
| 5           | NPC Fae  | Trader    | NPC Ann  | NPC Dan  | failed because not vulnerable  |
| 5           | NPC Igi  | Demagog   | Spy      |          | voting in progress             |
| 5           | NPC Jeff | Prophet   | NPC Ed   |          | successful                     |
| 5           | NPC Ken  | Inspector | NPC Dan  |          | successful                     |
| 5           | NPC Lee  | Psychic   |          |          | successful                     |

#### States Round 5
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Gia  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Han  | Executioner | False      | False     | True       | 1         | True   | 0              | 0                  |
| 5           | NPC Bob  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Ken  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Ann  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Igi  | Demagog     | False      | True      | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Jeff | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Fae  | Trader      | False      | False     | True       | 4         | True   | 0              | 0                  |
| 5           | NPC Lee  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Cal  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Ann) am the Thief and I have made NPC Han vulnerable    |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi         |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia         |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae         |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff        |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Gia         |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Ken) inspected NPC Dan and they are not possessed       |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed    |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 5           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ann  | Thief       | vote      | Demagog has initiated a vote on eliminating Spy                |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Ann) am the Thief and I have made NPC Han vulnerable    |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi         |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia         |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae         |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff        |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Gia         |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Ken) inspected NPC Dan and they are not possessed       |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed    |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 5           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Bob  | Assassin    | silenced  | You have been silenced                                         |
| 5           | NPC Bob  | Assassin    | vote      | Demagog has initiated a vote on eliminating Spy                |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Ann) am the Thief and I have made NPC Han vulnerable    |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi         |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia         |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae         |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff        |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Gia         |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Ken) inspected NPC Dan and they are not possessed       |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed    |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 5           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Cal  | Judge       | vote      | Demagog has initiated a vote on eliminating Spy                |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Ann) am the Thief and I have made NPC Han vulnerable    |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi         |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia         |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae         |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff        |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Gia         |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Ken) inspected NPC Dan and they are not possessed       |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed    |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Dan  | Silencer    | vote      | Demagog has initiated a vote on eliminating Spy                |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ann) am the Thief and I have made NPC Han vulnerable    |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi         |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia         |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae         |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff        |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Gia         |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ken) inspected NPC Dan and they are not possessed       |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed    |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ed   | Spy         | reveal    | NPC Han is targeting NPC Igi                                   |
| 5           | NPC Ed   | Spy         | reveal    | NPC Bob is targeting NPC Gia                                   |
| 5           | NPC Ed   | Spy         | reveal    | NPC Ken is targeting NPC Dan                                   |
| 5           | NPC Ed   | Spy         | reveal    | NPC Ann is targeting NPC Han                                   |
| 5           | NPC Ed   | Spy         | reveal    | NPC Igi is targeting NPC Fae                                   |
| 5           | NPC Ed   | Spy         | reveal    | NPC Jeff is targeting NPC Ken                                  |
| 5           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Gia                                   |
| 5           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Gia                                   |
| 5           | NPC Ed   | Spy         | reveal    | NPC Cal is targeting NPC Igi                                   |
| 5           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Bob                                   |
| 5           | NPC Ed   | Spy         | vote      | Demagog has initiated a vote on eliminating Spy                |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Ann) am the Thief and I have made NPC Han vulnerable    |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi         |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia         |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae         |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff        |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Gia         |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Ken) inspected NPC Dan and they are not possessed       |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed    |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 5           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Fae  | Trader      | vote      | Demagog has initiated a vote on eliminating Spy                |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Ann) am the Thief and I have made NPC Han vulnerable    |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi         |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia         |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae         |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff        |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Gia         |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Ken) inspected NPC Dan and they are not possessed       |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed    |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 5           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Gia  | Jailer      | vote      | Demagog has initiated a vote on eliminating Spy                |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Ann) am the Thief and I have made NPC Han vulnerable    |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi         |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia         |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae         |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff        |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Gia         |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Ken) inspected NPC Dan and they are not possessed       |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed    |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 5           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Han  | Executioner | vote      | Demagog has initiated a vote on eliminating Spy                |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Ann) am the Thief and I have made NPC Han vulnerable    |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi         |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia         |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae         |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff        |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Gia         |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Ken) inspected NPC Dan and they are not possessed       |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed    |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 5           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Igi  | Demagog     | vote      | Demagog has initiated a vote on eliminating Spy                |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Ann) am the Thief and I have made NPC Han vulnerable    |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi         |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia         |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae         |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff        |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Gia         |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Ken) inspected NPC Dan and they are not possessed       |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed    |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 5           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Jeff | Prophet     | vote      | Demagog has initiated a vote on eliminating Spy                |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Ann) am the Thief and I have made NPC Han vulnerable    |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi         |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia         |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae         |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff        |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Gia         |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Ken) inspected NPC Dan and they are not possessed       |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed    |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ken  | Inspector   | reveal    | Silencer is Innocent                                           |
| 5           | NPC Ken  | Inspector   | vote      | Demagog has initiated a vote on eliminating Spy                |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Ann) am the Thief and I have made NPC Han vulnerable    |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi         |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Gia         |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Igi         |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Fae         |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Fae         |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ken        |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Gia         |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff        |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Gia         |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Ken) inspected NPC Dan and they are not possessed       |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed    |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed        |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Lee  | Psychic     | reveal    | Player: NPC Cal is not possessed                               |
| 5           | NPC Lee  | Psychic     | reveal    | Player: NPC Ken is not possessed                               |
| 5           | NPC Lee  | Psychic     | reveal    | Player: NPC Ann is not possessed                               |
| 5           | NPC Lee  | Psychic     | reveal    | Player: NPC Jeff is not possessed                              |
| 5           | NPC Lee  | Psychic     | reveal    | Player: NPC Han is not possessed                               |
| 5           | NPC Lee  | Psychic     | vote      | Demagog has initiated a vote on eliminating Spy                |

#### Actions Round 6
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 6           | NPC Cal  | Judge    | Silencer |          | successful  |
| 6           | NPC Dan  | Silencer | NPC Fae  |          | successful  |
| 6           | NPC Ed   | Spy      |          |          | successful  |
| 6           | NPC Jeff | Prophet  | NPC Igi  |          | successful  |
| 6           | NPC Lee  | Psychic  |          |          | successful  |

#### States Round 6
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Gia  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Han  | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Bob  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ken  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ann  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Igi  | Demagog     | False      | True      | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Jeff | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Fae  | Trader      | False      | False     | True       | 3         | True   | 0              | 0                  |
| 6           | NPC Lee  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Cal  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Dan           |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Han           |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Ed            |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ed           |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi           |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Bob           |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 6           | NPC Ann  | Thief       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Dan           |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Han           |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Ed            |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ed           |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi           |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Bob           |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 6           | NPC Bob  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Dan           |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Han           |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Ed            |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ed           |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi           |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Bob           |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 6           | NPC Cal  | Judge       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Dan           |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Han           |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Ed            |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ed           |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi           |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Bob           |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Dan           |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Han           |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Ed            |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ed           |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi           |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Bob           |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 6           | NPC Ed   | Spy         | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 6           | NPC Ed   | Spy         | reveal    | NPC Bob is targeting NPC Cal                                     |
| 6           | NPC Ed   | Spy         | reveal    | NPC Ken is targeting NPC Dan                                     |
| 6           | NPC Ed   | Spy         | reveal    | NPC Ann is targeting NPC Han                                     |
| 6           | NPC Ed   | Spy         | reveal    | NPC Igi is targeting NPC Ed                                      |
| 6           | NPC Ed   | Spy         | reveal    | NPC Jeff is targeting NPC Ed                                     |
| 6           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Ann                                     |
| 6           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Ann                                     |
| 6           | NPC Ed   | Spy         | reveal    | NPC Cal is targeting NPC Dan                                     |
| 6           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Fae                                     |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Dan           |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Han           |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Ed            |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ed           |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi           |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Bob           |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 6           | NPC Fae  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 6           | NPC Fae  | Trader      | silenced  | You have been silenced                                           |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Dan           |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Han           |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Ed            |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ed           |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi           |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Bob           |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 6           | NPC Gia  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Dan           |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Han           |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Ed            |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ed           |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi           |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Bob           |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 6           | NPC Han  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Dan           |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Han           |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Ed            |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ed           |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi           |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Bob           |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 6           | NPC Igi  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Dan           |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Han           |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Ed            |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ed           |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi           |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Bob           |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 6           | NPC Jeff | Prophet     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Dan           |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Han           |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Ed            |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ed           |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi           |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Bob           |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Igi           |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Ken is targeting NPC Dan           |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Han           |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Ed            |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Ed           |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann           |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Igi           |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Bob           |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed    |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed     |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 6           | NPC Lee  | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 6           | NPC Lee  | Psychic     | reveal    | Player: NPC Gia is not possessed                                 |
| 6           | NPC Lee  | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 6           | NPC Lee  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 6           | NPC Lee  | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |