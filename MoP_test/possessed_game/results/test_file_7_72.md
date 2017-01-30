#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 72   | 7       | 5       |

#### Roles
| Role         |
| :----------- |
| Executioner  |
| Silencer     |
| Spy          |
| Jailer       |
| Demagog      |
| Psychic      |
| Trader       |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Ann | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Bob | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Cal | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Dan | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Ed  | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Trader      | role change | Your Role is Trader       |
| 0           | NPC Fae | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Gia | Spy         | role change | Your Role is Spy          |
| 0           | NPC Gia | Spy         | possessed   | You are Possessed         |

#### Actions Round 1
| round_index | Player  | action   | Target 1    | Target 2 | status                         |
| :-----------| :-------| :--------| :-----------| :--------| :----------------------------- |
| 1           | NPC Ann | Demagog  | Executioner |          | voting in progress             |
| 1           | NPC Cal | Psychic  |             |          | successful                     |
| 1           | NPC Dan | Silencer | NPC Gia     |          | successful                     |
| 1           | NPC Fae | Trader   | NPC Ann     | NPC Bob  | failed because not vulnerable  |
| 1           | NPC Gia | Spy      |             |          | successful                     |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Gia | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Fae | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 1           | NPC Ann | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ann | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ann | Demagog     | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Bob | Executioner | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Cal | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 1           | NPC Cal | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 1           | NPC Cal | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 1           | NPC Cal | Psychic     | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Dan | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Dan | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Dan | Silencer    | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Ed  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ed  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ed  | Jailer      | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Fae | Trader      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Fae | Trader      | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Fae | Trader      | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Gia | Spy         | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Gia | Spy         | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Gia | Spy         | silenced  | You have been silenced                                           |
| 1           | NPC Gia | Spy         | reveal    | NPC Dan is targeting NPC Gia                                     |
| 1           | NPC Gia | Spy         | vote      | Demagog has initiated a vote on eliminating Executioner          |

#### Actions Round 2
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 2           | NPC Cal | Psychic  |          |          | successful  |
| 2           | NPC Dan | Silencer | NPC Cal  |          | successful  |
| 2           | NPC Gia | Spy      |          |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Fae | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 2           | NPC Ann | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ann | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Cal | Psychic     | silenced  | You have been silenced                                           |
| 2           | NPC Cal | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 2           | NPC Cal | Psychic     | reveal    | Player: NPC Ann is not possessed                                 |
| 2           | NPC Dan | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Dan | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Ed  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ed  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Fae | Trader      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Fae | Trader      | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Gia | Spy         | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Gia | Spy         | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 2           | NPC Gia | Spy         | reveal    | NPC Dan is targeting NPC Cal                                     |
| 2           | NPC Gia | Spy         | reveal    | NPC Ann is targeting NPC Bob                                     |
| 2           | NPC Gia | Spy         | reveal    | NPC Fae is targeting NPC Ann                                     |
| 2           | NPC Gia | Spy         | reveal    | NPC Fae is targeting NPC Ann                                     |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 3           | NPC Ann | Demagog  | Psychic  |          | voting in progress  |
| 3           | NPC Cal | Psychic  |          |          | successful          |
| 3           | NPC Dan | Silencer | NPC Ed   |          | successful          |
| 3           | NPC Gia | Spy      |          |          | successful          |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Gia | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Fae | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 3           | NPC Ann | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Cal  |
| 3           | NPC Ann | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Bob  |
| 3           | NPC Ann | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Ann | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Ann | Demagog     | vote      | Demagog has initiated a vote on eliminating Psychic      |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Cal  |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Bob  |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Bob | Executioner | vote      | Demagog has initiated a vote on eliminating Psychic      |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Cal  |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Bob  |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Cal | Psychic     | reveal    | Player: NPC Dan is not possessed                         |
| 3           | NPC Cal | Psychic     | reveal    | Player: NPC Fae is not possessed                         |
| 3           | NPC Cal | Psychic     | reveal    | Player: NPC Ann is not possessed                         |
| 3           | NPC Cal | Psychic     | vote      | Demagog has initiated a vote on eliminating Psychic      |
| 3           | NPC Dan | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Cal  |
| 3           | NPC Dan | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Bob  |
| 3           | NPC Dan | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Dan | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Dan | Silencer    | vote      | Demagog has initiated a vote on eliminating Psychic      |
| 3           | NPC Ed  | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Cal  |
| 3           | NPC Ed  | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Bob  |
| 3           | NPC Ed  | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Ed  | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Ed  | Jailer      | silenced  | You have been silenced                                   |
| 3           | NPC Ed  | Jailer      | vote      | Demagog has initiated a vote on eliminating Psychic      |
| 3           | NPC Fae | Trader      | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Cal  |
| 3           | NPC Fae | Trader      | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Bob  |
| 3           | NPC Fae | Trader      | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Fae | Trader      | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Fae | Trader      | vote      | Demagog has initiated a vote on eliminating Psychic      |
| 3           | NPC Gia | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Cal  |
| 3           | NPC Gia | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Bob  |
| 3           | NPC Gia | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Gia | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann  |
| 3           | NPC Gia | Spy         | reveal    | NPC Dan is targeting NPC Ed                              |
| 3           | NPC Gia | Spy         | reveal    | NPC Ann is targeting NPC Bob                             |
| 3           | NPC Gia | Spy         | reveal    | NPC Fae is targeting NPC Ann                             |
| 3           | NPC Gia | Spy         | reveal    | NPC Fae is targeting NPC Ann                             |
| 3           | NPC Gia | Spy         | vote      | Demagog has initiated a vote on eliminating Psychic      |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 4           | NPC Cal | Psychic  |          |          | successful  |
| 4           | NPC Dan | Silencer | NPC Dan  |          | successful  |
| 4           | NPC Gia | Spy      |          |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Gia | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Fae | Trader      | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 4           | NPC Ann | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ann | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Ann | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 4           | NPC Ann | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed           |
| 4           | NPC Ann | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal          |
| 4           | NPC Ann | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Ann | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed           |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal          |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed           |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal          |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Cal | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 4           | NPC Cal | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 4           | NPC Cal | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 4           | NPC Dan | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Dan | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Dan | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 4           | NPC Dan | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed           |
| 4           | NPC Dan | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal          |
| 4           | NPC Dan | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Dan | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Dan | Silencer    | silenced  | You have been silenced                                           |
| 4           | NPC Ed  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ed  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Ed  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 4           | NPC Ed  | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed           |
| 4           | NPC Ed  | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal          |
| 4           | NPC Ed  | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Ed  | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Fae | Trader      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Fae | Trader      | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Fae | Trader      | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 4           | NPC Fae | Trader      | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed           |
| 4           | NPC Fae | Trader      | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal          |
| 4           | NPC Fae | Trader      | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Fae | Trader      | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Gia | Spy         | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Gia | Spy         | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Gia | Spy         | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 4           | NPC Gia | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Ed           |
| 4           | NPC Gia | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal          |
| 4           | NPC Gia | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Gia | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann          |
| 4           | NPC Gia | Spy         | reveal    | NPC Dan is targeting NPC Dan                                     |
| 4           | NPC Gia | Spy         | reveal    | NPC Ann is targeting NPC Cal                                     |
| 4           | NPC Gia | Spy         | reveal    | NPC Fae is targeting NPC Ann                                     |
| 4           | NPC Gia | Spy         | reveal    | NPC Fae is targeting NPC Ann                                     |

#### Actions Round 5
| round_index | Player  | action   | Target 1 | Target 2 | status                         |
| :-----------| :-------| :--------| :--------| :--------| :----------------------------- |
| 5           | NPC Ann | Demagog  | Jailer   |          | voting in progress             |
| 5           | NPC Cal | Psychic  |          |          | successful                     |
| 5           | NPC Dan | Silencer | NPC Ed   |          | successful                     |
| 5           | NPC Fae | Trader   | NPC Ed   | NPC Bob  | failed because not vulnerable  |
| 5           | NPC Gia | Spy      |          |          | successful                     |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Gia | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ann | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Fae | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 5           | NPC Ann | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed   |
| 5           | NPC Ann | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 5           | NPC Ann | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Dan      |
| 5           | NPC Ann | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal      |
| 5           | NPC Ann | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Ann | Demagog     | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Ann | Demagog     | vote      | Demagog has initiated a vote on eliminating Jailer           |
| 5           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed   |
| 5           | NPC Bob | Executioner | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 5           | NPC Bob | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Dan      |
| 5           | NPC Bob | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal      |
| 5           | NPC Bob | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Bob | Executioner | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Bob | Executioner | vote      | Demagog has initiated a vote on eliminating Jailer           |
| 5           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed   |
| 5           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 5           | NPC Cal | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Dan      |
| 5           | NPC Cal | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal      |
| 5           | NPC Cal | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Cal | Psychic     | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Cal | Psychic     | reveal    | Player: NPC Ann is not possessed                             |
| 5           | NPC Cal | Psychic     | reveal    | Player: NPC Fae is not possessed                             |
| 5           | NPC Cal | Psychic     | vote      | Demagog has initiated a vote on eliminating Jailer           |
| 5           | NPC Dan | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed   |
| 5           | NPC Dan | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 5           | NPC Dan | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Dan      |
| 5           | NPC Dan | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal      |
| 5           | NPC Dan | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Dan | Silencer    | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Dan | Silencer    | vote      | Demagog has initiated a vote on eliminating Jailer           |
| 5           | NPC Ed  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed   |
| 5           | NPC Ed  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 5           | NPC Ed  | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Dan      |
| 5           | NPC Ed  | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal      |
| 5           | NPC Ed  | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Ed  | Jailer      | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Ed  | Jailer      | silenced  | You have been silenced                                       |
| 5           | NPC Ed  | Jailer      | vote      | Demagog has initiated a vote on eliminating Jailer           |
| 5           | NPC Fae | Trader      | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed   |
| 5           | NPC Fae | Trader      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 5           | NPC Fae | Trader      | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Dan      |
| 5           | NPC Fae | Trader      | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal      |
| 5           | NPC Fae | Trader      | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Fae | Trader      | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Fae | Trader      | vote      | Demagog has initiated a vote on eliminating Jailer           |
| 5           | NPC Gia | Spy         | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed   |
| 5           | NPC Gia | Spy         | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 5           | NPC Gia | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Dan is targeting NPC Dan      |
| 5           | NPC Gia | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Ann is targeting NPC Cal      |
| 5           | NPC Gia | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Gia | Spy         | broadcast | I (NPC Gia) am the Spy and NPC Fae is targeting NPC Ann      |
| 5           | NPC Gia | Spy         | reveal    | NPC Dan is targeting NPC Ed                                  |
| 5           | NPC Gia | Spy         | reveal    | NPC Ann is targeting NPC Cal                                 |
| 5           | NPC Gia | Spy         | reveal    | NPC Fae is targeting NPC Ann                                 |
| 5           | NPC Gia | Spy         | reveal    | NPC Fae is targeting NPC Ann                                 |
| 5           | NPC Gia | Spy         | vote      | Demagog has initiated a vote on eliminating Jailer           |