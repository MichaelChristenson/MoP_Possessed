#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 94   | 10      | 3       |

#### Roles
| Role         |
| :----------- |
| Judge        |
| Reporter     |
| Assassin     |
| Executioner  |
| Medic        |
| Jailer       |
| Priest       |
| Demagog      |
| Trader       |
| Inspector    |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ed   | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Jailer      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Ann  | Jailer      | possessed   | You are Possessed         |
| 0           | NPC Bob  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Bob  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Cal  | Trader      | role change | Your Role is Trader       |
| 0           | NPC Cal  | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Dan  | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Judge       | role change | Your Role is Judge        |
| 0           | NPC Ed   | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Fae  | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Gia  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Han  | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Priest      | role change | Your Role is Priest       |
| 0           | NPC Igi  | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Jeff | Demagog     | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 1           | NPC Ann  | Jailer    | NPC Bob  |          | successful          |
| 1           | NPC Cal  | Trader    | NPC Gia  | NPC Ed   | successful          |
| 1           | NPC Dan  | Reporter  | NPC Cal  |          | successful          |
| 1           | NPC Ed   | Judge     | Priest   |          | successful          |
| 1           | NPC Fae  | Assassin  | Medic    |          | successful          |
| 1           | NPC Gia  | Inspector | NPC Fae  |          | successful          |
| 1           | NPC Han  | Medic     | NPC Dan  |          | successful          |
| 1           | NPC Jeff | Demagog   | Priest   |          | voting in progress  |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ed   | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob  | Executioner | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Han  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann  | Jailer      | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Igi  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Jeff | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                   |
| :-----------| :--------| :-----------| :---------| :-------------------------------------------------------- |
| 1           | NPC Ann  | Jailer      | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader     |
| 1           | NPC Ann  | Jailer      | broadcast | I (NPC Gia) inspected NPC Fae and they are not possessed  |
| 1           | NPC Ann  | Jailer      | vote      | Demagog has initiated a vote on eliminating Priest        |
| 1           | NPC Bob  | Executioner | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader     |
| 1           | NPC Bob  | Executioner | broadcast | I (NPC Gia) inspected NPC Fae and they are not possessed  |
| 1           | NPC Bob  | Executioner | vote      | Demagog has initiated a vote on eliminating Priest        |
| 1           | NPC Cal  | Trader      | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader     |
| 1           | NPC Cal  | Trader      | broadcast | I (NPC Gia) inspected NPC Fae and they are not possessed  |
| 1           | NPC Cal  | Trader      | vote      | Demagog has initiated a vote on eliminating Priest        |
| 1           | NPC Dan  | Reporter    | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader     |
| 1           | NPC Dan  | Reporter    | broadcast | I (NPC Gia) inspected NPC Fae and they are not possessed  |
| 1           | NPC Dan  | Reporter    | reveal    | NPC Cal is Trader                                         |
| 1           | NPC Dan  | Reporter    | vote      | Demagog has initiated a vote on eliminating Priest        |
| 1           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader     |
| 1           | NPC Ed   | Inspector   | broadcast | I (NPC Gia) inspected NPC Fae and they are not possessed  |
| 1           | NPC Ed   | Inspector   | vote      | Demagog has initiated a vote on eliminating Priest        |
| 1           | NPC Fae  | Assassin    | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader     |
| 1           | NPC Fae  | Assassin    | broadcast | I (NPC Gia) inspected NPC Fae and they are not possessed  |
| 1           | NPC Fae  | Assassin    | vote      | Demagog has initiated a vote on eliminating Priest        |
| 1           | NPC Gia  | Judge       | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader     |
| 1           | NPC Gia  | Judge       | broadcast | I (NPC Gia) inspected NPC Fae and they are not possessed  |
| 1           | NPC Gia  | Judge       | reveal    | Assassin is Innocent                                      |
| 1           | NPC Gia  | Judge       | vote      | Demagog has initiated a vote on eliminating Priest        |
| 1           | NPC Han  | Medic       | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader     |
| 1           | NPC Han  | Medic       | broadcast | I (NPC Gia) inspected NPC Fae and they are not possessed  |
| 1           | NPC Han  | Medic       | vote      | Demagog has initiated a vote on eliminating Priest        |
| 1           | NPC Igi  | Priest      | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader     |
| 1           | NPC Igi  | Priest      | broadcast | I (NPC Gia) inspected NPC Fae and they are not possessed  |
| 1           | NPC Igi  | Priest      | vote      | Demagog has initiated a vote on eliminating Priest        |
| 1           | NPC Jeff | Demagog     | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader     |
| 1           | NPC Jeff | Demagog     | broadcast | I (NPC Gia) inspected NPC Fae and they are not possessed  |
| 1           | NPC Jeff | Demagog     | vote      | Demagog has initiated a vote on eliminating Priest        |

#### Actions Round 2
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 2           | NPC Dan | Reporter  | NPC Han  |          | successful  |
| 2           | NPC Ed  | Inspector | NPC Jeff |          | successful  |
| 2           | NPC Gia | Judge     | Priest   |          | successful  |
| 2           | NPC Han | Medic     | NPC Fae  |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ed   | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Dan  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Fae  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann  | Jailer      | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Igi  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Jeff | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                   |
| :-----------| :--------| :-----------| :---------| :-------------------------------------------------------- |
| 2           | NPC Ann  | Jailer      | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Medic      |
| 2           | NPC Ann  | Jailer      | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 2           | NPC Bob  | Executioner | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Medic      |
| 2           | NPC Bob  | Executioner | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 2           | NPC Cal  | Trader      | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Medic      |
| 2           | NPC Cal  | Trader      | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Medic      |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 2           | NPC Dan  | Reporter    | reveal    | NPC Han is Medic                                          |
| 2           | NPC Ed   | Inspector   | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Medic      |
| 2           | NPC Ed   | Inspector   | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 2           | NPC Ed   | Inspector   | reveal    | Demagog is Innocent                                       |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Medic      |
| 2           | NPC Fae  | Assassin    | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Medic      |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Medic      |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 2           | NPC Igi  | Priest      | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Medic      |
| 2           | NPC Igi  | Priest      | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |
| 2           | NPC Jeff | Demagog     | broadcast | I (NPC Dan) am the Reporter and NPC Han is the Medic      |
| 2           | NPC Jeff | Demagog     | broadcast | I (NPC Ed) inspected NPC Jeff and they are not possessed  |

#### Actions Round 3
| round_index | Player   | action   | Target 1 | Target 2 | status              |
| :-----------| :--------| :--------| :--------| :--------| :------------------ |
| 3           | NPC Ann  | Jailer   | NPC Fae  |          | successful          |
| 3           | NPC Fae  | Assassin | Demagog  |          | successful          |
| 3           | NPC Gia  | Judge    | Trader   |          | successful          |
| 3           | NPC Han  | Medic    | NPC Bob  |          | successful          |
| 3           | NPC Jeff | Demagog  | Judge    |          | voting in progress  |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ed   | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Dan  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Fae  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Bob  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Han  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann  | Jailer      | False      | True      | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Igi  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Jeff | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Cal  | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message | details                                            |
| :-----------| :--------| :-----------| :-------| :------------------------------------------------- |
| 3           | NPC Ann  | Jailer      | vote    | Demagog has initiated a vote on eliminating Judge  |
| 3           | NPC Bob  | Executioner | vote    | Demagog has initiated a vote on eliminating Judge  |
| 3           | NPC Cal  | Trader      | vote    | Demagog has initiated a vote on eliminating Judge  |
| 3           | NPC Dan  | Reporter    | vote    | Demagog has initiated a vote on eliminating Judge  |
| 3           | NPC Ed   | Inspector   | vote    | Demagog has initiated a vote on eliminating Judge  |
| 3           | NPC Fae  | Assassin    | vote    | Demagog has initiated a vote on eliminating Judge  |
| 3           | NPC Gia  | Judge       | vote    | Demagog has initiated a vote on eliminating Judge  |
| 3           | NPC Han  | Medic       | vote    | Demagog has initiated a vote on eliminating Judge  |
| 3           | NPC Igi  | Priest      | vote    | Demagog has initiated a vote on eliminating Judge  |
| 3           | NPC Jeff | Demagog     | vote    | Demagog has initiated a vote on eliminating Judge  |