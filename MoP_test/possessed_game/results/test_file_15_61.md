#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 61   | 15      | 4       |

#### Roles
| Role         |
| :----------- |
| Judge        |
| Thief        |
| Spy          |
| Trader       |
| Reporter     |
| Medic        |
| Priest       |
| Assassin     |
| Inspector    |
| Silencer     |
| Jailer       |
| Demagog      |
| Executioner  |
| Psychic      |
| Prophet      |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Mark | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Norm | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ozie | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Ann  | Prophet     | possessed   | You are Possessed         |
| 0           | NPC Bob  | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Bob  | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Cal  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Cal  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Thief       | role change | Your Role is Thief        |
| 0           | NPC Dan  | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Ed   | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Fae  | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Priest      | role change | Your Role is Priest       |
| 0           | NPC Gia  | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Trader      | role change | Your Role is Trader       |
| 0           | NPC Han  | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Igi  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Jeff | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Ken  | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Lee  | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Mark | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Mark | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Norm | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Norm | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Ozie | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Ozie | Demagog     | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player   | action    | Target 1  | Target 2 | status              |
| :-----------| :--------| :---------| :---------| :--------| :------------------ |
| 1           | NPC Ann  | Prophet   | NPC Cal   |          | successful          |
| 1           | NPC Bob  | Reporter  | NPC Ed    |          | successful          |
| 1           | NPC Dan  | Thief     | NPC Cal   |          | successful          |
| 1           | NPC Ed   | Psychic   |           |          | successful          |
| 1           | NPC Fae  | Spy       |           |          | successful          |
| 1           | NPC Han  | Trader    | NPC Mark  | NPC Lee  | successful          |
| 1           | NPC Igi  | Judge     | Inspector |          | successful          |
| 1           | NPC Ken  | Assassin  | Prophet   |          | successful          |
| 1           | NPC Lee  | Medic     | NPC Dan   |          | successful          |
| 1           | NPC Mark | Inspector | NPC Jeff  |          | successful          |
| 1           | NPC Norm | Silencer  | NPC Gia   |          | successful          |
| 1           | NPC Ozie | Demagog   | Psychic   |          | voting in progress  |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Bob  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Lee  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ken  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Mark | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Norm | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Jeff | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ozie | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal  | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Ed   | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ann  | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                         |
| :-----------| :--------| :-----------| :---------| :-------------------------------------------------------------- |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Ann  | Prophet     | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Bob  | Reporter    | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Bob  | Reporter    | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Bob  | Reporter    | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Bob  | Reporter    | reveal    | NPC Ed is Psychic                                               |
| 1           | NPC Bob  | Reporter    | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Cal  | Executioner | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Dan  | Thief       | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Dan  | Thief       | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Dan  | Thief       | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Dan  | Thief       | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Dan  | Thief       | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Dan  | Thief       | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Dan  | Thief       | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Dan  | Thief       | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Dan  | Thief       | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Dan  | Thief       | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Ed   | Psychic     | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Ed   | Psychic     | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Ed   | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ed   | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ed   | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ed   | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ed   | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Ed   | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Ed   | Psychic     | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Ed   | Psychic     | reveal    | Player: NPC Han is not possessed                                |
| 1           | NPC Ed   | Psychic     | reveal    | Player: NPC Jeff is not possessed                               |
| 1           | NPC Ed   | Psychic     | reveal    | Player: NPC Fae is not possessed                                |
| 1           | NPC Ed   | Psychic     | reveal    | Player: NPC Ken is not possessed                                |
| 1           | NPC Ed   | Psychic     | reveal    | Player: NPC Norm is not possessed                               |
| 1           | NPC Ed   | Psychic     | reveal    | Player: NPC Mark is not possessed                               |
| 1           | NPC Ed   | Psychic     | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Fae  | Spy         | reveal    | NPC Igi is targeting NPC Mark                                   |
| 1           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Cal                                    |
| 1           | NPC Fae  | Spy         | reveal    | NPC Bob is targeting NPC Ed                                     |
| 1           | NPC Fae  | Spy         | reveal    | NPC Mark is targeting NPC Jeff                                  |
| 1           | NPC Fae  | Spy         | reveal    | NPC Norm is targeting NPC Gia                                   |
| 1           | NPC Fae  | Spy         | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Gia  | Priest      | silenced  | You have been silenced                                          |
| 1           | NPC Gia  | Priest      | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Han  | Trader      | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Han  | Trader      | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Igi  | Judge       | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Igi  | Judge       | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Jeff | Jailer      | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Jeff | Jailer      | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Jeff | Jailer      | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Jeff | Jailer      | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Ken  | Assassin    | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Lee  | Inspector   | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Lee  | Inspector   | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Lee  | Inspector   | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Lee  | Inspector   | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Mark | Medic       | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Mark | Medic       | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Mark | Medic       | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Mark | Medic       | reveal    | Jailer is Innocent                                              |
| 1           | NPC Mark | Medic       | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Norm | Silencer    | vote      | Demagog has initiated a vote on eliminating Psychic             |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Bob) am the Reporter and NPC Ed is the Psychic           |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable     |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed        |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Mark) inspected NPC Jeff and they are not possessed      |
| 1           | NPC Ozie | Demagog     | vote      | Demagog has initiated a vote on eliminating Psychic             |

#### Actions Round 2
| round_index | Player   | action    | Target 1 | Target 2 | status      |
| :-----------| :--------| :---------| :--------| :--------| :---------- |
| 2           | NPC Ann  | Prophet   | NPC Fae  |          | successful  |
| 2           | NPC Dan  | Thief     | NPC Ann  |          | successful  |
| 2           | NPC Ed   | Psychic   |          |          | successful  |
| 2           | NPC Fae  | Spy       |          |          | successful  |
| 2           | NPC Igi  | Judge     | Priest   |          | successful  |
| 2           | NPC Lee  | Inspector | NPC Igi  |          | successful  |
| 2           | NPC Mark | Medic     | NPC Fae  |          | successful  |
| 2           | NPC Norm | Silencer  | NPC Ed   |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Bob  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Lee  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Gia  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ken  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Mark | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Norm | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Jeff | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ozie | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal  | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 2           | NPC Ed   | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann  | Prophet     | False      | True      | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                         |
| :-----------| :--------| :-----------| :---------| :-------------------------------------------------------------- |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Bob  | Reporter    | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Dan  | Thief       | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Ed   | Psychic     | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Ed   | Psychic     | silenced  | You have been silenced                                          |
| 2           | NPC Ed   | Psychic     | reveal    | Player: NPC Han is not possessed                                |
| 2           | NPC Ed   | Psychic     | reveal    | Player: NPC Ozie is not possessed                               |
| 2           | NPC Ed   | Psychic     | reveal    | Player: NPC Norm is not possessed                               |
| 2           | NPC Ed   | Psychic     | reveal    | Player: NPC Fae is not possessed                                |
| 2           | NPC Ed   | Psychic     | reveal    | Player: NPC Jeff is not possessed                               |
| 2           | NPC Ed   | Psychic     | reveal    | Player: NPC Ken is not possessed                                |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Fae  | Spy         | reveal    | NPC Igi is targeting NPC Gia                                    |
| 2           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Ann                                    |
| 2           | NPC Fae  | Spy         | reveal    | NPC Han is targeting NPC Mark                                   |
| 2           | NPC Fae  | Spy         | reveal    | NPC Han is targeting NPC Mark                                   |
| 2           | NPC Fae  | Spy         | reveal    | NPC Bob is targeting NPC Ed                                     |
| 2           | NPC Fae  | Spy         | reveal    | NPC Lee is targeting NPC Igi                                    |
| 2           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Ann                                    |
| 2           | NPC Fae  | Spy         | reveal    | NPC Norm is targeting NPC Ed                                    |
| 2           | NPC Fae  | Spy         | reveal    | NPC Ozie is targeting NPC Ed                                    |
| 2           | NPC Fae  | Spy         | reveal    | NPC Ann is targeting NPC Cal                                    |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Gia  | Priest      | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Han  | Trader      | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Igi  | Judge       | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Lee  | Inspector   | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Lee  | Inspector   | reveal    | Judge is Innocent                                               |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Mark | Medic       | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable     |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed       |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed      |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Spy is not possessed          |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee         |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Cal         |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark        |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed          |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Dan         |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann         |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Gia        |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed         |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Cal         |
| 2           | NPC Ozie | Demagog     | broadcast | I (NPC Lee) inspected NPC Igi and they are not possessed        |

#### Actions Round 3
| round_index | Player   | action   | Target 1  | Target 2 | status              |
| :-----------| :--------| :--------| :---------| :--------| :------------------ |
| 3           | NPC Ann  | Prophet  | NPC Gia   |          | successful          |
| 3           | NPC Bob  | Reporter | NPC Ozie  |          | successful          |
| 3           | NPC Ed   | Psychic  |           |          | successful          |
| 3           | NPC Fae  | Spy      |           |          | successful          |
| 3           | NPC Igi  | Judge    | Inspector |          | successful          |
| 3           | NPC Ken  | Assassin | Silencer  |          | successful          |
| 3           | NPC Mark | Medic    | NPC Han   |          | successful          |
| 3           | NPC Norm | Silencer | NPC Jeff  |          | successful          |
| 3           | NPC Ozie | Demagog  | Medic     |          | voting in progress  |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Igi  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Han  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Lee  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Gia  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ken  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Mark | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Norm | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Jeff | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ozie | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Cal  | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Ed   | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ann  | Prophet     | False      | True      | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message   | details                                                   |
| :-----------| :--------| :-----------| :---------| :-------------------------------------------------------- |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Ann  | Prophet     | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Bob  | Reporter    | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Bob  | Reporter    | reveal    | NPC Ozie is Demagog                                       |
| 3           | NPC Bob  | Reporter    | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Cal  | Executioner | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Dan  | Thief       | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Dan  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Dan  | Thief       | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Ed   | Psychic     | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Ed   | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Ed   | Psychic     | reveal    | Player: NPC Han is not possessed                          |
| 3           | NPC Ed   | Psychic     | reveal    | Player: NPC Fae is not possessed                          |
| 3           | NPC Ed   | Psychic     | reveal    | Player: NPC Igi is not possessed                          |
| 3           | NPC Ed   | Psychic     | reveal    | Player: NPC Ken is not possessed                          |
| 3           | NPC Ed   | Psychic     | reveal    | Player: NPC Gia is not possessed                          |
| 3           | NPC Ed   | Psychic     | reveal    | Player: NPC Dan is not possessed                          |
| 3           | NPC Ed   | Psychic     | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Fae  | Spy         | reveal    | NPC Igi is targeting NPC Lee                              |
| 3           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Ann                              |
| 3           | NPC Fae  | Spy         | reveal    | NPC Han is targeting NPC Mark                             |
| 3           | NPC Fae  | Spy         | reveal    | NPC Han is targeting NPC Mark                             |
| 3           | NPC Fae  | Spy         | reveal    | NPC Bob is targeting NPC Ozie                             |
| 3           | NPC Fae  | Spy         | reveal    | NPC Lee is targeting NPC Igi                              |
| 3           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Ann                              |
| 3           | NPC Fae  | Spy         | reveal    | NPC Mark is targeting NPC Fae                             |
| 3           | NPC Fae  | Spy         | reveal    | NPC Norm is targeting NPC Jeff                            |
| 3           | NPC Fae  | Spy         | reveal    | NPC Ozie is targeting NPC Ed                              |
| 3           | NPC Fae  | Spy         | reveal    | NPC Ann is targeting NPC Fae                              |
| 3           | NPC Fae  | Spy         | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Gia  | Priest      | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Gia  | Priest      | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Han  | Trader      | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Igi  | Judge       | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Jeff | Jailer      | silenced  | You have been silenced                                    |
| 3           | NPC Jeff | Jailer      | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Ken  | Assassin    | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Ken  | Assassin    | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Lee  | Inspector   | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Lee  | Inspector   | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Mark | Medic       | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Mark | Medic       | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Norm | Silencer    | vote      | Demagog has initiated a vote on eliminating Medic         |
| 3           | NPC Ozie | Demagog     | broadcast | I (NPC Bob) am the Reporter and NPC Ozie is the Demagog   |
| 3           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Gia   |
| 3           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann   |
| 3           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark  |
| 3           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ed    |
| 3           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi   |
| 3           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann   |
| 3           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Fae  |
| 3           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Ed   |
| 3           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Ed   |
| 3           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Fae   |
| 3           | NPC Ozie | Demagog     | vote      | Demagog has initiated a vote on eliminating Medic         |

#### Actions Round 4
| round_index | Player   | action    | Target 1 | Target 2 | status      |
| :-----------| :--------| :---------| :--------| :--------| :---------- |
| 4           | NPC Ann  | Prophet   | NPC Bob  |          | successful  |
| 4           | NPC Dan  | Thief     | NPC Igi  |          | successful  |
| 4           | NPC Ed   | Psychic   |          |          | successful  |
| 4           | NPC Fae  | Spy       |          |          | successful  |
| 4           | NPC Han  | Trader    | NPC Ed   | NPC Dan  | successful  |
| 4           | NPC Igi  | Judge     | Spy      |          | successful  |
| 4           | NPC Lee  | Inspector | NPC Bob  |          | successful  |
| 4           | NPC Mark | Medic     | NPC Bob  |          | successful  |
| 4           | NPC Norm | Silencer  | NPC Ozie |          | successful  |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Igi  | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Dan  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Han  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 4           | NPC Bob  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Lee  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Gia  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ken  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Mark | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Norm | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Jeff | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ozie | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Cal  | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Ed   | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann  | Prophet     | False      | True      | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                      |
| :-----------| :--------| :-----------| :---------| :----------------------------------------------------------- |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Bob  | Reporter    | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Dan  | Psychic     | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Ed   | Thief       | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Ed   | Thief       | reveal    | Player: NPC Igi is not possessed                             |
| 4           | NPC Ed   | Thief       | reveal    | Player: NPC Han is not possessed                             |
| 4           | NPC Ed   | Thief       | reveal    | Player: NPC Jeff is not possessed                            |
| 4           | NPC Ed   | Thief       | reveal    | Player: NPC Mark is not possessed                            |
| 4           | NPC Ed   | Thief       | reveal    | Player: NPC Ken is not possessed                             |
| 4           | NPC Ed   | Thief       | reveal    | Player: NPC Gia is not possessed                             |
| 4           | NPC Ed   | Thief       | reveal    | Player: NPC Ozie is not possessed                            |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Fae  | Spy         | reveal    | NPC Igi is targeting NPC Fae                                 |
| 4           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Igi                                 |
| 4           | NPC Fae  | Spy         | reveal    | NPC Han is targeting NPC Mark                                |
| 4           | NPC Fae  | Spy         | reveal    | NPC Han is targeting NPC Mark                                |
| 4           | NPC Fae  | Spy         | reveal    | NPC Bob is targeting NPC Ozie                                |
| 4           | NPC Fae  | Spy         | reveal    | NPC Lee is targeting NPC Bob                                 |
| 4           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Norm                                |
| 4           | NPC Fae  | Spy         | reveal    | NPC Mark is targeting NPC Han                                |
| 4           | NPC Fae  | Spy         | reveal    | NPC Norm is targeting NPC Ozie                               |
| 4           | NPC Fae  | Spy         | reveal    | NPC Ozie is targeting NPC Mark                               |
| 4           | NPC Fae  | Spy         | reveal    | NPC Ann is targeting NPC Gia                                 |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Gia  | Priest      | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Han  | Trader      | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Igi  | Judge       | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Jeff | Jailer      | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Ken  | Assassin    | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Lee  | Inspector   | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Lee  | Inspector   | reveal    | Reporter is Innocent                                         |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Mark | Medic       | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Dan) am the Thief and I have made NPC Igi vulnerable  |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Thief is not possessed     |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Priest is not possessed    |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed    |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Lee      |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann      |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Mark     |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ozie     |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Lee is targeting NPC Igi      |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Norm     |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Han     |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Jeff    |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ozie is targeting NPC Mark    |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ann is targeting NPC Gia      |
| 4           | NPC Ozie | Demagog     | broadcast | I (NPC Lee) inspected NPC Bob and they are not possessed     |
| 4           | NPC Ozie | Demagog     | silenced  | You have been silenced                                       |