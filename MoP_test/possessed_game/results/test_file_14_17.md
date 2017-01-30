#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 17   | 14      | 2       |

#### Roles
| Role       |
| :--------- |
| Jailer     |
| Demagog    |
| Reporter   |
| Prophet    |
| Psychic    |
| Spy        |
| Thief      |
| Priest     |
| Inspector  |
| Judge      |
| Assassin   |
| Silencer   |
| Trader     |
| Medic      |

#### States Round 0
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal  | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Norm | Demagog   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Assassin  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Silencer  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Mark | Trader    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role      | message     | details                 |
| :-----------| :--------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann  | Psychic   | role change | Your Role is Psychic    |
| 0           | NPC Ann  | Psychic   | possessed   | You are Not Possessed   |
| 0           | NPC Bob  | Priest    | role change | Your Role is Priest     |
| 0           | NPC Bob  | Priest    | possessed   | You are Not Possessed   |
| 0           | NPC Cal  | Jailer    | role change | Your Role is Jailer     |
| 0           | NPC Cal  | Jailer    | possessed   | You are Not Possessed   |
| 0           | NPC Dan  | Assassin  | role change | Your Role is Assassin   |
| 0           | NPC Dan  | Assassin  | possessed   | You are Not Possessed   |
| 0           | NPC Ed   | Silencer  | role change | Your Role is Silencer   |
| 0           | NPC Ed   | Silencer  | possessed   | You are Not Possessed   |
| 0           | NPC Fae  | Prophet   | role change | Your Role is Prophet    |
| 0           | NPC Fae  | Prophet   | possessed   | You are Not Possessed   |
| 0           | NPC Gia  | Thief     | role change | Your Role is Thief      |
| 0           | NPC Gia  | Thief     | possessed   | You are Not Possessed   |
| 0           | NPC Han  | Judge     | role change | Your Role is Judge      |
| 0           | NPC Han  | Judge     | possessed   | You are Not Possessed   |
| 0           | NPC Igi  | Spy       | role change | Your Role is Spy        |
| 0           | NPC Igi  | Spy       | possessed   | You are Not Possessed   |
| 0           | NPC Jeff | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Jeff | Inspector | possessed   | You are Not Possessed   |
| 0           | NPC Ken  | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Ken  | Reporter  | possessed   | You are Not Possessed   |
| 0           | NPC Lee  | Medic     | role change | Your Role is Medic      |
| 0           | NPC Lee  | Medic     | possessed   | You are Not Possessed   |
| 0           | NPC Mark | Trader    | role change | Your Role is Trader     |
| 0           | NPC Mark | Trader    | possessed   | You are Not Possessed   |
| 0           | NPC Norm | Demagog   | role change | Your Role is Demagog    |
| 0           | NPC Norm | Demagog   | possessed   | You are Possessed       |

#### Actions Round 1
| round_index | Player   | action    | Target 1 | Target 2 | status                         |
| :-----------| :--------| :---------| :--------| :--------| :----------------------------- |
| 1           | NPC Ann  | Psychic   |          |          | successful                     |
| 1           | NPC Dan  | Assassin  | Reporter |          | successful                     |
| 1           | NPC Ed   | Silencer  | NPC Han  |          | successful                     |
| 1           | NPC Fae  | Prophet   | NPC Norm |          | successful                     |
| 1           | NPC Gia  | Thief     | NPC Ann  |          | successful                     |
| 1           | NPC Han  | Judge     | Demagog  |          | successful                     |
| 1           | NPC Igi  | Spy       |          |          | successful                     |
| 1           | NPC Jeff | Inspector | NPC Ken  |          | successful                     |
| 1           | NPC Ken  | Reporter  | NPC Lee  |          | successful                     |
| 1           | NPC Lee  | Medic     | NPC Norm |          | successful                     |
| 1           | NPC Mark | Trader    | NPC Igi  | NPC Lee  | failed because not vulnerable  |
| 1           | NPC Norm | Demagog   | Thief    |          | voting in progress             |

#### States Round 1
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal  | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Norm | Demagog   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ken  | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Fae  | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann  | Psychic   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 1           | NPC Igi  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia  | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob  | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Jeff | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Han  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed   | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Mark | Trader    | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Lee  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role      | message   | details                                                        |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------- |
| 1           | NPC Ann  | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Ann  | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Ann  | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ann  | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ann  | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ann  | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Ann  | Psychic   | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Ann  | Psychic   | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Ann  | Psychic   | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Ann  | Psychic   | reveal    | Player: NPC Fae is not possessed                               |
| 1           | NPC Ann  | Psychic   | reveal    | Player: NPC Ed is not possessed                                |
| 1           | NPC Ann  | Psychic   | reveal    | Player: NPC Igi is not possessed                               |
| 1           | NPC Ann  | Psychic   | reveal    | Player: NPC Ken is not possessed                               |
| 1           | NPC Ann  | Psychic   | reveal    | Player: NPC Han is not possessed                               |
| 1           | NPC Ann  | Psychic   | reveal    | Player: NPC Mark is not possessed                              |
| 1           | NPC Ann  | Psychic   | vote      | Demagog has initiated a vote on eliminating Thief              |
| 1           | NPC Bob  | Priest    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Bob  | Priest    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Bob  | Priest    | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Bob  | Priest    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Bob  | Priest    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob  | Priest    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Bob  | Priest    | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Bob  | Priest    | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Bob  | Priest    | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Bob  | Priest    | vote      | Demagog has initiated a vote on eliminating Thief              |
| 1           | NPC Cal  | Jailer    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Cal  | Jailer    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Cal  | Jailer    | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Cal  | Jailer    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Cal  | Jailer    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Cal  | Jailer    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Cal  | Jailer    | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Cal  | Jailer    | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Cal  | Jailer    | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Cal  | Jailer    | vote      | Demagog has initiated a vote on eliminating Thief              |
| 1           | NPC Dan  | Assassin  | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Dan  | Assassin  | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Dan  | Assassin  | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Dan  | Assassin  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Dan  | Assassin  | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Dan  | Assassin  | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Dan  | Assassin  | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Dan  | Assassin  | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Dan  | Assassin  | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Dan  | Assassin  | vote      | Demagog has initiated a vote on eliminating Thief              |
| 1           | NPC Ed   | Silencer  | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Ed   | Silencer  | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Ed   | Silencer  | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ed   | Silencer  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ed   | Silencer  | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ed   | Silencer  | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Ed   | Silencer  | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Ed   | Silencer  | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Ed   | Silencer  | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Ed   | Silencer  | vote      | Demagog has initiated a vote on eliminating Thief              |
| 1           | NPC Fae  | Prophet   | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Fae  | Prophet   | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Fae  | Prophet   | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Fae  | Prophet   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Fae  | Prophet   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Fae  | Prophet   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Fae  | Prophet   | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Fae  | Prophet   | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Fae  | Prophet   | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Fae  | Prophet   | vote      | Demagog has initiated a vote on eliminating Thief              |
| 1           | NPC Gia  | Thief     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Gia  | Thief     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Gia  | Thief     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Gia  | Thief     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Gia  | Thief     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Gia  | Thief     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Gia  | Thief     | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Gia  | Thief     | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Gia  | Thief     | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Gia  | Thief     | vote      | Demagog has initiated a vote on eliminating Thief              |
| 1           | NPC Han  | Judge     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Han  | Judge     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Han  | Judge     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Han  | Judge     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Han  | Judge     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Han  | Judge     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Han  | Judge     | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Han  | Judge     | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Han  | Judge     | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Han  | Judge     | silenced  | You have been silenced                                         |
| 1           | NPC Han  | Judge     | vote      | Demagog has initiated a vote on eliminating Thief              |
| 1           | NPC Igi  | Spy       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Igi  | Spy       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Igi  | Spy       | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Igi  | Spy       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Igi  | Spy       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Igi  | Spy       | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Igi  | Spy       | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Igi  | Spy       | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Igi  | Spy       | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Igi  | Spy       | reveal    | NPC Ken is targeting NPC Lee                                   |
| 1           | NPC Igi  | Spy       | reveal    | NPC Gia is targeting NPC Ann                                   |
| 1           | NPC Igi  | Spy       | reveal    | NPC Jeff is targeting NPC Ken                                  |
| 1           | NPC Igi  | Spy       | reveal    | NPC Han is targeting NPC Norm                                  |
| 1           | NPC Igi  | Spy       | reveal    | NPC Ed is targeting NPC Han                                    |
| 1           | NPC Igi  | Spy       | vote      | Demagog has initiated a vote on eliminating Thief              |
| 1           | NPC Jeff | Inspector | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Jeff | Inspector | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Jeff | Inspector | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Jeff | Inspector | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Jeff | Inspector | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Jeff | Inspector | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Jeff | Inspector | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Jeff | Inspector | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Jeff | Inspector | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Jeff | Inspector | reveal    | Reporter is Innocent                                           |
| 1           | NPC Jeff | Inspector | vote      | Demagog has initiated a vote on eliminating Thief              |
| 1           | NPC Ken  | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Ken  | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Ken  | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ken  | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ken  | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ken  | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Ken  | Reporter  | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Ken  | Reporter  | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Ken  | Reporter  | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Ken  | Reporter  | reveal    | NPC Lee is Medic                                               |
| 1           | NPC Ken  | Reporter  | vote      | Demagog has initiated a vote on eliminating Thief              |
| 1           | NPC Lee  | Medic     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Lee  | Medic     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Lee  | Medic     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Lee  | Medic     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Lee  | Medic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Lee  | Medic     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Lee  | Medic     | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Lee  | Medic     | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Lee  | Medic     | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Lee  | Medic     | vote      | Demagog has initiated a vote on eliminating Thief              |
| 1           | NPC Mark | Trader    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Mark | Trader    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Mark | Trader    | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Mark | Trader    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Mark | Trader    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Mark | Trader    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Mark | Trader    | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Mark | Trader    | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Mark | Trader    | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Mark | Trader    | vote      | Demagog has initiated a vote on eliminating Thief              |
| 1           | NPC Norm | Demagog   | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed        |
| 1           | NPC Norm | Demagog   | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 1           | NPC Norm | Demagog   | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed      |
| 1           | NPC Norm | Demagog   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Norm | Demagog   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Norm | Demagog   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Norm | Demagog   | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable    |
| 1           | NPC Norm | Demagog   | broadcast | I (NPC Jeff) inspected NPC Ken and they are not possessed      |
| 1           | NPC Norm | Demagog   | broadcast | I (NPC Ken) am the Reporter and NPC Lee is the Medic           |
| 1           | NPC Norm | Demagog   | vote      | Demagog has initiated a vote on eliminating Thief              |

#### Actions Round 2
| round_index | Player   | action   | Target 1 | Target 2 | status              |
| :-----------| :--------| :--------| :--------| :--------| :------------------ |
| 2           | NPC Ann  | Psychic  |          |          | successful          |
| 2           | NPC Ed   | Silencer | NPC Bob  |          | successful          |
| 2           | NPC Fae  | Prophet  | NPC Gia  |          | successful          |
| 2           | NPC Han  | Judge    | Thief    |          | successful          |
| 2           | NPC Igi  | Spy      |          |          | successful          |
| 2           | NPC Lee  | Medic    | NPC Ken  |          | successful          |
| 2           | NPC Norm | Demagog  | Thief    |          | voting in progress  |

#### States Round 2
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal  | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Norm | Demagog   | False      | True      | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Ken  | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae  | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann  | Psychic   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Igi  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Gia  | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Bob  | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Jeff | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Han  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed   | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Mark | Trader    | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Lee  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role      | message   | details                                                        |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------- |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Ann  | Psychic   | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Ann  | Psychic   | reveal    | Player: NPC Fae is not possessed                               |
| 2           | NPC Ann  | Psychic   | reveal    | Player: NPC Han is not possessed                               |
| 2           | NPC Ann  | Psychic   | reveal    | Player: NPC Cal is not possessed                               |
| 2           | NPC Ann  | Psychic   | reveal    | Player: NPC Bob is not possessed                               |
| 2           | NPC Ann  | Psychic   | reveal    | Player: NPC Ken is not possessed                               |
| 2           | NPC Ann  | Psychic   | reveal    | Player: NPC Igi is not possessed                               |
| 2           | NPC Ann  | Psychic   | vote      | Demagog has initiated a vote on eliminating Thief              |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Bob  | Priest    | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Bob  | Priest    | silenced  | You have been silenced                                         |
| 2           | NPC Bob  | Priest    | vote      | Demagog has initiated a vote on eliminating Thief              |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Cal  | Jailer    | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Cal  | Jailer    | vote      | Demagog has initiated a vote on eliminating Thief              |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Dan  | Assassin  | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Dan  | Assassin  | vote      | Demagog has initiated a vote on eliminating Thief              |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Ed   | Silencer  | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Ed   | Silencer  | vote      | Demagog has initiated a vote on eliminating Thief              |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Fae  | Prophet   | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Fae  | Prophet   | vote      | Demagog has initiated a vote on eliminating Thief              |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Gia  | Thief     | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Gia  | Thief     | vote      | Demagog has initiated a vote on eliminating Thief              |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Han  | Judge     | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Han  | Judge     | vote      | Demagog has initiated a vote on eliminating Thief              |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Igi  | Spy       | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Igi  | Spy       | reveal    | NPC Norm is targeting NPC Gia                                  |
| 2           | NPC Igi  | Spy       | reveal    | NPC Ken is targeting NPC Lee                                   |
| 2           | NPC Igi  | Spy       | reveal    | NPC Fae is targeting NPC Norm                                  |
| 2           | NPC Igi  | Spy       | reveal    | NPC Gia is targeting NPC Ann                                   |
| 2           | NPC Igi  | Spy       | reveal    | NPC Jeff is targeting NPC Ken                                  |
| 2           | NPC Igi  | Spy       | reveal    | NPC Han is targeting NPC Gia                                   |
| 2           | NPC Igi  | Spy       | reveal    | NPC Dan is targeting NPC Ken                                   |
| 2           | NPC Igi  | Spy       | reveal    | NPC Ed is targeting NPC Bob                                    |
| 2           | NPC Igi  | Spy       | reveal    | NPC Mark is targeting NPC Igi                                  |
| 2           | NPC Igi  | Spy       | reveal    | NPC Mark is targeting NPC Igi                                  |
| 2           | NPC Igi  | Spy       | reveal    | NPC Lee is targeting NPC Norm                                  |
| 2           | NPC Igi  | Spy       | vote      | Demagog has initiated a vote on eliminating Thief              |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Jeff | Inspector | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Jeff | Inspector | vote      | Demagog has initiated a vote on eliminating Thief              |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Ken  | Reporter  | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Ken  | Reporter  | vote      | Demagog has initiated a vote on eliminating Thief              |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Lee  | Medic     | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Lee  | Medic     | vote      | Demagog has initiated a vote on eliminating Thief              |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Mark | Trader    | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Mark | Trader    | vote      | Demagog has initiated a vote on eliminating Thief              |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed   |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed     |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Igi) am the Spy and NPC Norm is targeting NPC Gia       |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Lee        |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Norm       |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ann        |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ken       |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Igi) am the Spy and NPC Han is targeting NPC Norm       |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Ken        |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Igi) am the Spy and NPC Ed is targeting NPC Han         |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Igi       |
| 2           | NPC Norm | Demagog   | broadcast | I (NPC Igi) am the Spy and NPC Lee is targeting NPC Norm       |
| 2           | NPC Norm | Demagog   | vote      | Demagog has initiated a vote on eliminating Thief              |