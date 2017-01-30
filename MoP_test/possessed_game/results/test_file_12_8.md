#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 8    | 12      | 8       |

#### Roles
| Role         |
| :----------- |
| Judge        |
| Assassin     |
| Medic        |
| Thief        |
| Demagog      |
| Executioner  |
| Jailer       |
| Reporter     |
| Prophet      |
| Spy          |
| Psychic      |
| Inspector    |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Executioner | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Ann  | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Bob  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Bob  | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Cal  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Cal  | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Dan  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Ed   | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Fae  | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Gia  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Han  | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Igi  | Executioner | possessed   | You are Possessed         |
| 0           | NPC Jeff | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Jeff | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Thief       | role change | Your Role is Thief        |
| 0           | NPC Ken  | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Lee  | Spy         | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action      | Target 1    | Target 2 | status                        |
| :-----------| :-------| :-----------| :-----------| :--------| :---------------------------- |
| 1           | NPC Ann | Demagog     | Executioner |          | voting in progress            |
| 1           | NPC Bob | Medic       | NPC Han     |          | successful                    |
| 1           | NPC Cal | Psychic     |             |          | successful                    |
| 1           | NPC Dan | Inspector   | NPC Ken     |          | successful                    |
| 1           | NPC Ed  | Reporter    | NPC Ann     |          | successful                    |
| 1           | NPC Fae | Prophet     | NPC Cal     |          | successful                    |
| 1           | NPC Gia | Judge       | Assassin    |          | successful                    |
| 1           | NPC Han | Assassin    | Judge       |          | successful                    |
| 1           | NPC Igi | Executioner | NPC Dan     |          | failed because of no support  |
| 1           | NPC Ken | Thief       | NPC Jeff    |          | successful                    |
| 1           | NPC Lee | Spy         |             |          | successful                    |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ken  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Igi  | Executioner | False      | True      | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Jeff | Jailer      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Ed   | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Fae  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Lee  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Dan  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message       | details                                                        |
| :-----------| :--------| :-----------| :-------------| :------------------------------------------------------------- |
| 1           | NPC Ann  | Demagog     | broadcast     | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ann  | Demagog     | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ann  | Demagog     | broadcast     | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 1           | NPC Ann  | Demagog     | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Ann  | Demagog     | broadcast     | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ann  | Demagog     | broadcast     | I (NPC Dan) inspected NPC Ken and they are not possessed       |
| 1           | NPC Ann  | Demagog     | broadcast     | I (NPC Ed) am the Reporter and NPC Ann is the Demagog          |
| 1           | NPC Ann  | Demagog     | broadcast     | I (NPC Ken) am the Thief and I have made NPC Jeff vulnerable   |
| 1           | NPC Ann  | Demagog     | vote          | Demagog has initiated a vote on eliminating Executioner        |
| 1           | NPC Bob  | Medic       | broadcast     | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob  | Medic       | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 1           | NPC Bob  | Medic       | broadcast     | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 1           | NPC Bob  | Medic       | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Bob  | Medic       | broadcast     | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Bob  | Medic       | broadcast     | I (NPC Dan) inspected NPC Ken and they are not possessed       |
| 1           | NPC Bob  | Medic       | broadcast     | I (NPC Ed) am the Reporter and NPC Ann is the Demagog          |
| 1           | NPC Bob  | Medic       | broadcast     | I (NPC Ken) am the Thief and I have made NPC Jeff vulnerable   |
| 1           | NPC Bob  | Medic       | vote          | Demagog has initiated a vote on eliminating Executioner        |
| 1           | NPC Cal  | Psychic     | broadcast     | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Cal  | Psychic     | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 1           | NPC Cal  | Psychic     | broadcast     | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 1           | NPC Cal  | Psychic     | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Cal  | Psychic     | broadcast     | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Cal  | Psychic     | broadcast     | I (NPC Dan) inspected NPC Ken and they are not possessed       |
| 1           | NPC Cal  | Psychic     | broadcast     | I (NPC Ed) am the Reporter and NPC Ann is the Demagog          |
| 1           | NPC Cal  | Psychic     | broadcast     | I (NPC Ken) am the Thief and I have made NPC Jeff vulnerable   |
| 1           | NPC Cal  | Psychic     | reveal        | Player: NPC Ken is not possessed                               |
| 1           | NPC Cal  | Psychic     | reveal        | Player: NPC Bob is not possessed                               |
| 1           | NPC Cal  | Psychic     | reveal        | Player: NPC Ed is not possessed                                |
| 1           | NPC Cal  | Psychic     | reveal        | Player: NPC Lee is not possessed                               |
| 1           | NPC Cal  | Psychic     | reveal        | Player: NPC Fae is not possessed                               |
| 1           | NPC Cal  | Psychic     | vote          | Demagog has initiated a vote on eliminating Executioner        |
| 1           | NPC Dan  | Inspector   | broadcast     | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Dan  | Inspector   | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 1           | NPC Dan  | Inspector   | broadcast     | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 1           | NPC Dan  | Inspector   | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Dan  | Inspector   | broadcast     | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Dan  | Inspector   | broadcast     | I (NPC Dan) inspected NPC Ken and they are not possessed       |
| 1           | NPC Dan  | Inspector   | broadcast     | I (NPC Ed) am the Reporter and NPC Ann is the Demagog          |
| 1           | NPC Dan  | Inspector   | broadcast     | I (NPC Ken) am the Thief and I have made NPC Jeff vulnerable   |
| 1           | NPC Dan  | Inspector   | reveal        | Thief is Innocent                                              |
| 1           | NPC Dan  | Inspector   | vote          | Demagog has initiated a vote on eliminating Executioner        |
| 1           | NPC Ed   | Reporter    | broadcast     | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ed   | Reporter    | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ed   | Reporter    | broadcast     | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 1           | NPC Ed   | Reporter    | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Ed   | Reporter    | broadcast     | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ed   | Reporter    | broadcast     | I (NPC Dan) inspected NPC Ken and they are not possessed       |
| 1           | NPC Ed   | Reporter    | broadcast     | I (NPC Ed) am the Reporter and NPC Ann is the Demagog          |
| 1           | NPC Ed   | Reporter    | broadcast     | I (NPC Ken) am the Thief and I have made NPC Jeff vulnerable   |
| 1           | NPC Ed   | Reporter    | reveal        | NPC Ann is Demagog                                             |
| 1           | NPC Ed   | Reporter    | vote          | Demagog has initiated a vote on eliminating Executioner        |
| 1           | NPC Fae  | Prophet     | broadcast     | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Fae  | Prophet     | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 1           | NPC Fae  | Prophet     | broadcast     | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 1           | NPC Fae  | Prophet     | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Fae  | Prophet     | broadcast     | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Fae  | Prophet     | broadcast     | I (NPC Dan) inspected NPC Ken and they are not possessed       |
| 1           | NPC Fae  | Prophet     | broadcast     | I (NPC Ed) am the Reporter and NPC Ann is the Demagog          |
| 1           | NPC Fae  | Prophet     | broadcast     | I (NPC Ken) am the Thief and I have made NPC Jeff vulnerable   |
| 1           | NPC Fae  | Prophet     | vote          | Demagog has initiated a vote on eliminating Executioner        |
| 1           | NPC Gia  | Judge       | broadcast     | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Gia  | Judge       | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 1           | NPC Gia  | Judge       | broadcast     | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 1           | NPC Gia  | Judge       | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Gia  | Judge       | broadcast     | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Gia  | Judge       | broadcast     | I (NPC Dan) inspected NPC Ken and they are not possessed       |
| 1           | NPC Gia  | Judge       | broadcast     | I (NPC Ed) am the Reporter and NPC Ann is the Demagog          |
| 1           | NPC Gia  | Judge       | broadcast     | I (NPC Ken) am the Thief and I have made NPC Jeff vulnerable   |
| 1           | NPC Gia  | Judge       | vote          | Demagog has initiated a vote on eliminating Executioner        |
| 1           | NPC Han  | Assassin    | broadcast     | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Han  | Assassin    | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 1           | NPC Han  | Assassin    | broadcast     | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 1           | NPC Han  | Assassin    | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Han  | Assassin    | broadcast     | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Han  | Assassin    | broadcast     | I (NPC Dan) inspected NPC Ken and they are not possessed       |
| 1           | NPC Han  | Assassin    | broadcast     | I (NPC Ed) am the Reporter and NPC Ann is the Demagog          |
| 1           | NPC Han  | Assassin    | broadcast     | I (NPC Ken) am the Thief and I have made NPC Jeff vulnerable   |
| 1           | NPC Han  | Assassin    | vote          | Demagog has initiated a vote on eliminating Executioner        |
| 1           | NPC Igi  | Executioner | broadcast     | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Igi  | Executioner | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 1           | NPC Igi  | Executioner | broadcast     | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 1           | NPC Igi  | Executioner | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Igi  | Executioner | broadcast     | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Igi  | Executioner | broadcast     | I (NPC Dan) inspected NPC Ken and they are not possessed       |
| 1           | NPC Igi  | Executioner | broadcast     | I (NPC Ed) am the Reporter and NPC Ann is the Demagog          |
| 1           | NPC Igi  | Executioner | broadcast     | I (NPC Ken) am the Thief and I have made NPC Jeff vulnerable   |
| 1           | NPC Igi  | Executioner | action failed |                                                                |
| 1           | NPC Igi  | Executioner | vote          | Demagog has initiated a vote on eliminating Executioner        |
| 1           | NPC Jeff | Jailer      | broadcast     | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Jeff | Jailer      | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 1           | NPC Jeff | Jailer      | broadcast     | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 1           | NPC Jeff | Jailer      | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Jeff | Jailer      | broadcast     | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Jeff | Jailer      | broadcast     | I (NPC Dan) inspected NPC Ken and they are not possessed       |
| 1           | NPC Jeff | Jailer      | broadcast     | I (NPC Ed) am the Reporter and NPC Ann is the Demagog          |
| 1           | NPC Jeff | Jailer      | broadcast     | I (NPC Ken) am the Thief and I have made NPC Jeff vulnerable   |
| 1           | NPC Jeff | Jailer      | vote          | Demagog has initiated a vote on eliminating Executioner        |
| 1           | NPC Ken  | Thief       | broadcast     | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ken  | Thief       | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ken  | Thief       | broadcast     | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 1           | NPC Ken  | Thief       | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Ken  | Thief       | broadcast     | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ken  | Thief       | broadcast     | I (NPC Dan) inspected NPC Ken and they are not possessed       |
| 1           | NPC Ken  | Thief       | broadcast     | I (NPC Ed) am the Reporter and NPC Ann is the Demagog          |
| 1           | NPC Ken  | Thief       | broadcast     | I (NPC Ken) am the Thief and I have made NPC Jeff vulnerable   |
| 1           | NPC Ken  | Thief       | vote          | Demagog has initiated a vote on eliminating Executioner        |
| 1           | NPC Lee  | Spy         | broadcast     | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Lee  | Spy         | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 1           | NPC Lee  | Spy         | broadcast     | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 1           | NPC Lee  | Spy         | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Lee  | Spy         | broadcast     | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Lee  | Spy         | broadcast     | I (NPC Dan) inspected NPC Ken and they are not possessed       |
| 1           | NPC Lee  | Spy         | broadcast     | I (NPC Ed) am the Reporter and NPC Ann is the Demagog          |
| 1           | NPC Lee  | Spy         | broadcast     | I (NPC Ken) am the Thief and I have made NPC Jeff vulnerable   |
| 1           | NPC Lee  | Spy         | reveal        | NPC Gia is targeting NPC Han                                   |
| 1           | NPC Lee  | Spy         | reveal        | NPC Ken is targeting NPC Jeff                                  |
| 1           | NPC Lee  | Spy         | reveal        | NPC Igi is targeting NPC Dan                                   |
| 1           | NPC Lee  | Spy         | reveal        | NPC Ed is targeting NPC Ann                                    |
| 1           | NPC Lee  | Spy         | reveal        | NPC Dan is targeting NPC Ken                                   |
| 1           | NPC Lee  | Spy         | vote          | Demagog has initiated a vote on eliminating Executioner        |

#### Actions Round 2
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 2           | NPC Bob | Medic    | NPC Ken  |          | successful  |
| 2           | NPC Cal | Psychic  |          |          | successful  |
| 2           | NPC Fae | Prophet  | NPC Ed   |          | successful  |
| 2           | NPC Gia | Judge    | Demagog  |          | successful  |
| 2           | NPC Han | Assassin | Demagog  |          | successful  |
| 2           | NPC Lee | Spy      |          |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Bob  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ken  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Igi  | Executioner | False      | True      | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Jeff | Jailer      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 2           | NPC Ed   | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Fae  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Lee  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Han        |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia        |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Han        |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff       |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi        |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann         |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Cal        |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Han        |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia        |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Han        |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff       |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi        |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann         |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Cal        |
| 2           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Han        |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia        |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Han        |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff       |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi        |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann         |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Cal        |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Cal  | Psychic     | reveal    | Player: NPC Jeff is not possessed                              |
| 2           | NPC Cal  | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 2           | NPC Cal  | Psychic     | reveal    | Player: NPC Fae is not possessed                               |
| 2           | NPC Cal  | Psychic     | reveal    | Player: NPC Ann is not possessed                               |
| 2           | NPC Cal  | Psychic     | reveal    | Player: NPC Ed is not possessed                                |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Han        |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia        |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Han        |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff       |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi        |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann         |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Cal        |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Han        |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia        |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Han        |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff       |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi        |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann         |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Cal        |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Han        |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia        |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Han        |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff       |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi        |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann         |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Cal        |
| 2           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Han        |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia        |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Han        |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff       |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi        |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann         |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Cal        |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Han        |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia        |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Han        |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff       |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi        |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann         |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Cal        |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Han        |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia        |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Han        |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff       |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi        |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann         |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Cal        |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Han        |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia        |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Han        |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff       |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi        |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann         |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Cal        |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Han        |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia        |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Han        |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff       |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi        |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann         |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Cal        |
| 2           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Han        |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia        |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Han        |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff       |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi        |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann         |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Cal        |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Lee  | Spy         | reveal    | NPC Gia is targeting NPC Ann                                   |
| 2           | NPC Lee  | Spy         | reveal    | NPC Han is targeting NPC Gia                                   |
| 2           | NPC Lee  | Spy         | reveal    | NPC Bob is targeting NPC Han                                   |
| 2           | NPC Lee  | Spy         | reveal    | NPC Ken is targeting NPC Jeff                                  |
| 2           | NPC Lee  | Spy         | reveal    | NPC Ann is targeting NPC Igi                                   |
| 2           | NPC Lee  | Spy         | reveal    | NPC Igi is targeting NPC Dan                                   |
| 2           | NPC Lee  | Spy         | reveal    | NPC Ed is targeting NPC Ann                                    |
| 2           | NPC Lee  | Spy         | reveal    | NPC Fae is targeting NPC Cal                                   |
| 2           | NPC Lee  | Spy         | reveal    | NPC Dan is targeting NPC Ken                                   |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status              |
| :-----------| :-------| :---------| :--------| :--------| :------------------ |
| 3           | NPC Ann | Demagog   | Assassin |          | voting in progress  |
| 3           | NPC Bob | Medic     | NPC Ann  |          | successful          |
| 3           | NPC Cal | Psychic   |          |          | successful          |
| 3           | NPC Dan | Inspector | NPC Gia  |          | successful          |
| 3           | NPC Ed  | Reporter  | NPC Igi  |          | successful          |
| 3           | NPC Fae | Prophet   | NPC Bob  |          | successful          |
| 3           | NPC Gia | Judge     | Thief    |          | successful          |
| 3           | NPC Ken | Thief     | NPC Igi  |          | successful          |
| 3           | NPC Lee | Spy       |          |          | successful          |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Han  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Bob  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ken  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Igi  | Executioner | False      | True      | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Jeff | Jailer      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Ed   | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Fae  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Lee  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Dan  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed    |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed       |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed      |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Thief and I have made NPC Igi vulnerable   |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann       |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann       |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ken       |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff      |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi       |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed        |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken       |
| 3           | NPC Ann  | Demagog     | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed    |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed       |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed      |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Ken) am the Thief and I have made NPC Igi vulnerable   |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann       |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann       |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ken       |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff      |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi       |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed        |
| 3           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken       |
| 3           | NPC Bob  | Medic       | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed    |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed       |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed      |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Ken) am the Thief and I have made NPC Igi vulnerable   |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann       |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann       |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ken       |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff      |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi       |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed        |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken       |
| 3           | NPC Cal  | Psychic     | reveal    | Player: NPC Ann is not possessed                              |
| 3           | NPC Cal  | Psychic     | reveal    | Player: NPC Jeff is not possessed                             |
| 3           | NPC Cal  | Psychic     | reveal    | Player: NPC Ken is not possessed                              |
| 3           | NPC Cal  | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 3           | NPC Cal  | Psychic     | reveal    | Player: NPC Ed is not possessed                               |
| 3           | NPC Cal  | Psychic     | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed    |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed       |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed      |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Ken) am the Thief and I have made NPC Igi vulnerable   |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann       |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann       |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ken       |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff      |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi       |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed        |
| 3           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken       |
| 3           | NPC Dan  | Inspector   | reveal    | Judge is Innocent                                             |
| 3           | NPC Dan  | Inspector   | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed    |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed       |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed      |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Thief and I have made NPC Igi vulnerable   |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann       |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann       |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ken       |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff      |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi       |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed        |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken       |
| 3           | NPC Ed   | Reporter    | reveal    | NPC Igi is Executioner                                        |
| 3           | NPC Ed   | Reporter    | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed    |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed       |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed      |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Ken) am the Thief and I have made NPC Igi vulnerable   |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann       |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann       |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ken       |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff      |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi       |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed        |
| 3           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken       |
| 3           | NPC Fae  | Prophet     | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed    |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed       |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Ken) am the Thief and I have made NPC Igi vulnerable   |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann       |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann       |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ken       |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi       |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed        |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken       |
| 3           | NPC Gia  | Judge       | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed    |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed       |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed      |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Ken) am the Thief and I have made NPC Igi vulnerable   |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann       |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann       |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ken       |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff      |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi       |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed        |
| 3           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken       |
| 3           | NPC Han  | Assassin    | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed    |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed       |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed      |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Ken) am the Thief and I have made NPC Igi vulnerable   |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann       |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann       |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ken       |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff      |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi       |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed        |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken       |
| 3           | NPC Igi  | Executioner | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed    |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed       |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed      |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Thief and I have made NPC Igi vulnerable   |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann       |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann       |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ken       |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff      |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi       |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed        |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken       |
| 3           | NPC Jeff | Jailer      | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed    |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed       |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed      |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Ken) am the Thief and I have made NPC Igi vulnerable   |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann       |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann       |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ken       |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff      |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi       |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed        |
| 3           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken       |
| 3           | NPC Ken  | Thief       | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed    |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed       |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed      |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Ken) am the Thief and I have made NPC Igi vulnerable   |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann       |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann       |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ken       |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Jeff      |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Igi       |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed        |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ken       |
| 3           | NPC Lee  | Spy         | reveal    | NPC Gia is targeting NPC Ken                                  |
| 3           | NPC Lee  | Spy         | reveal    | NPC Han is targeting NPC Ann                                  |
| 3           | NPC Lee  | Spy         | reveal    | NPC Bob is targeting NPC Ken                                  |
| 3           | NPC Lee  | Spy         | reveal    | NPC Ken is targeting NPC Igi                                  |
| 3           | NPC Lee  | Spy         | reveal    | NPC Ann is targeting NPC Igi                                  |
| 3           | NPC Lee  | Spy         | reveal    | NPC Igi is targeting NPC Dan                                  |
| 3           | NPC Lee  | Spy         | reveal    | NPC Ed is targeting NPC Igi                                   |
| 3           | NPC Lee  | Spy         | reveal    | NPC Fae is targeting NPC Ed                                   |
| 3           | NPC Lee  | Spy         | reveal    | NPC Dan is targeting NPC Gia                                  |
| 3           | NPC Lee  | Spy         | vote      | Demagog has initiated a vote on eliminating Assassin          |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 4           | NPC Ann | Demagog  | Reporter |          | voting in progress  |
| 4           | NPC Bob | Medic    | NPC Igi  |          | successful          |
| 4           | NPC Cal | Psychic  |          |          | successful          |
| 4           | NPC Fae | Prophet  | NPC Ed   |          | successful          |
| 4           | NPC Gia | Judge    | Thief    |          | successful          |
| 4           | NPC Han | Assassin | Jailer   |          | successful          |
| 4           | NPC Lee | Spy      |          |          | successful          |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Han  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Bob  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ken  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Igi  | Executioner | False      | True      | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Jeff | Jailer      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Ed   | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Fae  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Lee  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Cal  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann        |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ann        |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Han        |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 4           | NPC Ann  | Demagog     | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann        |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ann        |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Han        |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 4           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 4           | NPC Bob  | Medic       | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann        |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ann        |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Han        |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 4           | NPC Cal  | Psychic     | reveal    | Player: NPC Fae is not possessed                               |
| 4           | NPC Cal  | Psychic     | reveal    | Player: NPC Ann is not possessed                               |
| 4           | NPC Cal  | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 4           | NPC Cal  | Psychic     | reveal    | Player: NPC Lee is not possessed                               |
| 4           | NPC Cal  | Psychic     | reveal    | Player: NPC Ed is not possessed                                |
| 4           | NPC Cal  | Psychic     | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann        |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ann        |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Han        |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 4           | NPC Dan  | Inspector   | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann        |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ann        |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Han        |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 4           | NPC Ed   | Reporter    | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann        |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ann        |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Han        |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 4           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 4           | NPC Fae  | Prophet     | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann        |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ann        |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Han        |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 4           | NPC Gia  | Judge       | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann        |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ann        |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Han        |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 4           | NPC Han  | Assassin    | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann        |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ann        |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Han        |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 4           | NPC Igi  | Executioner | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann        |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ann        |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Han        |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 4           | NPC Jeff | Jailer      | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann        |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ann        |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Han        |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 4           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 4           | NPC Ken  | Thief       | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed        |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ann        |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ann        |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Han        |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 4           | NPC Lee  | Spy         | reveal    | NPC Gia is targeting NPC Ken                                   |
| 4           | NPC Lee  | Spy         | reveal    | NPC Han is targeting NPC Ann                                   |
| 4           | NPC Lee  | Spy         | reveal    | NPC Bob is targeting NPC Ann                                   |
| 4           | NPC Lee  | Spy         | reveal    | NPC Ken is targeting NPC Igi                                   |
| 4           | NPC Lee  | Spy         | reveal    | NPC Ann is targeting NPC Han                                   |
| 4           | NPC Lee  | Spy         | reveal    | NPC Igi is targeting NPC Dan                                   |
| 4           | NPC Lee  | Spy         | reveal    | NPC Ed is targeting NPC Igi                                    |
| 4           | NPC Lee  | Spy         | reveal    | NPC Fae is targeting NPC Bob                                   |
| 4           | NPC Lee  | Spy         | reveal    | NPC Dan is targeting NPC Gia                                   |
| 4           | NPC Lee  | Spy         | vote      | Demagog has initiated a vote on eliminating Reporter           |

#### Actions Round 5
| round_index | Player  | action      | Target 1  | Target 2 | status      |
| :-----------| :-------| :-----------| :---------| :--------| :---------- |
| 5           | NPC Bob | Medic       | NPC Jeff  |          | successful  |
| 5           | NPC Cal | Psychic     |           |          | successful  |
| 5           | NPC Dan | Inspector   | NPC Cal   |          | successful  |
| 5           | NPC Ed  | Reporter    | NPC Fae   |          | successful  |
| 5           | NPC Fae | Prophet     | NPC Jeff  |          | successful  |
| 5           | NPC Gia | Judge       | Inspector |          | successful  |
| 5           | NPC Igi | Executioner | NPC Dan   |          | successful  |
| 5           | NPC Ken | Thief       | NPC Lee   |          | successful  |
| 5           | NPC Lee | Spy         |           |          | successful  |

#### States Round 5
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Han  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Bob  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ken  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Ann  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Igi  | Executioner | False      | True      | True       | 4         | True   | 0              | 0                  |
| 5           | NPC Jeff | Jailer      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Ed   | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Fae  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Lee  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Cal  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Dan  | Inspector   | True       | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player   | Role        | message     | details                                                        |
| :-----------| :--------| :-----------| :-----------| :------------------------------------------------------------- |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Ed) am the Reporter and NPC Fae is the Prophet          |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Ken) am the Thief and I have made NPC Lee vulnerable    |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Igi        |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed         |
| 5           | NPC Ann  | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 5           | NPC Ann  | Demagog     | elimination | NPC Dan has been eliminated                                    |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Ed) am the Reporter and NPC Fae is the Prophet          |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Ken) am the Thief and I have made NPC Lee vulnerable    |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Igi        |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed         |
| 5           | NPC Bob  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 5           | NPC Bob  | Medic       | elimination | NPC Dan has been eliminated                                    |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Ed) am the Reporter and NPC Fae is the Prophet          |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Ken) am the Thief and I have made NPC Lee vulnerable    |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Igi        |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed         |
| 5           | NPC Cal  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 5           | NPC Cal  | Psychic     | elimination | NPC Dan has been eliminated                                    |
| 5           | NPC Cal  | Psychic     | reveal      | Player: NPC Bob is not possessed                               |
| 5           | NPC Cal  | Psychic     | reveal      | Player: NPC Fae is not possessed                               |
| 5           | NPC Cal  | Psychic     | reveal      | Player: NPC Ken is not possessed                               |
| 5           | NPC Cal  | Psychic     | reveal      | Player: NPC Han is not possessed                               |
| 5           | NPC Cal  | Psychic     | reveal      | Player: NPC Gia is not possessed                               |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Ed) am the Reporter and NPC Fae is the Prophet          |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Ken) am the Thief and I have made NPC Lee vulnerable    |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Igi        |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed         |
| 5           | NPC Dan  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 5           | NPC Dan  | Inspector   | elimination | NPC Dan has been eliminated                                    |
| 5           | NPC Dan  | Inspector   | reveal      | Psychic is Innocent                                            |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Ed) am the Reporter and NPC Fae is the Prophet          |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Ken) am the Thief and I have made NPC Lee vulnerable    |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Igi        |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed         |
| 5           | NPC Ed   | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 5           | NPC Ed   | Reporter    | elimination | NPC Dan has been eliminated                                    |
| 5           | NPC Ed   | Reporter    | reveal      | NPC Fae is Prophet                                             |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Ed) am the Reporter and NPC Fae is the Prophet          |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Ken) am the Thief and I have made NPC Lee vulnerable    |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Igi        |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed         |
| 5           | NPC Fae  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 5           | NPC Fae  | Prophet     | elimination | NPC Dan has been eliminated                                    |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Ed) am the Reporter and NPC Fae is the Prophet          |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Ken) am the Thief and I have made NPC Lee vulnerable    |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Igi        |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed         |
| 5           | NPC Gia  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 5           | NPC Gia  | Judge       | elimination | NPC Dan has been eliminated                                    |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Ed) am the Reporter and NPC Fae is the Prophet          |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Ken) am the Thief and I have made NPC Lee vulnerable    |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Igi        |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed         |
| 5           | NPC Han  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 5           | NPC Han  | Assassin    | elimination | NPC Dan has been eliminated                                    |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Ed) am the Reporter and NPC Fae is the Prophet          |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Ken) am the Thief and I have made NPC Lee vulnerable    |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Igi        |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed         |
| 5           | NPC Igi  | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 5           | NPC Igi  | Executioner | elimination | NPC Dan has been eliminated                                    |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Ed) am the Reporter and NPC Fae is the Prophet          |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Ken) am the Thief and I have made NPC Lee vulnerable    |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Igi        |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed         |
| 5           | NPC Jeff | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 5           | NPC Jeff | Jailer      | elimination | NPC Dan has been eliminated                                    |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Ed) am the Reporter and NPC Fae is the Prophet          |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Ken) am the Thief and I have made NPC Lee vulnerable    |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Igi        |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed         |
| 5           | NPC Ken  | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 5           | NPC Ken  | Thief       | elimination | NPC Dan has been eliminated                                    |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Cal) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Ed) am the Reporter and NPC Fae is the Prophet          |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Ken) am the Thief and I have made NPC Lee vulnerable    |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ken        |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Igi        |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Igi        |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi         |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ed         |
| 5           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Gia        |
| 5           | NPC Lee  | Spy         | elimination | NPC Dan has been eliminated                                    |
| 5           | NPC Lee  | Spy         | reveal      | NPC Gia is targeting NPC Dan                                   |
| 5           | NPC Lee  | Spy         | reveal      | NPC Han is targeting NPC Jeff                                  |
| 5           | NPC Lee  | Spy         | reveal      | NPC Bob is targeting NPC Igi                                   |
| 5           | NPC Lee  | Spy         | reveal      | NPC Ken is targeting NPC Lee                                   |
| 5           | NPC Lee  | Spy         | reveal      | NPC Ann is targeting NPC Ed                                    |
| 5           | NPC Lee  | Spy         | reveal      | NPC Igi is targeting NPC Dan                                   |
| 5           | NPC Lee  | Spy         | reveal      | NPC Ed is targeting NPC Fae                                    |
| 5           | NPC Lee  | Spy         | reveal      | NPC Fae is targeting NPC Ed                                    |

#### Actions Round 6
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 6           | NPC Ann | Demagog  | Prophet  |          | voting in progress  |
| 6           | NPC Bob | Medic    | NPC Ed   |          | successful          |
| 6           | NPC Cal | Psychic  |          |          | successful          |
| 6           | NPC Fae | Prophet  | NPC Igi  |          | successful          |
| 6           | NPC Gia | Judge    | Prophet  |          | successful          |
| 6           | NPC Han | Assassin | Medic    |          | successful          |
| 6           | NPC Lee | Spy      |          |          | successful          |

#### States Round 6
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Han  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Bob  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ken  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ann  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Igi  | Executioner | False      | True      | True       | 3         | True   | 0              | 0                  |
| 6           | NPC Jeff | Jailer      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Ed   | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Fae  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Lee  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Cal  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Dan  | Inspector   | True       | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Dan        |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Jeff       |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee        |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae         |
| 6           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Jeff       |
| 6           | NPC Ann  | Demagog     | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 6           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 6           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 6           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 6           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Dan        |
| 6           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 6           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Jeff       |
| 6           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee        |
| 6           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 6           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 6           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae         |
| 6           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Jeff       |
| 6           | NPC Bob  | Medic       | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 6           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 6           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 6           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 6           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Dan        |
| 6           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 6           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Jeff       |
| 6           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee        |
| 6           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 6           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 6           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae         |
| 6           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Jeff       |
| 6           | NPC Cal  | Psychic     | reveal    | Player: NPC Gia is not possessed                               |
| 6           | NPC Cal  | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 6           | NPC Cal  | Psychic     | reveal    | Player: NPC Han is not possessed                               |
| 6           | NPC Cal  | Psychic     | reveal    | Player: NPC Ken is not possessed                               |
| 6           | NPC Cal  | Psychic     | reveal    | Player: NPC Lee is not possessed                               |
| 6           | NPC Cal  | Psychic     | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Dan        |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Jeff       |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee        |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae         |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Jeff       |
| 6           | NPC Dan  | Inspector   | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Dan        |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Jeff       |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee        |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae         |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Jeff       |
| 6           | NPC Ed   | Reporter    | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 6           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 6           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 6           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 6           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Dan        |
| 6           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 6           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Jeff       |
| 6           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee        |
| 6           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 6           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 6           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae         |
| 6           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Jeff       |
| 6           | NPC Fae  | Prophet     | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 6           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 6           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 6           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 6           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Dan        |
| 6           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 6           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Jeff       |
| 6           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee        |
| 6           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 6           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 6           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae         |
| 6           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Jeff       |
| 6           | NPC Gia  | Judge       | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Dan        |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Jeff       |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee        |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae         |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Jeff       |
| 6           | NPC Han  | Assassin    | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Dan        |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Jeff       |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee        |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae         |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Jeff       |
| 6           | NPC Igi  | Executioner | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 6           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 6           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 6           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 6           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Dan        |
| 6           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 6           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Jeff       |
| 6           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee        |
| 6           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 6           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 6           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae         |
| 6           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Jeff       |
| 6           | NPC Jeff | Jailer      | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 6           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 6           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 6           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 6           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Dan        |
| 6           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 6           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Jeff       |
| 6           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee        |
| 6           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 6           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 6           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae         |
| 6           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Jeff       |
| 6           | NPC Ken  | Thief       | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Dan        |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Jeff       |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Jeff       |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee        |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae         |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Jeff       |
| 6           | NPC Lee  | Spy         | reveal    | NPC Gia is targeting NPC Fae                                   |
| 6           | NPC Lee  | Spy         | reveal    | NPC Han is targeting NPC Jeff                                  |
| 6           | NPC Lee  | Spy         | reveal    | NPC Bob is targeting NPC Jeff                                  |
| 6           | NPC Lee  | Spy         | reveal    | NPC Ken is targeting NPC Lee                                   |
| 6           | NPC Lee  | Spy         | reveal    | NPC Ann is targeting NPC Ed                                    |
| 6           | NPC Lee  | Spy         | reveal    | NPC Igi is targeting NPC Dan                                   |
| 6           | NPC Lee  | Spy         | reveal    | NPC Ed is targeting NPC Fae                                    |
| 6           | NPC Lee  | Spy         | reveal    | NPC Fae is targeting NPC Jeff                                  |
| 6           | NPC Lee  | Spy         | vote      | Demagog has initiated a vote on eliminating Prophet            |

#### Actions Round 7
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 7           | NPC Bob | Medic     | NPC Fae  |          | successful  |
| 7           | NPC Cal | Psychic   |          |          | successful  |
| 7           | NPC Dan | Inspector | NPC Ken  |          | successful  |
| 7           | NPC Ed  | Reporter  | NPC Dan  |          | successful  |
| 7           | NPC Fae | Prophet   | NPC Gia  |          | successful  |
| 7           | NPC Gia | Judge     | Demagog  |          | successful  |
| 7           | NPC Ken | Thief     | NPC Bob  |          | successful  |
| 7           | NPC Lee | Spy       |          |          | successful  |

#### States Round 7
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Han  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Bob  | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Ken  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Ann  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Igi  | Executioner | False      | True      | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Jeff | Jailer      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Ed   | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Fae  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Lee  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Cal  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Dan  | Inspector   | True       | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Dan) inspected NPC Ken and they are not possessed      |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Inspector       |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Ken) am the Thief and I have made NPC Bob vulnerable   |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Fae       |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee       |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae       |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Igi       |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Dan) inspected NPC Ken and they are not possessed      |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Inspector       |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Ken) am the Thief and I have made NPC Bob vulnerable   |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Fae       |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee       |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae       |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Igi       |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Dan) inspected NPC Ken and they are not possessed      |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Inspector       |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Ken) am the Thief and I have made NPC Bob vulnerable   |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Fae       |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee       |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae       |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Igi       |
| 7           | NPC Cal  | Psychic     | reveal    | Player: NPC Fae is not possessed                              |
| 7           | NPC Cal  | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 7           | NPC Cal  | Psychic     | reveal    | Player: NPC Jeff is not possessed                             |
| 7           | NPC Cal  | Psychic     | reveal    | Player: NPC Gia is not possessed                              |
| 7           | NPC Cal  | Psychic     | reveal    | Player: NPC Ann is not possessed                              |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Dan) inspected NPC Ken and they are not possessed      |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Inspector       |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Ken) am the Thief and I have made NPC Bob vulnerable   |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Fae       |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee       |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae       |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Igi       |
| 7           | NPC Dan  | Inspector   | reveal    | Thief is Innocent                                             |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Dan) inspected NPC Ken and they are not possessed      |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Inspector       |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) am the Thief and I have made NPC Bob vulnerable   |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Fae       |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee       |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae       |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Igi       |
| 7           | NPC Ed   | Reporter    | reveal    | NPC Dan is Inspector                                          |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Dan) inspected NPC Ken and they are not possessed      |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Inspector       |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Ken) am the Thief and I have made NPC Bob vulnerable   |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Fae       |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee       |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae       |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Igi       |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Dan) inspected NPC Ken and they are not possessed      |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Inspector       |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Ken) am the Thief and I have made NPC Bob vulnerable   |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Fae       |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee       |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae       |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Igi       |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Dan) inspected NPC Ken and they are not possessed      |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Inspector       |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Ken) am the Thief and I have made NPC Bob vulnerable   |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Fae       |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee       |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae       |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Igi       |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Dan) inspected NPC Ken and they are not possessed      |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Inspector       |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Ken) am the Thief and I have made NPC Bob vulnerable   |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Fae       |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee       |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae       |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Igi       |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Dan) inspected NPC Ken and they are not possessed      |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Inspector       |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Ken) am the Thief and I have made NPC Bob vulnerable   |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Fae       |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee       |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae       |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Igi       |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Dan) inspected NPC Ken and they are not possessed      |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Inspector       |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Ken) am the Thief and I have made NPC Bob vulnerable   |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Fae       |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee       |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae       |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Igi       |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed   |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Dan) inspected NPC Ken and they are not possessed      |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Inspector       |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Ken) am the Thief and I have made NPC Bob vulnerable   |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Fae       |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Lee       |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae       |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan       |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Igi       |
| 7           | NPC Lee  | Spy         | reveal    | NPC Gia is targeting NPC Ann                                  |
| 7           | NPC Lee  | Spy         | reveal    | NPC Han is targeting NPC Bob                                  |
| 7           | NPC Lee  | Spy         | reveal    | NPC Bob is targeting NPC Ed                                   |
| 7           | NPC Lee  | Spy         | reveal    | NPC Ken is targeting NPC Bob                                  |
| 7           | NPC Lee  | Spy         | reveal    | NPC Ann is targeting NPC Fae                                  |
| 7           | NPC Lee  | Spy         | reveal    | NPC Igi is targeting NPC Dan                                  |
| 7           | NPC Lee  | Spy         | reveal    | NPC Ed is targeting NPC Dan                                   |
| 7           | NPC Lee  | Spy         | reveal    | NPC Fae is targeting NPC Igi                                  |

#### Actions Round 8
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 8           | NPC Ann | Demagog  | Prophet  |          | voting in progress  |
| 8           | NPC Bob | Medic    | NPC Lee  |          | successful          |
| 8           | NPC Cal | Psychic  |          |          | successful          |
| 8           | NPC Fae | Prophet  | NPC Ken  |          | successful          |
| 8           | NPC Gia | Judge    | Spy      |          | successful          |
| 8           | NPC Han | Assassin | Demagog  |          | successful          |
| 8           | NPC Lee | Spy      |          |          | successful          |

#### States Round 8
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Han  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 8           | NPC Bob  | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Ken  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Ann  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 8           | NPC Igi  | Executioner | False      | True      | True       | 1         | True   | 0              | 0                  |
| 8           | NPC Jeff | Jailer      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Ed   | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Fae  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Lee  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Cal  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Dan  | Inspector   | True       | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 8           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 8           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 8           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 8           | NPC Ann  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 8           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann        |
| 8           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob        |
| 8           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Fae        |
| 8           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Bob        |
| 8           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae        |
| 8           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 8           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Dan         |
| 8           | NPC Ann  | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia        |
| 8           | NPC Ann  | Demagog     | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 8           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 8           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 8           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 8           | NPC Bob  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 8           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann        |
| 8           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob        |
| 8           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Fae        |
| 8           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Bob        |
| 8           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae        |
| 8           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 8           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Dan         |
| 8           | NPC Bob  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia        |
| 8           | NPC Bob  | Medic       | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 8           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 8           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 8           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 8           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 8           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann        |
| 8           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob        |
| 8           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Fae        |
| 8           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Bob        |
| 8           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae        |
| 8           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 8           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Dan         |
| 8           | NPC Cal  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia        |
| 8           | NPC Cal  | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 8           | NPC Cal  | Psychic     | reveal    | Player: NPC Ed is not possessed                                |
| 8           | NPC Cal  | Psychic     | reveal    | Player: NPC Jeff is not possessed                              |
| 8           | NPC Cal  | Psychic     | reveal    | Player: NPC Lee is not possessed                               |
| 8           | NPC Cal  | Psychic     | reveal    | Player: NPC Ken is not possessed                               |
| 8           | NPC Cal  | Psychic     | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 8           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 8           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 8           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 8           | NPC Dan  | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 8           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann        |
| 8           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob        |
| 8           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Fae        |
| 8           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Bob        |
| 8           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae        |
| 8           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 8           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Dan         |
| 8           | NPC Dan  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia        |
| 8           | NPC Dan  | Inspector   | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 8           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 8           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 8           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 8           | NPC Ed   | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 8           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann        |
| 8           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob        |
| 8           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Fae        |
| 8           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Bob        |
| 8           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae        |
| 8           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 8           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Dan         |
| 8           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia        |
| 8           | NPC Ed   | Reporter    | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 8           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 8           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 8           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 8           | NPC Fae  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 8           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann        |
| 8           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob        |
| 8           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Fae        |
| 8           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Bob        |
| 8           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae        |
| 8           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 8           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Dan         |
| 8           | NPC Fae  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia        |
| 8           | NPC Fae  | Prophet     | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 8           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 8           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 8           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 8           | NPC Gia  | Judge       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 8           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann        |
| 8           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob        |
| 8           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Fae        |
| 8           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Bob        |
| 8           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae        |
| 8           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 8           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Dan         |
| 8           | NPC Gia  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia        |
| 8           | NPC Gia  | Judge       | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 8           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 8           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 8           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 8           | NPC Han  | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 8           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann        |
| 8           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob        |
| 8           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Fae        |
| 8           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Bob        |
| 8           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae        |
| 8           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 8           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Dan         |
| 8           | NPC Han  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia        |
| 8           | NPC Han  | Assassin    | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 8           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 8           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 8           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 8           | NPC Igi  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 8           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann        |
| 8           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob        |
| 8           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Fae        |
| 8           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Bob        |
| 8           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae        |
| 8           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 8           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Dan         |
| 8           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia        |
| 8           | NPC Igi  | Executioner | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 8           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 8           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 8           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 8           | NPC Jeff | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 8           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann        |
| 8           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob        |
| 8           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Fae        |
| 8           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Bob        |
| 8           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae        |
| 8           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 8           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Dan         |
| 8           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia        |
| 8           | NPC Jeff | Jailer      | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 8           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 8           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 8           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 8           | NPC Ken  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 8           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann        |
| 8           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob        |
| 8           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Fae        |
| 8           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Bob        |
| 8           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae        |
| 8           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 8           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Dan         |
| 8           | NPC Ken  | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia        |
| 8           | NPC Ken  | Thief       | vote      | Demagog has initiated a vote on eliminating Prophet            |
| 8           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed   |
| 8           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 8           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 8           | NPC Lee  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed    |
| 8           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Gia is targeting NPC Ann        |
| 8           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob        |
| 8           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Bob is targeting NPC Fae        |
| 8           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ken is targeting NPC Bob        |
| 8           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Fae        |
| 8           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Dan        |
| 8           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Dan         |
| 8           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia        |
| 8           | NPC Lee  | Spy         | reveal    | NPC Gia is targeting NPC Lee                                   |
| 8           | NPC Lee  | Spy         | reveal    | NPC Han is targeting NPC Bob                                   |
| 8           | NPC Lee  | Spy         | reveal    | NPC Bob is targeting NPC Fae                                   |
| 8           | NPC Lee  | Spy         | reveal    | NPC Ken is targeting NPC Bob                                   |
| 8           | NPC Lee  | Spy         | reveal    | NPC Ann is targeting NPC Fae                                   |
| 8           | NPC Lee  | Spy         | reveal    | NPC Igi is targeting NPC Dan                                   |
| 8           | NPC Lee  | Spy         | reveal    | NPC Ed is targeting NPC Dan                                    |
| 8           | NPC Lee  | Spy         | reveal    | NPC Fae is targeting NPC Gia                                   |
| 8           | NPC Lee  | Spy         | vote      | Demagog has initiated a vote on eliminating Prophet            |