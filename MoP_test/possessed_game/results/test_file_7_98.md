#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 98   | 7       | 2       |

#### Roles
| Role         |
| :----------- |
| Trader       |
| Prophet      |
| Demagog      |
| Inspector    |
| Psychic      |
| Executioner  |
| Silencer     |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Demagog     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Ann | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Trader      | role change | Your Role is Trader       |
| 0           | NPC Bob | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Cal | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Dan | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Ed  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Fae | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Gia | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Gia | Demagog     | possessed   | You are Possessed         |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status              |
| :-----------| :-------| :---------| :--------| :--------| :------------------ |
| 1           | NPC Ann | Psychic   |          |          | successful          |
| 1           | NPC Bob | Trader    | NPC Dan  | NPC Ann  | successful          |
| 1           | NPC Dan | Prophet   | NPC Cal  |          | successful          |
| 1           | NPC Ed  | Inspector | NPC Bob  |          | successful          |
| 1           | NPC Fae | Silencer  | NPC Dan  |          | successful          |
| 1           | NPC Gia | Demagog   | Psychic  |          | voting in progress  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Dan | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia | Demagog     | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann | Prophet     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Cal | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 1           | NPC Ann | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ann | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed     |
| 1           | NPC Ann | Prophet     | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed        |
| 1           | NPC Ann | Prophet     | reveal    | Player: NPC Ed is not possessed                                |
| 1           | NPC Ann | Prophet     | reveal    | Player: NPC Fae is not possessed                               |
| 1           | NPC Ann | Prophet     | reveal    | Player: NPC Dan is not possessed                               |
| 1           | NPC Ann | Prophet     | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Bob | Trader      | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob | Trader      | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed     |
| 1           | NPC Bob | Trader      | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed        |
| 1           | NPC Bob | Trader      | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Cal | Executioner | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Cal | Executioner | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed     |
| 1           | NPC Cal | Executioner | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed        |
| 1           | NPC Cal | Executioner | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed     |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed        |
| 1           | NPC Dan | Psychic     | silenced  | You have been silenced                                         |
| 1           | NPC Dan | Psychic     | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Ed  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ed  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed     |
| 1           | NPC Ed  | Inspector   | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed        |
| 1           | NPC Ed  | Inspector   | reveal    | Trader is Innocent                                             |
| 1           | NPC Ed  | Inspector   | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Fae | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Fae | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed     |
| 1           | NPC Fae | Silencer    | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed        |
| 1           | NPC Fae | Silencer    | vote      | Demagog has initiated a vote on eliminating Psychic            |
| 1           | NPC Gia | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Gia | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed     |
| 1           | NPC Gia | Demagog     | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed        |
| 1           | NPC Gia | Demagog     | vote      | Demagog has initiated a vote on eliminating Psychic            |

#### Actions Round 2
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 2           | NPC Ann | Prophet  | NPC Dan  |          | successful  |
| 2           | NPC Dan | Psychic  |          |          | successful  |
| 2           | NPC Fae | Silencer | NPC Gia  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Dan | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia | Demagog     | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role    | message  | details                           |
| :-----------| :-------| :-------| :--------| :-------------------------------- |
| 2           | NPC Dan | Psychic | reveal   | Player: NPC Ed is not possessed   |
| 2           | NPC Dan | Psychic | reveal   | Player: NPC Bob is not possessed  |
| 2           | NPC Gia | Demagog | silenced | You have been silenced            |