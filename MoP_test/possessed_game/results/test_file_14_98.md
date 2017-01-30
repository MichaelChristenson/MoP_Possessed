#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 98   | 14      | 7       |

#### Roles
| Role         |
| :----------- |
| Medic        |
| Judge        |
| Spy          |
| Assassin     |
| Demagog      |
| Jailer       |
| Inspector    |
| Silencer     |
| Priest       |
| Prophet      |
| Trader       |
| Reporter     |
| Psychic      |
| Executioner  |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Norm | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Mark | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Ann  | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Bob  | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Bob  | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Cal  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Cal  | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Trader      | role change | Your Role is Trader       |
| 0           | NPC Dan  | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Ed   | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Fae  | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Gia  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Han  | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Igi  | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Priest      | role change | Your Role is Priest       |
| 0           | NPC Jeff | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Ken  | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Lee  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Mark | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Mark | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Norm | Judge       | role change | Your Role is Judge        |
| 0           | NPC Norm | Judge       | possessed   | You are Possessed         |

#### Actions Round 1
| round_index | Player   | action    | Target 1  | Target 2 | status                         |
| :-----------| :--------| :---------| :---------| :--------| :----------------------------- |
| 1           | NPC Ann  | Demagog   | Jailer    |          | voting in progress             |
| 1           | NPC Bob  | Silencer  | NPC Fae   |          | successful                     |
| 1           | NPC Cal  | Medic     | NPC Ken   |          | successful                     |
| 1           | NPC Dan  | Trader    | NPC Ed    | NPC Bob  | failed because not vulnerable  |
| 1           | NPC Ed   | Reporter  | NPC Norm  |          | successful                     |
| 1           | NPC Fae  | Assassin  | Priest    |          | successful                     |
| 1           | NPC Gia  | Inspector | NPC Han   |          | successful                     |
| 1           | NPC Han  | Prophet   | NPC Ken   |          | successful                     |
| 1           | NPC Ken  | Spy       |           |          | successful                     |
| 1           | NPC Mark | Psychic   |           |          | successful                     |
| 1           | NPC Norm | Judge     | Inspector |          | successful                     |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Norm | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ken  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Ed   | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Mark | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                           |
| :-----------| :--------| :-----------| :---------| :---------------------------------------------------------------- |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Ann  | Demagog     | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 1           | NPC Bob  | Silencer    | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Bob  | Silencer    | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 1           | NPC Cal  | Medic       | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Cal  | Medic       | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Dan  | Trader      | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Ed   | Reporter    | reveal    | NPC Norm is Judge                                                 |
| 1           | NPC Ed   | Reporter    | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 1           | NPC Fae  | Assassin    | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Fae  | Assassin    | silenced  | You have been silenced                                            |
| 1           | NPC Fae  | Assassin    | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 1           | NPC Gia  | Inspector   | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Gia  | Inspector   | reveal    | Prophet is Innocent                                               |
| 1           | NPC Gia  | Inspector   | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Han  | Prophet     | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Igi  | Jailer      | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Jeff | Priest      | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 1           | NPC Ken  | Spy         | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Ken  | Spy         | reveal    | NPC Norm is targeting NPC Gia                                     |
| 1           | NPC Ken  | Spy         | reveal    | NPC Gia is targeting NPC Han                                      |
| 1           | NPC Ken  | Spy         | reveal    | NPC Bob is targeting NPC Fae                                      |
| 1           | NPC Ken  | Spy         | reveal    | NPC Ed is targeting NPC Norm                                      |
| 1           | NPC Ken  | Spy         | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Lee  | Executioner | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 1           | NPC Mark | Psychic     | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Mark | Psychic     | reveal    | Player: NPC Fae is not possessed                                  |
| 1           | NPC Mark | Psychic     | reveal    | Player: NPC Dan is not possessed                                  |
| 1           | NPC Mark | Psychic     | reveal    | Player: NPC Ann is not possessed                                  |
| 1           | NPC Mark | Psychic     | reveal    | Player: NPC Ken is not possessed                                  |
| 1           | NPC Mark | Psychic     | reveal    | Player: NPC Jeff is not possessed                                 |
| 1           | NPC Mark | Psychic     | reveal    | Player: NPC Ed is not possessed                                   |
| 1           | NPC Mark | Psychic     | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 1           | NPC Norm | Judge       | broadcast | I (NPC Gia) inspected NPC Han and they are not possessed          |
| 1           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed          |
| 1           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 1           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Norm | Judge       | vote      | Demagog has initiated a vote on eliminating Jailer                |

#### Actions Round 2
| round_index | Player   | action   | Target 1  | Target 2 | status      |
| :-----------| :--------| :--------| :---------| :--------| :---------- |
| 2           | NPC Bob  | Silencer | NPC Cal   |          | successful  |
| 2           | NPC Cal  | Medic    | NPC Fae   |          | successful  |
| 2           | NPC Han  | Prophet  | NPC Dan   |          | successful  |
| 2           | NPC Ken  | Spy      |           |          | successful  |
| 2           | NPC Mark | Psychic  |           |          | successful  |
| 2           | NPC Norm | Judge    | Inspector |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Norm | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ken  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Gia  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Bob  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Ed   | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Mark | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                         |
| :-----------| :--------| :-----------| :---------| :-------------------------------------------------------------- |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Cal  | Medic       | silenced  | You have been silenced                                          |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Ken  | Spy         | reveal    | NPC Cal is targeting NPC Ken                                    |
| 2           | NPC Ken  | Spy         | reveal    | NPC Norm is targeting NPC Gia                                   |
| 2           | NPC Ken  | Spy         | reveal    | NPC Fae is targeting NPC Jeff                                   |
| 2           | NPC Ken  | Spy         | reveal    | NPC Ann is targeting NPC Igi                                    |
| 2           | NPC Ken  | Spy         | reveal    | NPC Gia is targeting NPC Han                                    |
| 2           | NPC Ken  | Spy         | reveal    | NPC Bob is targeting NPC Cal                                    |
| 2           | NPC Ken  | Spy         | reveal    | NPC Han is targeting NPC Ken                                    |
| 2           | NPC Ken  | Spy         | reveal    | NPC Dan is targeting NPC Ed                                     |
| 2           | NPC Ken  | Spy         | reveal    | NPC Dan is targeting NPC Ed                                     |
| 2           | NPC Ken  | Spy         | reveal    | NPC Ed is targeting NPC Norm                                    |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Mark | Psychic     | reveal    | Player: NPC Bob is not possessed                                |
| 2           | NPC Mark | Psychic     | reveal    | Player: NPC Igi is not possessed                                |
| 2           | NPC Mark | Psychic     | reveal    | Player: NPC Han is not possessed                                |
| 2           | NPC Mark | Psychic     | reveal    | Player: NPC Ed is not possessed                                 |
| 2           | NPC Mark | Psychic     | reveal    | Player: NPC Gia is not possessed                                |
| 2           | NPC Mark | Psychic     | reveal    | Player: NPC Jeff is not possessed                               |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Ken         |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff        |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi         |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han         |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Fae         |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Ken         |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed          |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm         |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed     |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 2           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |

#### Actions Round 3
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 3           | NPC Ann  | Demagog   | Assassin |          | voting in progress  |
| 3           | NPC Bob  | Silencer  | NPC Ken  |          | successful          |
| 3           | NPC Cal  | Medic     | NPC Ann  |          | successful          |
| 3           | NPC Ed   | Reporter  | NPC Jeff |          | successful          |
| 3           | NPC Fae  | Assassin  | Silencer |          | successful          |
| 3           | NPC Gia  | Inspector | NPC Ann  |          | successful          |
| 3           | NPC Han  | Prophet   | NPC Igi  |          | successful          |
| 3           | NPC Ken  | Spy       |          |          | successful          |
| 3           | NPC Mark | Psychic   |          |          | successful          |
| 3           | NPC Norm | Judge     | Demagog  |          | successful          |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Norm | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ken  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Fae  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Gia  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Bob  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan  | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ed   | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Mark | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message   | details                                                           |
| :-----------| :--------| :-----------| :---------| :---------------------------------------------------------------- |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Ann  | Demagog     | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Bob  | Silencer    | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Cal  | Medic       | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Dan  | Trader      | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Ed   | Reporter    | reveal    | NPC Jeff is Priest                                                |
| 3           | NPC Ed   | Reporter    | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Fae  | Assassin    | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Gia  | Inspector   | reveal    | Demagog is Innocent                                               |
| 3           | NPC Gia  | Inspector   | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Han  | Prophet     | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Igi  | Jailer      | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Jeff | Priest      | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Ken  | Spy         | silenced  | You have been silenced                                            |
| 3           | NPC Ken  | Spy         | reveal    | NPC Cal is targeting NPC Fae                                      |
| 3           | NPC Ken  | Spy         | reveal    | NPC Norm is targeting NPC Ann                                     |
| 3           | NPC Ken  | Spy         | reveal    | NPC Fae is targeting NPC Jeff                                     |
| 3           | NPC Ken  | Spy         | reveal    | NPC Ann is targeting NPC Igi                                      |
| 3           | NPC Ken  | Spy         | reveal    | NPC Gia is targeting NPC Ann                                      |
| 3           | NPC Ken  | Spy         | reveal    | NPC Bob is targeting NPC Ken                                      |
| 3           | NPC Ken  | Spy         | reveal    | NPC Han is targeting NPC Dan                                      |
| 3           | NPC Ken  | Spy         | reveal    | NPC Dan is targeting NPC Ed                                       |
| 3           | NPC Ken  | Spy         | reveal    | NPC Dan is targeting NPC Ed                                       |
| 3           | NPC Ken  | Spy         | reveal    | NPC Ed is targeting NPC Jeff                                      |
| 3           | NPC Ken  | Spy         | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Lee  | Executioner | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Mark | Psychic     | reveal    | Player: NPC Lee is not possessed                                  |
| 3           | NPC Mark | Psychic     | reveal    | Player: NPC Han is not possessed                                  |
| 3           | NPC Mark | Psychic     | reveal    | Player: NPC Jeff is not possessed                                 |
| 3           | NPC Mark | Psychic     | reveal    | Player: NPC Bob is not possessed                                  |
| 3           | NPC Mark | Psychic     | reveal    | Player: NPC Ed is not possessed                                   |
| 3           | NPC Mark | Psychic     | reveal    | Player: NPC Fae is not possessed                                  |
| 3           | NPC Mark | Psychic     | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Ed) am the Reporter and NPC Jeff is the Priest             |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Gia) inspected NPC Ann and they are not possessed          |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Fae           |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Gia          |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Jeff          |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Han           |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Cal           |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Han is targeting NPC Dan           |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Norm           |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 3           | NPC Norm | Judge       | vote      | Demagog has initiated a vote on eliminating Assassin              |

#### Actions Round 4
| round_index | Player   | action   | Target 1 | Target 2 | status              |
| :-----------| :--------| :--------| :--------| :--------| :------------------ |
| 4           | NPC Ann  | Demagog  | Jailer   |          | voting in progress  |
| 4           | NPC Bob  | Silencer | NPC Lee  |          | successful          |
| 4           | NPC Cal  | Medic    | NPC Igi  |          | successful          |
| 4           | NPC Han  | Prophet  | NPC Bob  |          | successful          |
| 4           | NPC Ken  | Spy      |          |          | successful          |
| 4           | NPC Mark | Psychic  |          |          | successful          |
| 4           | NPC Norm | Judge    | Demagog  |          | successful          |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Norm | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ken  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Gia  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Bob  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan  | Trader      | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed   | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Mark | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                           |
| :-----------| :--------| :-----------| :---------| :---------------------------------------------------------------- |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Ann  | Demagog     | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 4           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Bob  | Silencer    | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 4           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Cal  | Medic       | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Dan  | Trader      | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Ed   | Reporter    | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 4           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Fae  | Assassin    | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 4           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Gia  | Inspector   | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Han  | Prophet     | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Igi  | Jailer      | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Jeff | Priest      | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Ken  | Spy         | reveal    | NPC Cal is targeting NPC Ann                                      |
| 4           | NPC Ken  | Spy         | reveal    | NPC Norm is targeting NPC Ann                                     |
| 4           | NPC Ken  | Spy         | reveal    | NPC Fae is targeting NPC Bob                                      |
| 4           | NPC Ken  | Spy         | reveal    | NPC Ann is targeting NPC Fae                                      |
| 4           | NPC Ken  | Spy         | reveal    | NPC Gia is targeting NPC Ann                                      |
| 4           | NPC Ken  | Spy         | reveal    | NPC Bob is targeting NPC Lee                                      |
| 4           | NPC Ken  | Spy         | reveal    | NPC Han is targeting NPC Igi                                      |
| 4           | NPC Ken  | Spy         | reveal    | NPC Dan is targeting NPC Ed                                       |
| 4           | NPC Ken  | Spy         | reveal    | NPC Dan is targeting NPC Ed                                       |
| 4           | NPC Ken  | Spy         | reveal    | NPC Ed is targeting NPC Jeff                                      |
| 4           | NPC Ken  | Spy         | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Lee  | Executioner | silenced  | You have been silenced                                            |
| 4           | NPC Lee  | Executioner | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 4           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Mark | Psychic     | reveal    | Player: NPC Ken is not possessed                                  |
| 4           | NPC Mark | Psychic     | reveal    | Player: NPC Ann is not possessed                                  |
| 4           | NPC Mark | Psychic     | reveal    | Player: NPC Bob is not possessed                                  |
| 4           | NPC Mark | Psychic     | reveal    | Player: NPC Dan is not possessed                                  |
| 4           | NPC Mark | Psychic     | reveal    | Player: NPC Gia is not possessed                                  |
| 4           | NPC Mark | Psychic     | reveal    | Player: NPC Igi is not possessed                                  |
| 4           | NPC Mark | Psychic     | vote      | Demagog has initiated a vote on eliminating Jailer                |
| 4           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 4           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed     |
| 4           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Norm | Judge       | vote      | Demagog has initiated a vote on eliminating Jailer                |

#### Actions Round 5
| round_index | Player   | action    | Target 1 | Target 2 | status                         |
| :-----------| :--------| :---------| :--------| :--------| :----------------------------- |
| 5           | NPC Bob  | Silencer  | NPC Han  |          | successful                     |
| 5           | NPC Cal  | Medic     | NPC Gia  |          | successful                     |
| 5           | NPC Dan  | Trader    | NPC Jeff | NPC Ann  | failed because not vulnerable  |
| 5           | NPC Ed   | Reporter  | NPC Lee  |          | successful                     |
| 5           | NPC Fae  | Assassin  | Prophet  |          | successful                     |
| 5           | NPC Gia  | Inspector | NPC Bob  |          | successful                     |
| 5           | NPC Han  | Prophet   | NPC Cal  |          | successful                     |
| 5           | NPC Ken  | Spy       |          |          | successful                     |
| 5           | NPC Mark | Psychic   |          |          | successful                     |
| 5           | NPC Norm | Judge     | Psychic  |          | successful                     |

#### States Round 5
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Norm | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ken  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Fae  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Ann  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Gia  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Han  | Prophet     | True       | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 5           | NPC Ed   | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Mark | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player   | Role        | message     | details                                                           |
| :-----------| :--------| :-----------| :-----------| :---------------------------------------------------------------- |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Ann  | Demagog     | elimination | NPC Han has been eliminated                                       |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Bob  | Silencer    | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Bob  | Silencer    | elimination | NPC Han has been eliminated                                       |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Cal  | Medic       | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Cal  | Medic       | elimination | NPC Han has been eliminated                                       |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Dan  | Trader      | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Dan  | Trader      | elimination | NPC Han has been eliminated                                       |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Ed   | Reporter    | reveal      | NPC Lee is Executioner                                            |
| 5           | NPC Ed   | Reporter    | elimination | NPC Han has been eliminated                                       |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Fae  | Assassin    | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Fae  | Assassin    | elimination | NPC Han has been eliminated                                       |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Gia  | Inspector   | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Gia  | Inspector   | reveal      | Silencer is Innocent                                              |
| 5           | NPC Gia  | Inspector   | elimination | NPC Han has been eliminated                                       |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Han  | Prophet     | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Han  | Prophet     | silenced    | You have been silenced                                            |
| 5           | NPC Han  | Prophet     | elimination | NPC Han has been eliminated                                       |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Igi  | Jailer      | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Igi  | Jailer      | elimination | NPC Han has been eliminated                                       |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Jeff | Priest      | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Jeff | Priest      | elimination | NPC Han has been eliminated                                       |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Ken  | Spy         | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Ken  | Spy         | reveal      | NPC Cal is targeting NPC Igi                                      |
| 5           | NPC Ken  | Spy         | reveal      | NPC Norm is targeting NPC Mark                                    |
| 5           | NPC Ken  | Spy         | reveal      | NPC Fae is targeting NPC Bob                                      |
| 5           | NPC Ken  | Spy         | reveal      | NPC Ann is targeting NPC Igi                                      |
| 5           | NPC Ken  | Spy         | reveal      | NPC Gia is targeting NPC Bob                                      |
| 5           | NPC Ken  | Spy         | reveal      | NPC Bob is targeting NPC Han                                      |
| 5           | NPC Ken  | Spy         | reveal      | NPC Han is targeting NPC Bob                                      |
| 5           | NPC Ken  | Spy         | reveal      | NPC Dan is targeting NPC Ed                                       |
| 5           | NPC Ken  | Spy         | reveal      | NPC Dan is targeting NPC Ed                                       |
| 5           | NPC Ken  | Spy         | reveal      | NPC Ed is targeting NPC Lee                                       |
| 5           | NPC Ken  | Spy         | elimination | NPC Han has been eliminated                                       |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Lee  | Executioner | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Lee  | Executioner | elimination | NPC Han has been eliminated                                       |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Mark | Psychic     | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Mark | Psychic     | reveal      | Player: NPC Bob is not possessed                                  |
| 5           | NPC Mark | Psychic     | reveal      | Player: NPC Han is not possessed                                  |
| 5           | NPC Mark | Psychic     | reveal      | Player: NPC Cal is not possessed                                  |
| 5           | NPC Mark | Psychic     | reveal      | Player: NPC Jeff is not possessed                                 |
| 5           | NPC Mark | Psychic     | reveal      | Player: NPC Ann is not possessed                                  |
| 5           | NPC Mark | Psychic     | reveal      | Player: NPC Dan is not possessed                                  |
| 5           | NPC Mark | Psychic     | elimination | NPC Han has been eliminated                                       |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Gia) inspected NPC Bob and they are not possessed          |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Igi           |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Ann          |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Bob           |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ann           |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee           |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Ken) am the Spy and NPC Han is targeting NPC Bob           |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Jeff           |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Mark) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 5           | NPC Norm | Judge       | broadcast   | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 5           | NPC Norm | Judge       | elimination | NPC Han has been eliminated                                       |

#### Actions Round 6
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 6           | NPC Ann  | Demagog   | Assassin |          | voting in progress  |
| 6           | NPC Bob  | Silencer  | NPC Lee  |          | successful          |
| 6           | NPC Cal  | Medic     | NPC Bob  |          | successful          |
| 6           | NPC Gia  | Inspector | NPC Ken  |          | successful          |
| 6           | NPC Han  | Prophet   | NPC Jeff |          | successful          |
| 6           | NPC Ken  | Spy       |          |          | successful          |
| 6           | NPC Mark | Psychic   |          |          | successful          |
| 6           | NPC Norm | Judge     | Jailer   |          | successful          |

#### States Round 6
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Cal  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Norm | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ken  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Fae  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ann  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Gia  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Bob  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Han  | Prophet     | True       | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 6           | NPC Ed   | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Mark | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player   | Role        | message   | details                                                           |
| :-----------| :--------| :-----------| :---------| :---------------------------------------------------------------- |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Ann  | Demagog     | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Bob  | Silencer    | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Cal  | Medic       | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Dan  | Trader      | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Ed   | Reporter    | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Fae  | Assassin    | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Gia  | Inspector   | reveal    | Spy is Innocent                                                   |
| 6           | NPC Gia  | Inspector   | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Han  | Prophet     | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Igi  | Jailer      | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Jeff | Priest      | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Ken  | Spy         | reveal    | NPC Cal is targeting NPC Gia                                      |
| 6           | NPC Ken  | Spy         | reveal    | NPC Norm is targeting NPC Igi                                     |
| 6           | NPC Ken  | Spy         | reveal    | NPC Fae is targeting NPC Han                                      |
| 6           | NPC Ken  | Spy         | reveal    | NPC Ann is targeting NPC Igi                                      |
| 6           | NPC Ken  | Spy         | reveal    | NPC Gia is targeting NPC Ken                                      |
| 6           | NPC Ken  | Spy         | reveal    | NPC Bob is targeting NPC Lee                                      |
| 6           | NPC Ken  | Spy         | reveal    | NPC Dan is targeting NPC Jeff                                     |
| 6           | NPC Ken  | Spy         | reveal    | NPC Dan is targeting NPC Jeff                                     |
| 6           | NPC Ken  | Spy         | reveal    | NPC Ed is targeting NPC Lee                                       |
| 6           | NPC Ken  | Spy         | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Lee  | Executioner | silenced  | You have been silenced                                            |
| 6           | NPC Lee  | Executioner | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Mark | Psychic     | reveal    | Player: NPC Ann is not possessed                                  |
| 6           | NPC Mark | Psychic     | reveal    | Player: NPC Dan is not possessed                                  |
| 6           | NPC Mark | Psychic     | reveal    | Player: NPC Bob is not possessed                                  |
| 6           | NPC Mark | Psychic     | reveal    | Player: NPC Gia is not possessed                                  |
| 6           | NPC Mark | Psychic     | reveal    | Player: NPC Cal is not possessed                                  |
| 6           | NPC Mark | Psychic     | reveal    | Player: NPC Ed is not possessed                                   |
| 6           | NPC Mark | Psychic     | vote      | Demagog has initiated a vote on eliminating Assassin              |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Gia) inspected NPC Ken and they are not possessed          |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Gia           |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Mark         |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han           |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Igi           |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Bob           |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Han           |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff          |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee            |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Medic is not possessed        |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Trader is not possessed       |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed       |
| 6           | NPC Norm | Judge       | vote      | Demagog has initiated a vote on eliminating Assassin              |

#### Actions Round 7
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 7           | NPC Bob  | Silencer | NPC Lee  |          | successful  |
| 7           | NPC Cal  | Medic    | NPC Jeff |          | successful  |
| 7           | NPC Ed   | Reporter | NPC Igi  |          | successful  |
| 7           | NPC Fae  | Assassin | Spy      |          | successful  |
| 7           | NPC Han  | Prophet  | NPC Cal  |          | successful  |
| 7           | NPC Ken  | Spy      |          |          | successful  |
| 7           | NPC Mark | Psychic  |          |          | successful  |
| 7           | NPC Norm | Judge    | Reporter |          | successful  |

#### States Round 7
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Cal  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Norm | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Ken  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Fae  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Ann  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Gia  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Bob  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Han  | Prophet     | True       | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Dan  | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Ed   | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Mark | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player   | Role        | message   | details                                                         |
| :-----------| :--------| :-----------| :---------| :-------------------------------------------------------------- |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Bob  | Silencer    | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Cal  | Medic       | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Ed   | Reporter    | reveal    | NPC Igi is Jailer                                               |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Fae  | Assassin    | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Gia  | Inspector   | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Han  | Prophet     | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Igi  | Jailer      | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Jeff | Priest      | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Ken  | Spy         | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Ken  | Spy         | reveal    | NPC Cal is targeting NPC Bob                                    |
| 7           | NPC Ken  | Spy         | reveal    | NPC Norm is targeting NPC Ed                                    |
| 7           | NPC Ken  | Spy         | reveal    | NPC Fae is targeting NPC Han                                    |
| 7           | NPC Ken  | Spy         | reveal    | NPC Ann is targeting NPC Fae                                    |
| 7           | NPC Ken  | Spy         | reveal    | NPC Gia is targeting NPC Ken                                    |
| 7           | NPC Ken  | Spy         | reveal    | NPC Bob is targeting NPC Lee                                    |
| 7           | NPC Ken  | Spy         | reveal    | NPC Dan is targeting NPC Jeff                                   |
| 7           | NPC Ken  | Spy         | reveal    | NPC Dan is targeting NPC Jeff                                   |
| 7           | NPC Ken  | Spy         | reveal    | NPC Ed is targeting NPC Igi                                     |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Lee  | Executioner | silenced  | You have been silenced                                          |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Mark | Psychic     | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Mark | Psychic     | reveal    | Player: NPC Bob is not possessed                                |
| 7           | NPC Mark | Psychic     | reveal    | Player: NPC Ed is not possessed                                 |
| 7           | NPC Mark | Psychic     | reveal    | Player: NPC Dan is not possessed                                |
| 7           | NPC Mark | Psychic     | reveal    | Player: NPC Lee is not possessed                                |
| 7           | NPC Mark | Psychic     | reveal    | Player: NPC Ann is not possessed                                |
| 7           | NPC Mark | Psychic     | reveal    | Player: NPC Gia is not possessed                                |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Ed) am the Reporter and NPC Igi is the Jailer            |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Cal is targeting NPC Bob         |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Norm is targeting NPC Igi        |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Fae is targeting NPC Han         |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Ann is targeting NPC Fae         |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Gia is targeting NPC Ken         |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Bob is targeting NPC Lee         |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Dan is targeting NPC Jeff        |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Ken) am the Spy and NPC Ed is targeting NPC Lee          |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Priest is not possessed     |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Spy is not possessed        |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Assassin is not possessed   |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Norm | Judge       | broadcast | I (NPC Mark) am the Psychic and the Silencer is not possessed   |