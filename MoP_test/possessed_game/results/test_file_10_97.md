#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 97   | 10      | 6       |

#### Roles
| Role       |
| :--------- |
| Priest     |
| Jailer     |
| Judge      |
| Spy        |
| Psychic    |
| Medic      |
| Demagog    |
| Reporter   |
| Assassin   |
| Inspector  |

#### States Round 0
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ed   | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Demagog   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal  | Assassin  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role      | message     | details                 |
| :-----------| :--------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann  | Medic     | role change | Your Role is Medic      |
| 0           | NPC Ann  | Medic     | possessed   | You are Possessed       |
| 0           | NPC Bob  | Spy       | role change | Your Role is Spy        |
| 0           | NPC Bob  | Spy       | possessed   | You are Not Possessed   |
| 0           | NPC Cal  | Assassin  | role change | Your Role is Assassin   |
| 0           | NPC Cal  | Assassin  | possessed   | You are Not Possessed   |
| 0           | NPC Dan  | Jailer    | role change | Your Role is Jailer     |
| 0           | NPC Dan  | Jailer    | possessed   | You are Not Possessed   |
| 0           | NPC Ed   | Priest    | role change | Your Role is Priest     |
| 0           | NPC Ed   | Priest    | possessed   | You are Not Possessed   |
| 0           | NPC Fae  | Judge     | role change | Your Role is Judge      |
| 0           | NPC Fae  | Judge     | possessed   | You are Not Possessed   |
| 0           | NPC Gia  | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Gia  | Inspector | possessed   | You are Not Possessed   |
| 0           | NPC Han  | Psychic   | role change | Your Role is Psychic    |
| 0           | NPC Han  | Psychic   | possessed   | You are Not Possessed   |
| 0           | NPC Igi  | Demagog   | role change | Your Role is Demagog    |
| 0           | NPC Igi  | Demagog   | possessed   | You are Not Possessed   |
| 0           | NPC Jeff | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Jeff | Reporter  | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player   | action    | Target 1  | Target 2 | status              |
| :-----------| :--------| :---------| :---------| :--------| :------------------ |
| 1           | NPC Ann  | Medic     | NPC Dan   |          | successful          |
| 1           | NPC Bob  | Spy       |           |          | successful          |
| 1           | NPC Cal  | Assassin  | Inspector |          | successful          |
| 1           | NPC Fae  | Judge     | Inspector |          | successful          |
| 1           | NPC Gia  | Inspector | NPC Ed    |          | successful          |
| 1           | NPC Han  | Psychic   |           |          | successful          |
| 1           | NPC Igi  | Demagog   | Reporter  |          | voting in progress  |
| 1           | NPC Jeff | Reporter  | NPC Ann   |          | successful          |

#### States Round 1
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ed   | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ann  | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Igi  | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Jeff | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal  | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Gia  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role      | message   | details                                                       |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------ |
| 1           | NPC Ann  | Medic     | broadcast | I (NPC Gia) inspected NPC Ed and they are not possessed       |
| 1           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Ann  | Medic     | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic         |
| 1           | NPC Ann  | Medic     | vote      | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Bob  | Spy       | broadcast | I (NPC Gia) inspected NPC Ed and they are not possessed       |
| 1           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Bob  | Spy       | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic         |
| 1           | NPC Bob  | Spy       | reveal    | NPC Fae is targeting NPC Gia                                  |
| 1           | NPC Bob  | Spy       | reveal    | NPC Jeff is targeting NPC Ann                                 |
| 1           | NPC Bob  | Spy       | reveal    | NPC Gia is targeting NPC Ed                                   |
| 1           | NPC Bob  | Spy       | vote      | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Cal  | Assassin  | broadcast | I (NPC Gia) inspected NPC Ed and they are not possessed       |
| 1           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Cal  | Assassin  | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic         |
| 1           | NPC Cal  | Assassin  | vote      | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Dan  | Jailer    | broadcast | I (NPC Gia) inspected NPC Ed and they are not possessed       |
| 1           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Dan  | Jailer    | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic         |
| 1           | NPC Dan  | Jailer    | vote      | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Ed   | Priest    | broadcast | I (NPC Gia) inspected NPC Ed and they are not possessed       |
| 1           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Ed   | Priest    | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic         |
| 1           | NPC Ed   | Priest    | vote      | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Fae  | Judge     | broadcast | I (NPC Gia) inspected NPC Ed and they are not possessed       |
| 1           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Fae  | Judge     | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic         |
| 1           | NPC Fae  | Judge     | vote      | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Gia  | Inspector | broadcast | I (NPC Gia) inspected NPC Ed and they are not possessed       |
| 1           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Gia  | Inspector | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic         |
| 1           | NPC Gia  | Inspector | reveal    | Priest is Innocent                                            |
| 1           | NPC Gia  | Inspector | vote      | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Han  | Psychic   | broadcast | I (NPC Gia) inspected NPC Ed and they are not possessed       |
| 1           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Han  | Psychic   | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic         |
| 1           | NPC Han  | Psychic   | reveal    | Player: NPC Ed is not possessed                               |
| 1           | NPC Han  | Psychic   | reveal    | Player: NPC Gia is not possessed                              |
| 1           | NPC Han  | Psychic   | reveal    | Player: NPC Fae is not possessed                              |
| 1           | NPC Han  | Psychic   | reveal    | Player: NPC Jeff is not possessed                             |
| 1           | NPC Han  | Psychic   | vote      | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Igi  | Demagog   | broadcast | I (NPC Gia) inspected NPC Ed and they are not possessed       |
| 1           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Igi  | Demagog   | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic         |
| 1           | NPC Igi  | Demagog   | vote      | Demagog has initiated a vote on eliminating Reporter          |
| 1           | NPC Jeff | Reporter  | broadcast | I (NPC Gia) inspected NPC Ed and they are not possessed       |
| 1           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Jeff | Reporter  | broadcast | I (NPC Jeff) am the Reporter and NPC Ann is the Medic         |
| 1           | NPC Jeff | Reporter  | reveal    | NPC Ann is Medic                                              |
| 1           | NPC Jeff | Reporter  | vote      | Demagog has initiated a vote on eliminating Reporter          |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Ann | Medic   | NPC Fae  |          | successful  |
| 2           | NPC Bob | Spy     |          |          | successful  |
| 2           | NPC Fae | Judge   | Medic    |          | successful  |
| 2           | NPC Han | Psychic |          |          | successful  |

#### States Round 2
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ed   | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann  | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Igi  | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Jeff | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal  | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia  | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role      | message   | details                                                        |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------- |
| 2           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Gia        |
| 2           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan        |
| 2           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 2           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 2           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 2           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Gia        |
| 2           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan        |
| 2           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 2           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 2           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 2           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed     |
| 2           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Bob  | Spy       | reveal    | NPC Fae is targeting NPC Ann                                   |
| 2           | NPC Bob  | Spy       | reveal    | NPC Ann is targeting NPC Dan                                   |
| 2           | NPC Bob  | Spy       | reveal    | NPC Igi is targeting NPC Jeff                                  |
| 2           | NPC Bob  | Spy       | reveal    | NPC Jeff is targeting NPC Ann                                  |
| 2           | NPC Bob  | Spy       | reveal    | NPC Cal is targeting NPC Gia                                   |
| 2           | NPC Bob  | Spy       | reveal    | NPC Gia is targeting NPC Ed                                    |
| 2           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Gia        |
| 2           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan        |
| 2           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 2           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 2           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 2           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed     |
| 2           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Gia        |
| 2           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan        |
| 2           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 2           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 2           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 2           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed     |
| 2           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Gia        |
| 2           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan        |
| 2           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 2           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 2           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 2           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Gia        |
| 2           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan        |
| 2           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 2           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 2           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 2           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed     |
| 2           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Gia        |
| 2           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan        |
| 2           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 2           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 2           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 2           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed     |
| 2           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Gia        |
| 2           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan        |
| 2           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 2           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 2           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 2           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed     |
| 2           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Han  | Psychic   | reveal    | Player: NPC Cal is not possessed                               |
| 2           | NPC Han  | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 2           | NPC Han  | Psychic   | reveal    | Player: NPC Jeff is not possessed                              |
| 2           | NPC Han  | Psychic   | reveal    | Player: NPC Fae is not possessed                               |
| 2           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Gia        |
| 2           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan        |
| 2           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 2           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 2           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 2           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed     |
| 2           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 2           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Gia        |
| 2           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan        |
| 2           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 2           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 2           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 2           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 2           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed     |
| 2           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |

#### Actions Round 3
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 3           | NPC Ann  | Medic     | NPC Bob  |          | successful          |
| 3           | NPC Bob  | Spy       |          |          | successful          |
| 3           | NPC Cal  | Assassin  | Demagog  |          | successful          |
| 3           | NPC Fae  | Judge     | Priest   |          | successful          |
| 3           | NPC Gia  | Inspector | NPC Dan  |          | successful          |
| 3           | NPC Han  | Psychic   |          |          | successful          |
| 3           | NPC Igi  | Demagog   | Medic    |          | voting in progress  |
| 3           | NPC Jeff | Reporter  | NPC Dan  |          | successful          |

#### States Round 3
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ed   | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan  | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Fae  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Han  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ann  | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Igi  | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Jeff | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Cal  | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Gia  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role      | message   | details                                                        |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------- |
| 3           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 3           | NPC Ann  | Medic     | broadcast | I (NPC Gia) inspected NPC Dan and they are not possessed       |
| 3           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed        |
| 3           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 3           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Ann  | Medic     | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Ann  | Medic     | vote      | Demagog has initiated a vote on eliminating Medic              |
| 3           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 3           | NPC Bob  | Spy       | broadcast | I (NPC Gia) inspected NPC Dan and they are not possessed       |
| 3           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed        |
| 3           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 3           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Bob  | Spy       | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Bob  | Spy       | reveal    | NPC Fae is targeting NPC Ed                                    |
| 3           | NPC Bob  | Spy       | reveal    | NPC Ann is targeting NPC Fae                                   |
| 3           | NPC Bob  | Spy       | reveal    | NPC Igi is targeting NPC Jeff                                  |
| 3           | NPC Bob  | Spy       | reveal    | NPC Jeff is targeting NPC Dan                                  |
| 3           | NPC Bob  | Spy       | reveal    | NPC Cal is targeting NPC Gia                                   |
| 3           | NPC Bob  | Spy       | reveal    | NPC Gia is targeting NPC Dan                                   |
| 3           | NPC Bob  | Spy       | vote      | Demagog has initiated a vote on eliminating Medic              |
| 3           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 3           | NPC Cal  | Assassin  | broadcast | I (NPC Gia) inspected NPC Dan and they are not possessed       |
| 3           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed        |
| 3           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 3           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Cal  | Assassin  | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Cal  | Assassin  | vote      | Demagog has initiated a vote on eliminating Medic              |
| 3           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 3           | NPC Dan  | Jailer    | broadcast | I (NPC Gia) inspected NPC Dan and they are not possessed       |
| 3           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed        |
| 3           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 3           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Dan  | Jailer    | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Dan  | Jailer    | vote      | Demagog has initiated a vote on eliminating Medic              |
| 3           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 3           | NPC Ed   | Priest    | broadcast | I (NPC Gia) inspected NPC Dan and they are not possessed       |
| 3           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed        |
| 3           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 3           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Ed   | Priest    | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Ed   | Priest    | vote      | Demagog has initiated a vote on eliminating Medic              |
| 3           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 3           | NPC Fae  | Judge     | broadcast | I (NPC Gia) inspected NPC Dan and they are not possessed       |
| 3           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed        |
| 3           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 3           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Fae  | Judge     | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Fae  | Judge     | vote      | Demagog has initiated a vote on eliminating Medic              |
| 3           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 3           | NPC Gia  | Inspector | broadcast | I (NPC Gia) inspected NPC Dan and they are not possessed       |
| 3           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed        |
| 3           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 3           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Gia  | Inspector | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Gia  | Inspector | reveal    | Jailer is Innocent                                             |
| 3           | NPC Gia  | Inspector | vote      | Demagog has initiated a vote on eliminating Medic              |
| 3           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 3           | NPC Han  | Psychic   | broadcast | I (NPC Gia) inspected NPC Dan and they are not possessed       |
| 3           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed        |
| 3           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 3           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Han  | Psychic   | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Han  | Psychic   | reveal    | Player: NPC Ed is not possessed                                |
| 3           | NPC Han  | Psychic   | reveal    | Player: NPC Bob is not possessed                               |
| 3           | NPC Han  | Psychic   | reveal    | Player: NPC Gia is not possessed                               |
| 3           | NPC Han  | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 3           | NPC Han  | Psychic   | vote      | Demagog has initiated a vote on eliminating Medic              |
| 3           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 3           | NPC Igi  | Demagog   | broadcast | I (NPC Gia) inspected NPC Dan and they are not possessed       |
| 3           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed        |
| 3           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 3           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Igi  | Demagog   | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Igi  | Demagog   | vote      | Demagog has initiated a vote on eliminating Medic              |
| 3           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann        |
| 3           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae        |
| 3           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ann       |
| 3           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia        |
| 3           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed         |
| 3           | NPC Jeff | Reporter  | broadcast | I (NPC Gia) inspected NPC Dan and they are not possessed       |
| 3           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed        |
| 3           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 3           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Jeff | Reporter  | broadcast | I (NPC Jeff) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Jeff | Reporter  | reveal    | NPC Dan is Jailer                                              |
| 3           | NPC Jeff | Reporter  | vote      | Demagog has initiated a vote on eliminating Medic              |

#### Actions Round 4
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 4           | NPC Ann | Medic   | NPC Han  |          | successful  |
| 4           | NPC Bob | Spy     |          |          | successful  |
| 4           | NPC Fae | Judge   | Priest   |          | successful  |
| 4           | NPC Han | Psychic |          |          | successful  |

#### States Round 4
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ed   | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan  | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Han  | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann  | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Igi  | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Jeff | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Cal  | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Gia  | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role      | message   | details                                                        |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------- |
| 4           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed         |
| 4           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Bob        |
| 4           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann        |
| 4           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan       |
| 4           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi        |
| 4           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan        |
| 4           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 4           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 4           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed         |
| 4           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Bob        |
| 4           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann        |
| 4           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan       |
| 4           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi        |
| 4           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan        |
| 4           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 4           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 4           | NPC Bob  | Spy       | reveal    | NPC Fae is targeting NPC Ed                                    |
| 4           | NPC Bob  | Spy       | reveal    | NPC Ann is targeting NPC Bob                                   |
| 4           | NPC Bob  | Spy       | reveal    | NPC Igi is targeting NPC Ann                                   |
| 4           | NPC Bob  | Spy       | reveal    | NPC Jeff is targeting NPC Dan                                  |
| 4           | NPC Bob  | Spy       | reveal    | NPC Cal is targeting NPC Igi                                   |
| 4           | NPC Bob  | Spy       | reveal    | NPC Gia is targeting NPC Dan                                   |
| 4           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed         |
| 4           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Bob        |
| 4           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann        |
| 4           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan       |
| 4           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi        |
| 4           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan        |
| 4           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 4           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 4           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed         |
| 4           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Bob        |
| 4           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann        |
| 4           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan       |
| 4           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi        |
| 4           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan        |
| 4           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 4           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 4           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed         |
| 4           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Bob        |
| 4           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann        |
| 4           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan       |
| 4           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi        |
| 4           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan        |
| 4           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 4           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 4           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed         |
| 4           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Bob        |
| 4           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann        |
| 4           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan       |
| 4           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi        |
| 4           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan        |
| 4           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 4           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 4           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed         |
| 4           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Bob        |
| 4           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann        |
| 4           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan       |
| 4           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi        |
| 4           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan        |
| 4           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 4           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 4           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed         |
| 4           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Bob        |
| 4           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann        |
| 4           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan       |
| 4           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi        |
| 4           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan        |
| 4           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 4           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 4           | NPC Han  | Psychic   | reveal    | Player: NPC Cal is not possessed                               |
| 4           | NPC Han  | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 4           | NPC Han  | Psychic   | reveal    | Player: NPC Bob is not possessed                               |
| 4           | NPC Han  | Psychic   | reveal    | Player: NPC Gia is not possessed                               |
| 4           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed         |
| 4           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Bob        |
| 4           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann        |
| 4           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan       |
| 4           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi        |
| 4           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan        |
| 4           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 4           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |
| 4           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed         |
| 4           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Bob        |
| 4           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann        |
| 4           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan       |
| 4           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi        |
| 4           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan        |
| 4           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed      |
| 4           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed   |

#### Actions Round 5
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 5           | NPC Ann  | Medic     | NPC Igi  |          | successful          |
| 5           | NPC Bob  | Spy       |          |          | successful          |
| 5           | NPC Cal  | Assassin  | Jailer   |          | successful          |
| 5           | NPC Fae  | Judge     | Psychic  |          | successful          |
| 5           | NPC Gia  | Inspector | NPC Cal  |          | successful          |
| 5           | NPC Han  | Psychic   |          |          | successful          |
| 5           | NPC Igi  | Demagog   | Priest   |          | voting in progress  |
| 5           | NPC Jeff | Reporter  | NPC Ed   |          | successful          |

#### States Round 5
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ed   | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan  | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Fae  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Han  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Ann  | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Igi  | Demagog   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Jeff | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Cal  | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Gia  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player   | Role      | message   | details                                                       |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------ |
| 5           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Han       |
| 5           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann       |
| 5           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 5           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi       |
| 5           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan       |
| 5           | NPC Ann  | Medic     | broadcast | I (NPC Gia) inspected NPC Cal and they are not possessed      |
| 5           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed    |
| 5           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 5           | NPC Ann  | Medic     | broadcast | I (NPC Jeff) am the Reporter and NPC Ed is the Priest         |
| 5           | NPC Ann  | Medic     | vote      | Demagog has initiated a vote on eliminating Priest            |
| 5           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Han       |
| 5           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann       |
| 5           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 5           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi       |
| 5           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan       |
| 5           | NPC Bob  | Spy       | broadcast | I (NPC Gia) inspected NPC Cal and they are not possessed      |
| 5           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed    |
| 5           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 5           | NPC Bob  | Spy       | broadcast | I (NPC Jeff) am the Reporter and NPC Ed is the Priest         |
| 5           | NPC Bob  | Spy       | reveal    | NPC Fae is targeting NPC Han                                  |
| 5           | NPC Bob  | Spy       | reveal    | NPC Ann is targeting NPC Han                                  |
| 5           | NPC Bob  | Spy       | reveal    | NPC Igi is targeting NPC Ann                                  |
| 5           | NPC Bob  | Spy       | reveal    | NPC Jeff is targeting NPC Ed                                  |
| 5           | NPC Bob  | Spy       | reveal    | NPC Cal is targeting NPC Igi                                  |
| 5           | NPC Bob  | Spy       | reveal    | NPC Gia is targeting NPC Cal                                  |
| 5           | NPC Bob  | Spy       | vote      | Demagog has initiated a vote on eliminating Priest            |
| 5           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Han       |
| 5           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann       |
| 5           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 5           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi       |
| 5           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan       |
| 5           | NPC Cal  | Assassin  | broadcast | I (NPC Gia) inspected NPC Cal and they are not possessed      |
| 5           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed    |
| 5           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 5           | NPC Cal  | Assassin  | broadcast | I (NPC Jeff) am the Reporter and NPC Ed is the Priest         |
| 5           | NPC Cal  | Assassin  | vote      | Demagog has initiated a vote on eliminating Priest            |
| 5           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Han       |
| 5           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann       |
| 5           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 5           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi       |
| 5           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan       |
| 5           | NPC Dan  | Jailer    | broadcast | I (NPC Gia) inspected NPC Cal and they are not possessed      |
| 5           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed    |
| 5           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 5           | NPC Dan  | Jailer    | broadcast | I (NPC Jeff) am the Reporter and NPC Ed is the Priest         |
| 5           | NPC Dan  | Jailer    | vote      | Demagog has initiated a vote on eliminating Priest            |
| 5           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Han       |
| 5           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann       |
| 5           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 5           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi       |
| 5           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan       |
| 5           | NPC Ed   | Priest    | broadcast | I (NPC Gia) inspected NPC Cal and they are not possessed      |
| 5           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed    |
| 5           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 5           | NPC Ed   | Priest    | broadcast | I (NPC Jeff) am the Reporter and NPC Ed is the Priest         |
| 5           | NPC Ed   | Priest    | vote      | Demagog has initiated a vote on eliminating Priest            |
| 5           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Han       |
| 5           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann       |
| 5           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 5           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi       |
| 5           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan       |
| 5           | NPC Fae  | Judge     | broadcast | I (NPC Gia) inspected NPC Cal and they are not possessed      |
| 5           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed    |
| 5           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 5           | NPC Fae  | Judge     | broadcast | I (NPC Jeff) am the Reporter and NPC Ed is the Priest         |
| 5           | NPC Fae  | Judge     | vote      | Demagog has initiated a vote on eliminating Priest            |
| 5           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Han       |
| 5           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann       |
| 5           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 5           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi       |
| 5           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan       |
| 5           | NPC Gia  | Inspector | broadcast | I (NPC Gia) inspected NPC Cal and they are not possessed      |
| 5           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed    |
| 5           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 5           | NPC Gia  | Inspector | broadcast | I (NPC Jeff) am the Reporter and NPC Ed is the Priest         |
| 5           | NPC Gia  | Inspector | reveal    | Assassin is Innocent                                          |
| 5           | NPC Gia  | Inspector | vote      | Demagog has initiated a vote on eliminating Priest            |
| 5           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Han       |
| 5           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann       |
| 5           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 5           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi       |
| 5           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan       |
| 5           | NPC Han  | Psychic   | broadcast | I (NPC Gia) inspected NPC Cal and they are not possessed      |
| 5           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed    |
| 5           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 5           | NPC Han  | Psychic   | broadcast | I (NPC Jeff) am the Reporter and NPC Ed is the Priest         |
| 5           | NPC Han  | Psychic   | reveal    | Player: NPC Jeff is not possessed                             |
| 5           | NPC Han  | Psychic   | reveal    | Player: NPC Ed is not possessed                               |
| 5           | NPC Han  | Psychic   | reveal    | Player: NPC Fae is not possessed                              |
| 5           | NPC Han  | Psychic   | reveal    | Player: NPC Dan is not possessed                              |
| 5           | NPC Han  | Psychic   | vote      | Demagog has initiated a vote on eliminating Priest            |
| 5           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Han       |
| 5           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann       |
| 5           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 5           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi       |
| 5           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan       |
| 5           | NPC Igi  | Demagog   | broadcast | I (NPC Gia) inspected NPC Cal and they are not possessed      |
| 5           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed    |
| 5           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 5           | NPC Igi  | Demagog   | broadcast | I (NPC Jeff) am the Reporter and NPC Ed is the Priest         |
| 5           | NPC Igi  | Demagog   | vote      | Demagog has initiated a vote on eliminating Priest            |
| 5           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Han       |
| 5           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ann       |
| 5           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 5           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Igi       |
| 5           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Dan       |
| 5           | NPC Jeff | Reporter  | broadcast | I (NPC Gia) inspected NPC Cal and they are not possessed      |
| 5           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed    |
| 5           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 5           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 5           | NPC Jeff | Reporter  | broadcast | I (NPC Jeff) am the Reporter and NPC Ed is the Priest         |
| 5           | NPC Jeff | Reporter  | reveal    | NPC Ed is Priest                                              |
| 5           | NPC Jeff | Reporter  | vote      | Demagog has initiated a vote on eliminating Priest            |

#### Actions Round 6
| round_index | Player  | action  | Target 1 | Target 2 | status              |
| :-----------| :-------| :-------| :--------| :--------| :------------------ |
| 6           | NPC Ann | Medic   | NPC Jeff |          | successful          |
| 6           | NPC Bob | Spy     |          |          | successful          |
| 6           | NPC Fae | Judge   | Jailer   |          | successful          |
| 6           | NPC Han | Psychic |          |          | successful          |
| 6           | NPC Igi | Demagog | Assassin |          | voting in progress  |

#### States Round 6
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Ed   | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan  | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Fae  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob  | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Han  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ann  | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Igi  | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Jeff | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Cal  | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Gia  | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player   | Role      | message   | details                                                       |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------ |
| 6           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han       |
| 6           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Igi       |
| 6           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ed        |
| 6           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ed       |
| 6           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan       |
| 6           | NPC Ann  | Medic     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Cal       |
| 6           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 6           | NPC Ann  | Medic     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 6           | NPC Ann  | Medic     | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 6           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han       |
| 6           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Igi       |
| 6           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ed        |
| 6           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ed       |
| 6           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan       |
| 6           | NPC Bob  | Spy       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Cal       |
| 6           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 6           | NPC Bob  | Spy       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 6           | NPC Bob  | Spy       | reveal    | NPC Fae is targeting NPC Dan                                  |
| 6           | NPC Bob  | Spy       | reveal    | NPC Ann is targeting NPC Igi                                  |
| 6           | NPC Bob  | Spy       | reveal    | NPC Igi is targeting NPC Ed                                   |
| 6           | NPC Bob  | Spy       | reveal    | NPC Jeff is targeting NPC Ed                                  |
| 6           | NPC Bob  | Spy       | reveal    | NPC Cal is targeting NPC Dan                                  |
| 6           | NPC Bob  | Spy       | reveal    | NPC Gia is targeting NPC Cal                                  |
| 6           | NPC Bob  | Spy       | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 6           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han       |
| 6           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Igi       |
| 6           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ed        |
| 6           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ed       |
| 6           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan       |
| 6           | NPC Cal  | Assassin  | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Cal       |
| 6           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 6           | NPC Cal  | Assassin  | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 6           | NPC Cal  | Assassin  | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 6           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han       |
| 6           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Igi       |
| 6           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ed        |
| 6           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ed       |
| 6           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan       |
| 6           | NPC Dan  | Jailer    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Cal       |
| 6           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 6           | NPC Dan  | Jailer    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 6           | NPC Dan  | Jailer    | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 6           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han       |
| 6           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Igi       |
| 6           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ed        |
| 6           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ed       |
| 6           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan       |
| 6           | NPC Ed   | Priest    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Cal       |
| 6           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 6           | NPC Ed   | Priest    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 6           | NPC Ed   | Priest    | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 6           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han       |
| 6           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Igi       |
| 6           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ed        |
| 6           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ed       |
| 6           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan       |
| 6           | NPC Fae  | Judge     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Cal       |
| 6           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 6           | NPC Fae  | Judge     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 6           | NPC Fae  | Judge     | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 6           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han       |
| 6           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Igi       |
| 6           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ed        |
| 6           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ed       |
| 6           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan       |
| 6           | NPC Gia  | Inspector | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Cal       |
| 6           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 6           | NPC Gia  | Inspector | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 6           | NPC Gia  | Inspector | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 6           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han       |
| 6           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Igi       |
| 6           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ed        |
| 6           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ed       |
| 6           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan       |
| 6           | NPC Han  | Psychic   | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Cal       |
| 6           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 6           | NPC Han  | Psychic   | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 6           | NPC Han  | Psychic   | reveal    | Player: NPC Cal is not possessed                              |
| 6           | NPC Han  | Psychic   | reveal    | Player: NPC Fae is not possessed                              |
| 6           | NPC Han  | Psychic   | reveal    | Player: NPC Igi is not possessed                              |
| 6           | NPC Han  | Psychic   | reveal    | Player: NPC Bob is not possessed                              |
| 6           | NPC Han  | Psychic   | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 6           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han       |
| 6           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Igi       |
| 6           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ed        |
| 6           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ed       |
| 6           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan       |
| 6           | NPC Igi  | Demagog   | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Cal       |
| 6           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 6           | NPC Igi  | Demagog   | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 6           | NPC Igi  | Demagog   | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 6           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han       |
| 6           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Igi       |
| 6           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Igi is targeting NPC Ed        |
| 6           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Ed       |
| 6           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan       |
| 6           | NPC Jeff | Reporter  | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Cal       |
| 6           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 6           | NPC Jeff | Reporter  | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 6           | NPC Jeff | Reporter  | vote      | Demagog has initiated a vote on eliminating Assassin          |