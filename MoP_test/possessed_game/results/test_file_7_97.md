#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 97   | 7       | 4       |

#### Roles
| Role         |
| :----------- |
| Executioner  |
| Medic        |
| Prophet      |
| Demagog      |
| Silencer     |
| Psychic      |
| Inspector    |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Ann | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Bob | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Cal | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Medic       | role change | Your Role is Medic        |
| 0           | NPC Dan | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Ed  | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Fae | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Gia | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Gia | Prophet     | possessed   | You are Possessed         |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status              |
| :-----------| :-------| :---------| :--------| :--------| :------------------ |
| 1           | NPC Ann | Silencer  | NPC Bob  |          | successful          |
| 1           | NPC Cal | Psychic   |          |          | successful          |
| 1           | NPC Dan | Medic     | NPC Gia  |          | successful          |
| 1           | NPC Ed  | Demagog   | Prophet  |          | voting in progress  |
| 1           | NPC Fae | Inspector | NPC Ann  |          | successful          |
| 1           | NPC Gia | Prophet   | NPC Bob  |          | successful          |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Fae | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 1           | NPC Ann | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ann | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ann | Silencer    | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed         |
| 1           | NPC Ann | Silencer    | vote      | Demagog has initiated a vote on eliminating Prophet              |
| 1           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Bob | Executioner | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed         |
| 1           | NPC Bob | Executioner | silenced  | You have been silenced                                           |
| 1           | NPC Bob | Executioner | vote      | Demagog has initiated a vote on eliminating Prophet              |
| 1           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Cal | Psychic     | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed         |
| 1           | NPC Cal | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 1           | NPC Cal | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 1           | NPC Cal | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 1           | NPC Cal | Psychic     | vote      | Demagog has initiated a vote on eliminating Prophet              |
| 1           | NPC Dan | Medic       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Dan | Medic       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Dan | Medic       | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed         |
| 1           | NPC Dan | Medic       | vote      | Demagog has initiated a vote on eliminating Prophet              |
| 1           | NPC Ed  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ed  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ed  | Demagog     | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed         |
| 1           | NPC Ed  | Demagog     | vote      | Demagog has initiated a vote on eliminating Prophet              |
| 1           | NPC Fae | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Fae | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Fae | Inspector   | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed         |
| 1           | NPC Fae | Inspector   | reveal    | Silencer is Innocent                                             |
| 1           | NPC Fae | Inspector   | vote      | Demagog has initiated a vote on eliminating Prophet              |
| 1           | NPC Gia | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Gia | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Gia | Prophet     | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed         |
| 1           | NPC Gia | Prophet     | vote      | Demagog has initiated a vote on eliminating Prophet              |

#### Actions Round 2
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 2           | NPC Ann | Silencer | NPC Dan  |          | successful  |
| 2           | NPC Cal | Psychic  |          |          | successful  |
| 2           | NPC Dan | Medic    | NPC Ed   |          | successful  |
| 2           | NPC Gia | Prophet  | NPC Dan  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Gia | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Fae | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 2           | NPC Ann | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 2           | NPC Ann | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 2           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal | Psychic     | reveal    | Player: NPC Ed is not possessed                                |
| 2           | NPC Cal | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 2           | NPC Dan | Medic       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 2           | NPC Dan | Medic       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Dan | Medic       | silenced  | You have been silenced                                         |
| 2           | NPC Ed  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 2           | NPC Ed  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Fae | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 2           | NPC Fae | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Gia | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 2           | NPC Gia | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status              |
| :-----------| :-------| :---------| :--------| :--------| :------------------ |
| 3           | NPC Ann | Silencer  | NPC Gia  |          | successful          |
| 3           | NPC Cal | Psychic   |          |          | successful          |
| 3           | NPC Dan | Medic     | NPC Ann  |          | successful          |
| 3           | NPC Ed  | Demagog   | Medic    |          | voting in progress  |
| 3           | NPC Fae | Inspector | NPC Ann  |          | successful          |
| 3           | NPC Gia | Prophet   | NPC Cal  |          | successful          |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Gia | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Fae | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Ann | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed    |
| 3           | NPC Ann | Silencer    | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed     |
| 3           | NPC Ann | Silencer    | vote      | Demagog has initiated a vote on eliminating Medic            |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed    |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed     |
| 3           | NPC Bob | Executioner | vote      | Demagog has initiated a vote on eliminating Medic            |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed    |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed     |
| 3           | NPC Cal | Psychic     | reveal    | Player: NPC Ann is not possessed                             |
| 3           | NPC Cal | Psychic     | reveal    | Player: NPC Bob is not possessed                             |
| 3           | NPC Cal | Psychic     | vote      | Demagog has initiated a vote on eliminating Medic            |
| 3           | NPC Dan | Medic       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Dan | Medic       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed    |
| 3           | NPC Dan | Medic       | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed     |
| 3           | NPC Dan | Medic       | vote      | Demagog has initiated a vote on eliminating Medic            |
| 3           | NPC Ed  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Ed  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed    |
| 3           | NPC Ed  | Demagog     | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed     |
| 3           | NPC Ed  | Demagog     | vote      | Demagog has initiated a vote on eliminating Medic            |
| 3           | NPC Fae | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Fae | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed    |
| 3           | NPC Fae | Inspector   | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed     |
| 3           | NPC Fae | Inspector   | reveal    | Silencer is Innocent                                         |
| 3           | NPC Fae | Inspector   | vote      | Demagog has initiated a vote on eliminating Medic            |
| 3           | NPC Gia | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Gia | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed    |
| 3           | NPC Gia | Prophet     | broadcast | I (NPC Fae) inspected NPC Ann and they are not possessed     |
| 3           | NPC Gia | Prophet     | silenced  | You have been silenced                                       |
| 3           | NPC Gia | Prophet     | vote      | Demagog has initiated a vote on eliminating Medic            |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 4           | NPC Ann | Silencer | NPC Gia  |          | successful  |
| 4           | NPC Cal | Psychic  |          |          | successful  |
| 4           | NPC Dan | Medic    | NPC Cal  |          | successful  |
| 4           | NPC Gia | Prophet  | NPC Cal  |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Gia | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Cal | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 4           | NPC Ann | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ann | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Ann | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Cal | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 4           | NPC Cal | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 4           | NPC Cal | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 4           | NPC Dan | Medic       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Dan | Medic       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Dan | Medic       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Ed  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ed  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Ed  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Fae | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Fae | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Fae | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Gia | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Gia | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Gia | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Gia | Prophet     | silenced  | You have been silenced                                           |