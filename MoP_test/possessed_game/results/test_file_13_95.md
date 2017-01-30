#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 95   | 13      | 6       |

#### Roles
| Role         |
| :----------- |
| Silencer     |
| Assassin     |
| Psychic      |
| Demagog      |
| Thief        |
| Judge        |
| Prophet      |
| Jailer       |
| Spy          |
| Executioner  |
| Inspector    |
| Priest       |
| Reporter     |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Demagog     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Mark | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Ann  | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Bob  | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Bob  | Demagog     | possessed   | You are Possessed         |
| 0           | NPC Cal  | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Cal  | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Dan  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Ed   | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Priest      | role change | Your Role is Priest       |
| 0           | NPC Fae  | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Gia  | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Han  | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Igi  | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Thief       | role change | Your Role is Thief        |
| 0           | NPC Jeff | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ken  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Lee  | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Mark | Judge       | role change | Your Role is Judge        |
| 0           | NPC Mark | Judge       | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player   | action    | Target 1  | Target 2 | status              |
| :-----------| :--------| :---------| :---------| :--------| :------------------ |
| 1           | NPC Ann  | Psychic   |           |          | successful          |
| 1           | NPC Bob  | Demagog   | Inspector |          | voting in progress  |
| 1           | NPC Cal  | Silencer  | NPC Dan   |          | successful          |
| 1           | NPC Dan  | Inspector | NPC Gia   |          | successful          |
| 1           | NPC Gia  | Spy       |           |          | successful          |
| 1           | NPC Han  | Assassin  | Reporter  |          | successful          |
| 1           | NPC Igi  | Reporter  | NPC Ken   |          | successful          |
| 1           | NPC Jeff | Thief     | NPC Bob   |          | successful          |
| 1           | NPC Lee  | Prophet   | NPC Fae   |          | successful          |
| 1           | NPC Mark | Judge     | Prophet   |          | successful          |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Han  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Bob  | Demagog     | False      | True      | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Jeff | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Mark | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Lee  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Fae  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Igi  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed      |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed       |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Jeff) am the Thief and I have made NPC Bob vulnerable   |
| 1           | NPC Ann  | Psychic     | reveal    | Player: NPC Dan is not possessed                               |
| 1           | NPC Ann  | Psychic     | reveal    | Player: NPC Ed is not possessed                                |
| 1           | NPC Ann  | Psychic     | reveal    | Player: NPC Cal is not possessed                               |
| 1           | NPC Ann  | Psychic     | reveal    | Player: NPC Lee is not possessed                               |
| 1           | NPC Ann  | Psychic     | reveal    | Player: NPC Mark is not possessed                              |
| 1           | NPC Ann  | Psychic     | reveal    | Player: NPC Jeff is not possessed                              |
| 1           | NPC Ann  | Psychic     | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed      |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed       |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Jeff) am the Thief and I have made NPC Bob vulnerable   |
| 1           | NPC Bob  | Demagog     | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed      |
| 1           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Cal  | Silencer    | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed       |
| 1           | NPC Cal  | Silencer    | broadcast | I (NPC Jeff) am the Thief and I have made NPC Bob vulnerable   |
| 1           | NPC Cal  | Silencer    | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed      |
| 1           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Dan  | Inspector   | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed       |
| 1           | NPC Dan  | Inspector   | broadcast | I (NPC Jeff) am the Thief and I have made NPC Bob vulnerable   |
| 1           | NPC Dan  | Inspector   | reveal    | Spy is Innocent                                                |
| 1           | NPC Dan  | Inspector   | silenced  | You have been silenced                                         |
| 1           | NPC Dan  | Inspector   | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed      |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed       |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Jeff) am the Thief and I have made NPC Bob vulnerable   |
| 1           | NPC Ed   | Jailer      | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed      |
| 1           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Fae  | Priest      | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed       |
| 1           | NPC Fae  | Priest      | broadcast | I (NPC Jeff) am the Thief and I have made NPC Bob vulnerable   |
| 1           | NPC Fae  | Priest      | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed      |
| 1           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Gia  | Spy         | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed       |
| 1           | NPC Gia  | Spy         | broadcast | I (NPC Jeff) am the Thief and I have made NPC Bob vulnerable   |
| 1           | NPC Gia  | Spy         | reveal    | NPC Cal is targeting NPC Dan                                   |
| 1           | NPC Gia  | Spy         | reveal    | NPC Jeff is targeting NPC Bob                                  |
| 1           | NPC Gia  | Spy         | reveal    | NPC Mark is targeting NPC Lee                                  |
| 1           | NPC Gia  | Spy         | reveal    | NPC Dan is targeting NPC Gia                                   |
| 1           | NPC Gia  | Spy         | reveal    | NPC Igi is targeting NPC Ken                                   |
| 1           | NPC Gia  | Spy         | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed      |
| 1           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Han  | Assassin    | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed       |
| 1           | NPC Han  | Assassin    | broadcast | I (NPC Jeff) am the Thief and I have made NPC Bob vulnerable   |
| 1           | NPC Han  | Assassin    | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed      |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed       |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Jeff) am the Thief and I have made NPC Bob vulnerable   |
| 1           | NPC Igi  | Reporter    | reveal    | NPC Ken is Executioner                                         |
| 1           | NPC Igi  | Reporter    | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed      |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed       |
| 1           | NPC Jeff | Thief       | broadcast | I (NPC Jeff) am the Thief and I have made NPC Bob vulnerable   |
| 1           | NPC Jeff | Thief       | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed      |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed       |
| 1           | NPC Ken  | Executioner | broadcast | I (NPC Jeff) am the Thief and I have made NPC Bob vulnerable   |
| 1           | NPC Ken  | Executioner | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed      |
| 1           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Lee  | Prophet     | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed       |
| 1           | NPC Lee  | Prophet     | broadcast | I (NPC Jeff) am the Thief and I have made NPC Bob vulnerable   |
| 1           | NPC Lee  | Prophet     | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed      |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Dan) inspected NPC Gia and they are not possessed       |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Jeff) am the Thief and I have made NPC Bob vulnerable   |
| 1           | NPC Mark | Judge       | vote      | Demagog has initiated a vote on eliminating Inspector          |

#### Actions Round 2
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 2           | NPC Ann  | Psychic  |          |          | successful  |
| 2           | NPC Cal  | Silencer | NPC Bob  |          | successful  |
| 2           | NPC Gia  | Spy      |          |          | successful  |
| 2           | NPC Lee  | Prophet  | NPC Ann  |          | successful  |
| 2           | NPC Mark | Judge    | Psychic  |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Han  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Bob  | Demagog     | False      | True      | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Jeff | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Mark | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Lee  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Gia  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Fae  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Igi  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed        |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Dan          |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee         |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Fae          |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 2           | NPC Ann  | Psychic     | reveal    | Player: NPC Han is not possessed                                 |
| 2           | NPC Ann  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 2           | NPC Ann  | Psychic     | reveal    | Player: NPC Gia is not possessed                                 |
| 2           | NPC Ann  | Psychic     | reveal    | Player: NPC Mark is not possessed                                |
| 2           | NPC Ann  | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 2           | NPC Ann  | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed        |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Dan          |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee         |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Fae          |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 2           | NPC Bob  | Demagog     | silenced  | You have been silenced                                           |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed        |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Dan          |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee         |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Fae          |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 2           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed        |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Dan          |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee         |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Fae          |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 2           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed        |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Dan          |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee         |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Fae          |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed        |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Dan          |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee         |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Fae          |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 2           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed        |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Dan          |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee         |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Fae          |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 2           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 2           | NPC Gia  | Spy         | reveal    | NPC Cal is targeting NPC Bob                                     |
| 2           | NPC Gia  | Spy         | reveal    | NPC Han is targeting NPC Igi                                     |
| 2           | NPC Gia  | Spy         | reveal    | NPC Bob is targeting NPC Dan                                     |
| 2           | NPC Gia  | Spy         | reveal    | NPC Jeff is targeting NPC Bob                                    |
| 2           | NPC Gia  | Spy         | reveal    | NPC Mark is targeting NPC Ann                                    |
| 2           | NPC Gia  | Spy         | reveal    | NPC Lee is targeting NPC Fae                                     |
| 2           | NPC Gia  | Spy         | reveal    | NPC Dan is targeting NPC Gia                                     |
| 2           | NPC Gia  | Spy         | reveal    | NPC Igi is targeting NPC Ken                                     |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed        |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Dan          |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee         |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Fae          |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 2           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed        |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Dan          |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee         |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Fae          |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed        |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Dan          |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee         |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Fae          |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 2           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed        |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Dan          |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee         |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Fae          |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 2           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed        |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Dan          |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee         |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Fae          |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 2           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed        |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Dan          |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee         |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Fae          |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 2           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |

#### Actions Round 3
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 3           | NPC Ann  | Psychic   |          |          | successful          |
| 3           | NPC Bob  | Demagog   | Psychic  |          | voting in progress  |
| 3           | NPC Cal  | Silencer  | NPC Gia  |          | successful          |
| 3           | NPC Dan  | Inspector | NPC Ed   |          | successful          |
| 3           | NPC Gia  | Spy       |          |          | successful          |
| 3           | NPC Han  | Assassin  | Spy      |          | successful          |
| 3           | NPC Igi  | Reporter  | NPC Bob  |          | successful          |
| 3           | NPC Jeff | Thief     | NPC Dan  |          | successful          |
| 3           | NPC Lee  | Prophet   | NPC Jeff |          | successful          |
| 3           | NPC Mark | Judge     | Demagog  |          | successful          |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Han  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Bob  | Demagog     | False      | True      | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Jeff | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Mark | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Lee  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Gia  | Spy         | True       | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Fae  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Igi  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message     | details                                                          |
| :-----------| :--------| :-----------| :-----------| :--------------------------------------------------------------- |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Ann) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Bob          |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Ann         |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Ann          |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 3           | NPC Ann  | Psychic     | broadcast   | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 3           | NPC Ann  | Psychic     | reveal      | Player: NPC Dan is not possessed                                 |
| 3           | NPC Ann  | Psychic     | reveal      | Player: NPC Han is not possessed                                 |
| 3           | NPC Ann  | Psychic     | reveal      | Player: NPC Jeff is not possessed                                |
| 3           | NPC Ann  | Psychic     | reveal      | Player: NPC Mark is not possessed                                |
| 3           | NPC Ann  | Psychic     | reveal      | Player: NPC Cal is not possessed                                 |
| 3           | NPC Ann  | Psychic     | elimination | NPC Gia has been eliminated                                      |
| 3           | NPC Ann  | Psychic     | vote        | Demagog has initiated a vote on eliminating Psychic              |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Ann) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Bob          |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Ann         |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Ann          |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 3           | NPC Bob  | Demagog     | broadcast   | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 3           | NPC Bob  | Demagog     | elimination | NPC Gia has been eliminated                                      |
| 3           | NPC Bob  | Demagog     | vote        | Demagog has initiated a vote on eliminating Psychic              |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Ann) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Bob          |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Ann         |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Ann          |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 3           | NPC Cal  | Silencer    | broadcast   | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 3           | NPC Cal  | Silencer    | elimination | NPC Gia has been eliminated                                      |
| 3           | NPC Cal  | Silencer    | vote        | Demagog has initiated a vote on eliminating Psychic              |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Ann) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Bob          |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Ann         |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Ann          |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 3           | NPC Dan  | Inspector   | broadcast   | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 3           | NPC Dan  | Inspector   | reveal      | Jailer is Innocent                                               |
| 3           | NPC Dan  | Inspector   | elimination | NPC Gia has been eliminated                                      |
| 3           | NPC Dan  | Inspector   | vote        | Demagog has initiated a vote on eliminating Psychic              |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Ann) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Bob          |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Ann         |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Ann          |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 3           | NPC Ed   | Jailer      | broadcast   | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 3           | NPC Ed   | Jailer      | elimination | NPC Gia has been eliminated                                      |
| 3           | NPC Ed   | Jailer      | vote        | Demagog has initiated a vote on eliminating Psychic              |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Ann) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Bob          |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Ann         |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Ann          |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 3           | NPC Fae  | Priest      | broadcast   | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 3           | NPC Fae  | Priest      | elimination | NPC Gia has been eliminated                                      |
| 3           | NPC Fae  | Priest      | vote        | Demagog has initiated a vote on eliminating Psychic              |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Ann) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Bob          |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Ann         |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Ann          |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 3           | NPC Gia  | Spy         | broadcast   | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 3           | NPC Gia  | Spy         | silenced    | You have been silenced                                           |
| 3           | NPC Gia  | Spy         | reveal      | NPC Cal is targeting NPC Gia                                     |
| 3           | NPC Gia  | Spy         | reveal      | NPC Han is targeting NPC Igi                                     |
| 3           | NPC Gia  | Spy         | reveal      | NPC Bob is targeting NPC Dan                                     |
| 3           | NPC Gia  | Spy         | reveal      | NPC Jeff is targeting NPC Dan                                    |
| 3           | NPC Gia  | Spy         | reveal      | NPC Mark is targeting NPC Bob                                    |
| 3           | NPC Gia  | Spy         | reveal      | NPC Lee is targeting NPC Ann                                     |
| 3           | NPC Gia  | Spy         | reveal      | NPC Dan is targeting NPC Ed                                      |
| 3           | NPC Gia  | Spy         | reveal      | NPC Igi is targeting NPC Bob                                     |
| 3           | NPC Gia  | Spy         | elimination | NPC Gia has been eliminated                                      |
| 3           | NPC Gia  | Spy         | vote        | Demagog has initiated a vote on eliminating Psychic              |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Ann) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Bob          |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Ann         |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Ann          |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 3           | NPC Han  | Assassin    | broadcast   | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 3           | NPC Han  | Assassin    | elimination | NPC Gia has been eliminated                                      |
| 3           | NPC Han  | Assassin    | vote        | Demagog has initiated a vote on eliminating Psychic              |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Ann) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Bob          |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Ann         |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Ann          |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 3           | NPC Igi  | Reporter    | broadcast   | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 3           | NPC Igi  | Reporter    | reveal      | NPC Bob is Demagog                                               |
| 3           | NPC Igi  | Reporter    | elimination | NPC Gia has been eliminated                                      |
| 3           | NPC Igi  | Reporter    | vote        | Demagog has initiated a vote on eliminating Psychic              |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Ann) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Bob          |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Ann         |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Ann          |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 3           | NPC Jeff | Thief       | broadcast   | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 3           | NPC Jeff | Thief       | elimination | NPC Gia has been eliminated                                      |
| 3           | NPC Jeff | Thief       | vote        | Demagog has initiated a vote on eliminating Psychic              |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Ann) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Bob          |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Ann         |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Ann          |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 3           | NPC Ken  | Executioner | broadcast   | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 3           | NPC Ken  | Executioner | elimination | NPC Gia has been eliminated                                      |
| 3           | NPC Ken  | Executioner | vote        | Demagog has initiated a vote on eliminating Psychic              |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Ann) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Bob          |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Ann         |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Ann          |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 3           | NPC Lee  | Prophet     | broadcast   | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 3           | NPC Lee  | Prophet     | elimination | NPC Gia has been eliminated                                      |
| 3           | NPC Lee  | Prophet     | vote        | Demagog has initiated a vote on eliminating Psychic              |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Ann) am the Psychic and the Assassin is not possessed     |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Bob          |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Gia) am the Spy and NPC Han is targeting NPC Igi          |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Dan          |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Bob         |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Ann         |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Ann          |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Gia          |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ken          |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 3           | NPC Mark | Judge       | broadcast   | I (NPC Jeff) am the Thief and I have made NPC Dan vulnerable     |
| 3           | NPC Mark | Judge       | elimination | NPC Gia has been eliminated                                      |
| 3           | NPC Mark | Judge       | vote        | Demagog has initiated a vote on eliminating Psychic              |

#### Actions Round 4
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 4           | NPC Ann  | Psychic  |          |          | successful  |
| 4           | NPC Cal  | Silencer | NPC Lee  |          | successful  |
| 4           | NPC Gia  | Spy      |          |          | successful  |
| 4           | NPC Lee  | Prophet  | NPC Igi  |          | successful  |
| 4           | NPC Mark | Judge    | Prophet  |          | successful  |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Han  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Bob  | Demagog     | False      | True      | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Jeff | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Mark | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Lee  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Gia  | Spy         | True       | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan  | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Fae  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Igi  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 4           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 4           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 4           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ann  | Psychic     | reveal    | Player: NPC Jeff is not possessed                             |
| 4           | NPC Ann  | Psychic     | reveal    | Player: NPC Igi is not possessed                              |
| 4           | NPC Ann  | Psychic     | reveal    | Player: NPC Cal is not possessed                              |
| 4           | NPC Ann  | Psychic     | reveal    | Player: NPC Ken is not possessed                              |
| 4           | NPC Ann  | Psychic     | reveal    | Player: NPC Han is not possessed                              |
| 4           | NPC Ann  | Psychic     | reveal    | Player: NPC Mark is not possessed                             |
| 4           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 4           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 4           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 4           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 4           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 4           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 4           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 4           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 4           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 4           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 4           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 4           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 4           | NPC Gia  | Spy         | reveal    | NPC Cal is targeting NPC Lee                                  |
| 4           | NPC Gia  | Spy         | reveal    | NPC Han is targeting NPC Gia                                  |
| 4           | NPC Gia  | Spy         | reveal    | NPC Bob is targeting NPC Ann                                  |
| 4           | NPC Gia  | Spy         | reveal    | NPC Jeff is targeting NPC Dan                                 |
| 4           | NPC Gia  | Spy         | reveal    | NPC Mark is targeting NPC Lee                                 |
| 4           | NPC Gia  | Spy         | reveal    | NPC Lee is targeting NPC Jeff                                 |
| 4           | NPC Gia  | Spy         | reveal    | NPC Dan is targeting NPC Ed                                   |
| 4           | NPC Gia  | Spy         | reveal    | NPC Igi is targeting NPC Bob                                  |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 4           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 4           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 4           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 4           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 4           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 4           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 4           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 4           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 4           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 4           | NPC Lee  | Prophet     | silenced  | You have been silenced                                        |
| 4           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 4           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 4           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |

#### Actions Round 5
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 5           | NPC Ann  | Psychic   |          |          | successful          |
| 5           | NPC Bob  | Demagog   | Psychic  |          | voting in progress  |
| 5           | NPC Cal  | Silencer  | NPC Lee  |          | successful          |
| 5           | NPC Dan  | Inspector | NPC Ed   |          | successful          |
| 5           | NPC Gia  | Spy       |          |          | successful          |
| 5           | NPC Han  | Assassin  | Thief    |          | successful          |
| 5           | NPC Igi  | Reporter  | NPC Ann  |          | successful          |
| 5           | NPC Jeff | Thief     | NPC Lee  |          | successful          |
| 5           | NPC Lee  | Prophet   | NPC Han  |          | successful          |
| 5           | NPC Mark | Judge     | Priest   |          | successful          |

#### States Round 5
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Han  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Ann  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Bob  | Demagog     | False      | True      | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Jeff | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Mark | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Lee  | Prophet     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Gia  | Spy         | True       | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Fae  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Igi  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee        |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Gia        |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann        |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Dan       |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee       |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Igi        |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed         |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Bob        |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Igi) am the Reporter and NPC Ann is the Psychic         |
| 5           | NPC Ann  | Psychic     | broadcast | I (NPC Jeff) am the Thief and I have made NPC Lee vulnerable   |
| 5           | NPC Ann  | Psychic     | reveal    | Player: NPC Ken is not possessed                               |
| 5           | NPC Ann  | Psychic     | reveal    | Player: NPC Cal is not possessed                               |
| 5           | NPC Ann  | Psychic     | reveal    | Player: NPC Fae is not possessed                               |
| 5           | NPC Ann  | Psychic     | reveal    | Player: NPC Jeff is not possessed                              |
| 5           | NPC Ann  | Psychic     | reveal    | Player: NPC Igi is not possessed                               |
| 5           | NPC Ann  | Psychic     | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee        |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Gia        |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann        |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Dan       |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee       |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Igi        |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed         |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Bob        |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Igi) am the Reporter and NPC Ann is the Psychic         |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Jeff) am the Thief and I have made NPC Lee vulnerable   |
| 5           | NPC Bob  | Demagog     | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee        |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Gia        |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann        |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Dan       |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee       |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Igi        |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed         |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Bob        |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Igi) am the Reporter and NPC Ann is the Psychic         |
| 5           | NPC Cal  | Silencer    | broadcast | I (NPC Jeff) am the Thief and I have made NPC Lee vulnerable   |
| 5           | NPC Cal  | Silencer    | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee        |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Gia        |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann        |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Dan       |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee       |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Igi        |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed         |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Bob        |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Igi) am the Reporter and NPC Ann is the Psychic         |
| 5           | NPC Dan  | Inspector   | broadcast | I (NPC Jeff) am the Thief and I have made NPC Lee vulnerable   |
| 5           | NPC Dan  | Inspector   | reveal    | Jailer is Innocent                                             |
| 5           | NPC Dan  | Inspector   | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee        |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Gia        |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann        |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Dan       |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee       |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Igi        |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed         |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Bob        |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Reporter and NPC Ann is the Psychic         |
| 5           | NPC Ed   | Jailer      | broadcast | I (NPC Jeff) am the Thief and I have made NPC Lee vulnerable   |
| 5           | NPC Ed   | Jailer      | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee        |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Gia        |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann        |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Dan       |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee       |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Igi        |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed         |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Bob        |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Igi) am the Reporter and NPC Ann is the Psychic         |
| 5           | NPC Fae  | Priest      | broadcast | I (NPC Jeff) am the Thief and I have made NPC Lee vulnerable   |
| 5           | NPC Fae  | Priest      | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee        |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Gia        |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann        |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Dan       |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee       |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Igi        |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed         |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Bob        |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Igi) am the Reporter and NPC Ann is the Psychic         |
| 5           | NPC Gia  | Spy         | broadcast | I (NPC Jeff) am the Thief and I have made NPC Lee vulnerable   |
| 5           | NPC Gia  | Spy         | reveal    | NPC Cal is targeting NPC Lee                                   |
| 5           | NPC Gia  | Spy         | reveal    | NPC Han is targeting NPC Gia                                   |
| 5           | NPC Gia  | Spy         | reveal    | NPC Bob is targeting NPC Ann                                   |
| 5           | NPC Gia  | Spy         | reveal    | NPC Jeff is targeting NPC Lee                                  |
| 5           | NPC Gia  | Spy         | reveal    | NPC Mark is targeting NPC Fae                                  |
| 5           | NPC Gia  | Spy         | reveal    | NPC Lee is targeting NPC Igi                                   |
| 5           | NPC Gia  | Spy         | reveal    | NPC Dan is targeting NPC Ed                                    |
| 5           | NPC Gia  | Spy         | reveal    | NPC Igi is targeting NPC Ann                                   |
| 5           | NPC Gia  | Spy         | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee        |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Gia        |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann        |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Dan       |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee       |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Igi        |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed         |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Bob        |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Igi) am the Reporter and NPC Ann is the Psychic         |
| 5           | NPC Han  | Assassin    | broadcast | I (NPC Jeff) am the Thief and I have made NPC Lee vulnerable   |
| 5           | NPC Han  | Assassin    | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee        |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Gia        |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann        |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Dan       |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee       |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Igi        |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed         |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Bob        |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Igi) am the Reporter and NPC Ann is the Psychic         |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Jeff) am the Thief and I have made NPC Lee vulnerable   |
| 5           | NPC Igi  | Reporter    | reveal    | NPC Ann is Psychic                                             |
| 5           | NPC Igi  | Reporter    | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee        |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Gia        |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann        |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Dan       |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee       |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Igi        |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed         |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Bob        |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Igi) am the Reporter and NPC Ann is the Psychic         |
| 5           | NPC Jeff | Thief       | broadcast | I (NPC Jeff) am the Thief and I have made NPC Lee vulnerable   |
| 5           | NPC Jeff | Thief       | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee        |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Gia        |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann        |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Dan       |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee       |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Igi        |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed         |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Bob        |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Igi) am the Reporter and NPC Ann is the Psychic         |
| 5           | NPC Ken  | Executioner | broadcast | I (NPC Jeff) am the Thief and I have made NPC Lee vulnerable   |
| 5           | NPC Ken  | Executioner | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee        |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Gia        |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann        |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Dan       |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee       |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Igi        |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed         |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Bob        |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Igi) am the Reporter and NPC Ann is the Psychic         |
| 5           | NPC Lee  | Prophet     | broadcast | I (NPC Jeff) am the Thief and I have made NPC Lee vulnerable   |
| 5           | NPC Lee  | Prophet     | silenced  | You have been silenced                                         |
| 5           | NPC Lee  | Prophet     | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee        |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Gia        |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann        |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Dan       |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Lee       |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Igi        |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed         |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Bob        |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Igi) am the Reporter and NPC Ann is the Psychic         |
| 5           | NPC Mark | Judge       | broadcast | I (NPC Jeff) am the Thief and I have made NPC Lee vulnerable   |
| 5           | NPC Mark | Judge       | vote      | Demagog has initiated a vote on eliminating Psychic            |

#### Actions Round 6
| round_index | Player   | action   | Target 1  | Target 2 | status      |
| :-----------| :--------| :--------| :---------| :--------| :---------- |
| 6           | NPC Ann  | Psychic  |           |          | successful  |
| 6           | NPC Cal  | Silencer | NPC Jeff  |          | successful  |
| 6           | NPC Gia  | Spy      |           |          | successful  |
| 6           | NPC Lee  | Prophet  | NPC Bob   |          | successful  |
| 6           | NPC Mark | Judge    | Inspector |          | successful  |

#### States Round 6
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Cal  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Han  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ann  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Bob  | Demagog     | False      | True      | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Jeff | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Mark | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Lee  | Prophet     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Gia  | Spy         | True       | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ken  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan  | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Fae  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Igi  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed     |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee       |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Jeff      |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Lee      |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Fae      |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Han       |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed        |
| 6           | NPC Ann  | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ann       |
| 6           | NPC Ann  | Psychic     | reveal    | Player: NPC Gia is not possessed                              |
| 6           | NPC Ann  | Psychic     | reveal    | Player: NPC Han is not possessed                              |
| 6           | NPC Ann  | Psychic     | reveal    | Player: NPC Ed is not possessed                               |
| 6           | NPC Ann  | Psychic     | reveal    | Player: NPC Jeff is not possessed                             |
| 6           | NPC Ann  | Psychic     | reveal    | Player: NPC Ken is not possessed                              |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed     |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee       |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Jeff      |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Lee      |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Fae      |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Han       |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed        |
| 6           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ann       |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed     |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee       |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Jeff      |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Lee      |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Fae      |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Han       |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed        |
| 6           | NPC Cal  | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ann       |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed     |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee       |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Jeff      |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Lee      |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Fae      |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Han       |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed        |
| 6           | NPC Dan  | Inspector   | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ann       |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed     |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee       |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Jeff      |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Lee      |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Fae      |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Han       |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed        |
| 6           | NPC Ed   | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ann       |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed     |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee       |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Jeff      |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Lee      |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Fae      |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Han       |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed        |
| 6           | NPC Fae  | Priest      | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ann       |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed     |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee       |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Jeff      |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Lee      |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Fae      |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Han       |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed        |
| 6           | NPC Gia  | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ann       |
| 6           | NPC Gia  | Spy         | reveal    | NPC Cal is targeting NPC Jeff                                 |
| 6           | NPC Gia  | Spy         | reveal    | NPC Han is targeting NPC Jeff                                 |
| 6           | NPC Gia  | Spy         | reveal    | NPC Bob is targeting NPC Ann                                  |
| 6           | NPC Gia  | Spy         | reveal    | NPC Jeff is targeting NPC Lee                                 |
| 6           | NPC Gia  | Spy         | reveal    | NPC Mark is targeting NPC Dan                                 |
| 6           | NPC Gia  | Spy         | reveal    | NPC Lee is targeting NPC Han                                  |
| 6           | NPC Gia  | Spy         | reveal    | NPC Dan is targeting NPC Ed                                   |
| 6           | NPC Gia  | Spy         | reveal    | NPC Igi is targeting NPC Ann                                  |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed     |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee       |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Jeff      |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Lee      |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Fae      |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Han       |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed        |
| 6           | NPC Han  | Assassin    | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ann       |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed     |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee       |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Jeff      |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Lee      |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Fae      |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Han       |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed        |
| 6           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ann       |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed     |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee       |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Jeff      |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Lee      |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Fae      |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Han       |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed        |
| 6           | NPC Jeff | Thief       | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ann       |
| 6           | NPC Jeff | Thief       | silenced  | You have been silenced                                        |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed     |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee       |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Jeff      |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Lee      |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Fae      |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Han       |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed        |
| 6           | NPC Ken  | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ann       |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed     |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee       |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Jeff      |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Lee      |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Fae      |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Han       |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed        |
| 6           | NPC Lee  | Prophet     | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ann       |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed  |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed     |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed       |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Cal is targeting NPC Lee       |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Han is targeting NPC Jeff      |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Jeff is targeting NPC Lee      |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Mark is targeting NPC Fae      |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Lee is targeting NPC Han       |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed        |
| 6           | NPC Mark | Judge       | broadcast | I (NPC Gia) am the Spy and NPC Igi is targeting NPC Ann       |