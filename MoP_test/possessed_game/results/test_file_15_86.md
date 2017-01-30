#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 86   | 15      | 7       |

#### Roles
| Role         |
| :----------- |
| Judge        |
| Spy          |
| Psychic      |
| Thief        |
| Jailer       |
| Executioner  |
| Demagog      |
| Priest       |
| Inspector    |
| Prophet      |
| Reporter     |
| Silencer     |
| Assassin     |
| Trader       |
| Medic        |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Mark | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Norm | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ozie | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Ann  | Medic       | possessed   | You are Possessed         |
| 0           | NPC Bob  | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Bob  | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Cal  | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Cal  | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Dan  | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Trader      | role change | Your Role is Trader       |
| 0           | NPC Ed   | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Fae  | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Gia  | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Thief       | role change | Your Role is Thief        |
| 0           | NPC Han  | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Igi  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Jeff | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Priest      | role change | Your Role is Priest       |
| 0           | NPC Ken  | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Lee  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Mark | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Mark | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Norm | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Norm | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Ozie | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Ozie | Silencer    | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player   | action    | Target 1  | Target 2 | status                         |
| :-----------| :--------| :---------| :---------| :--------| :----------------------------- |
| 1           | NPC Ann  | Medic     | NPC Dan   |          | successful                     |
| 1           | NPC Cal  | Assassin  | Trader    |          | successful                     |
| 1           | NPC Dan  | Spy       |           |          | successful                     |
| 1           | NPC Ed   | Trader    | NPC Cal   | NPC Jeff | failed because not vulnerable  |
| 1           | NPC Fae  | Psychic   |           |          | successful                     |
| 1           | NPC Gia  | Demagog   | Inspector |          | voting in progress             |
| 1           | NPC Han  | Thief     | NPC Gia   |          | successful                     |
| 1           | NPC Igi  | Judge     | Prophet   |          | successful                     |
| 1           | NPC Jeff | Reporter  | NPC Ann   |          | successful                     |
| 1           | NPC Mark | Inspector | NPC Jeff  |          | successful                     |
| 1           | NPC Norm | Prophet   | NPC Lee   |          | successful                     |
| 1           | NPC Ozie | Silencer  | NPC Cal   |          | successful                     |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Han  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia  | Demagog     | False      | False     | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Ken  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Mark | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Norm | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Jeff | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ozie | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Cal  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed   | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Ann  | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Ann  | Medic       | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Bob  | Jailer      | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Cal  | Assassin    | silenced  | You have been silenced                                           |
| 1           | NPC Cal  | Assassin    | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Dan  | Spy         | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Norm                                    |
| 1           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Gia                                     |
| 1           | NPC Dan  | Spy         | reveal    | NPC Mark is targeting NPC Jeff                                   |
| 1           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Ann                                    |
| 1           | NPC Dan  | Spy         | reveal    | NPC Ozie is targeting NPC Cal                                    |
| 1           | NPC Dan  | Spy         | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Ed   | Trader      | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Ed   | Trader      | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Ed   | Trader      | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Ed   | Trader      | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Fae  | Psychic     | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Fae  | Psychic     | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Fae  | Psychic     | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Fae  | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 1           | NPC Fae  | Psychic     | reveal    | Player: NPC Ozie is not possessed                                |
| 1           | NPC Fae  | Psychic     | reveal    | Player: NPC Han is not possessed                                 |
| 1           | NPC Fae  | Psychic     | reveal    | Player: NPC Mark is not possessed                                |
| 1           | NPC Fae  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 1           | NPC Fae  | Psychic     | reveal    | Player: NPC Norm is not possessed                                |
| 1           | NPC Fae  | Psychic     | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Gia  | Demagog     | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Gia  | Demagog     | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Gia  | Demagog     | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Gia  | Demagog     | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Han  | Thief       | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Igi  | Judge       | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Jeff | Reporter    | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Jeff | Reporter    | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Jeff | Reporter    | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Jeff | Reporter    | reveal    | NPC Ann is Medic                                                 |
| 1           | NPC Jeff | Reporter    | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Ken  | Priest      | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Ken  | Priest      | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Ken  | Priest      | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Ken  | Priest      | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Lee  | Executioner | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Mark | Inspector   | reveal    | Reporter is Innocent                                             |
| 1           | NPC Mark | Inspector   | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Norm | Prophet     | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Norm | Prophet     | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Norm | Prophet     | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Norm | Prophet     | vote      | Demagog has initiated a vote on eliminating Inspector            |
| 1           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 1           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 1           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed        |
| 1           | NPC Ozie | Silencer    | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Ozie | Silencer    | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic            |
| 1           | NPC Ozie | Silencer    | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed       |
| 1           | NPC Ozie | Silencer    | vote      | Demagog has initiated a vote on eliminating Inspector            |

#### Actions Round 2
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 2           | NPC Ann  | Medic    | NPC Fae  |          | successful  |
| 2           | NPC Dan  | Spy      |          |          | successful  |
| 2           | NPC Fae  | Psychic  |          |          | successful  |
| 2           | NPC Igi  | Judge    | Trader   |          | successful  |
| 2           | NPC Norm | Prophet  | NPC Bob  |          | successful  |
| 2           | NPC Ozie | Silencer | NPC Gia  |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Bob  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Gia  | Demagog     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Ken  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Mark | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Norm | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Jeff | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ozie | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed   | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Ann  | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Ed                                      |
| 2           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Gia                                     |
| 2           | NPC Dan  | Spy         | reveal    | NPC Gia is targeting NPC Mark                                    |
| 2           | NPC Dan  | Spy         | reveal    | NPC Mark is targeting NPC Jeff                                   |
| 2           | NPC Dan  | Spy         | reveal    | NPC Norm is targeting NPC Lee                                    |
| 2           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Ann                                    |
| 2           | NPC Dan  | Spy         | reveal    | NPC Ozie is targeting NPC Gia                                    |
| 2           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Ed                                      |
| 2           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Cal                                      |
| 2           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Cal                                      |
| 2           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Dan                                     |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Fae  | Psychic     | reveal    | Player: NPC Lee is not possessed                                 |
| 2           | NPC Fae  | Psychic     | reveal    | Player: NPC Gia is not possessed                                 |
| 2           | NPC Fae  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 2           | NPC Fae  | Psychic     | reveal    | Player: NPC Norm is not possessed                                |
| 2           | NPC Fae  | Psychic     | reveal    | Player: NPC Cal is not possessed                                 |
| 2           | NPC Fae  | Psychic     | reveal    | Player: NPC Igi is not possessed                                 |
| 2           | NPC Fae  | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Gia  | Demagog     | silenced  | You have been silenced                                           |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia          |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark         |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff        |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann         |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Cal         |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed           |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal           |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Dan          |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed        |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |

#### Actions Round 3
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 3           | NPC Ann  | Medic     | NPC Han  |          | successful          |
| 3           | NPC Cal  | Assassin  | Priest   |          | successful          |
| 3           | NPC Dan  | Spy       |          |          | successful          |
| 3           | NPC Fae  | Psychic   |          |          | successful          |
| 3           | NPC Gia  | Demagog   | Jailer   |          | voting in progress  |
| 3           | NPC Han  | Thief     | NPC Jeff |          | successful          |
| 3           | NPC Igi  | Judge     | Demagog  |          | successful          |
| 3           | NPC Jeff | Reporter  | NPC Bob  |          | successful          |
| 3           | NPC Mark | Inspector | NPC Jeff |          | successful          |
| 3           | NPC Norm | Prophet   | NPC Jeff |          | successful          |
| 3           | NPC Ozie | Silencer  | NPC Mark |          | successful          |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Fae  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Han  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Gia  | Demagog     | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Ken  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Mark | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Norm | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Jeff | Reporter    | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Ozie | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Cal  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ed   | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann  | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Ann  | Medic       | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Ann  | Medic       | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Bob  | Jailer      | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Cal  | Assassin    | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Dan  | Spy         | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Gia                                   |
| 3           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Jeff                                  |
| 3           | NPC Dan  | Spy         | reveal    | NPC Gia is targeting NPC Mark                                  |
| 3           | NPC Dan  | Spy         | reveal    | NPC Mark is targeting NPC Jeff                                 |
| 3           | NPC Dan  | Spy         | reveal    | NPC Norm is targeting NPC Bob                                  |
| 3           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Bob                                  |
| 3           | NPC Dan  | Spy         | reveal    | NPC Ozie is targeting NPC Mark                                 |
| 3           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Ed                                    |
| 3           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Cal                                    |
| 3           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Cal                                    |
| 3           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Fae                                   |
| 3           | NPC Dan  | Spy         | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Ed   | Trader      | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Ed   | Trader      | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Fae  | Psychic     | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Fae  | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 3           | NPC Fae  | Psychic     | reveal    | Player: NPC Han is not possessed                               |
| 3           | NPC Fae  | Psychic     | reveal    | Player: NPC Igi is not possessed                               |
| 3           | NPC Fae  | Psychic     | reveal    | Player: NPC Mark is not possessed                              |
| 3           | NPC Fae  | Psychic     | reveal    | Player: NPC Ken is not possessed                               |
| 3           | NPC Fae  | Psychic     | reveal    | Player: NPC Dan is not possessed                               |
| 3           | NPC Fae  | Psychic     | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Gia  | Demagog     | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Gia  | Demagog     | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Han  | Thief       | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Han  | Thief       | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Igi  | Judge       | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Jeff | Reporter    | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Jeff | Reporter    | reveal    | NPC Bob is Jailer                                              |
| 3           | NPC Jeff | Reporter    | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Ken  | Priest      | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Ken  | Priest      | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Lee  | Executioner | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Lee  | Executioner | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Mark | Inspector   | reveal    | Reporter is Innocent                                           |
| 3           | NPC Mark | Inspector   | silenced  | You have been silenced                                         |
| 3           | NPC Mark | Inspector   | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Norm | Prophet     | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Norm | Prophet     | vote      | Demagog has initiated a vote on eliminating Jailer             |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed         |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Gia        |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Mark       |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff      |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Bob       |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Gia       |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ed         |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal         |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed      |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed        |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Han) am the Thief and I have made NPC Jeff vulnerable   |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Jeff) am the Reporter and NPC Bob is the Jailer         |
| 3           | NPC Ozie | Silencer    | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed     |
| 3           | NPC Ozie | Silencer    | vote      | Demagog has initiated a vote on eliminating Jailer             |

#### Actions Round 4
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 4           | NPC Ann  | Medic    | NPC Bob  |          | successful  |
| 4           | NPC Dan  | Spy      |          |          | successful  |
| 4           | NPC Fae  | Psychic  |          |          | successful  |
| 4           | NPC Han  | Thief    | NPC Mark |          | successful  |
| 4           | NPC Igi  | Judge    | Demagog  |          | successful  |
| 4           | NPC Norm | Prophet  | NPC Ed   |          | successful  |
| 4           | NPC Ozie | Silencer | NPC Dan  |          | successful  |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Han  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Bob  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Gia  | Demagog     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Ken  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Mark | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Norm | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Jeff | Reporter    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Ozie | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Cal  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed   | Trader      | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann  | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Ann  | Medic       | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Dan  | Spy         | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Dan  | Spy         | silenced  | You have been silenced                                        |
| 4           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Gia                                  |
| 4           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Mark                                 |
| 4           | NPC Dan  | Spy         | reveal    | NPC Gia is targeting NPC Bob                                  |
| 4           | NPC Dan  | Spy         | reveal    | NPC Mark is targeting NPC Jeff                                |
| 4           | NPC Dan  | Spy         | reveal    | NPC Norm is targeting NPC Jeff                                |
| 4           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Bob                                 |
| 4           | NPC Dan  | Spy         | reveal    | NPC Ozie is targeting NPC Dan                                 |
| 4           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Ken                                  |
| 4           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Cal                                   |
| 4           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Cal                                   |
| 4           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Han                                  |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Ed   | Trader      | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Fae  | Psychic     | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Fae  | Psychic     | reveal    | Player: NPC Cal is not possessed                              |
| 4           | NPC Fae  | Psychic     | reveal    | Player: NPC Bob is not possessed                              |
| 4           | NPC Fae  | Psychic     | reveal    | Player: NPC Mark is not possessed                             |
| 4           | NPC Fae  | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 4           | NPC Fae  | Psychic     | reveal    | Player: NPC Ozie is not possessed                             |
| 4           | NPC Fae  | Psychic     | reveal    | Player: NPC Han is not possessed                              |
| 4           | NPC Fae  | Psychic     | reveal    | Player: NPC Lee is not possessed                              |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Gia  | Demagog     | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Han  | Thief       | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Jeff | Reporter    | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Ken  | Priest      | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Lee  | Executioner | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Norm | Prophet     | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Gia       |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Jeff      |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob       |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Jeff     |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Jeff     |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Bob      |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Mark     |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ken       |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal        |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Han       |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Judge is not possessed     |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Ozie | Silencer    | broadcast | I (NPC Han) am the Thief and I have made NPC Mark vulnerable  |

#### Actions Round 5
| round_index | Player   | action    | Target 1    | Target 2 | status                         |
| :-----------| :--------| :---------| :-----------| :--------| :----------------------------- |
| 5           | NPC Ann  | Medic     | NPC Lee     |          | successful                     |
| 5           | NPC Cal  | Assassin  | Spy         |          | successful                     |
| 5           | NPC Dan  | Spy       |             |          | successful                     |
| 5           | NPC Ed   | Trader    | NPC Ken     | NPC Gia  | failed because not vulnerable  |
| 5           | NPC Fae  | Psychic   |             |          | successful                     |
| 5           | NPC Gia  | Demagog   | Executioner |          | voting in progress             |
| 5           | NPC Igi  | Judge     | Jailer      |          | successful                     |
| 5           | NPC Jeff | Reporter  | NPC Dan     |          | successful                     |
| 5           | NPC Mark | Inspector | NPC Bob     |          | successful                     |
| 5           | NPC Norm | Prophet   | NPC Ann     |          | successful                     |
| 5           | NPC Ozie | Silencer  | NPC Igi     |          | successful                     |

#### States Round 5
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Fae  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Han  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Bob  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Gia  | Demagog     | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Ken  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Mark | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Norm | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Jeff | Reporter    | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Ozie | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Cal  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Ed   | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 5           | NPC Ann  | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 5           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Ann  | Medic       | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Ann  | Medic       | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Ann  | Medic       | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Bob  | Jailer      | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Cal  | Assassin    | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Dan  | Spy         | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Bob                                  |
| 5           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Mark                                 |
| 5           | NPC Dan  | Spy         | reveal    | NPC Gia is targeting NPC Bob                                  |
| 5           | NPC Dan  | Spy         | reveal    | NPC Mark is targeting NPC Bob                                 |
| 5           | NPC Dan  | Spy         | reveal    | NPC Norm is targeting NPC Ed                                  |
| 5           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Dan                                 |
| 5           | NPC Dan  | Spy         | reveal    | NPC Ozie is targeting NPC Igi                                 |
| 5           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Ken                                  |
| 5           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Cal                                   |
| 5           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Cal                                   |
| 5           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Bob                                  |
| 5           | NPC Dan  | Spy         | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Ed   | Trader      | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Ed   | Trader      | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Ed   | Trader      | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Fae  | Psychic     | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Fae  | Psychic     | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Fae  | Psychic     | reveal    | Player: NPC Bob is not possessed                              |
| 5           | NPC Fae  | Psychic     | reveal    | Player: NPC Ken is not possessed                              |
| 5           | NPC Fae  | Psychic     | reveal    | Player: NPC Lee is not possessed                              |
| 5           | NPC Fae  | Psychic     | reveal    | Player: NPC Ozie is not possessed                             |
| 5           | NPC Fae  | Psychic     | reveal    | Player: NPC Jeff is not possessed                             |
| 5           | NPC Fae  | Psychic     | reveal    | Player: NPC Norm is not possessed                             |
| 5           | NPC Fae  | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 5           | NPC Fae  | Psychic     | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Gia  | Demagog     | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Gia  | Demagog     | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Gia  | Demagog     | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Han  | Thief       | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Han  | Thief       | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Han  | Thief       | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Igi  | Judge       | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Igi  | Judge       | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Igi  | Judge       | silenced  | You have been silenced                                        |
| 5           | NPC Igi  | Judge       | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Jeff | Reporter    | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Jeff | Reporter    | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Jeff | Reporter    | reveal    | NPC Dan is Spy                                                |
| 5           | NPC Jeff | Reporter    | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Ken  | Priest      | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Ken  | Priest      | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Ken  | Priest      | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Lee  | Executioner | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Lee  | Executioner | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Lee  | Executioner | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Mark | Inspector   | reveal    | Jailer is Innocent                                            |
| 5           | NPC Mark | Inspector   | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Norm | Prophet     | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Norm | Prophet     | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Norm | Prophet     | vote      | Demagog has initiated a vote on eliminating Executioner       |
| 5           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed  |
| 5           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Assassin is not possessed  |
| 5           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed    |
| 5           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed    |
| 5           | NPC Ozie | Silencer    | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Spy           |
| 5           | NPC Ozie | Silencer    | broadcast | I (NPC Mark) inspected NPC Bob and they are not possessed     |
| 5           | NPC Ozie | Silencer    | vote      | Demagog has initiated a vote on eliminating Executioner       |

#### Actions Round 6
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 6           | NPC Ann  | Medic    | NPC Gia  |          | successful  |
| 6           | NPC Dan  | Spy      |          |          | successful  |
| 6           | NPC Fae  | Psychic  |          |          | successful  |
| 6           | NPC Han  | Thief    | NPC Ann  |          | successful  |
| 6           | NPC Igi  | Judge    | Jailer   |          | successful  |
| 6           | NPC Norm | Prophet  | NPC Ann  |          | successful  |
| 6           | NPC Ozie | Silencer | NPC Igi  |          | successful  |

#### States Round 6
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Fae  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Han  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Bob  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Gia  | Demagog     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Ken  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Mark | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Norm | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Jeff | Reporter    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Ozie | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Cal  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ed   | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 6           | NPC Ann  | Medic       | False      | True      | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Ann  | Medic       | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Dan  | Spy         | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Bob                                     |
| 6           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Ann                                     |
| 6           | NPC Dan  | Spy         | reveal    | NPC Gia is targeting NPC Lee                                     |
| 6           | NPC Dan  | Spy         | reveal    | NPC Mark is targeting NPC Bob                                    |
| 6           | NPC Dan  | Spy         | reveal    | NPC Norm is targeting NPC Ann                                    |
| 6           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Dan                                    |
| 6           | NPC Dan  | Spy         | reveal    | NPC Ozie is targeting NPC Igi                                    |
| 6           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Dan                                     |
| 6           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Ken                                      |
| 6           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Ken                                      |
| 6           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Lee                                     |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Ed   | Trader      | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Fae  | Psychic     | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Fae  | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 6           | NPC Fae  | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 6           | NPC Fae  | Psychic     | reveal    | Player: NPC Han is not possessed                                 |
| 6           | NPC Fae  | Psychic     | reveal    | Player: NPC Lee is not possessed                                 |
| 6           | NPC Fae  | Psychic     | reveal    | Player: NPC Ken is not possessed                                 |
| 6           | NPC Fae  | Psychic     | reveal    | Player: NPC Norm is not possessed                                |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Gia  | Demagog     | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Han  | Thief       | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Igi  | Judge       | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Igi  | Judge       | silenced  | You have been silenced                                           |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Jeff | Reporter    | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Ken  | Priest      | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Lee  | Executioner | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Mark | Inspector   | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Norm | Prophet     | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob          |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Mark         |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee          |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob         |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann         |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan         |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi         |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan          |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken           |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Lee          |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed       |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Demagog is not possessed      |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed      |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed       |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed       |
| 6           | NPC Ozie | Silencer    | broadcast | I (NPC Han) am the Thief and I have made NPC Ann vulnerable      |

#### Actions Round 7
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 7           | NPC Ann  | Medic     | NPC Ken  |          | successful          |
| 7           | NPC Cal  | Assassin  | Medic    |          | successful          |
| 7           | NPC Dan  | Spy       |          |          | successful          |
| 7           | NPC Fae  | Psychic   |          |          | successful          |
| 7           | NPC Gia  | Demagog   | Reporter |          | voting in progress  |
| 7           | NPC Igi  | Judge     | Demagog  |          | successful          |
| 7           | NPC Jeff | Reporter  | NPC Cal  |          | successful          |
| 7           | NPC Mark | Inspector | NPC Gia  |          | successful          |
| 7           | NPC Norm | Prophet   | NPC Fae  |          | successful          |
| 7           | NPC Ozie | Silencer  | NPC Ed   |          | successful          |

#### States Round 7
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Dan  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Fae  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Han  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Bob  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Gia  | Demagog     | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Ken  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Mark | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Norm | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Jeff | Reporter    | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Ozie | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Cal  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Ed   | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Ann  | Medic       | False      | True      | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Ann  | Medic       | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Ann  | Medic       | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Bob  | Jailer      | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Cal  | Assassin    | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Dan  | Spy         | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Dan  | Spy         | reveal    | NPC Igi is targeting NPC Gia                                   |
| 7           | NPC Dan  | Spy         | reveal    | NPC Han is targeting NPC Ann                                   |
| 7           | NPC Dan  | Spy         | reveal    | NPC Gia is targeting NPC Lee                                   |
| 7           | NPC Dan  | Spy         | reveal    | NPC Mark is targeting NPC Gia                                  |
| 7           | NPC Dan  | Spy         | reveal    | NPC Norm is targeting NPC Ann                                  |
| 7           | NPC Dan  | Spy         | reveal    | NPC Jeff is targeting NPC Cal                                  |
| 7           | NPC Dan  | Spy         | reveal    | NPC Ozie is targeting NPC Ed                                   |
| 7           | NPC Dan  | Spy         | reveal    | NPC Cal is targeting NPC Dan                                   |
| 7           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Ken                                    |
| 7           | NPC Dan  | Spy         | reveal    | NPC Ed is targeting NPC Ken                                    |
| 7           | NPC Dan  | Spy         | reveal    | NPC Ann is targeting NPC Gia                                   |
| 7           | NPC Dan  | Spy         | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Ed   | Trader      | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Ed   | Trader      | silenced  | You have been silenced                                         |
| 7           | NPC Ed   | Trader      | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Fae  | Psychic     | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Fae  | Psychic     | reveal    | Player: NPC Ken is not possessed                               |
| 7           | NPC Fae  | Psychic     | reveal    | Player: NPC Lee is not possessed                               |
| 7           | NPC Fae  | Psychic     | reveal    | Player: NPC Gia is not possessed                               |
| 7           | NPC Fae  | Psychic     | reveal    | Player: NPC Han is not possessed                               |
| 7           | NPC Fae  | Psychic     | reveal    | Player: NPC Cal is not possessed                               |
| 7           | NPC Fae  | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 7           | NPC Fae  | Psychic     | reveal    | Player: NPC Jeff is not possessed                              |
| 7           | NPC Fae  | Psychic     | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Gia  | Demagog     | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Gia  | Demagog     | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Han  | Thief       | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Han  | Thief       | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Igi  | Judge       | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Igi  | Judge       | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Jeff | Reporter    | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Jeff | Reporter    | reveal    | NPC Cal is Assassin                                            |
| 7           | NPC Jeff | Reporter    | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Ken  | Priest      | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Ken  | Priest      | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Lee  | Executioner | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Lee  | Executioner | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Mark | Inspector   | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Mark | Inspector   | reveal    | Demagog is Innocent                                            |
| 7           | NPC Mark | Inspector   | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Norm | Prophet     | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Norm | Prophet     | vote      | Demagog has initiated a vote on eliminating Reporter           |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Bob        |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann        |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Lee        |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Mark is targeting NPC Bob       |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Norm is targeting NPC Ann       |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Jeff is targeting NPC Dan       |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ozie is targeting NPC Igi       |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan        |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ken         |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Dan) am the Spy and NPC Ann is targeting NPC Gia        |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Priest is not possessed     |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Jailer is not possessed     |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Fae) am the Psychic and the Prophet is not possessed    |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Jeff) am the Reporter and NPC Cal is the Assassin       |
| 7           | NPC Ozie | Silencer    | broadcast | I (NPC Mark) inspected NPC Gia and they are not possessed      |
| 7           | NPC Ozie | Silencer    | vote      | Demagog has initiated a vote on eliminating Reporter           |