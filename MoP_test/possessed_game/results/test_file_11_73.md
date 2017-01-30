#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 73   | 11      | 2       |

#### Roles
| Role         |
| :----------- |
| Priest       |
| Judge        |
| Silencer     |
| Spy          |
| Executioner  |
| Medic        |
| Prophet      |
| Demagog      |
| Psychic      |
| Reporter     |
| Inspector    |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Executioner | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ann  | Executioner | possessed   | You are Possessed         |
| 0           | NPC Bob  | Priest      | role change | Your Role is Priest       |
| 0           | NPC Bob  | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Cal  | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Cal  | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Dan  | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Spy         | role change | Your Role is Spy          |
| 0           | NPC Ed   | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Fae  | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Gia  | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Han  | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Igi  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Jeff | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Ken  | Psychic     | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player   | action      | Target 1  | Target 2 | status                        |
| :-----------| :--------| :-----------| :---------| :--------| :---------------------------- |
| 1           | NPC Ann  | Executioner | NPC Bob   |          | failed because of no support  |
| 1           | NPC Cal  | Demagog     | Reporter  |          | voting in progress            |
| 1           | NPC Dan  | Prophet     | NPC Cal   |          | successful                    |
| 1           | NPC Ed   | Spy         |           |          | successful                    |
| 1           | NPC Fae  | Reporter    | NPC Bob   |          | successful                    |
| 1           | NPC Gia  | Medic       | NPC Igi   |          | successful                    |
| 1           | NPC Han  | Silencer    | NPC Jeff  |          | successful                    |
| 1           | NPC Igi  | Judge       | Inspector |          | successful                    |
| 1           | NPC Jeff | Inspector   | NPC Dan   |          | successful                    |
| 1           | NPC Ken  | Psychic     |           |          | successful                    |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann  | Executioner | False      | True      | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Gia  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ken  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Fae  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Jeff | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message       | details                                                       |
| :-----------| :--------| :-----------| :-------------| :------------------------------------------------------------ |
| 1           | NPC Ann  | Executioner | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Priest         |
| 1           | NPC Ann  | Executioner | broadcast     | I (NPC Jeff) inspected NPC Dan and they are not possessed     |
| 1           | NPC Ann  | Executioner | broadcast     | I (NPC Ken) am the Psychic and the Judge is not possessed     |
| 1           | NPC Ann  | Executioner | broadcast     | I (NPC Ken) am the Psychic and the Priest is not possessed    |
| 1           | NPC Ann  | Executioner | broadcast     | I (NPC Ken) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Ann  | Executioner | broadcast     | I (NPC Ken) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Ann  | Executioner | broadcast     | I (NPC Ken) am the Psychic and the Spy is not possessed       |
| 1           | NPC Ann  | Executioner | action failed |                                                               |
| 1           | NPC Ann  | Executioner | vote          | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Bob  | Priest      | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Priest         |
| 1           | NPC Bob  | Priest      | broadcast     | I (NPC Jeff) inspected NPC Dan and they are not possessed     |
| 1           | NPC Bob  | Priest      | broadcast     | I (NPC Ken) am the Psychic and the Judge is not possessed     |
| 1           | NPC Bob  | Priest      | broadcast     | I (NPC Ken) am the Psychic and the Priest is not possessed    |
| 1           | NPC Bob  | Priest      | broadcast     | I (NPC Ken) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Bob  | Priest      | broadcast     | I (NPC Ken) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Bob  | Priest      | broadcast     | I (NPC Ken) am the Psychic and the Spy is not possessed       |
| 1           | NPC Bob  | Priest      | vote          | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Cal  | Demagog     | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Priest         |
| 1           | NPC Cal  | Demagog     | broadcast     | I (NPC Jeff) inspected NPC Dan and they are not possessed     |
| 1           | NPC Cal  | Demagog     | broadcast     | I (NPC Ken) am the Psychic and the Judge is not possessed     |
| 1           | NPC Cal  | Demagog     | broadcast     | I (NPC Ken) am the Psychic and the Priest is not possessed    |
| 1           | NPC Cal  | Demagog     | broadcast     | I (NPC Ken) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Cal  | Demagog     | broadcast     | I (NPC Ken) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Cal  | Demagog     | broadcast     | I (NPC Ken) am the Psychic and the Spy is not possessed       |
| 1           | NPC Cal  | Demagog     | vote          | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Dan  | Prophet     | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Priest         |
| 1           | NPC Dan  | Prophet     | broadcast     | I (NPC Jeff) inspected NPC Dan and they are not possessed     |
| 1           | NPC Dan  | Prophet     | broadcast     | I (NPC Ken) am the Psychic and the Judge is not possessed     |
| 1           | NPC Dan  | Prophet     | broadcast     | I (NPC Ken) am the Psychic and the Priest is not possessed    |
| 1           | NPC Dan  | Prophet     | broadcast     | I (NPC Ken) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Dan  | Prophet     | broadcast     | I (NPC Ken) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Dan  | Prophet     | broadcast     | I (NPC Ken) am the Psychic and the Spy is not possessed       |
| 1           | NPC Dan  | Prophet     | vote          | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Ed   | Spy         | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Priest         |
| 1           | NPC Ed   | Spy         | broadcast     | I (NPC Jeff) inspected NPC Dan and they are not possessed     |
| 1           | NPC Ed   | Spy         | broadcast     | I (NPC Ken) am the Psychic and the Judge is not possessed     |
| 1           | NPC Ed   | Spy         | broadcast     | I (NPC Ken) am the Psychic and the Priest is not possessed    |
| 1           | NPC Ed   | Spy         | broadcast     | I (NPC Ken) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Ed   | Spy         | broadcast     | I (NPC Ken) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Ed   | Spy         | broadcast     | I (NPC Ken) am the Psychic and the Spy is not possessed       |
| 1           | NPC Ed   | Spy         | reveal        | NPC Igi is targeting NPC Jeff                                 |
| 1           | NPC Ed   | Spy         | reveal        | NPC Han is targeting NPC Jeff                                 |
| 1           | NPC Ed   | Spy         | reveal        | NPC Ann is targeting NPC Bob                                  |
| 1           | NPC Ed   | Spy         | reveal        | NPC Fae is targeting NPC Bob                                  |
| 1           | NPC Ed   | Spy         | reveal        | NPC Jeff is targeting NPC Dan                                 |
| 1           | NPC Ed   | Spy         | vote          | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Fae  | Reporter    | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Priest         |
| 1           | NPC Fae  | Reporter    | broadcast     | I (NPC Jeff) inspected NPC Dan and they are not possessed     |
| 1           | NPC Fae  | Reporter    | broadcast     | I (NPC Ken) am the Psychic and the Judge is not possessed     |
| 1           | NPC Fae  | Reporter    | broadcast     | I (NPC Ken) am the Psychic and the Priest is not possessed    |
| 1           | NPC Fae  | Reporter    | broadcast     | I (NPC Ken) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Fae  | Reporter    | broadcast     | I (NPC Ken) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Fae  | Reporter    | broadcast     | I (NPC Ken) am the Psychic and the Spy is not possessed       |
| 1           | NPC Fae  | Reporter    | reveal        | NPC Bob is Priest                                             |
| 1           | NPC Fae  | Reporter    | vote          | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Gia  | Medic       | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Priest         |
| 1           | NPC Gia  | Medic       | broadcast     | I (NPC Jeff) inspected NPC Dan and they are not possessed     |
| 1           | NPC Gia  | Medic       | broadcast     | I (NPC Ken) am the Psychic and the Judge is not possessed     |
| 1           | NPC Gia  | Medic       | broadcast     | I (NPC Ken) am the Psychic and the Priest is not possessed    |
| 1           | NPC Gia  | Medic       | broadcast     | I (NPC Ken) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Gia  | Medic       | broadcast     | I (NPC Ken) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Gia  | Medic       | broadcast     | I (NPC Ken) am the Psychic and the Spy is not possessed       |
| 1           | NPC Gia  | Medic       | vote          | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Han  | Silencer    | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Priest         |
| 1           | NPC Han  | Silencer    | broadcast     | I (NPC Jeff) inspected NPC Dan and they are not possessed     |
| 1           | NPC Han  | Silencer    | broadcast     | I (NPC Ken) am the Psychic and the Judge is not possessed     |
| 1           | NPC Han  | Silencer    | broadcast     | I (NPC Ken) am the Psychic and the Priest is not possessed    |
| 1           | NPC Han  | Silencer    | broadcast     | I (NPC Ken) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Han  | Silencer    | broadcast     | I (NPC Ken) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Han  | Silencer    | broadcast     | I (NPC Ken) am the Psychic and the Spy is not possessed       |
| 1           | NPC Han  | Silencer    | vote          | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Igi  | Judge       | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Priest         |
| 1           | NPC Igi  | Judge       | broadcast     | I (NPC Jeff) inspected NPC Dan and they are not possessed     |
| 1           | NPC Igi  | Judge       | broadcast     | I (NPC Ken) am the Psychic and the Judge is not possessed     |
| 1           | NPC Igi  | Judge       | broadcast     | I (NPC Ken) am the Psychic and the Priest is not possessed    |
| 1           | NPC Igi  | Judge       | broadcast     | I (NPC Ken) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Igi  | Judge       | broadcast     | I (NPC Ken) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Igi  | Judge       | broadcast     | I (NPC Ken) am the Psychic and the Spy is not possessed       |
| 1           | NPC Igi  | Judge       | vote          | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Jeff | Inspector   | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Priest         |
| 1           | NPC Jeff | Inspector   | broadcast     | I (NPC Jeff) inspected NPC Dan and they are not possessed     |
| 1           | NPC Jeff | Inspector   | broadcast     | I (NPC Ken) am the Psychic and the Judge is not possessed     |
| 1           | NPC Jeff | Inspector   | broadcast     | I (NPC Ken) am the Psychic and the Priest is not possessed    |
| 1           | NPC Jeff | Inspector   | broadcast     | I (NPC Ken) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Jeff | Inspector   | broadcast     | I (NPC Ken) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Jeff | Inspector   | broadcast     | I (NPC Ken) am the Psychic and the Spy is not possessed       |
| 1           | NPC Jeff | Inspector   | reveal        | Prophet is Innocent                                           |
| 1           | NPC Jeff | Inspector   | silenced      | You have been silenced                                        |
| 1           | NPC Jeff | Inspector   | vote          | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Ken  | Psychic     | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Priest         |
| 1           | NPC Ken  | Psychic     | broadcast     | I (NPC Jeff) inspected NPC Dan and they are not possessed     |
| 1           | NPC Ken  | Psychic     | broadcast     | I (NPC Ken) am the Psychic and the Judge is not possessed     |
| 1           | NPC Ken  | Psychic     | broadcast     | I (NPC Ken) am the Psychic and the Priest is not possessed    |
| 1           | NPC Ken  | Psychic     | broadcast     | I (NPC Ken) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Ken  | Psychic     | broadcast     | I (NPC Ken) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Ken  | Psychic     | broadcast     | I (NPC Ken) am the Psychic and the Spy is not possessed       |
| 1           | NPC Ken  | Psychic     | reveal        | Player: NPC Ed is not possessed                               |
| 1           | NPC Ken  | Psychic     | reveal        | Player: NPC Gia is not possessed                              |
| 1           | NPC Ken  | Psychic     | reveal        | Player: NPC Jeff is not possessed                             |
| 1           | NPC Ken  | Psychic     | reveal        | Player: NPC Cal is not possessed                              |
| 1           | NPC Ken  | Psychic     | vote          | Demagog has initiated a vote on eliminating Reporter          |

#### Actions Round 2
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 2           | NPC Dan | Prophet  | NPC Ken  |          | successful  |
| 2           | NPC Ed  | Spy      |          |          | successful  |
| 2           | NPC Gia | Medic    | NPC Han  |          | successful  |
| 2           | NPC Han | Silencer | NPC Ed   |          | successful  |
| 2           | NPC Igi | Judge    | Spy      |          | successful  |
| 2           | NPC Ken | Psychic  |          |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed   | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann  | Executioner | False      | True      | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Gia  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ken  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Fae  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Jeff | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Jeff        |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Jeff        |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Bob         |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Igi         |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Fae         |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob         |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan        |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Ken) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Ken) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Ken) am the Psychic and the Spy is not possessed        |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Ken) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Jeff        |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Jeff        |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Bob         |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Igi         |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Fae         |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob         |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan        |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Ken) am the Psychic and the Priest is not possessed     |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Ken) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Ken) am the Psychic and the Spy is not possessed        |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Ken) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Jeff        |
| 2           | NPC Cal  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Jeff        |
| 2           | NPC Cal  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Bob         |
| 2           | NPC Cal  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Igi         |
| 2           | NPC Cal  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Cal  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Fae         |
| 2           | NPC Cal  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob         |
| 2           | NPC Cal  | Demagog     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan        |
| 2           | NPC Cal  | Demagog     | broadcast | I (NPC Ken) am the Psychic and the Priest is not possessed     |
| 2           | NPC Cal  | Demagog     | broadcast | I (NPC Ken) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Cal  | Demagog     | broadcast | I (NPC Ken) am the Psychic and the Spy is not possessed        |
| 2           | NPC Cal  | Demagog     | broadcast | I (NPC Ken) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Dan  | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Jeff        |
| 2           | NPC Dan  | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Jeff        |
| 2           | NPC Dan  | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Bob         |
| 2           | NPC Dan  | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Igi         |
| 2           | NPC Dan  | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Dan  | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Fae         |
| 2           | NPC Dan  | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob         |
| 2           | NPC Dan  | Prophet     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan        |
| 2           | NPC Dan  | Prophet     | broadcast | I (NPC Ken) am the Psychic and the Priest is not possessed     |
| 2           | NPC Dan  | Prophet     | broadcast | I (NPC Ken) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Dan  | Prophet     | broadcast | I (NPC Ken) am the Psychic and the Spy is not possessed        |
| 2           | NPC Dan  | Prophet     | broadcast | I (NPC Ken) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Jeff        |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Jeff        |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Bob         |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Igi         |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Fae         |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob         |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan        |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ken) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ken) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ken) am the Psychic and the Spy is not possessed        |
| 2           | NPC Ed   | Spy         | broadcast | I (NPC Ken) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ed   | Spy         | silenced  | You have been silenced                                         |
| 2           | NPC Ed   | Spy         | reveal    | NPC Igi is targeting NPC Ed                                    |
| 2           | NPC Ed   | Spy         | reveal    | NPC Han is targeting NPC Ed                                    |
| 2           | NPC Ed   | Spy         | reveal    | NPC Ann is targeting NPC Bob                                   |
| 2           | NPC Ed   | Spy         | reveal    | NPC Gia is targeting NPC Igi                                   |
| 2           | NPC Ed   | Spy         | reveal    | NPC Dan is targeting NPC Cal                                   |
| 2           | NPC Ed   | Spy         | reveal    | NPC Cal is targeting NPC Fae                                   |
| 2           | NPC Ed   | Spy         | reveal    | NPC Fae is targeting NPC Bob                                   |
| 2           | NPC Ed   | Spy         | reveal    | NPC Jeff is targeting NPC Dan                                  |
| 2           | NPC Fae  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Jeff        |
| 2           | NPC Fae  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Jeff        |
| 2           | NPC Fae  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Bob         |
| 2           | NPC Fae  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Igi         |
| 2           | NPC Fae  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Fae  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Fae         |
| 2           | NPC Fae  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob         |
| 2           | NPC Fae  | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan        |
| 2           | NPC Fae  | Reporter    | broadcast | I (NPC Ken) am the Psychic and the Priest is not possessed     |
| 2           | NPC Fae  | Reporter    | broadcast | I (NPC Ken) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Fae  | Reporter    | broadcast | I (NPC Ken) am the Psychic and the Spy is not possessed        |
| 2           | NPC Fae  | Reporter    | broadcast | I (NPC Ken) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Gia  | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Jeff        |
| 2           | NPC Gia  | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Jeff        |
| 2           | NPC Gia  | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Bob         |
| 2           | NPC Gia  | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Igi         |
| 2           | NPC Gia  | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Gia  | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Fae         |
| 2           | NPC Gia  | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob         |
| 2           | NPC Gia  | Medic       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan        |
| 2           | NPC Gia  | Medic       | broadcast | I (NPC Ken) am the Psychic and the Priest is not possessed     |
| 2           | NPC Gia  | Medic       | broadcast | I (NPC Ken) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Gia  | Medic       | broadcast | I (NPC Ken) am the Psychic and the Spy is not possessed        |
| 2           | NPC Gia  | Medic       | broadcast | I (NPC Ken) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Han  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Jeff        |
| 2           | NPC Han  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Jeff        |
| 2           | NPC Han  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Bob         |
| 2           | NPC Han  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Igi         |
| 2           | NPC Han  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Han  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Fae         |
| 2           | NPC Han  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob         |
| 2           | NPC Han  | Silencer    | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan        |
| 2           | NPC Han  | Silencer    | broadcast | I (NPC Ken) am the Psychic and the Priest is not possessed     |
| 2           | NPC Han  | Silencer    | broadcast | I (NPC Ken) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Han  | Silencer    | broadcast | I (NPC Ken) am the Psychic and the Spy is not possessed        |
| 2           | NPC Han  | Silencer    | broadcast | I (NPC Ken) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Jeff        |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Jeff        |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Bob         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Igi         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Fae         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan        |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Psychic and the Priest is not possessed     |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Psychic and the Spy is not possessed        |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ken) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Jeff | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Jeff        |
| 2           | NPC Jeff | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Jeff        |
| 2           | NPC Jeff | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Bob         |
| 2           | NPC Jeff | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Igi         |
| 2           | NPC Jeff | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Jeff | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Fae         |
| 2           | NPC Jeff | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob         |
| 2           | NPC Jeff | Inspector   | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan        |
| 2           | NPC Jeff | Inspector   | broadcast | I (NPC Ken) am the Psychic and the Priest is not possessed     |
| 2           | NPC Jeff | Inspector   | broadcast | I (NPC Ken) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Jeff | Inspector   | broadcast | I (NPC Ken) am the Psychic and the Spy is not possessed        |
| 2           | NPC Jeff | Inspector   | broadcast | I (NPC Ken) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ken  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Igi is targeting NPC Jeff        |
| 2           | NPC Ken  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Han is targeting NPC Jeff        |
| 2           | NPC Ken  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Bob         |
| 2           | NPC Ken  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Gia is targeting NPC Igi         |
| 2           | NPC Ken  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Ken  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Cal is targeting NPC Fae         |
| 2           | NPC Ken  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Fae is targeting NPC Bob         |
| 2           | NPC Ken  | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Jeff is targeting NPC Dan        |
| 2           | NPC Ken  | Psychic     | broadcast | I (NPC Ken) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ken  | Psychic     | broadcast | I (NPC Ken) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Ken  | Psychic     | broadcast | I (NPC Ken) am the Psychic and the Spy is not possessed        |
| 2           | NPC Ken  | Psychic     | broadcast | I (NPC Ken) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ken  | Psychic     | reveal    | Player: NPC Han is not possessed                               |
| 2           | NPC Ken  | Psychic     | reveal    | Player: NPC Igi is not possessed                               |
| 2           | NPC Ken  | Psychic     | reveal    | Player: NPC Gia is not possessed                               |
| 2           | NPC Ken  | Psychic     | reveal    | Player: NPC Ed is not possessed                                |