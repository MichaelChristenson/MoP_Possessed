#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 77   | 9       | 8       |

#### Roles
| Role       |
| :--------- |
| Inspector  |
| Reporter   |
| Assassin   |
| Priest     |
| Prophet    |
| Jailer     |
| Trader     |
| Demagog    |
| Spy        |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Fae | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi | Assassin  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Prophet   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Trader    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Demagog   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Jailer    | role change | Your Role is Jailer     |
| 0           | NPC Ann | Jailer    | possessed   | You are Not Possessed   |
| 0           | NPC Bob | Trader    | role change | Your Role is Trader     |
| 0           | NPC Bob | Trader    | possessed   | You are Not Possessed   |
| 0           | NPC Cal | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Cal | Reporter  | possessed   | You are Not Possessed   |
| 0           | NPC Dan | Spy       | role change | Your Role is Spy        |
| 0           | NPC Dan | Spy       | possessed   | You are Not Possessed   |
| 0           | NPC Ed  | Prophet   | role change | Your Role is Prophet    |
| 0           | NPC Ed  | Prophet   | possessed   | You are Possessed       |
| 0           | NPC Fae | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Fae | Inspector | possessed   | You are Not Possessed   |
| 0           | NPC Gia | Demagog   | role change | Your Role is Demagog    |
| 0           | NPC Gia | Demagog   | possessed   | You are Not Possessed   |
| 0           | NPC Han | Priest    | role change | Your Role is Priest     |
| 0           | NPC Han | Priest    | possessed   | You are Not Possessed   |
| 0           | NPC Igi | Assassin  | role change | Your Role is Assassin   |
| 0           | NPC Igi | Assassin  | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status              |
| :-----------| :-------| :---------| :--------| :--------| :------------------ |
| 1           | NPC Bob | Trader    | NPC Fae  | NPC Han  | successful          |
| 1           | NPC Cal | Reporter  | NPC Bob  |          | successful          |
| 1           | NPC Dan | Spy       |          |          | successful          |
| 1           | NPC Ed  | Prophet   | NPC Han  |          | successful          |
| 1           | NPC Fae | Inspector | NPC Bob  |          | successful          |
| 1           | NPC Gia | Demagog   | Reporter |          | voting in progress  |
| 1           | NPC Igi | Assassin  | Reporter |          | successful          |

#### States Round 1
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Fae | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Igi | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Han | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Prophet   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Trader    | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Gia | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role      | message   | details                                                   |
| :-----------| :-------| :---------| :---------| :-------------------------------------------------------- |
| 1           | NPC Ann | Jailer    | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Trader     |
| 1           | NPC Ann | Jailer    | broadcast | I (NPC Fae) inspected NPC Bob and they are not possessed  |
| 1           | NPC Ann | Jailer    | vote      | Demagog has initiated a vote on eliminating Reporter      |
| 1           | NPC Bob | Trader    | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Trader     |
| 1           | NPC Bob | Trader    | broadcast | I (NPC Fae) inspected NPC Bob and they are not possessed  |
| 1           | NPC Bob | Trader    | vote      | Demagog has initiated a vote on eliminating Reporter      |
| 1           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Trader     |
| 1           | NPC Cal | Reporter  | broadcast | I (NPC Fae) inspected NPC Bob and they are not possessed  |
| 1           | NPC Cal | Reporter  | reveal    | NPC Bob is Trader                                         |
| 1           | NPC Cal | Reporter  | vote      | Demagog has initiated a vote on eliminating Reporter      |
| 1           | NPC Dan | Spy       | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Trader     |
| 1           | NPC Dan | Spy       | broadcast | I (NPC Fae) inspected NPC Bob and they are not possessed  |
| 1           | NPC Dan | Spy       | reveal    | NPC Fae is targeting NPC Bob                              |
| 1           | NPC Dan | Spy       | reveal    | NPC Cal is targeting NPC Bob                              |
| 1           | NPC Dan | Spy       | vote      | Demagog has initiated a vote on eliminating Reporter      |
| 1           | NPC Ed  | Prophet   | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Trader     |
| 1           | NPC Ed  | Prophet   | broadcast | I (NPC Fae) inspected NPC Bob and they are not possessed  |
| 1           | NPC Ed  | Prophet   | vote      | Demagog has initiated a vote on eliminating Reporter      |
| 1           | NPC Fae | Priest    | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Trader     |
| 1           | NPC Fae | Priest    | broadcast | I (NPC Fae) inspected NPC Bob and they are not possessed  |
| 1           | NPC Fae | Priest    | reveal    | Trader is Innocent                                        |
| 1           | NPC Fae | Priest    | vote      | Demagog has initiated a vote on eliminating Reporter      |
| 1           | NPC Gia | Demagog   | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Trader     |
| 1           | NPC Gia | Demagog   | broadcast | I (NPC Fae) inspected NPC Bob and they are not possessed  |
| 1           | NPC Gia | Demagog   | vote      | Demagog has initiated a vote on eliminating Reporter      |
| 1           | NPC Han | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Trader     |
| 1           | NPC Han | Inspector | broadcast | I (NPC Fae) inspected NPC Bob and they are not possessed  |
| 1           | NPC Han | Inspector | vote      | Demagog has initiated a vote on eliminating Reporter      |
| 1           | NPC Igi | Assassin  | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Trader     |
| 1           | NPC Igi | Assassin  | broadcast | I (NPC Fae) inspected NPC Bob and they are not possessed  |
| 1           | NPC Igi | Assassin  | vote      | Demagog has initiated a vote on eliminating Reporter      |

#### Actions Round 2
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 2           | NPC Dan | Spy       |          |          | successful  |
| 2           | NPC Ed  | Prophet   | NPC Fae  |          | successful  |
| 2           | NPC Han | Inspector | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Fae | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Igi | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Han | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Ed  | Prophet   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Trader    | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Gia | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role      | message   | details                                                   |
| :-----------| :-------| :---------| :---------| :-------------------------------------------------------- |
| 2           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob   |
| 2           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal   |
| 2           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 2           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal   |
| 2           | NPC Ann | Jailer    | broadcast | I (NPC Han) inspected NPC Ann and they are not possessed  |
| 2           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob   |
| 2           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal   |
| 2           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 2           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal   |
| 2           | NPC Bob | Trader    | broadcast | I (NPC Han) inspected NPC Ann and they are not possessed  |
| 2           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob   |
| 2           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal   |
| 2           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 2           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal   |
| 2           | NPC Cal | Reporter  | broadcast | I (NPC Han) inspected NPC Ann and they are not possessed  |
| 2           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob   |
| 2           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal   |
| 2           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 2           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal   |
| 2           | NPC Dan | Spy       | broadcast | I (NPC Han) inspected NPC Ann and they are not possessed  |
| 2           | NPC Dan | Spy       | reveal    | NPC Cal is targeting NPC Bob                              |
| 2           | NPC Dan | Spy       | reveal    | NPC Igi is targeting NPC Cal                              |
| 2           | NPC Dan | Spy       | reveal    | NPC Han is targeting NPC Ann                              |
| 2           | NPC Dan | Spy       | reveal    | NPC Ed is targeting NPC Han                               |
| 2           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Fae                              |
| 2           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Fae                              |
| 2           | NPC Dan | Spy       | reveal    | NPC Gia is targeting NPC Cal                              |
| 2           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob   |
| 2           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal   |
| 2           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 2           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal   |
| 2           | NPC Ed  | Prophet   | broadcast | I (NPC Han) inspected NPC Ann and they are not possessed  |
| 2           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob   |
| 2           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal   |
| 2           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 2           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal   |
| 2           | NPC Fae | Priest    | broadcast | I (NPC Han) inspected NPC Ann and they are not possessed  |
| 2           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob   |
| 2           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal   |
| 2           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 2           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal   |
| 2           | NPC Gia | Demagog   | broadcast | I (NPC Han) inspected NPC Ann and they are not possessed  |
| 2           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob   |
| 2           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal   |
| 2           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 2           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal   |
| 2           | NPC Han | Inspector | broadcast | I (NPC Han) inspected NPC Ann and they are not possessed  |
| 2           | NPC Han | Inspector | reveal    | Jailer is Innocent                                        |
| 2           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob   |
| 2           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal   |
| 2           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 2           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 2           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal   |
| 2           | NPC Igi | Assassin  | broadcast | I (NPC Han) inspected NPC Ann and they are not possessed  |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 3           | NPC Cal | Reporter | NPC Dan  |          | successful          |
| 3           | NPC Dan | Spy      |          |          | successful          |
| 3           | NPC Ed  | Prophet  | NPC Ann  |          | successful          |
| 3           | NPC Gia | Demagog  | Trader   |          | voting in progress  |
| 3           | NPC Igi | Assassin | Prophet  |          | successful          |

#### States Round 3
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Fae | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Igi | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Han | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ed  | Prophet   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob | Trader    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Gia | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role      | message   | details                                                  |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------- |
| 3           | NPC Ann | Jailer    | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Spy       |
| 3           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob  |
| 3           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal  |
| 3           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann  |
| 3           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae   |
| 3           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal  |
| 3           | NPC Ann | Jailer    | vote      | Demagog has initiated a vote on eliminating Trader       |
| 3           | NPC Bob | Trader    | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Spy       |
| 3           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob  |
| 3           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal  |
| 3           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann  |
| 3           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae   |
| 3           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal  |
| 3           | NPC Bob | Trader    | vote      | Demagog has initiated a vote on eliminating Trader       |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Spy       |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob  |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal  |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann  |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae   |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal  |
| 3           | NPC Cal | Reporter  | reveal    | NPC Dan is Spy                                           |
| 3           | NPC Cal | Reporter  | vote      | Demagog has initiated a vote on eliminating Trader       |
| 3           | NPC Dan | Spy       | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Spy       |
| 3           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob  |
| 3           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal  |
| 3           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann  |
| 3           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae   |
| 3           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal  |
| 3           | NPC Dan | Spy       | reveal    | NPC Cal is targeting NPC Dan                             |
| 3           | NPC Dan | Spy       | reveal    | NPC Igi is targeting NPC Cal                             |
| 3           | NPC Dan | Spy       | reveal    | NPC Han is targeting NPC Ann                             |
| 3           | NPC Dan | Spy       | reveal    | NPC Ed is targeting NPC Fae                              |
| 3           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Fae                             |
| 3           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Fae                             |
| 3           | NPC Dan | Spy       | reveal    | NPC Gia is targeting NPC Cal                             |
| 3           | NPC Dan | Spy       | vote      | Demagog has initiated a vote on eliminating Trader       |
| 3           | NPC Ed  | Prophet   | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Spy       |
| 3           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob  |
| 3           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal  |
| 3           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann  |
| 3           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae   |
| 3           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal  |
| 3           | NPC Ed  | Prophet   | vote      | Demagog has initiated a vote on eliminating Trader       |
| 3           | NPC Fae | Priest    | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Spy       |
| 3           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob  |
| 3           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal  |
| 3           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann  |
| 3           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae   |
| 3           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal  |
| 3           | NPC Fae | Priest    | vote      | Demagog has initiated a vote on eliminating Trader       |
| 3           | NPC Gia | Demagog   | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Spy       |
| 3           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob  |
| 3           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal  |
| 3           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann  |
| 3           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae   |
| 3           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal  |
| 3           | NPC Gia | Demagog   | vote      | Demagog has initiated a vote on eliminating Trader       |
| 3           | NPC Han | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Spy       |
| 3           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob  |
| 3           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal  |
| 3           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann  |
| 3           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae   |
| 3           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal  |
| 3           | NPC Han | Inspector | vote      | Demagog has initiated a vote on eliminating Trader       |
| 3           | NPC Igi | Assassin  | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Spy       |
| 3           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Bob  |
| 3           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Cal  |
| 3           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann  |
| 3           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Fae   |
| 3           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 3           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Cal  |
| 3           | NPC Igi | Assassin  | vote      | Demagog has initiated a vote on eliminating Trader       |

#### Actions Round 4
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 4           | NPC Dan | Spy       |          |          | successful  |
| 4           | NPC Ed  | Prophet   | NPC Bob  |          | successful  |
| 4           | NPC Han | Inspector | NPC Fae  |          | successful  |

#### States Round 4
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Fae | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Igi | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Han | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Ed  | Prophet   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob | Trader    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Gia | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role      | message   | details                                                   |
| :-----------| :-------| :---------| :---------| :-------------------------------------------------------- |
| 4           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan   |
| 4           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed    |
| 4           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann   |
| 4           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ann    |
| 4           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob   |
| 4           | NPC Ann | Jailer    | broadcast | I (NPC Han) inspected NPC Fae and they are not possessed  |
| 4           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan   |
| 4           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed    |
| 4           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann   |
| 4           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ann    |
| 4           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob   |
| 4           | NPC Bob | Trader    | broadcast | I (NPC Han) inspected NPC Fae and they are not possessed  |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan   |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed    |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann   |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ann    |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob   |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Han) inspected NPC Fae and they are not possessed  |
| 4           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan   |
| 4           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed    |
| 4           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann   |
| 4           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ann    |
| 4           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob   |
| 4           | NPC Dan | Spy       | broadcast | I (NPC Han) inspected NPC Fae and they are not possessed  |
| 4           | NPC Dan | Spy       | reveal    | NPC Cal is targeting NPC Dan                              |
| 4           | NPC Dan | Spy       | reveal    | NPC Igi is targeting NPC Ed                               |
| 4           | NPC Dan | Spy       | reveal    | NPC Han is targeting NPC Fae                              |
| 4           | NPC Dan | Spy       | reveal    | NPC Ed is targeting NPC Ann                               |
| 4           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Fae                              |
| 4           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Fae                              |
| 4           | NPC Dan | Spy       | reveal    | NPC Gia is targeting NPC Bob                              |
| 4           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan   |
| 4           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed    |
| 4           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann   |
| 4           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ann    |
| 4           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob   |
| 4           | NPC Ed  | Prophet   | broadcast | I (NPC Han) inspected NPC Fae and they are not possessed  |
| 4           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan   |
| 4           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed    |
| 4           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann   |
| 4           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ann    |
| 4           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob   |
| 4           | NPC Fae | Priest    | broadcast | I (NPC Han) inspected NPC Fae and they are not possessed  |
| 4           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan   |
| 4           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed    |
| 4           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann   |
| 4           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ann    |
| 4           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob   |
| 4           | NPC Gia | Demagog   | broadcast | I (NPC Han) inspected NPC Fae and they are not possessed  |
| 4           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan   |
| 4           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed    |
| 4           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann   |
| 4           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ann    |
| 4           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob   |
| 4           | NPC Han | Inspector | broadcast | I (NPC Han) inspected NPC Fae and they are not possessed  |
| 4           | NPC Han | Inspector | reveal    | Priest is Innocent                                        |
| 4           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan   |
| 4           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed    |
| 4           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Ann   |
| 4           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Ann    |
| 4           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae   |
| 4           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob   |
| 4           | NPC Igi | Assassin  | broadcast | I (NPC Han) inspected NPC Fae and they are not possessed  |

#### Actions Round 5
| round_index | Player  | action   | Target 1  | Target 2 | status                         |
| :-----------| :-------| :--------| :---------| :--------| :----------------------------- |
| 5           | NPC Bob | Trader   | NPC Igi   | NPC Ann  | failed because not vulnerable  |
| 5           | NPC Cal | Reporter | NPC Ann   |          | successful                     |
| 5           | NPC Dan | Spy      |           |          | successful                     |
| 5           | NPC Ed  | Prophet  | NPC Han   |          | successful                     |
| 5           | NPC Gia | Demagog  | Priest    |          | voting in progress             |
| 5           | NPC Igi | Assassin | Inspector |          | successful                     |

#### States Round 5
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Fae | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Cal | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Igi | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Han | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Ed  | Prophet   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ann | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob | Trader    | False      | False     | False      | 4         | True   | 0              | 0                  |
| 5           | NPC Gia | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Dan | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role      | message   | details                                                  |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------- |
| 5           | NPC Ann | Jailer    | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Jailer    |
| 5           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan  |
| 5           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed   |
| 5           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae  |
| 5           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Bob   |
| 5           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob  |
| 5           | NPC Ann | Jailer    | vote      | Demagog has initiated a vote on eliminating Priest       |
| 5           | NPC Bob | Trader    | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Jailer    |
| 5           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan  |
| 5           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed   |
| 5           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae  |
| 5           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Bob   |
| 5           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob  |
| 5           | NPC Bob | Trader    | vote      | Demagog has initiated a vote on eliminating Priest       |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Jailer    |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan  |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed   |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae  |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Bob   |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob  |
| 5           | NPC Cal | Reporter  | reveal    | NPC Ann is Jailer                                        |
| 5           | NPC Cal | Reporter  | vote      | Demagog has initiated a vote on eliminating Priest       |
| 5           | NPC Dan | Spy       | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Jailer    |
| 5           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan  |
| 5           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed   |
| 5           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae  |
| 5           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Bob   |
| 5           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob  |
| 5           | NPC Dan | Spy       | reveal    | NPC Cal is targeting NPC Ann                             |
| 5           | NPC Dan | Spy       | reveal    | NPC Igi is targeting NPC Ed                              |
| 5           | NPC Dan | Spy       | reveal    | NPC Han is targeting NPC Fae                             |
| 5           | NPC Dan | Spy       | reveal    | NPC Ed is targeting NPC Bob                              |
| 5           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Fae                             |
| 5           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Fae                             |
| 5           | NPC Dan | Spy       | reveal    | NPC Gia is targeting NPC Bob                             |
| 5           | NPC Dan | Spy       | vote      | Demagog has initiated a vote on eliminating Priest       |
| 5           | NPC Ed  | Prophet   | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Jailer    |
| 5           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan  |
| 5           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed   |
| 5           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae  |
| 5           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Bob   |
| 5           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob  |
| 5           | NPC Ed  | Prophet   | vote      | Demagog has initiated a vote on eliminating Priest       |
| 5           | NPC Fae | Priest    | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Jailer    |
| 5           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan  |
| 5           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed   |
| 5           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae  |
| 5           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Bob   |
| 5           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob  |
| 5           | NPC Fae | Priest    | vote      | Demagog has initiated a vote on eliminating Priest       |
| 5           | NPC Gia | Demagog   | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Jailer    |
| 5           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan  |
| 5           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed   |
| 5           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae  |
| 5           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Bob   |
| 5           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob  |
| 5           | NPC Gia | Demagog   | vote      | Demagog has initiated a vote on eliminating Priest       |
| 5           | NPC Han | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Jailer    |
| 5           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan  |
| 5           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed   |
| 5           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae  |
| 5           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Bob   |
| 5           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob  |
| 5           | NPC Han | Inspector | vote      | Demagog has initiated a vote on eliminating Priest       |
| 5           | NPC Igi | Assassin  | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Jailer    |
| 5           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Dan  |
| 5           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Ed   |
| 5           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae  |
| 5           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Bob   |
| 5           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Fae  |
| 5           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Bob  |
| 5           | NPC Igi | Assassin  | vote      | Demagog has initiated a vote on eliminating Priest       |

#### Actions Round 6
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 6           | NPC Dan | Spy       |          |          | successful  |
| 6           | NPC Ed  | Prophet   | NPC Cal  |          | successful  |
| 6           | NPC Han | Inspector | NPC Igi  |          | successful  |

#### States Round 6
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Fae | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Igi | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Han | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Ed  | Prophet   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ann | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Trader    | False      | False     | False      | 3         | True   | 0              | 0                  |
| 6           | NPC Gia | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Dan | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role      | message   | details                                                   |
| :-----------| :-------| :---------| :---------| :-------------------------------------------------------- |
| 6           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann   |
| 6           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han   |
| 6           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae   |
| 6           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 6           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae   |
| 6           | NPC Ann | Jailer    | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed  |
| 6           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann   |
| 6           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han   |
| 6           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae   |
| 6           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 6           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae   |
| 6           | NPC Bob | Trader    | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed  |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann   |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han   |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae   |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae   |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed  |
| 6           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann   |
| 6           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han   |
| 6           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae   |
| 6           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 6           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae   |
| 6           | NPC Dan | Spy       | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed  |
| 6           | NPC Dan | Spy       | reveal    | NPC Cal is targeting NPC Ann                              |
| 6           | NPC Dan | Spy       | reveal    | NPC Igi is targeting NPC Han                              |
| 6           | NPC Dan | Spy       | reveal    | NPC Han is targeting NPC Igi                              |
| 6           | NPC Dan | Spy       | reveal    | NPC Ed is targeting NPC Han                               |
| 6           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Igi                              |
| 6           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Igi                              |
| 6           | NPC Dan | Spy       | reveal    | NPC Gia is targeting NPC Fae                              |
| 6           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann   |
| 6           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han   |
| 6           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae   |
| 6           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 6           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae   |
| 6           | NPC Ed  | Prophet   | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed  |
| 6           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann   |
| 6           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han   |
| 6           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae   |
| 6           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 6           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae   |
| 6           | NPC Fae | Priest    | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed  |
| 6           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann   |
| 6           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han   |
| 6           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae   |
| 6           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 6           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae   |
| 6           | NPC Gia | Demagog   | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed  |
| 6           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann   |
| 6           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han   |
| 6           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae   |
| 6           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 6           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae   |
| 6           | NPC Han | Inspector | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed  |
| 6           | NPC Han | Inspector | reveal    | Assassin is Innocent                                      |
| 6           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann   |
| 6           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han   |
| 6           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Fae   |
| 6           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Han    |
| 6           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi   |
| 6           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae   |
| 6           | NPC Igi | Assassin  | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed  |

#### Actions Round 7
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 7           | NPC Cal | Reporter | NPC Gia  |          | successful          |
| 7           | NPC Dan | Spy      |          |          | successful          |
| 7           | NPC Ed  | Prophet  | NPC Cal  |          | successful          |
| 7           | NPC Gia | Demagog  | Spy      |          | voting in progress  |
| 7           | NPC Igi | Assassin | Spy      |          | successful          |

#### States Round 7
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Fae | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Cal | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Igi | Assassin  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Han | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Ed  | Prophet   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Ann | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Bob | Trader    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Gia | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Dan | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role      | message   | details                                                  |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------- |
| 7           | NPC Ann | Jailer    | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Demagog   |
| 7           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann  |
| 7           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han  |
| 7           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 7           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 7           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae  |
| 7           | NPC Ann | Jailer    | vote      | Demagog has initiated a vote on eliminating Spy          |
| 7           | NPC Bob | Trader    | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Demagog   |
| 7           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann  |
| 7           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han  |
| 7           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 7           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 7           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae  |
| 7           | NPC Bob | Trader    | vote      | Demagog has initiated a vote on eliminating Spy          |
| 7           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Demagog   |
| 7           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann  |
| 7           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han  |
| 7           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 7           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 7           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae  |
| 7           | NPC Cal | Reporter  | reveal    | NPC Gia is Demagog                                       |
| 7           | NPC Cal | Reporter  | vote      | Demagog has initiated a vote on eliminating Spy          |
| 7           | NPC Dan | Spy       | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Demagog   |
| 7           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann  |
| 7           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han  |
| 7           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 7           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 7           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae  |
| 7           | NPC Dan | Spy       | reveal    | NPC Cal is targeting NPC Gia                             |
| 7           | NPC Dan | Spy       | reveal    | NPC Igi is targeting NPC Han                             |
| 7           | NPC Dan | Spy       | reveal    | NPC Han is targeting NPC Igi                             |
| 7           | NPC Dan | Spy       | reveal    | NPC Ed is targeting NPC Cal                              |
| 7           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Igi                             |
| 7           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Igi                             |
| 7           | NPC Dan | Spy       | reveal    | NPC Gia is targeting NPC Fae                             |
| 7           | NPC Dan | Spy       | vote      | Demagog has initiated a vote on eliminating Spy          |
| 7           | NPC Ed  | Prophet   | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Demagog   |
| 7           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann  |
| 7           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han  |
| 7           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 7           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 7           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae  |
| 7           | NPC Ed  | Prophet   | vote      | Demagog has initiated a vote on eliminating Spy          |
| 7           | NPC Fae | Priest    | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Demagog   |
| 7           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann  |
| 7           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han  |
| 7           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 7           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 7           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae  |
| 7           | NPC Fae | Priest    | vote      | Demagog has initiated a vote on eliminating Spy          |
| 7           | NPC Gia | Demagog   | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Demagog   |
| 7           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann  |
| 7           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han  |
| 7           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 7           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 7           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae  |
| 7           | NPC Gia | Demagog   | vote      | Demagog has initiated a vote on eliminating Spy          |
| 7           | NPC Han | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Demagog   |
| 7           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann  |
| 7           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han  |
| 7           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 7           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 7           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae  |
| 7           | NPC Han | Inspector | vote      | Demagog has initiated a vote on eliminating Spy          |
| 7           | NPC Igi | Assassin  | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Demagog   |
| 7           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Ann  |
| 7           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Han  |
| 7           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 7           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 7           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 7           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Fae  |
| 7           | NPC Igi | Assassin  | vote      | Demagog has initiated a vote on eliminating Spy          |

#### Actions Round 8
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 8           | NPC Dan | Spy       |          |          | successful  |
| 8           | NPC Ed  | Prophet   | NPC Fae  |          | successful  |
| 8           | NPC Han | Inspector | NPC Ed   |          | successful  |

#### States Round 8
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Fae | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Cal | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Igi | Assassin  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Han | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 8           | NPC Ed  | Prophet   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Ann | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Bob | Trader    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Gia | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Dan | Spy       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player  | Role      | message   | details                                                  |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------- |
| 8           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Gia  |
| 8           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan  |
| 8           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 8           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 8           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Ann | Jailer    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Dan  |
| 8           | NPC Ann | Jailer    | broadcast | I (NPC Han) inspected NPC Ed and they are possessed      |
| 8           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Gia  |
| 8           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan  |
| 8           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 8           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 8           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Dan  |
| 8           | NPC Bob | Trader    | broadcast | I (NPC Han) inspected NPC Ed and they are possessed      |
| 8           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Gia  |
| 8           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan  |
| 8           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 8           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 8           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Cal | Reporter  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Dan  |
| 8           | NPC Cal | Reporter  | broadcast | I (NPC Han) inspected NPC Ed and they are possessed      |
| 8           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Gia  |
| 8           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan  |
| 8           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 8           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 8           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Dan | Spy       | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Dan  |
| 8           | NPC Dan | Spy       | broadcast | I (NPC Han) inspected NPC Ed and they are possessed      |
| 8           | NPC Dan | Spy       | reveal    | NPC Cal is targeting NPC Gia                             |
| 8           | NPC Dan | Spy       | reveal    | NPC Igi is targeting NPC Dan                             |
| 8           | NPC Dan | Spy       | reveal    | NPC Han is targeting NPC Ed                              |
| 8           | NPC Dan | Spy       | reveal    | NPC Ed is targeting NPC Cal                              |
| 8           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Igi                             |
| 8           | NPC Dan | Spy       | reveal    | NPC Bob is targeting NPC Igi                             |
| 8           | NPC Dan | Spy       | reveal    | NPC Gia is targeting NPC Dan                             |
| 8           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Gia  |
| 8           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan  |
| 8           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 8           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 8           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Ed  | Prophet   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Dan  |
| 8           | NPC Ed  | Prophet   | broadcast | I (NPC Han) inspected NPC Ed and they are possessed      |
| 8           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Gia  |
| 8           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan  |
| 8           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 8           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 8           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Fae | Priest    | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Dan  |
| 8           | NPC Fae | Priest    | broadcast | I (NPC Han) inspected NPC Ed and they are possessed      |
| 8           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Gia  |
| 8           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan  |
| 8           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 8           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 8           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Gia | Demagog   | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Dan  |
| 8           | NPC Gia | Demagog   | broadcast | I (NPC Han) inspected NPC Ed and they are possessed      |
| 8           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Gia  |
| 8           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan  |
| 8           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 8           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 8           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Han | Inspector | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Dan  |
| 8           | NPC Han | Inspector | broadcast | I (NPC Han) inspected NPC Ed and they are possessed      |
| 8           | NPC Han | Inspector | reveal    | Prophet is Possessed                                     |
| 8           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Cal is targeting NPC Gia  |
| 8           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Igi is targeting NPC Dan  |
| 8           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Han is targeting NPC Igi  |
| 8           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Ed is targeting NPC Cal   |
| 8           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Bob is targeting NPC Igi  |
| 8           | NPC Igi | Assassin  | broadcast | I (NPC Dan) am the Spy and NPC Gia is targeting NPC Dan  |
| 8           | NPC Igi | Assassin  | broadcast | I (NPC Han) inspected NPC Ed and they are possessed      |