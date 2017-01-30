#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 15   | 12      | 9       |

#### Roles
| Role         |
| :----------- |
| Judge        |
| Trader       |
| Psychic      |
| Executioner  |
| Assassin     |
| Thief        |
| Silencer     |
| Jailer       |
| Inspector    |
| Priest       |
| Reporter     |
| Spy          |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Thief       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Ann  | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Bob  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Bob  | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Cal  | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Cal  | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Dan  | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Ed   | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Fae  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Gia  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Trader      | role change | Your Role is Trader       |
| 0           | NPC Han  | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Thief       | role change | Your Role is Thief        |
| 0           | NPC Igi  | Thief       | possessed   | You are Possessed         |
| 0           | NPC Jeff | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Jeff | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ken  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Priest      | role change | Your Role is Priest       |
| 0           | NPC Lee  | Priest      | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player   | action    | Target 1 | Target 2 | status      |
| :-----------| :--------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann  | Assassin  | Thief    |          | successful  |
| 1           | NPC Bob  | Psychic   |          |          | successful  |
| 1           | NPC Cal  | Reporter  | NPC Ken  |          | successful  |
| 1           | NPC Dan  | Spy       |          |          | successful  |
| 1           | NPC Fae  | Inspector | NPC Ann  |          | successful  |
| 1           | NPC Gia  | Judge     | Reporter |          | successful  |
| 1           | NPC Han  | Trader    | NPC Gia  | NPC Bob  | successful  |
| 1           | NPC Igi  | Thief     | NPC Dan  |          | successful  |
| 1           | NPC Jeff | Silencer  | NPC Jeff |          | successful  |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Gia  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Bob  | Judge       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Igi  | Thief       | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Jeff | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Lee  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 1           | NPC Ann  | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Spy is not possessed        |
| 1           | NPC Ann  | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ann  | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed     |
| 1           | NPC Ann  | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Trader is not possessed     |
| 1           | NPC Ann  | Assassin    | broadcast | I (NPC Bob) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed       |
| 1           | NPC Ann  | Assassin    | broadcast | I (NPC Igi) am the Thief and I have made NPC Dan vulnerable    |
| 1           | NPC Bob  | Judge       | broadcast | I (NPC Bob) am the Psychic and the Spy is not possessed        |
| 1           | NPC Bob  | Judge       | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed      |
| 1           | NPC Bob  | Judge       | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed     |
| 1           | NPC Bob  | Judge       | broadcast | I (NPC Bob) am the Psychic and the Trader is not possessed     |
| 1           | NPC Bob  | Judge       | broadcast | I (NPC Bob) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob  | Judge       | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed       |
| 1           | NPC Bob  | Judge       | broadcast | I (NPC Igi) am the Thief and I have made NPC Dan vulnerable    |
| 1           | NPC Bob  | Judge       | reveal    | Player: NPC Ann is not possessed                               |
| 1           | NPC Bob  | Judge       | reveal    | Player: NPC Ken is not possessed                               |
| 1           | NPC Bob  | Judge       | reveal    | Player: NPC Fae is not possessed                               |
| 1           | NPC Bob  | Judge       | reveal    | Player: NPC Cal is not possessed                               |
| 1           | NPC Bob  | Judge       | reveal    | Player: NPC Lee is not possessed                               |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Bob) am the Psychic and the Spy is not possessed        |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed      |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed     |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Bob) am the Psychic and the Trader is not possessed     |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Bob) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed       |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Igi) am the Thief and I have made NPC Dan vulnerable    |
| 1           | NPC Cal  | Reporter    | reveal    | NPC Ken is Executioner                                         |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Bob) am the Psychic and the Spy is not possessed        |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed      |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed     |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Bob) am the Psychic and the Trader is not possessed     |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Bob) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed       |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Igi) am the Thief and I have made NPC Dan vulnerable    |
| 1           | NPC Dan  | Spy         | reveal    | NPC Gia is targeting NPC Cal                                   |
| 1           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Dan                                   |
| 1           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Jeff                                 |
| 1           | NPC Dan  | Spy         | reveal    | NPC Fae is targeting NPC Ann                                   |
| 1           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Ken                                   |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Bob) am the Psychic and the Spy is not possessed        |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed     |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Bob) am the Psychic and the Trader is not possessed     |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Bob) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed       |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Thief and I have made NPC Dan vulnerable    |
| 1           | NPC Fae  | Inspector   | broadcast | I (NPC Bob) am the Psychic and the Spy is not possessed        |
| 1           | NPC Fae  | Inspector   | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed      |
| 1           | NPC Fae  | Inspector   | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed     |
| 1           | NPC Fae  | Inspector   | broadcast | I (NPC Bob) am the Psychic and the Trader is not possessed     |
| 1           | NPC Fae  | Inspector   | broadcast | I (NPC Bob) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Fae  | Inspector   | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed       |
| 1           | NPC Fae  | Inspector   | broadcast | I (NPC Igi) am the Thief and I have made NPC Dan vulnerable    |
| 1           | NPC Fae  | Inspector   | reveal    | Assassin is Innocent                                           |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Spy is not possessed        |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed      |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed     |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Trader is not possessed     |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed       |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Igi) am the Thief and I have made NPC Dan vulnerable    |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Bob) am the Psychic and the Spy is not possessed        |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed      |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed     |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Bob) am the Psychic and the Trader is not possessed     |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Bob) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed       |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Igi) am the Thief and I have made NPC Dan vulnerable    |
| 1           | NPC Igi  | Thief       | broadcast | I (NPC Bob) am the Psychic and the Spy is not possessed        |
| 1           | NPC Igi  | Thief       | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed      |
| 1           | NPC Igi  | Thief       | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed     |
| 1           | NPC Igi  | Thief       | broadcast | I (NPC Bob) am the Psychic and the Trader is not possessed     |
| 1           | NPC Igi  | Thief       | broadcast | I (NPC Bob) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Igi  | Thief       | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed       |
| 1           | NPC Igi  | Thief       | broadcast | I (NPC Igi) am the Thief and I have made NPC Dan vulnerable    |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Bob) am the Psychic and the Spy is not possessed        |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed      |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed     |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Bob) am the Psychic and the Trader is not possessed     |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Bob) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed       |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Igi) am the Thief and I have made NPC Dan vulnerable    |
| 1           | NPC Jeff | Silencer    | silenced  | You have been silenced                                         |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Spy is not possessed        |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed     |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Trader is not possessed     |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Bob) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed       |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Igi) am the Thief and I have made NPC Dan vulnerable    |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Bob) am the Psychic and the Spy is not possessed        |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed      |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Bob) am the Psychic and the Priest is not possessed     |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Bob) am the Psychic and the Trader is not possessed     |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Bob) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed       |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Thief and I have made NPC Dan vulnerable    |

#### Actions Round 2
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 2           | NPC Bob  | Judge    | Silencer |          | successful  |
| 2           | NPC Dan  | Spy      |          |          | successful  |
| 2           | NPC Gia  | Psychic  |          |          | successful  |
| 2           | NPC Jeff | Silencer | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Gia  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Han  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Bob  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Igi  | Thief       | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Jeff | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Lee  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi       |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan       |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff     |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann       |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Ann  | Assassin    | silenced  | You have been silenced                                        |
| 2           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi       |
| 2           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan       |
| 2           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff     |
| 2           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann       |
| 2           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 2           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi       |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan       |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff     |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann       |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi       |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan       |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff     |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann       |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Gia                                  |
| 2           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Gia                                  |
| 2           | NPC Dan  | Spy         | reveal    | NPC Bob is targeting NPC Jeff                                 |
| 2           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Igi                                  |
| 2           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Dan                                  |
| 2           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Ann                                 |
| 2           | NPC Dan  | Spy         | reveal    | NPC Fae is targeting NPC Ann                                  |
| 2           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Ken                                  |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi       |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan       |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff     |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann       |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi       |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan       |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff     |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann       |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi       |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan       |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff     |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann       |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Gia  | Psychic     | reveal    | Player: NPC Ed is not possessed                               |
| 2           | NPC Gia  | Psychic     | reveal    | Player: NPC Cal is not possessed                              |
| 2           | NPC Gia  | Psychic     | reveal    | Player: NPC Ann is not possessed                              |
| 2           | NPC Gia  | Psychic     | reveal    | Player: NPC Han is not possessed                              |
| 2           | NPC Gia  | Psychic     | reveal    | Player: NPC Fae is not possessed                              |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi       |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan       |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff     |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann       |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi       |
| 2           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan       |
| 2           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff     |
| 2           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann       |
| 2           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 2           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi       |
| 2           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan       |
| 2           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff     |
| 2           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann       |
| 2           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 2           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi       |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan       |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff     |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann       |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia       |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi       |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan       |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff     |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann       |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |

#### Actions Round 3
| round_index | Player   | action    | Target 1 | Target 2 | status      |
| :-----------| :--------| :---------| :--------| :--------| :---------- |
| 3           | NPC Ann  | Assassin  | Priest   |          | successful  |
| 3           | NPC Bob  | Judge     | Trader   |          | successful  |
| 3           | NPC Cal  | Reporter  | NPC Jeff |          | successful  |
| 3           | NPC Dan  | Spy       |          |          | successful  |
| 3           | NPC Fae  | Inspector | NPC Han  |          | successful  |
| 3           | NPC Gia  | Psychic   |          |          | successful  |
| 3           | NPC Igi  | Thief     | NPC Bob  |          | successful  |
| 3           | NPC Jeff | Silencer  | NPC Ken  |          | successful  |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Gia  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Han  | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Bob  | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Igi  | Thief       | False      | True      | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Jeff | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Fae  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Lee  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Silencer       |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Jeff       |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan        |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken        |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed       |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ann  | Assassin    | broadcast | I (NPC Igi) am the Thief and I have made NPC Bob vulnerable    |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Silencer       |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Jeff       |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan        |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken        |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed       |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Bob  | Judge       | broadcast | I (NPC Igi) am the Thief and I have made NPC Bob vulnerable    |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Silencer       |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Jeff       |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan        |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken        |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed       |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Cal  | Reporter    | broadcast | I (NPC Igi) am the Thief and I have made NPC Bob vulnerable    |
| 3           | NPC Cal  | Reporter    | reveal    | NPC Jeff is Silencer                                           |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Silencer       |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Jeff       |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan        |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken        |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed       |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Igi) am the Thief and I have made NPC Bob vulnerable    |
| 3           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Gia                                   |
| 3           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Gia                                   |
| 3           | NPC Dan  | Spy         | reveal    | NPC Bob is targeting NPC Han                                   |
| 3           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Igi                                   |
| 3           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Bob                                   |
| 3           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Ken                                  |
| 3           | NPC Dan  | Spy         | reveal    | NPC Fae is targeting NPC Han                                   |
| 3           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Jeff                                  |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Silencer       |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Jeff       |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan        |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken        |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed       |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Thief and I have made NPC Bob vulnerable    |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Silencer       |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Jeff       |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan        |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken        |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed       |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Fae  | Inspector   | broadcast | I (NPC Igi) am the Thief and I have made NPC Bob vulnerable    |
| 3           | NPC Fae  | Inspector   | reveal    | Trader is Innocent                                             |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Silencer       |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Jeff       |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan        |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken        |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed       |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Igi) am the Thief and I have made NPC Bob vulnerable    |
| 3           | NPC Gia  | Psychic     | reveal    | Player: NPC Fae is not possessed                               |
| 3           | NPC Gia  | Psychic     | reveal    | Player: NPC Ed is not possessed                                |
| 3           | NPC Gia  | Psychic     | reveal    | Player: NPC Han is not possessed                               |
| 3           | NPC Gia  | Psychic     | reveal    | Player: NPC Lee is not possessed                               |
| 3           | NPC Gia  | Psychic     | reveal    | Player: NPC Jeff is not possessed                              |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Silencer       |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Jeff       |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan        |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken        |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed       |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Igi) am the Thief and I have made NPC Bob vulnerable    |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Silencer       |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Jeff       |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan        |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken        |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed       |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Igi  | Thief       | broadcast | I (NPC Igi) am the Thief and I have made NPC Bob vulnerable    |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Silencer       |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Jeff       |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan        |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken        |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed       |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Jeff | Silencer    | broadcast | I (NPC Igi) am the Thief and I have made NPC Bob vulnerable    |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Silencer       |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Jeff       |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan        |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken        |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed       |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ken  | Executioner | broadcast | I (NPC Igi) am the Thief and I have made NPC Bob vulnerable    |
| 3           | NPC Ken  | Executioner | silenced  | You have been silenced                                         |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Cal) am the Reporter and NPC Jeff is the Silencer       |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Jeff       |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi        |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan        |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken        |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed       |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Thief and I have made NPC Bob vulnerable    |

#### Actions Round 4
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 4           | NPC Bob  | Judge    | Psychic  |          | successful  |
| 4           | NPC Dan  | Spy      |          |          | successful  |
| 4           | NPC Gia  | Psychic  |          |          | successful  |
| 4           | NPC Jeff | Silencer | NPC Lee  |          | successful  |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Gia  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Han  | Trader      | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Bob  | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Igi  | Thief       | False      | True      | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Jeff | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Lee  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Cal  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Han          |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ken         |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed       |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Han          |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ken         |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed       |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Han          |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ken         |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed       |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Han          |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ken         |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed       |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Gia                                     |
| 4           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Gia                                     |
| 4           | NPC Dan  | Spy         | reveal    | NPC Bob is targeting NPC Gia                                     |
| 4           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Lee                                     |
| 4           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Bob                                     |
| 4           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Lee                                    |
| 4           | NPC Dan  | Spy         | reveal    | NPC Fae is targeting NPC Han                                     |
| 4           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Jeff                                    |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Han          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ken         |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed       |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Han          |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ken         |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed       |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Fae  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Han          |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ken         |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed       |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Gia  | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 4           | NPC Gia  | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 4           | NPC Gia  | Psychic     | reveal    | Player: NPC Ken is not possessed                                 |
| 4           | NPC Gia  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 4           | NPC Gia  | Psychic     | reveal    | Player: NPC Han is not possessed                                 |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Han          |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ken         |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed       |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Han          |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ken         |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed       |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Han          |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ken         |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed       |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Han          |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ken         |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed       |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Han          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ken         |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed       |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Lee  | Priest      | silenced  | You have been silenced                                           |

#### Actions Round 5
| round_index | Player   | action    | Target 1 | Target 2 | status      |
| :-----------| :--------| :---------| :--------| :--------| :---------- |
| 5           | NPC Ann  | Assassin  | Judge    |          | successful  |
| 5           | NPC Bob  | Judge     | Assassin |          | successful  |
| 5           | NPC Cal  | Reporter  | NPC Bob  |          | successful  |
| 5           | NPC Dan  | Spy       |          |          | successful  |
| 5           | NPC Fae  | Inspector | NPC Jeff |          | successful  |
| 5           | NPC Gia  | Psychic   |          |          | successful  |
| 5           | NPC Han  | Trader    | NPC Ed   | NPC Fae  | successful  |
| 5           | NPC Igi  | Thief     | NPC Cal  |          | successful  |
| 5           | NPC Jeff | Silencer  | NPC Dan  |          | successful  |

#### States Round 5
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Gia  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Han  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 5           | NPC Bob  | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ann  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Igi  | Thief       | False      | True      | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Jeff | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Ed   | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Fae  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Lee  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Cal  | Reporter    | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Dan  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia          |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Lee         |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Fae) inspected NPC Jeff and they are not possessed        |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 5           | NPC Ann  | Assassin    | broadcast | I (NPC Igi) am the Thief and I have made NPC Cal vulnerable      |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia          |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Lee         |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Fae) inspected NPC Jeff and they are not possessed        |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 5           | NPC Bob  | Judge       | broadcast | I (NPC Igi) am the Thief and I have made NPC Cal vulnerable      |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia          |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Lee         |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Fae) inspected NPC Jeff and they are not possessed        |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 5           | NPC Cal  | Reporter    | broadcast | I (NPC Igi) am the Thief and I have made NPC Cal vulnerable      |
| 5           | NPC Cal  | Reporter    | reveal    | NPC Bob is Judge                                                 |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia          |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Lee         |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Fae) inspected NPC Jeff and they are not possessed        |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Igi) am the Thief and I have made NPC Cal vulnerable      |
| 5           | NPC Dan  | Spy         | silenced  | You have been silenced                                           |
| 5           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Gia                                     |
| 5           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Gia                                     |
| 5           | NPC Dan  | Spy         | reveal    | NPC Bob is targeting NPC Ann                                     |
| 5           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Lee                                     |
| 5           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Cal                                     |
| 5           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Dan                                    |
| 5           | NPC Dan  | Spy         | reveal    | NPC Fae is targeting NPC Jeff                                    |
| 5           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Bob                                     |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia          |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Lee         |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Fae) inspected NPC Jeff and they are not possessed        |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 5           | NPC Ed   | Inspector   | broadcast | I (NPC Igi) am the Thief and I have made NPC Cal vulnerable      |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia          |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Lee         |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Fae) inspected NPC Jeff and they are not possessed        |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 5           | NPC Fae  | Jailer      | broadcast | I (NPC Igi) am the Thief and I have made NPC Cal vulnerable      |
| 5           | NPC Fae  | Jailer      | reveal    | Silencer is Innocent                                             |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia          |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Lee         |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Fae) inspected NPC Jeff and they are not possessed        |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Igi) am the Thief and I have made NPC Cal vulnerable      |
| 5           | NPC Gia  | Psychic     | reveal    | Player: NPC Han is not possessed                                 |
| 5           | NPC Gia  | Psychic     | reveal    | Player: NPC Ann is not possessed                                 |
| 5           | NPC Gia  | Psychic     | reveal    | Player: NPC Cal is not possessed                                 |
| 5           | NPC Gia  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 5           | NPC Gia  | Psychic     | reveal    | Player: NPC Ken is not possessed                                 |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia          |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Lee         |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Fae) inspected NPC Jeff and they are not possessed        |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 5           | NPC Han  | Trader      | broadcast | I (NPC Igi) am the Thief and I have made NPC Cal vulnerable      |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia          |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Lee         |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Fae) inspected NPC Jeff and they are not possessed        |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 5           | NPC Igi  | Thief       | broadcast | I (NPC Igi) am the Thief and I have made NPC Cal vulnerable      |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia          |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Lee         |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Fae) inspected NPC Jeff and they are not possessed        |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 5           | NPC Jeff | Silencer    | broadcast | I (NPC Igi) am the Thief and I have made NPC Cal vulnerable      |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia          |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Lee         |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Fae) inspected NPC Jeff and they are not possessed        |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Igi) am the Thief and I have made NPC Cal vulnerable      |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia          |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Lee         |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Fae is targeting NPC Han          |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Jeff         |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Fae) inspected NPC Jeff and they are not possessed        |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed          |
| 5           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Thief and I have made NPC Cal vulnerable      |

#### Actions Round 6
| round_index | Player   | action    | Target 1  | Target 2 | status      |
| :-----------| :--------| :---------| :---------| :--------| :---------- |
| 6           | NPC Bob  | Judge     | Inspector |          | successful  |
| 6           | NPC Dan  | Spy       |           |          | successful  |
| 6           | NPC Ed   | Inspector | NPC Fae   |          | successful  |
| 6           | NPC Gia  | Psychic   |           |          | successful  |
| 6           | NPC Jeff | Silencer  | NPC Jeff  |          | successful  |

#### States Round 6
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Gia  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Han  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 6           | NPC Bob  | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ann  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Igi  | Thief       | False      | True      | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Jeff | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ed   | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Fae  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Lee  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Cal  | Reporter    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Dan  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 6           | NPC Ann  | Assassin    | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed       |
| 6           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 6           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 6           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 6           | NPC Bob  | Judge       | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed       |
| 6           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 6           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 6           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 6           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed       |
| 6           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 6           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 6           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed       |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 6           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Ed                                   |
| 6           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Ed                                   |
| 6           | NPC Dan  | Spy         | reveal    | NPC Bob is targeting NPC Ed                                   |
| 6           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Bob                                  |
| 6           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Cal                                  |
| 6           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Jeff                                |
| 6           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Fae                                   |
| 6           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Bob                                  |
| 6           | NPC Ed   | Inspector   | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed       |
| 6           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 6           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 6           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 6           | NPC Ed   | Inspector   | reveal    | Jailer is Innocent                                            |
| 6           | NPC Fae  | Jailer      | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed       |
| 6           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 6           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 6           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed       |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 6           | NPC Gia  | Psychic     | reveal    | Player: NPC Lee is not possessed                              |
| 6           | NPC Gia  | Psychic     | reveal    | Player: NPC Han is not possessed                              |
| 6           | NPC Gia  | Psychic     | reveal    | Player: NPC Cal is not possessed                              |
| 6           | NPC Gia  | Psychic     | reveal    | Player: NPC Fae is not possessed                              |
| 6           | NPC Gia  | Psychic     | reveal    | Player: NPC Ann is not possessed                              |
| 6           | NPC Han  | Trader      | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed       |
| 6           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 6           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 6           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 6           | NPC Igi  | Thief       | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed       |
| 6           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 6           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 6           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 6           | NPC Jeff | Silencer    | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed       |
| 6           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 6           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 6           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 6           | NPC Jeff | Silencer    | silenced  | You have been silenced                                        |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed       |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 6           | NPC Lee  | Priest      | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed       |
| 6           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 6           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 6           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |

#### Actions Round 7
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 7           | NPC Ann  | Assassin | Thief    |          | successful  |
| 7           | NPC Bob  | Judge    | Psychic  |          | successful  |
| 7           | NPC Cal  | Reporter | NPC Igi  |          | successful  |
| 7           | NPC Dan  | Spy      |          |          | successful  |
| 7           | NPC Gia  | Psychic  |          |          | successful  |
| 7           | NPC Igi  | Thief    | NPC Lee  |          | successful  |
| 7           | NPC Jeff | Silencer | NPC Gia  |          | successful  |

#### States Round 7
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Gia  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Han  | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Bob  | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Ann  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Igi  | Thief       | False      | True      | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Jeff | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Ed   | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Fae  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Lee  | Priest      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Cal  | Reporter    | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Dan  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Cal) am the Reporter and NPC Igi is the Thief             |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ed           |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Bob          |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal          |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff        |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae           |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob          |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed     |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 7           | NPC Ann  | Assassin    | broadcast | I (NPC Igi) am the Thief and I have made NPC Lee vulnerable      |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Cal) am the Reporter and NPC Igi is the Thief             |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ed           |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Bob          |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal          |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff        |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae           |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob          |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed     |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 7           | NPC Bob  | Judge       | broadcast | I (NPC Igi) am the Thief and I have made NPC Lee vulnerable      |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Cal) am the Reporter and NPC Igi is the Thief             |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ed           |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Bob          |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal          |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff        |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae           |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob          |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed     |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 7           | NPC Cal  | Reporter    | broadcast | I (NPC Igi) am the Thief and I have made NPC Lee vulnerable      |
| 7           | NPC Cal  | Reporter    | reveal    | NPC Igi is Thief                                                 |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Cal) am the Reporter and NPC Igi is the Thief             |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ed           |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Bob          |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal          |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff        |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae           |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob          |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed     |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Igi) am the Thief and I have made NPC Lee vulnerable      |
| 7           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Ed                                      |
| 7           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Ed                                      |
| 7           | NPC Dan  | Spy         | reveal    | NPC Bob is targeting NPC Gia                                     |
| 7           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Bob                                     |
| 7           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Lee                                     |
| 7           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Gia                                    |
| 7           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Fae                                      |
| 7           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Igi                                     |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Cal) am the Reporter and NPC Igi is the Thief             |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ed           |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Bob          |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal          |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff        |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae           |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob          |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed     |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 7           | NPC Ed   | Inspector   | broadcast | I (NPC Igi) am the Thief and I have made NPC Lee vulnerable      |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Cal) am the Reporter and NPC Igi is the Thief             |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ed           |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Bob          |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal          |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff        |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae           |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob          |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed     |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 7           | NPC Fae  | Jailer      | broadcast | I (NPC Igi) am the Thief and I have made NPC Lee vulnerable      |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Cal) am the Reporter and NPC Igi is the Thief             |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ed           |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Bob          |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal          |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff        |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae           |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob          |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed     |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 7           | NPC Gia  | Psychic     | broadcast | I (NPC Igi) am the Thief and I have made NPC Lee vulnerable      |
| 7           | NPC Gia  | Psychic     | silenced  | You have been silenced                                           |
| 7           | NPC Gia  | Psychic     | reveal    | Player: NPC Lee is not possessed                                 |
| 7           | NPC Gia  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 7           | NPC Gia  | Psychic     | reveal    | Player: NPC Han is not possessed                                 |
| 7           | NPC Gia  | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 7           | NPC Gia  | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Cal) am the Reporter and NPC Igi is the Thief             |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ed           |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Bob          |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal          |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff        |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae           |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob          |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed     |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 7           | NPC Han  | Trader      | broadcast | I (NPC Igi) am the Thief and I have made NPC Lee vulnerable      |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Cal) am the Reporter and NPC Igi is the Thief             |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ed           |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Bob          |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal          |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff        |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae           |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob          |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed     |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 7           | NPC Igi  | Thief       | broadcast | I (NPC Igi) am the Thief and I have made NPC Lee vulnerable      |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Cal) am the Reporter and NPC Igi is the Thief             |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ed           |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Bob          |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal          |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff        |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae           |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob          |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed     |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 7           | NPC Jeff | Silencer    | broadcast | I (NPC Igi) am the Thief and I have made NPC Lee vulnerable      |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Cal) am the Reporter and NPC Igi is the Thief             |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ed           |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Bob          |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal          |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff        |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae           |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob          |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed     |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 7           | NPC Ken  | Executioner | broadcast | I (NPC Igi) am the Thief and I have made NPC Lee vulnerable      |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Cal) am the Reporter and NPC Igi is the Thief             |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ed           |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Bob          |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal          |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Jeff        |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae           |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob          |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed     |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 7           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Thief and I have made NPC Lee vulnerable      |

#### Actions Round 8
| round_index | Player   | action    | Target 1 | Target 2 | status      |
| :-----------| :--------| :---------| :--------| :--------| :---------- |
| 8           | NPC Bob  | Judge     | Assassin |          | successful  |
| 8           | NPC Dan  | Spy       |          |          | successful  |
| 8           | NPC Ed   | Inspector | NPC Jeff |          | successful  |
| 8           | NPC Gia  | Psychic   |          |          | successful  |
| 8           | NPC Jeff | Silencer  | NPC Ann  |          | successful  |

#### States Round 8
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Gia  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Han  | Trader      | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Bob  | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Ann  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Igi  | Thief       | False      | True      | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Jeff | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Ed   | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 8           | NPC Fae  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Lee  | Priest      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Cal  | Reporter    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 8           | NPC Dan  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player   | Role        | message   | details                                                   |
| :-----------| :--------| :-----------| :---------| :-------------------------------------------------------- |
| 8           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia   |
| 8           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi   |
| 8           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee   |
| 8           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Gia  |
| 8           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae    |
| 8           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi   |
| 8           | NPC Ann  | Assassin    | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 8           | NPC Ann  | Assassin    | silenced  | You have been silenced                                    |
| 8           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia   |
| 8           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi   |
| 8           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee   |
| 8           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Gia  |
| 8           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae    |
| 8           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi   |
| 8           | NPC Bob  | Judge       | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 8           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia   |
| 8           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi   |
| 8           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee   |
| 8           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Gia  |
| 8           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae    |
| 8           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi   |
| 8           | NPC Cal  | Reporter    | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 8           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia   |
| 8           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi   |
| 8           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee   |
| 8           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Gia  |
| 8           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae    |
| 8           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi   |
| 8           | NPC Dan  | Spy         | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 8           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Ed                               |
| 8           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Ed                               |
| 8           | NPC Dan  | Spy         | reveal    | NPC Bob is targeting NPC Ann                              |
| 8           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Igi                              |
| 8           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Lee                              |
| 8           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Ann                             |
| 8           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Jeff                              |
| 8           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Igi                              |
| 8           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia   |
| 8           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi   |
| 8           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee   |
| 8           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Gia  |
| 8           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae    |
| 8           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi   |
| 8           | NPC Ed   | Inspector   | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 8           | NPC Ed   | Inspector   | reveal    | Silencer is Innocent                                      |
| 8           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia   |
| 8           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi   |
| 8           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee   |
| 8           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Gia  |
| 8           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae    |
| 8           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi   |
| 8           | NPC Fae  | Jailer      | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 8           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia   |
| 8           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi   |
| 8           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee   |
| 8           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Gia  |
| 8           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae    |
| 8           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi   |
| 8           | NPC Gia  | Psychic     | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 8           | NPC Gia  | Psychic     | reveal    | Player: NPC Fae is not possessed                          |
| 8           | NPC Gia  | Psychic     | reveal    | Player: NPC Han is not possessed                          |
| 8           | NPC Gia  | Psychic     | reveal    | Player: NPC Bob is not possessed                          |
| 8           | NPC Gia  | Psychic     | reveal    | Player: NPC Cal is not possessed                          |
| 8           | NPC Gia  | Psychic     | reveal    | Player: NPC Lee is not possessed                          |
| 8           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia   |
| 8           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi   |
| 8           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee   |
| 8           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Gia  |
| 8           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae    |
| 8           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi   |
| 8           | NPC Han  | Trader      | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 8           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia   |
| 8           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi   |
| 8           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee   |
| 8           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Gia  |
| 8           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae    |
| 8           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi   |
| 8           | NPC Igi  | Thief       | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 8           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia   |
| 8           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi   |
| 8           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee   |
| 8           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Gia  |
| 8           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae    |
| 8           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi   |
| 8           | NPC Jeff | Silencer    | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 8           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia   |
| 8           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi   |
| 8           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee   |
| 8           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Gia  |
| 8           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae    |
| 8           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi   |
| 8           | NPC Ken  | Executioner | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 8           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed    |
| 8           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Gia   |
| 8           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi   |
| 8           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee   |
| 8           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Gia  |
| 8           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae    |
| 8           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi   |
| 8           | NPC Lee  | Priest      | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |

#### Actions Round 9
| round_index | Player   | action   | Target 1 | Target 2 | status                         |
| :-----------| :--------| :--------| :--------| :--------| :----------------------------- |
| 9           | NPC Ann  | Assassin | Reporter |          | successful                     |
| 9           | NPC Bob  | Judge    | Thief    |          | successful                     |
| 9           | NPC Cal  | Reporter | NPC Gia  |          | successful                     |
| 9           | NPC Dan  | Spy      |          |          | successful                     |
| 9           | NPC Gia  | Psychic  |          |          | successful                     |
| 9           | NPC Han  | Trader   | NPC Igi  | NPC Ann  | failed because not vulnerable  |
| 9           | NPC Igi  | Thief    | NPC Ken  |          | successful                     |
| 9           | NPC Jeff | Silencer | NPC Ann  |          | successful                     |

#### States Round 9
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 9           | NPC Gia  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 9           | NPC Han  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 9           | NPC Bob  | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Ken  | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Ann  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 9           | NPC Igi  | Thief       | False      | True      | False      | 2         | True   | 0              | 0                  |
| 9           | NPC Jeff | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 9           | NPC Ed   | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 9           | NPC Fae  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Lee  | Priest      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Cal  | Reporter    | False      | False     | True       | 2         | True   | 0              | 0                  |
| 9           | NPC Dan  | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 9
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Psychic           |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ann          |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi          |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee          |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Jeff          |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi          |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 9           | NPC Ann  | Assassin    | broadcast | I (NPC Igi) am the Thief and I have made NPC Ken vulnerable      |
| 9           | NPC Ann  | Assassin    | silenced  | You have been silenced                                           |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Psychic           |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ann          |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi          |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee          |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Jeff          |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi          |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 9           | NPC Bob  | Judge       | broadcast | I (NPC Igi) am the Thief and I have made NPC Ken vulnerable      |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Psychic           |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ann          |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi          |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee          |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Jeff          |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi          |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 9           | NPC Cal  | Reporter    | broadcast | I (NPC Igi) am the Thief and I have made NPC Ken vulnerable      |
| 9           | NPC Cal  | Reporter    | reveal    | NPC Gia is Psychic                                               |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Psychic           |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ann          |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi          |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee          |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Jeff          |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi          |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 9           | NPC Dan  | Spy         | broadcast | I (NPC Igi) am the Thief and I have made NPC Ken vulnerable      |
| 9           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Ed                                      |
| 9           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Ed                                      |
| 9           | NPC Dan  | Spy         | reveal    | NPC Bob is targeting NPC Igi                                     |
| 9           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Igi                                     |
| 9           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Ken                                     |
| 9           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Ann                                    |
| 9           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Jeff                                     |
| 9           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Gia                                     |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Psychic           |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ann          |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi          |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee          |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Jeff          |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi          |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 9           | NPC Ed   | Inspector   | broadcast | I (NPC Igi) am the Thief and I have made NPC Ken vulnerable      |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Psychic           |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ann          |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi          |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee          |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Jeff          |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi          |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 9           | NPC Fae  | Jailer      | broadcast | I (NPC Igi) am the Thief and I have made NPC Ken vulnerable      |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Psychic           |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ann          |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi          |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee          |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Jeff          |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi          |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 9           | NPC Gia  | Psychic     | broadcast | I (NPC Igi) am the Thief and I have made NPC Ken vulnerable      |
| 9           | NPC Gia  | Psychic     | reveal    | Player: NPC Lee is not possessed                                 |
| 9           | NPC Gia  | Psychic     | reveal    | Player: NPC Ken is not possessed                                 |
| 9           | NPC Gia  | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 9           | NPC Gia  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 9           | NPC Gia  | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Psychic           |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ann          |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi          |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee          |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Jeff          |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi          |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 9           | NPC Han  | Trader      | broadcast | I (NPC Igi) am the Thief and I have made NPC Ken vulnerable      |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Psychic           |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ann          |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi          |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee          |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Jeff          |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi          |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 9           | NPC Igi  | Thief       | broadcast | I (NPC Igi) am the Thief and I have made NPC Ken vulnerable      |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Psychic           |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ann          |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi          |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee          |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Jeff          |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi          |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 9           | NPC Jeff | Silencer    | broadcast | I (NPC Igi) am the Thief and I have made NPC Ken vulnerable      |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Psychic           |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ann          |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi          |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee          |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Jeff          |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi          |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 9           | NPC Ken  | Executioner | broadcast | I (NPC Igi) am the Thief and I have made NPC Ken vulnerable      |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Psychic           |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ed           |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Ann          |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Igi          |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Lee          |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Jeff          |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Igi          |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed     |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed    |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed       |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Executioner is not possessed  |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed     |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed        |
| 9           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Thief and I have made NPC Ken vulnerable      |