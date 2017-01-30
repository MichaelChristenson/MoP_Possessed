#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 59   | 10      | 9       |

#### Roles
| Role       |
| :--------- |
| Demagog    |
| Silencer   |
| Spy        |
| Inspector  |
| Medic      |
| Judge      |
| Psychic    |
| Trader     |
| Reporter   |
| Assassin   |

#### States Round 0
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ed   | Demagog   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Silencer  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Trader    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal  | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Assassin  | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role      | message     | details                 |
| :-----------| :--------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann  | Judge     | role change | Your Role is Judge      |
| 0           | NPC Ann  | Judge     | possessed   | You are Possessed       |
| 0           | NPC Bob  | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Bob  | Inspector | possessed   | You are Not Possessed   |
| 0           | NPC Cal  | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Cal  | Reporter  | possessed   | You are Not Possessed   |
| 0           | NPC Dan  | Silencer  | role change | Your Role is Silencer   |
| 0           | NPC Dan  | Silencer  | possessed   | You are Not Possessed   |
| 0           | NPC Ed   | Demagog   | role change | Your Role is Demagog    |
| 0           | NPC Ed   | Demagog   | possessed   | You are Not Possessed   |
| 0           | NPC Fae  | Spy       | role change | Your Role is Spy        |
| 0           | NPC Fae  | Spy       | possessed   | You are Not Possessed   |
| 0           | NPC Gia  | Assassin  | role change | Your Role is Assassin   |
| 0           | NPC Gia  | Assassin  | possessed   | You are Not Possessed   |
| 0           | NPC Han  | Medic     | role change | Your Role is Medic      |
| 0           | NPC Han  | Medic     | possessed   | You are Not Possessed   |
| 0           | NPC Igi  | Psychic   | role change | Your Role is Psychic    |
| 0           | NPC Igi  | Psychic   | possessed   | You are Not Possessed   |
| 0           | NPC Jeff | Trader    | role change | Your Role is Trader     |
| 0           | NPC Jeff | Trader    | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player   | action    | Target 1  | Target 2 | status                         |
| :-----------| :--------| :---------| :---------| :--------| :----------------------------- |
| 1           | NPC Ann  | Judge     | Assassin  |          | successful                     |
| 1           | NPC Bob  | Inspector | NPC Gia   |          | successful                     |
| 1           | NPC Cal  | Reporter  | NPC Ed    |          | successful                     |
| 1           | NPC Dan  | Silencer  | NPC Cal   |          | successful                     |
| 1           | NPC Ed   | Demagog   | Psychic   |          | voting in progress             |
| 1           | NPC Fae  | Spy       |           |          | successful                     |
| 1           | NPC Gia  | Assassin  | Inspector |          | successful                     |
| 1           | NPC Han  | Medic     | NPC Dan   |          | successful                     |
| 1           | NPC Igi  | Psychic   |           |          | successful                     |
| 1           | NPC Jeff | Trader    | NPC Dan   | NPC Cal  | failed because not vulnerable  |

#### States Round 1
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ed   | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan  | Silencer  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Han  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann  | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Igi  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Jeff | Trader    | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Cal  | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Gia  | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role      | message   | details                                                        |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------- |
| 1           | NPC Ann  | Judge     | broadcast | I (NPC Bob) inspected NPC Gia and they are not possessed       |
| 1           | NPC Ann  | Judge     | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Demagog          |
| 1           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Ann  | Judge     | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Bob  | Inspector | broadcast | I (NPC Bob) inspected NPC Gia and they are not possessed       |
| 1           | NPC Bob  | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Demagog          |
| 1           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Bob  | Inspector | reveal    | Assassin is Innocent                                           |
| 1           | NPC Bob  | Inspector | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Cal  | Reporter  | broadcast | I (NPC Bob) inspected NPC Gia and they are not possessed       |
| 1           | NPC Cal  | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Demagog          |
| 1           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Cal  | Reporter  | silenced  | You have been silenced                                         |
| 1           | NPC Cal  | Reporter  | reveal    | NPC Ed is Demagog                                              |
| 1           | NPC Cal  | Reporter  | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Dan  | Silencer  | broadcast | I (NPC Bob) inspected NPC Gia and they are not possessed       |
| 1           | NPC Dan  | Silencer  | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Demagog          |
| 1           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Dan  | Silencer  | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Ed   | Demagog   | broadcast | I (NPC Bob) inspected NPC Gia and they are not possessed       |
| 1           | NPC Ed   | Demagog   | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Demagog          |
| 1           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Ed   | Demagog   | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Fae  | Spy       | broadcast | I (NPC Bob) inspected NPC Gia and they are not possessed       |
| 1           | NPC Fae  | Spy       | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Demagog          |
| 1           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Fae  | Spy       | reveal    | NPC Dan is targeting NPC Cal                                   |
| 1           | NPC Fae  | Spy       | reveal    | NPC Bob is targeting NPC Gia                                   |
| 1           | NPC Fae  | Spy       | reveal    | NPC Ann is targeting NPC Gia                                   |
| 1           | NPC Fae  | Spy       | reveal    | NPC Cal is targeting NPC Ed                                    |
| 1           | NPC Fae  | Spy       | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Gia  | Assassin  | broadcast | I (NPC Bob) inspected NPC Gia and they are not possessed       |
| 1           | NPC Gia  | Assassin  | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Demagog          |
| 1           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Gia  | Assassin  | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Han  | Medic     | broadcast | I (NPC Bob) inspected NPC Gia and they are not possessed       |
| 1           | NPC Han  | Medic     | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Demagog          |
| 1           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Han  | Medic     | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Bob) inspected NPC Gia and they are not possessed       |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Demagog          |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Igi  | Psychic   | reveal    | Player: NPC Ed is not possessed                                |
| 1           | NPC Igi  | Psychic   | reveal    | Player: NPC Jeff is not possessed                              |
| 1           | NPC Igi  | Psychic   | reveal    | Player: NPC Fae is not possessed                               |
| 1           | NPC Igi  | Psychic   | reveal    | Player: NPC Gia is not possessed                               |
| 1           | NPC Igi  | Psychic   | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Jeff | Trader    | broadcast | I (NPC Bob) inspected NPC Gia and they are not possessed       |
| 1           | NPC Jeff | Trader    | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Demagog          |
| 1           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Jeff | Trader    | vote      | Demagog has initiated a vote on eliminating Psychic            |

#### Actions Round 2
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 2           | NPC Ann | Judge    | Demagog  |          | successful  |
| 2           | NPC Dan | Silencer | NPC Ann  |          | successful  |
| 2           | NPC Fae | Spy      |          |          | successful  |
| 2           | NPC Han | Medic    | NPC Fae  |          | successful  |
| 2           | NPC Igi | Psychic  |          |          | successful  |

#### States Round 2
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ed   | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan  | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Fae  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob  | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Han  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann  | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Igi  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Jeff | Trader    | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Cal  | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia  | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role      | message   | details                                                       |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------ |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ann  | Judge     | silenced  | You have been silenced                                        |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed       |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed    |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed       |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed    |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed       |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed    |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed       |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed    |
| 2           | NPC Fae  | Spy       | reveal    | NPC Ed is targeting NPC Igi                                   |
| 2           | NPC Fae  | Spy       | reveal    | NPC Dan is targeting NPC Ann                                  |
| 2           | NPC Fae  | Spy       | reveal    | NPC Bob is targeting NPC Gia                                  |
| 2           | NPC Fae  | Spy       | reveal    | NPC Han is targeting NPC Dan                                  |
| 2           | NPC Fae  | Spy       | reveal    | NPC Ann is targeting NPC Ed                                   |
| 2           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Dan                                 |
| 2           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Dan                                 |
| 2           | NPC Fae  | Spy       | reveal    | NPC Cal is targeting NPC Ed                                   |
| 2           | NPC Fae  | Spy       | reveal    | NPC Gia is targeting NPC Bob                                  |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed       |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed    |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed       |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed    |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed       |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed    |
| 2           | NPC Igi  | Psychic   | reveal    | Player: NPC Ed is not possessed                               |
| 2           | NPC Igi  | Psychic   | reveal    | Player: NPC Han is not possessed                              |
| 2           | NPC Igi  | Psychic   | reveal    | Player: NPC Cal is not possessed                              |
| 2           | NPC Igi  | Psychic   | reveal    | Player: NPC Bob is not possessed                              |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed       |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed    |

#### Actions Round 3
| round_index | Player  | action    | Target 1  | Target 2 | status              |
| :-----------| :-------| :---------| :---------| :--------| :------------------ |
| 3           | NPC Ann | Judge     | Assassin  |          | successful          |
| 3           | NPC Bob | Inspector | NPC Han   |          | successful          |
| 3           | NPC Cal | Reporter  | NPC Han   |          | successful          |
| 3           | NPC Dan | Silencer  | NPC Fae   |          | successful          |
| 3           | NPC Ed  | Demagog   | Inspector |          | voting in progress  |
| 3           | NPC Fae | Spy       |           |          | successful          |
| 3           | NPC Gia | Assassin  | Judge     |          | successful          |
| 3           | NPC Han | Medic     | NPC Bob   |          | successful          |
| 3           | NPC Igi | Psychic   |           |          | successful          |

#### States Round 3
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ed   | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan  | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Fae  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob  | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Han  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann  | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Igi  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Jeff | Trader    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Cal  | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Gia  | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role      | message   | details                                                       |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------ |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Bob) inspected NPC Han and they are not possessed      |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Cal) am the Reporter and NPC Han is the Medic          |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann       |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae       |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed        |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ann  | Judge     | vote      | Demagog has initiated a vote on eliminating Inspector         |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Bob) inspected NPC Han and they are not possessed      |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Han is the Medic          |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann       |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae       |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed        |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Bob  | Inspector | reveal    | Medic is Innocent                                             |
| 3           | NPC Bob  | Inspector | vote      | Demagog has initiated a vote on eliminating Inspector         |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Bob) inspected NPC Han and they are not possessed      |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Han is the Medic          |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann       |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae       |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed        |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Cal  | Reporter  | reveal    | NPC Han is Medic                                              |
| 3           | NPC Cal  | Reporter  | vote      | Demagog has initiated a vote on eliminating Inspector         |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Bob) inspected NPC Han and they are not possessed      |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Cal) am the Reporter and NPC Han is the Medic          |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann       |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae       |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed        |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Dan  | Silencer  | vote      | Demagog has initiated a vote on eliminating Inspector         |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Bob) inspected NPC Han and they are not possessed      |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Cal) am the Reporter and NPC Han is the Medic          |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann       |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae       |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed        |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ed   | Demagog   | vote      | Demagog has initiated a vote on eliminating Inspector         |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Bob) inspected NPC Han and they are not possessed      |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Cal) am the Reporter and NPC Han is the Medic          |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann       |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae       |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed        |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Fae  | Spy       | silenced  | You have been silenced                                        |
| 3           | NPC Fae  | Spy       | reveal    | NPC Ed is targeting NPC Igi                                   |
| 3           | NPC Fae  | Spy       | reveal    | NPC Dan is targeting NPC Fae                                  |
| 3           | NPC Fae  | Spy       | reveal    | NPC Bob is targeting NPC Han                                  |
| 3           | NPC Fae  | Spy       | reveal    | NPC Han is targeting NPC Fae                                  |
| 3           | NPC Fae  | Spy       | reveal    | NPC Ann is targeting NPC Gia                                  |
| 3           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Dan                                 |
| 3           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Dan                                 |
| 3           | NPC Fae  | Spy       | reveal    | NPC Cal is targeting NPC Han                                  |
| 3           | NPC Fae  | Spy       | reveal    | NPC Gia is targeting NPC Bob                                  |
| 3           | NPC Fae  | Spy       | vote      | Demagog has initiated a vote on eliminating Inspector         |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Bob) inspected NPC Han and they are not possessed      |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Cal) am the Reporter and NPC Han is the Medic          |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann       |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae       |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed        |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Gia  | Assassin  | vote      | Demagog has initiated a vote on eliminating Inspector         |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Bob) inspected NPC Han and they are not possessed      |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Cal) am the Reporter and NPC Han is the Medic          |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann       |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae       |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed        |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Han  | Medic     | vote      | Demagog has initiated a vote on eliminating Inspector         |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Bob) inspected NPC Han and they are not possessed      |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Cal) am the Reporter and NPC Han is the Medic          |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann       |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae       |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed        |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Igi  | Psychic   | reveal    | Player: NPC Jeff is not possessed                             |
| 3           | NPC Igi  | Psychic   | reveal    | Player: NPC Fae is not possessed                              |
| 3           | NPC Igi  | Psychic   | reveal    | Player: NPC Cal is not possessed                              |
| 3           | NPC Igi  | Psychic   | reveal    | Player: NPC Bob is not possessed                              |
| 3           | NPC Igi  | Psychic   | vote      | Demagog has initiated a vote on eliminating Inspector         |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Bob) inspected NPC Han and they are not possessed      |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Cal) am the Reporter and NPC Han is the Medic          |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Igi        |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann       |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Gia       |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae       |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed        |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Dan      |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ed        |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Bob       |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed   |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed     |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed  |
| 3           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Jeff | Trader    | vote      | Demagog has initiated a vote on eliminating Inspector         |

#### Actions Round 4
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 4           | NPC Ann | Judge     | Reporter |          | successful  |
| 4           | NPC Bob | Inspector | NPC Jeff |          | successful  |
| 4           | NPC Dan | Silencer  | NPC Fae  |          | successful  |
| 4           | NPC Fae | Spy       |          |          | successful  |
| 4           | NPC Han | Medic     | NPC Ann  |          | successful  |
| 4           | NPC Igi | Psychic   |          |          | successful  |

#### States Round 4
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ed   | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan  | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Fae  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Han  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann  | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Igi  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Jeff | Trader    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Cal  | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Gia  | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role      | message   | details                                                        |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------- |
| 4           | NPC Ann  | Judge     | broadcast | I (NPC Bob) inspected NPC Jeff and they are not possessed      |
| 4           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Assassin is not possessed   |
| 4           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 4           | NPC Bob  | Inspector | broadcast | I (NPC Bob) inspected NPC Jeff and they are not possessed      |
| 4           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Assassin is not possessed   |
| 4           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 4           | NPC Bob  | Inspector | reveal    | Trader is Innocent                                             |
| 4           | NPC Cal  | Reporter  | broadcast | I (NPC Bob) inspected NPC Jeff and they are not possessed      |
| 4           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Assassin is not possessed   |
| 4           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 4           | NPC Dan  | Silencer  | broadcast | I (NPC Bob) inspected NPC Jeff and they are not possessed      |
| 4           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Assassin is not possessed   |
| 4           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 4           | NPC Ed   | Demagog   | broadcast | I (NPC Bob) inspected NPC Jeff and they are not possessed      |
| 4           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Assassin is not possessed   |
| 4           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 4           | NPC Fae  | Spy       | broadcast | I (NPC Bob) inspected NPC Jeff and they are not possessed      |
| 4           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Assassin is not possessed   |
| 4           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 4           | NPC Fae  | Spy       | silenced  | You have been silenced                                         |
| 4           | NPC Fae  | Spy       | reveal    | NPC Ed is targeting NPC Bob                                    |
| 4           | NPC Fae  | Spy       | reveal    | NPC Dan is targeting NPC Fae                                   |
| 4           | NPC Fae  | Spy       | reveal    | NPC Bob is targeting NPC Jeff                                  |
| 4           | NPC Fae  | Spy       | reveal    | NPC Han is targeting NPC Bob                                   |
| 4           | NPC Fae  | Spy       | reveal    | NPC Ann is targeting NPC Cal                                   |
| 4           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Dan                                  |
| 4           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Dan                                  |
| 4           | NPC Fae  | Spy       | reveal    | NPC Cal is targeting NPC Han                                   |
| 4           | NPC Fae  | Spy       | reveal    | NPC Gia is targeting NPC Ann                                   |
| 4           | NPC Gia  | Assassin  | broadcast | I (NPC Bob) inspected NPC Jeff and they are not possessed      |
| 4           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Assassin is not possessed   |
| 4           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Gia  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 4           | NPC Han  | Medic     | broadcast | I (NPC Bob) inspected NPC Jeff and they are not possessed      |
| 4           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Assassin is not possessed   |
| 4           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 4           | NPC Igi  | Psychic   | broadcast | I (NPC Bob) inspected NPC Jeff and they are not possessed      |
| 4           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Assassin is not possessed   |
| 4           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 4           | NPC Igi  | Psychic   | reveal    | Player: NPC Gia is not possessed                               |
| 4           | NPC Igi  | Psychic   | reveal    | Player: NPC Cal is not possessed                               |
| 4           | NPC Igi  | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 4           | NPC Igi  | Psychic   | reveal    | Player: NPC Jeff is not possessed                              |
| 4           | NPC Jeff | Trader    | broadcast | I (NPC Bob) inspected NPC Jeff and they are not possessed      |
| 4           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Assassin is not possessed   |
| 4           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |

#### Actions Round 5
| round_index | Player   | action   | Target 1 | Target 2 | status              |
| :-----------| :--------| :--------| :--------| :--------| :------------------ |
| 5           | NPC Ann  | Judge    | Demagog  |          | successful          |
| 5           | NPC Cal  | Reporter | NPC Dan  |          | successful          |
| 5           | NPC Dan  | Silencer | NPC Dan  |          | successful          |
| 5           | NPC Ed   | Demagog  | Judge    |          | voting in progress  |
| 5           | NPC Fae  | Spy      |          |          | successful          |
| 5           | NPC Gia  | Assassin | Reporter |          | successful          |
| 5           | NPC Han  | Medic    | NPC Igi  |          | successful          |
| 5           | NPC Igi  | Psychic  |          |          | successful          |
| 5           | NPC Jeff | Trader   | NPC Igi  | NPC Gia  | successful          |

#### States Round 5
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ed   | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Dan  | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Fae  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob  | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Han  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ann  | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Igi  | Assassin  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Jeff | Trader    | False      | False     | False      | 4         | True   | 0              | 0                  |
| 5           | NPC Cal  | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Gia  | Psychic   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player   | Role      | message   | details                                                        |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------- |
| 5           | NPC Ann  | Judge     | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Silencer        |
| 5           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 5           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 5           | NPC Ann  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 5           | NPC Ann  | Judge     | vote      | Demagog has initiated a vote on eliminating Judge              |
| 5           | NPC Bob  | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Silencer        |
| 5           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 5           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 5           | NPC Bob  | Inspector | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 5           | NPC Bob  | Inspector | vote      | Demagog has initiated a vote on eliminating Judge              |
| 5           | NPC Cal  | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Silencer        |
| 5           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 5           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 5           | NPC Cal  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 5           | NPC Cal  | Reporter  | reveal    | NPC Dan is Silencer                                            |
| 5           | NPC Cal  | Reporter  | vote      | Demagog has initiated a vote on eliminating Judge              |
| 5           | NPC Dan  | Silencer  | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Silencer        |
| 5           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 5           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 5           | NPC Dan  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 5           | NPC Dan  | Silencer  | silenced  | You have been silenced                                         |
| 5           | NPC Dan  | Silencer  | vote      | Demagog has initiated a vote on eliminating Judge              |
| 5           | NPC Ed   | Demagog   | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Silencer        |
| 5           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 5           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 5           | NPC Ed   | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 5           | NPC Ed   | Demagog   | vote      | Demagog has initiated a vote on eliminating Judge              |
| 5           | NPC Fae  | Spy       | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Silencer        |
| 5           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 5           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 5           | NPC Fae  | Spy       | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 5           | NPC Fae  | Spy       | reveal    | NPC Ed is targeting NPC Bob                                    |
| 5           | NPC Fae  | Spy       | reveal    | NPC Dan is targeting NPC Dan                                   |
| 5           | NPC Fae  | Spy       | reveal    | NPC Bob is targeting NPC Jeff                                  |
| 5           | NPC Fae  | Spy       | reveal    | NPC Han is targeting NPC Ann                                   |
| 5           | NPC Fae  | Spy       | reveal    | NPC Ann is targeting NPC Ed                                    |
| 5           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Dan                                  |
| 5           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Dan                                  |
| 5           | NPC Fae  | Spy       | reveal    | NPC Cal is targeting NPC Dan                                   |
| 5           | NPC Fae  | Spy       | reveal    | NPC Gia is targeting NPC Ann                                   |
| 5           | NPC Fae  | Spy       | vote      | Demagog has initiated a vote on eliminating Judge              |
| 5           | NPC Gia  | Psychic   | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Silencer        |
| 5           | NPC Gia  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Gia  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 5           | NPC Gia  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 5           | NPC Gia  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 5           | NPC Gia  | Psychic   | vote      | Demagog has initiated a vote on eliminating Judge              |
| 5           | NPC Han  | Medic     | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Silencer        |
| 5           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 5           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 5           | NPC Han  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 5           | NPC Han  | Medic     | vote      | Demagog has initiated a vote on eliminating Judge              |
| 5           | NPC Igi  | Assassin  | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Silencer        |
| 5           | NPC Igi  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Igi  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 5           | NPC Igi  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 5           | NPC Igi  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 5           | NPC Igi  | Assassin  | reveal    | Player: NPC Fae is not possessed                               |
| 5           | NPC Igi  | Assassin  | reveal    | Player: NPC Ed is not possessed                                |
| 5           | NPC Igi  | Assassin  | reveal    | Player: NPC Dan is not possessed                               |
| 5           | NPC Igi  | Assassin  | reveal    | Player: NPC Bob is not possessed                               |
| 5           | NPC Igi  | Assassin  | vote      | Demagog has initiated a vote on eliminating Judge              |
| 5           | NPC Jeff | Trader    | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Silencer        |
| 5           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 5           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 5           | NPC Jeff | Trader    | broadcast | I (NPC Igi) am the Psychic and the Spy is not possessed        |
| 5           | NPC Jeff | Trader    | vote      | Demagog has initiated a vote on eliminating Judge              |

#### Actions Round 6
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 6           | NPC Ann | Judge     | Psychic  |          | successful  |
| 6           | NPC Bob | Inspector | NPC Ann  |          | successful  |
| 6           | NPC Dan | Silencer  | NPC Cal  |          | successful  |
| 6           | NPC Fae | Spy       |          |          | successful  |
| 6           | NPC Han | Medic     | NPC Jeff |          | successful  |
| 6           | NPC Igi | Assassin  | Trader   |          | successful  |

#### States Round 6
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Ed   | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Dan  | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Fae  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Han  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ann  | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Igi  | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Jeff | Trader    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Cal  | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Gia  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player   | Role      | message   | details                                                   |
| :-----------| :--------| :---------| :---------| :-------------------------------------------------------- |
| 6           | NPC Ann  | Judge     | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed      |
| 6           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann    |
| 6           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Dan   |
| 6           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Jeff  |
| 6           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Igi   |
| 6           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed    |
| 6           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan   |
| 6           | NPC Bob  | Inspector | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed      |
| 6           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann    |
| 6           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Dan   |
| 6           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Jeff  |
| 6           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Igi   |
| 6           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed    |
| 6           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan   |
| 6           | NPC Bob  | Inspector | reveal    | Judge is Possessed                                        |
| 6           | NPC Cal  | Reporter  | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed      |
| 6           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann    |
| 6           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Dan   |
| 6           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Jeff  |
| 6           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Igi   |
| 6           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed    |
| 6           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan   |
| 6           | NPC Cal  | Reporter  | silenced  | You have been silenced                                    |
| 6           | NPC Dan  | Silencer  | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed      |
| 6           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann    |
| 6           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Dan   |
| 6           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Jeff  |
| 6           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Igi   |
| 6           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed    |
| 6           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Dan  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan   |
| 6           | NPC Ed   | Demagog   | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed      |
| 6           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann    |
| 6           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Dan   |
| 6           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Jeff  |
| 6           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Igi   |
| 6           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed    |
| 6           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan   |
| 6           | NPC Fae  | Spy       | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed      |
| 6           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann    |
| 6           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Dan   |
| 6           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Jeff  |
| 6           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Igi   |
| 6           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed    |
| 6           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan   |
| 6           | NPC Fae  | Spy       | reveal    | NPC Ed is targeting NPC Ann                               |
| 6           | NPC Fae  | Spy       | reveal    | NPC Dan is targeting NPC Cal                              |
| 6           | NPC Fae  | Spy       | reveal    | NPC Bob is targeting NPC Ann                              |
| 6           | NPC Fae  | Spy       | reveal    | NPC Han is targeting NPC Igi                              |
| 6           | NPC Fae  | Spy       | reveal    | NPC Ann is targeting NPC Gia                              |
| 6           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Igi                             |
| 6           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Igi                             |
| 6           | NPC Fae  | Spy       | reveal    | NPC Cal is targeting NPC Dan                              |
| 6           | NPC Gia  | Psychic   | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed      |
| 6           | NPC Gia  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann    |
| 6           | NPC Gia  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Dan   |
| 6           | NPC Gia  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Jeff  |
| 6           | NPC Gia  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Igi   |
| 6           | NPC Gia  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed    |
| 6           | NPC Gia  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Gia  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Gia  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan   |
| 6           | NPC Han  | Medic     | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed      |
| 6           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann    |
| 6           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Dan   |
| 6           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Jeff  |
| 6           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Igi   |
| 6           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed    |
| 6           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan   |
| 6           | NPC Igi  | Assassin  | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed      |
| 6           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann    |
| 6           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Dan   |
| 6           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Jeff  |
| 6           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Igi   |
| 6           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed    |
| 6           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan   |
| 6           | NPC Jeff | Trader    | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed      |
| 6           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann    |
| 6           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Dan   |
| 6           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Jeff  |
| 6           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Igi   |
| 6           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Ed    |
| 6           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi  |
| 6           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan   |

#### Actions Round 7
| round_index | Player   | action   | Target 1 | Target 2 | status              |
| :-----------| :--------| :--------| :--------| :--------| :------------------ |
| 7           | NPC Ann  | Judge    | Reporter |          | successful          |
| 7           | NPC Cal  | Reporter | NPC Fae  |          | successful          |
| 7           | NPC Dan  | Silencer | NPC Gia  |          | successful          |
| 7           | NPC Ed   | Demagog  | Trader   |          | voting in progress  |
| 7           | NPC Fae  | Spy      |          |          | successful          |
| 7           | NPC Gia  | Psychic  |          |          | successful          |
| 7           | NPC Han  | Medic    | NPC Cal  |          | successful          |
| 7           | NPC Jeff | Trader   | NPC Gia  | NPC Dan  | successful          |

#### States Round 7
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Ed   | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Dan  | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Fae  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Bob  | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Han  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Ann  | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Igi  | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Jeff | Trader    | False      | False     | False      | 4         | True   | 0              | 0                  |
| 7           | NPC Cal  | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Gia  | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player   | Role      | message   | details                                                       |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------ |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann        |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff      |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan       |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Ann  | Judge     | broadcast | I (NPC Gia) am the Psychic and the Medic is not possessed     |
| 7           | NPC Ann  | Judge     | vote      | Demagog has initiated a vote on eliminating Trader            |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann        |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff      |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan       |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Bob  | Inspector | broadcast | I (NPC Gia) am the Psychic and the Medic is not possessed     |
| 7           | NPC Bob  | Inspector | vote      | Demagog has initiated a vote on eliminating Trader            |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann        |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff      |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan       |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Cal  | Reporter  | broadcast | I (NPC Gia) am the Psychic and the Medic is not possessed     |
| 7           | NPC Cal  | Reporter  | reveal    | NPC Fae is Spy                                                |
| 7           | NPC Cal  | Reporter  | vote      | Demagog has initiated a vote on eliminating Trader            |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann        |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff      |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan       |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Dan  | Psychic   | broadcast | I (NPC Gia) am the Psychic and the Medic is not possessed     |
| 7           | NPC Dan  | Psychic   | vote      | Demagog has initiated a vote on eliminating Trader            |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann        |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff      |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan       |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Ed   | Demagog   | broadcast | I (NPC Gia) am the Psychic and the Medic is not possessed     |
| 7           | NPC Ed   | Demagog   | vote      | Demagog has initiated a vote on eliminating Trader            |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann        |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff      |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan       |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Fae  | Spy       | broadcast | I (NPC Gia) am the Psychic and the Medic is not possessed     |
| 7           | NPC Fae  | Spy       | reveal    | NPC Ed is targeting NPC Ann                                   |
| 7           | NPC Fae  | Spy       | reveal    | NPC Dan is targeting NPC Gia                                  |
| 7           | NPC Fae  | Spy       | reveal    | NPC Bob is targeting NPC Ann                                  |
| 7           | NPC Fae  | Spy       | reveal    | NPC Han is targeting NPC Jeff                                 |
| 7           | NPC Fae  | Spy       | reveal    | NPC Ann is targeting NPC Cal                                  |
| 7           | NPC Fae  | Spy       | reveal    | NPC Igi is targeting NPC Jeff                                 |
| 7           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Igi                                 |
| 7           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Igi                                 |
| 7           | NPC Fae  | Spy       | reveal    | NPC Cal is targeting NPC Fae                                  |
| 7           | NPC Fae  | Spy       | vote      | Demagog has initiated a vote on eliminating Trader            |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann        |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff      |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan       |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Gia  | Silencer  | broadcast | I (NPC Gia) am the Psychic and the Medic is not possessed     |
| 7           | NPC Gia  | Silencer  | silenced  | You have been silenced                                        |
| 7           | NPC Gia  | Silencer  | reveal    | Player: NPC Cal is not possessed                              |
| 7           | NPC Gia  | Silencer  | reveal    | Player: NPC Bob is not possessed                              |
| 7           | NPC Gia  | Silencer  | reveal    | Player: NPC Fae is not possessed                              |
| 7           | NPC Gia  | Silencer  | reveal    | Player: NPC Jeff is not possessed                             |
| 7           | NPC Gia  | Silencer  | vote      | Demagog has initiated a vote on eliminating Trader            |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann        |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff      |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan       |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Han  | Medic     | broadcast | I (NPC Gia) am the Psychic and the Medic is not possessed     |
| 7           | NPC Han  | Medic     | vote      | Demagog has initiated a vote on eliminating Trader            |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann        |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff      |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan       |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Igi  | Assassin  | broadcast | I (NPC Gia) am the Psychic and the Medic is not possessed     |
| 7           | NPC Igi  | Assassin  | vote      | Demagog has initiated a vote on eliminating Trader            |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Ann        |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal       |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff      |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia       |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Igi      |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Dan       |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Jeff | Trader    | broadcast | I (NPC Gia) am the Psychic and the Medic is not possessed     |
| 7           | NPC Jeff | Trader    | vote      | Demagog has initiated a vote on eliminating Trader            |

#### Actions Round 8
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 8           | NPC Ann | Judge     | Medic    |          | successful  |
| 8           | NPC Bob | Inspector | NPC Fae  |          | successful  |
| 8           | NPC Cal | Reporter  | NPC Ann  |          | successful  |
| 8           | NPC Dan | Psychic   |          |          | successful  |
| 8           | NPC Fae | Spy       |          |          | successful  |
| 8           | NPC Gia | Silencer  | NPC Igi  |          | successful  |
| 8           | NPC Han | Medic     | NPC Gia  |          | successful  |
| 8           | NPC Igi | Assassin  | Demagog  |          | successful  |

#### States Round 8
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Ed   | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Dan  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Fae  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Bob  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 8           | NPC Han  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Ann  | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Igi  | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 8           | NPC Jeff | Trader    | False      | False     | False      | 3         | True   | 0              | 0                  |
| 8           | NPC Cal  | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 8           | NPC Gia  | Silencer  | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player   | Role      | message   | details                                                       |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------ |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed      |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Dan) am the Psychic and the Spy is not possessed       |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Dan) am the Psychic and the Silencer is not possessed  |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff       |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Cal       |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal       |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Fae       |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed      |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Dan) am the Psychic and the Spy is not possessed       |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Dan) am the Psychic and the Silencer is not possessed  |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff       |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Cal       |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal       |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Fae       |
| 8           | NPC Bob  | Inspector | reveal    | Spy is Innocent                                               |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed      |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Dan) am the Psychic and the Spy is not possessed       |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Dan) am the Psychic and the Silencer is not possessed  |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff       |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Cal       |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal       |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Fae       |
| 8           | NPC Cal  | Reporter  | reveal    | NPC Ann is Judge                                              |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed      |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Dan) am the Psychic and the Spy is not possessed       |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Dan) am the Psychic and the Silencer is not possessed  |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff       |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Cal       |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal       |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Fae       |
| 8           | NPC Dan  | Psychic   | reveal    | Player: NPC Ed is not possessed                               |
| 8           | NPC Dan  | Psychic   | reveal    | Player: NPC Gia is not possessed                              |
| 8           | NPC Dan  | Psychic   | reveal    | Player: NPC Fae is not possessed                              |
| 8           | NPC Dan  | Psychic   | reveal    | Player: NPC Igi is not possessed                              |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed      |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Dan) am the Psychic and the Spy is not possessed       |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Dan) am the Psychic and the Silencer is not possessed  |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff       |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Cal       |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal       |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Fae       |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed      |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Dan) am the Psychic and the Spy is not possessed       |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Dan) am the Psychic and the Silencer is not possessed  |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff       |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Cal       |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal       |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Fae       |
| 8           | NPC Fae  | Spy       | reveal    | NPC Ed is targeting NPC Jeff                                  |
| 8           | NPC Fae  | Spy       | reveal    | NPC Bob is targeting NPC Fae                                  |
| 8           | NPC Fae  | Spy       | reveal    | NPC Han is targeting NPC Cal                                  |
| 8           | NPC Fae  | Spy       | reveal    | NPC Ann is targeting NPC Han                                  |
| 8           | NPC Fae  | Spy       | reveal    | NPC Igi is targeting NPC Jeff                                 |
| 8           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Gia                                 |
| 8           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Gia                                 |
| 8           | NPC Fae  | Spy       | reveal    | NPC Cal is targeting NPC Ann                                  |
| 8           | NPC Fae  | Spy       | reveal    | NPC Gia is targeting NPC Igi                                  |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed      |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Dan) am the Psychic and the Spy is not possessed       |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Dan) am the Psychic and the Silencer is not possessed  |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff       |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Cal       |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal       |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Fae       |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed      |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Dan) am the Psychic and the Spy is not possessed       |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Dan) am the Psychic and the Silencer is not possessed  |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff       |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Cal       |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal       |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Fae       |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed      |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Dan) am the Psychic and the Spy is not possessed       |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Dan) am the Psychic and the Silencer is not possessed  |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff       |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Cal       |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal       |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Fae       |
| 8           | NPC Igi  | Assassin  | silenced  | You have been silenced                                        |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Bob) inspected NPC Fae and they are not possessed      |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Dan) am the Psychic and the Spy is not possessed       |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Dan) am the Psychic and the Silencer is not possessed  |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff       |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann       |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Cal       |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal       |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Jeff      |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia      |
| 8           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Fae       |

#### Actions Round 9
| round_index | Player  | action   | Target 1  | Target 2 | status              |
| :-----------| :-------| :--------| :---------| :--------| :------------------ |
| 9           | NPC Ann | Judge    | Inspector |          | successful          |
| 9           | NPC Dan | Psychic  |           |          | successful          |
| 9           | NPC Ed  | Demagog  | Trader    |          | voting in progress  |
| 9           | NPC Fae | Spy      |           |          | successful          |
| 9           | NPC Gia | Silencer | NPC Cal   |          | successful          |
| 9           | NPC Han | Medic    | NPC Ed    |          | successful          |

#### States Round 9
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 9           | NPC Ed   | Demagog   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Dan  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 9           | NPC Fae  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Bob  | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 9           | NPC Han  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Ann  | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Igi  | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 9           | NPC Jeff | Trader    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 9           | NPC Cal  | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 9           | NPC Gia  | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 9
| round_index | Player   | Role      | message   | details                                                        |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------- |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff        |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae        |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Gia        |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Han        |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Ed         |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ann        |
| 9           | NPC Ann  | Judge     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Igi        |
| 9           | NPC Ann  | Judge     | vote      | Demagog has initiated a vote on eliminating Trader             |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff        |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae        |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Gia        |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Han        |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Ed         |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ann        |
| 9           | NPC Bob  | Inspector | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Igi        |
| 9           | NPC Bob  | Inspector | vote      | Demagog has initiated a vote on eliminating Trader             |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff        |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae        |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Gia        |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Han        |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Ed         |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ann        |
| 9           | NPC Cal  | Reporter  | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Igi        |
| 9           | NPC Cal  | Reporter  | silenced  | You have been silenced                                         |
| 9           | NPC Cal  | Reporter  | vote      | Demagog has initiated a vote on eliminating Trader             |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff        |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae        |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Gia        |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Han        |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Ed         |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ann        |
| 9           | NPC Dan  | Psychic   | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Igi        |
| 9           | NPC Dan  | Psychic   | reveal    | Player: NPC Igi is not possessed                               |
| 9           | NPC Dan  | Psychic   | reveal    | Player: NPC Fae is not possessed                               |
| 9           | NPC Dan  | Psychic   | reveal    | Player: NPC Bob is not possessed                               |
| 9           | NPC Dan  | Psychic   | reveal    | Player: NPC Cal is not possessed                               |
| 9           | NPC Dan  | Psychic   | vote      | Demagog has initiated a vote on eliminating Trader             |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff        |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae        |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Gia        |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Han        |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Ed         |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ann        |
| 9           | NPC Ed   | Demagog   | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Igi        |
| 9           | NPC Ed   | Demagog   | vote      | Demagog has initiated a vote on eliminating Trader             |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff        |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae        |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Gia        |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Han        |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Ed         |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ann        |
| 9           | NPC Fae  | Spy       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Igi        |
| 9           | NPC Fae  | Spy       | reveal    | NPC Ed is targeting NPC Jeff                                   |
| 9           | NPC Fae  | Spy       | reveal    | NPC Bob is targeting NPC Fae                                   |
| 9           | NPC Fae  | Spy       | reveal    | NPC Han is targeting NPC Gia                                   |
| 9           | NPC Fae  | Spy       | reveal    | NPC Ann is targeting NPC Bob                                   |
| 9           | NPC Fae  | Spy       | reveal    | NPC Igi is targeting NPC Ed                                    |
| 9           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Gia                                  |
| 9           | NPC Fae  | Spy       | reveal    | NPC Jeff is targeting NPC Gia                                  |
| 9           | NPC Fae  | Spy       | reveal    | NPC Cal is targeting NPC Ann                                   |
| 9           | NPC Fae  | Spy       | reveal    | NPC Gia is targeting NPC Cal                                   |
| 9           | NPC Fae  | Spy       | vote      | Demagog has initiated a vote on eliminating Trader             |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff        |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae        |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Gia        |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Han        |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Ed         |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ann        |
| 9           | NPC Gia  | Silencer  | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Igi        |
| 9           | NPC Gia  | Silencer  | vote      | Demagog has initiated a vote on eliminating Trader             |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff        |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae        |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Gia        |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Han        |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Ed         |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ann        |
| 9           | NPC Han  | Medic     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Igi        |
| 9           | NPC Han  | Medic     | vote      | Demagog has initiated a vote on eliminating Trader             |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff        |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae        |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Gia        |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Han        |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Ed         |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ann        |
| 9           | NPC Igi  | Assassin  | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Igi        |
| 9           | NPC Igi  | Assassin  | vote      | Demagog has initiated a vote on eliminating Trader             |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff        |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Fae        |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Gia        |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Han        |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Ed         |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Jeff is targeting NPC Gia       |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Cal is targeting NPC Ann        |
| 9           | NPC Jeff | Trader    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Igi        |
| 9           | NPC Jeff | Trader    | vote      | Demagog has initiated a vote on eliminating Trader             |