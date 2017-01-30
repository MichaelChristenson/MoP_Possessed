#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 56   | 10      | 5       |

#### Roles
| Role         |
| :----------- |
| Spy          |
| Trader       |
| Judge        |
| Executioner  |
| Psychic      |
| Inspector    |
| Jailer       |
| Thief        |
| Reporter     |
| Silencer     |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Inspector   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Ann  | Inspector   | possessed   | You are Possessed         |
| 0           | NPC Bob  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Bob  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Cal  | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Cal  | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Trader      | role change | Your Role is Trader       |
| 0           | NPC Dan  | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Spy         | role change | Your Role is Spy          |
| 0           | NPC Ed   | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Fae  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Gia  | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Han  | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Igi  | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Thief       | role change | Your Role is Thief        |
| 0           | NPC Jeff | Thief       | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player   | action   | Target 1 | Target 2 | status                         |
| :-----------| :--------| :--------| :--------| :--------| :----------------------------- |
| 1           | NPC Cal  | Reporter | NPC Gia  |          | successful                     |
| 1           | NPC Dan  | Trader   | NPC Ed   | NPC Cal  | failed because not vulnerable  |
| 1           | NPC Ed   | Spy      |          |          | successful                     |
| 1           | NPC Fae  | Judge    | Jailer   |          | successful                     |
| 1           | NPC Gia  | Silencer | NPC Bob  |          | successful                     |
| 1           | NPC Han  | Psychic  |          |          | successful                     |
| 1           | NPC Jeff | Thief    | NPC Dan  |          | successful                     |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Trader      | False      | False     | True       | 4         | True   | 0              | 0                  |
| 1           | NPC Fae  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ann  | Inspector   | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Jeff | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Gia  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 1           | NPC Ann  | Inspector   | broadcast | I (NPC Ann) inspected NPC Gia and they are posssessed            |
| 1           | NPC Ann  | Inspector   | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Silencer          |
| 1           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed        |
| 1           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Ann  | Inspector   | broadcast | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Bob  | Executioner | broadcast | I (NPC Ann) inspected NPC Gia and they are posssessed            |
| 1           | NPC Bob  | Executioner | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Silencer          |
| 1           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed        |
| 1           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Bob  | Executioner | broadcast | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Bob  | Executioner | silenced  | You have been silenced                                           |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Ann) inspected NPC Gia and they are posssessed            |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Silencer          |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed        |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Cal  | Reporter    | reveal    | NPC Gia is Silencer                                              |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Ann) inspected NPC Gia and they are posssessed            |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Silencer          |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed        |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Ann) inspected NPC Gia and they are posssessed            |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Silencer          |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed        |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Ed   | Spy         | broadcast | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Igi                                     |
| 1           | NPC Ed   | Spy         | reveal    | NPC Jeff is targeting NPC Dan                                    |
| 1           | NPC Ed   | Spy         | reveal    | NPC Cal is targeting NPC Gia                                     |
| 1           | NPC Ed   | Spy         | reveal    | NPC Gia is targeting NPC Bob                                     |
| 1           | NPC Fae  | Judge       | broadcast | I (NPC Ann) inspected NPC Gia and they are posssessed            |
| 1           | NPC Fae  | Judge       | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Silencer          |
| 1           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed        |
| 1           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Fae  | Judge       | broadcast | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Gia  | Silencer    | broadcast | I (NPC Ann) inspected NPC Gia and they are posssessed            |
| 1           | NPC Gia  | Silencer    | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Silencer          |
| 1           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed        |
| 1           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Gia  | Silencer    | broadcast | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Ann) inspected NPC Gia and they are posssessed            |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Silencer          |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed        |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Han  | Psychic     | reveal    | Player: NPC Cal is not possessed                                 |
| 1           | NPC Han  | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 1           | NPC Han  | Psychic     | reveal    | Player: NPC Igi is not possessed                                 |
| 1           | NPC Han  | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Ann) inspected NPC Gia and they are posssessed            |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Silencer          |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed        |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Igi  | Jailer      | broadcast | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Ann) inspected NPC Gia and they are posssessed            |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Silencer          |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed        |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |

#### Actions Round 2
| round_index | Player  | action   | Target 1  | Target 2 | status      |
| :-----------| :-------| :--------| :---------| :--------| :---------- |
| 2           | NPC Ed  | Spy      |           |          | successful  |
| 2           | NPC Fae | Judge    | Inspector |          | successful  |
| 2           | NPC Gia | Silencer | NPC Ed    |          | successful  |
| 2           | NPC Han | Psychic  |           |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Trader      | False      | False     | True       | 3         | True   | 0              | 0                  |
| 2           | NPC Fae  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann  | Inspector   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Jeff | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 2           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi        |
| 2           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 2           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob        |
| 2           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 2           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 2           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi        |
| 2           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 2           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob        |
| 2           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 2           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 2           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi        |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob        |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi        |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob        |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi        |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob        |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ed   | Spy         | silenced  | You have been silenced                                        |
| 2           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Ed                                   |
| 2           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Ed                                   |
| 2           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Ann                                  |
| 2           | NPC Ed   | Spy         | reveal    | NPC Jeff is targeting NPC Dan                                 |
| 2           | NPC Ed   | Spy         | reveal    | NPC Cal is targeting NPC Gia                                  |
| 2           | NPC Ed   | Spy         | reveal    | NPC Gia is targeting NPC Ed                                   |
| 2           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi        |
| 2           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 2           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob        |
| 2           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 2           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 2           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 2           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi        |
| 2           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 2           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob        |
| 2           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 2           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 2           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi        |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob        |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 2           | NPC Han  | Psychic     | reveal    | Player: NPC Jeff is not possessed                             |
| 2           | NPC Han  | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 2           | NPC Han  | Psychic     | reveal    | Player: NPC Gia is not possessed                              |
| 2           | NPC Han  | Psychic     | reveal    | Player: NPC Ed is not possessed                               |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi        |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob        |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed         |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi        |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan       |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob        |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |

#### Actions Round 3
| round_index | Player   | action   | Target 1  | Target 2 | status      |
| :-----------| :--------| :--------| :---------| :--------| :---------- |
| 3           | NPC Cal  | Reporter | NPC Jeff  |          | successful  |
| 3           | NPC Ed   | Spy      |           |          | successful  |
| 3           | NPC Fae  | Judge    | Inspector |          | successful  |
| 3           | NPC Gia  | Silencer | NPC Han   |          | successful  |
| 3           | NPC Han  | Psychic  |           |          | successful  |
| 3           | NPC Jeff | Thief    | NPC Han   |          | successful  |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan  | Trader      | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Fae  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Han  | Psychic     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 3           | NPC Ann  | Inspector   | False      | True      | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Jeff | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Cal  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Gia  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 3           | NPC Ann  | Inspector   | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed         |
| 3           | NPC Ann  | Inspector   | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Thief         |
| 3           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 3           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed     |
| 3           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 3           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 3           | NPC Ann  | Inspector   | broadcast | I (NPC Jeff) am the Thief and I have made NPC Han vulnerable  |
| 3           | NPC Bob  | Executioner | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed         |
| 3           | NPC Bob  | Executioner | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Thief         |
| 3           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 3           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed     |
| 3           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 3           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 3           | NPC Bob  | Executioner | broadcast | I (NPC Jeff) am the Thief and I have made NPC Han vulnerable  |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed         |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Thief         |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed     |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Jeff) am the Thief and I have made NPC Han vulnerable  |
| 3           | NPC Cal  | Reporter    | reveal    | NPC Jeff is Thief                                             |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed         |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Thief         |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed     |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Jeff) am the Thief and I have made NPC Han vulnerable  |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed         |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Thief         |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed     |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 3           | NPC Ed   | Spy         | broadcast | I (NPC Jeff) am the Thief and I have made NPC Han vulnerable  |
| 3           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Ed                                   |
| 3           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Ed                                   |
| 3           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Ann                                  |
| 3           | NPC Ed   | Spy         | reveal    | NPC Jeff is targeting NPC Han                                 |
| 3           | NPC Ed   | Spy         | reveal    | NPC Cal is targeting NPC Jeff                                 |
| 3           | NPC Ed   | Spy         | reveal    | NPC Gia is targeting NPC Han                                  |
| 3           | NPC Fae  | Judge       | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed         |
| 3           | NPC Fae  | Judge       | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Thief         |
| 3           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 3           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed     |
| 3           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 3           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 3           | NPC Fae  | Judge       | broadcast | I (NPC Jeff) am the Thief and I have made NPC Han vulnerable  |
| 3           | NPC Gia  | Silencer    | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed         |
| 3           | NPC Gia  | Silencer    | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Thief         |
| 3           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 3           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed     |
| 3           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 3           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 3           | NPC Gia  | Silencer    | broadcast | I (NPC Jeff) am the Thief and I have made NPC Han vulnerable  |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed         |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Thief         |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed     |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Jeff) am the Thief and I have made NPC Han vulnerable  |
| 3           | NPC Han  | Psychic     | silenced  | You have been silenced                                        |
| 3           | NPC Han  | Psychic     | reveal    | Player: NPC Jeff is not possessed                             |
| 3           | NPC Han  | Psychic     | reveal    | Player: NPC Cal is not possessed                              |
| 3           | NPC Han  | Psychic     | reveal    | Player: NPC Gia is not possessed                              |
| 3           | NPC Han  | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed         |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Thief         |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed     |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 3           | NPC Igi  | Jailer      | broadcast | I (NPC Jeff) am the Thief and I have made NPC Han vulnerable  |
| 3           | NPC Jeff | Thief       | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed         |
| 3           | NPC Jeff | Thief       | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Thief         |
| 3           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 3           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Thief is not possessed     |
| 3           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 3           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 3           | NPC Jeff | Thief       | broadcast | I (NPC Jeff) am the Thief and I have made NPC Han vulnerable  |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 4           | NPC Ed  | Spy      |          |          | successful  |
| 4           | NPC Fae | Judge    | Jailer   |          | successful  |
| 4           | NPC Gia | Silencer | NPC Bob  |          | successful  |
| 4           | NPC Han | Psychic  |          |          | successful  |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan  | Trader      | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Fae  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Han  | Psychic     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Ann  | Inspector   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Jeff | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Cal  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Gia  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                  |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------- |
| 4           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann   |
| 4           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han  |
| 4           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff  |
| 4           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han   |
| 4           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann   |
| 4           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han  |
| 4           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff  |
| 4           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han   |
| 4           | NPC Bob  | Executioner | silenced  | You have been silenced                                   |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann   |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han  |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff  |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han   |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann   |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han  |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff  |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han   |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann   |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han  |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff  |
| 4           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han   |
| 4           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Ed                              |
| 4           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Ed                              |
| 4           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Igi                             |
| 4           | NPC Ed   | Spy         | reveal    | NPC Jeff is targeting NPC Han                            |
| 4           | NPC Ed   | Spy         | reveal    | NPC Cal is targeting NPC Jeff                            |
| 4           | NPC Ed   | Spy         | reveal    | NPC Gia is targeting NPC Bob                             |
| 4           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann   |
| 4           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han  |
| 4           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff  |
| 4           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han   |
| 4           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann   |
| 4           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han  |
| 4           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff  |
| 4           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han   |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann   |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han  |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff  |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han   |
| 4           | NPC Han  | Psychic     | reveal    | Player: NPC Igi is not possessed                         |
| 4           | NPC Han  | Psychic     | reveal    | Player: NPC Fae is not possessed                         |
| 4           | NPC Han  | Psychic     | reveal    | Player: NPC Ed is not possessed                          |
| 4           | NPC Han  | Psychic     | reveal    | Player: NPC Bob is not possessed                         |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann   |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han  |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff  |
| 4           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han   |
| 4           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed    |
| 4           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Ann   |
| 4           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han  |
| 4           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff  |
| 4           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Han   |

#### Actions Round 5
| round_index | Player   | action   | Target 1 | Target 2 | status                         |
| :-----------| :--------| :--------| :--------| :--------| :----------------------------- |
| 5           | NPC Cal  | Reporter | NPC Ed   |          | successful                     |
| 5           | NPC Dan  | Trader   | NPC Ann  | NPC Ed   | failed because not vulnerable  |
| 5           | NPC Ed   | Spy      |          |          | successful                     |
| 5           | NPC Fae  | Judge    | Spy      |          | successful                     |
| 5           | NPC Gia  | Silencer | NPC Dan  |          | successful                     |
| 5           | NPC Han  | Psychic  |          |          | successful                     |
| 5           | NPC Jeff | Thief    | NPC Ann  |          | successful                     |

#### States Round 5
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan  | Trader      | False      | False     | True       | 4         | True   | 0              | 0                  |
| 5           | NPC Fae  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Han  | Psychic     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 5           | NPC Ann  | Inspector   | False      | True      | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Igi  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Jeff | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Cal  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Gia  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 5           | NPC Ann  | Inspector   | broadcast | I (NPC Ann) inspected NPC Ed and they are posssessed             |
| 5           | NPC Ann  | Inspector   | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Spy                |
| 5           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi           |
| 5           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han          |
| 5           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff          |
| 5           | NPC Ann  | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob           |
| 5           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 5           | NPC Ann  | Inspector   | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Ann  | Inspector   | broadcast | I (NPC Jeff) am the Thief and I have made NPC Ann vulnerable     |
| 5           | NPC Bob  | Executioner | broadcast | I (NPC Ann) inspected NPC Ed and they are posssessed             |
| 5           | NPC Bob  | Executioner | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Spy                |
| 5           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi           |
| 5           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han          |
| 5           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff          |
| 5           | NPC Bob  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob           |
| 5           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 5           | NPC Bob  | Executioner | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Bob  | Executioner | broadcast | I (NPC Jeff) am the Thief and I have made NPC Ann vulnerable     |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Ann) inspected NPC Ed and they are posssessed             |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Spy                |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi           |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han          |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff          |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob           |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Jeff) am the Thief and I have made NPC Ann vulnerable     |
| 5           | NPC Cal  | Reporter    | reveal    | NPC Ed is Spy                                                    |
| 5           | NPC Dan  | Trader      | broadcast | I (NPC Ann) inspected NPC Ed and they are posssessed             |
| 5           | NPC Dan  | Trader      | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Spy                |
| 5           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi           |
| 5           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han          |
| 5           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff          |
| 5           | NPC Dan  | Trader      | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob           |
| 5           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 5           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Dan  | Trader      | broadcast | I (NPC Jeff) am the Thief and I have made NPC Ann vulnerable     |
| 5           | NPC Dan  | Trader      | silenced  | You have been silenced                                           |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ann) inspected NPC Ed and they are posssessed             |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Spy                |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi           |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han          |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff          |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob           |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Ed   | Spy         | broadcast | I (NPC Jeff) am the Thief and I have made NPC Ann vulnerable     |
| 5           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Ed                                      |
| 5           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Ed                                      |
| 5           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Ed                                      |
| 5           | NPC Ed   | Spy         | reveal    | NPC Jeff is targeting NPC Ann                                    |
| 5           | NPC Ed   | Spy         | reveal    | NPC Cal is targeting NPC Ed                                      |
| 5           | NPC Ed   | Spy         | reveal    | NPC Gia is targeting NPC Dan                                     |
| 5           | NPC Fae  | Judge       | broadcast | I (NPC Ann) inspected NPC Ed and they are posssessed             |
| 5           | NPC Fae  | Judge       | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Spy                |
| 5           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi           |
| 5           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han          |
| 5           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff          |
| 5           | NPC Fae  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob           |
| 5           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 5           | NPC Fae  | Judge       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Fae  | Judge       | broadcast | I (NPC Jeff) am the Thief and I have made NPC Ann vulnerable     |
| 5           | NPC Gia  | Silencer    | broadcast | I (NPC Ann) inspected NPC Ed and they are posssessed             |
| 5           | NPC Gia  | Silencer    | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Spy                |
| 5           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi           |
| 5           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han          |
| 5           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff          |
| 5           | NPC Gia  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob           |
| 5           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 5           | NPC Gia  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Gia  | Silencer    | broadcast | I (NPC Jeff) am the Thief and I have made NPC Ann vulnerable     |
| 5           | NPC Han  | Psychic     | broadcast | I (NPC Ann) inspected NPC Ed and they are posssessed             |
| 5           | NPC Han  | Psychic     | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Spy                |
| 5           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi           |
| 5           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han          |
| 5           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff          |
| 5           | NPC Han  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob           |
| 5           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 5           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Han  | Psychic     | broadcast | I (NPC Jeff) am the Thief and I have made NPC Ann vulnerable     |
| 5           | NPC Han  | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 5           | NPC Han  | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 5           | NPC Han  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 5           | NPC Han  | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 5           | NPC Igi  | Jailer      | broadcast | I (NPC Ann) inspected NPC Ed and they are posssessed             |
| 5           | NPC Igi  | Jailer      | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Spy                |
| 5           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi           |
| 5           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han          |
| 5           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff          |
| 5           | NPC Igi  | Jailer      | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob           |
| 5           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 5           | NPC Igi  | Jailer      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Igi  | Jailer      | broadcast | I (NPC Jeff) am the Thief and I have made NPC Ann vulnerable     |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Ann) inspected NPC Ed and they are posssessed             |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Spy                |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Ed            |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Igi           |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Han          |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Jeff          |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Bob           |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Jeff) am the Thief and I have made NPC Ann vulnerable     |