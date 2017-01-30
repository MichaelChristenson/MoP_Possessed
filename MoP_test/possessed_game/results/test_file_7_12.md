#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 12   | 7       | 9       |

#### Roles
| Role       |
| :--------- |
| Judge      |
| Inspector  |
| Thief      |
| Trader     |
| Psychic    |
| Reporter   |
| Medic      |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Thief     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Trader    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Psychic   | role change | Your Role is Psychic    |
| 0           | NPC Ann | Psychic   | possessed   | You are Not Possessed   |
| 0           | NPC Bob | Judge     | role change | Your Role is Judge      |
| 0           | NPC Bob | Judge     | possessed   | You are Not Possessed   |
| 0           | NPC Cal | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Cal | Reporter  | possessed   | You are Not Possessed   |
| 0           | NPC Dan | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Dan | Inspector | possessed   | You are Not Possessed   |
| 0           | NPC Ed  | Trader    | role change | Your Role is Trader     |
| 0           | NPC Ed  | Trader    | possessed   | You are Not Possessed   |
| 0           | NPC Fae | Medic     | role change | Your Role is Medic      |
| 0           | NPC Fae | Medic     | possessed   | You are Not Possessed   |
| 0           | NPC Gia | Thief     | role change | Your Role is Thief      |
| 0           | NPC Gia | Thief     | possessed   | You are Possessed       |

#### Actions Round 1
| round_index | Player  | action    | Target 1  | Target 2 | status      |
| :-----------| :-------| :---------| :---------| :--------| :---------- |
| 1           | NPC Ann | Psychic   |           |          | successful  |
| 1           | NPC Bob | Judge     | Inspector |          | successful  |
| 1           | NPC Cal | Reporter  | NPC Gia   |          | successful  |
| 1           | NPC Dan | Inspector | NPC Cal   |          | successful  |
| 1           | NPC Ed  | Trader    | NPC Bob   | NPC Gia  | successful  |
| 1           | NPC Fae | Medic     | NPC Dan   |          | successful  |
| 1           | NPC Gia | Thief     | NPC Ann   |          | successful  |

#### States Round 1
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Trader    | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Ann | Psychic   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 1           | NPC Cal | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Fae | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 1           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed    |
| 1           | NPC Ann | Psychic   | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Thief         |
| 1           | NPC Ann | Psychic   | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |
| 1           | NPC Ann | Psychic   | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Ann | Psychic   | reveal    | Player: NPC Ed is not possessed                              |
| 1           | NPC Ann | Psychic   | reveal    | Player: NPC Fae is not possessed                             |
| 1           | NPC Ann | Psychic   | reveal    | Player: NPC Dan is not possessed                             |
| 1           | NPC Bob | Thief     | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 1           | NPC Bob | Thief     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed    |
| 1           | NPC Bob | Thief     | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Thief         |
| 1           | NPC Bob | Thief     | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |
| 1           | NPC Bob | Thief     | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 1           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed    |
| 1           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Thief         |
| 1           | NPC Cal | Reporter  | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |
| 1           | NPC Cal | Reporter  | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Cal | Reporter  | reveal    | NPC Gia is Thief                                             |
| 1           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 1           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed    |
| 1           | NPC Dan | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Thief         |
| 1           | NPC Dan | Inspector | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |
| 1           | NPC Dan | Inspector | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Dan | Inspector | reveal    | Reporter is Innocent                                         |
| 1           | NPC Ed  | Trader    | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 1           | NPC Ed  | Trader    | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed    |
| 1           | NPC Ed  | Trader    | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Thief         |
| 1           | NPC Ed  | Trader    | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |
| 1           | NPC Ed  | Trader    | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Fae | Medic     | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 1           | NPC Fae | Medic     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed    |
| 1           | NPC Fae | Medic     | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Thief         |
| 1           | NPC Fae | Medic     | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |
| 1           | NPC Fae | Medic     | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Gia | Judge     | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 1           | NPC Gia | Judge     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed    |
| 1           | NPC Gia | Judge     | broadcast | I (NPC Cal) am the Reporter and NPC Gia is the Thief         |
| 1           | NPC Gia | Judge     | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |
| 1           | NPC Gia | Judge     | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable  |

#### Actions Round 2
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 2           | NPC Ann | Psychic   |          |          | successful  |
| 2           | NPC Bob | Thief     | NPC Ed   |          | successful  |
| 2           | NPC Dan | Inspector | NPC Ann  |          | successful  |
| 2           | NPC Fae | Medic     | NPC Gia  |          | successful  |
| 2           | NPC Gia | Judge     | Trader   |          | successful  |

#### States Round 2
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Dan | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Gia | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Trader    | False      | False     | True       | 3         | True   | 0              | 0                  |
| 2           | NPC Ann | Psychic   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Cal | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Fae | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role      | message   | details                                                     |
| :-----------| :-------| :---------| :---------| :---------------------------------------------------------- |
| 2           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed   |
| 2           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed   |
| 2           | NPC Ann | Psychic   | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 2           | NPC Ann | Psychic   | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed    |
| 2           | NPC Ann | Psychic   | reveal    | Player: NPC Dan is not possessed                            |
| 2           | NPC Ann | Psychic   | reveal    | Player: NPC Bob is not possessed                            |
| 2           | NPC Bob | Thief     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed   |
| 2           | NPC Bob | Thief     | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed   |
| 2           | NPC Bob | Thief     | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 2           | NPC Bob | Thief     | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed    |
| 2           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed   |
| 2           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed   |
| 2           | NPC Cal | Reporter  | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 2           | NPC Cal | Reporter  | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed    |
| 2           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed   |
| 2           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed   |
| 2           | NPC Dan | Inspector | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 2           | NPC Dan | Inspector | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed    |
| 2           | NPC Dan | Inspector | reveal    | Psychic is Innocent                                         |
| 2           | NPC Ed  | Trader    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed   |
| 2           | NPC Ed  | Trader    | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed   |
| 2           | NPC Ed  | Trader    | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 2           | NPC Ed  | Trader    | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed    |
| 2           | NPC Fae | Medic     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed   |
| 2           | NPC Fae | Medic     | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed   |
| 2           | NPC Fae | Medic     | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 2           | NPC Fae | Medic     | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed    |
| 2           | NPC Gia | Judge     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed   |
| 2           | NPC Gia | Judge     | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed   |
| 2           | NPC Gia | Judge     | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 2           | NPC Gia | Judge     | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed    |

#### Actions Round 3
| round_index | Player  | action   | Target 1  | Target 2 | status      |
| :-----------| :-------| :--------| :---------| :--------| :---------- |
| 3           | NPC Ann | Psychic  |           |          | successful  |
| 3           | NPC Cal | Reporter | NPC Ann   |          | successful  |
| 3           | NPC Fae | Medic    | NPC Ed    |          | successful  |
| 3           | NPC Gia | Judge    | Inspector |          | successful  |

#### States Round 3
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Dan | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Gia | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Trader    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Psychic   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 3           | NPC Cal | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Fae | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 3           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 3           | NPC Ann | Psychic   | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Psychic         |
| 3           | NPC Ann | Psychic   | reveal    | Player: NPC Fae is not possessed                               |
| 3           | NPC Ann | Psychic   | reveal    | Player: NPC Bob is not possessed                               |
| 3           | NPC Ann | Psychic   | reveal    | Player: NPC Ed is not possessed                                |
| 3           | NPC Bob | Thief     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Bob | Thief     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 3           | NPC Bob | Thief     | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Psychic         |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Psychic         |
| 3           | NPC Cal | Reporter  | reveal    | NPC Ann is Psychic                                             |
| 3           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 3           | NPC Dan | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Psychic         |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 3           | NPC Ed  | Trader    | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Psychic         |
| 3           | NPC Fae | Medic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Fae | Medic     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 3           | NPC Fae | Medic     | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Psychic         |
| 3           | NPC Gia | Judge     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Gia | Judge     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 3           | NPC Gia | Judge     | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Psychic         |

#### Actions Round 4
| round_index | Player  | action    | Target 1  | Target 2 | status      |
| :-----------| :-------| :---------| :---------| :--------| :---------- |
| 4           | NPC Ann | Psychic   |           |          | successful  |
| 4           | NPC Bob | Thief     | NPC Cal   |          | successful  |
| 4           | NPC Dan | Inspector | NPC Cal   |          | successful  |
| 4           | NPC Ed  | Trader    | NPC Ann   | NPC Fae  | successful  |
| 4           | NPC Fae | Medic     | NPC Ann   |          | successful  |
| 4           | NPC Gia | Judge     | Inspector |          | successful  |

#### States Round 4
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Bob | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Dan | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Gia | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Trader    | False      | False     | True       | 4         | True   | 0              | 0                  |
| 4           | NPC Ann | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Reporter  | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Fae | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 4           | NPC Ann | Medic     | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 4           | NPC Ann | Medic     | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed    |
| 4           | NPC Ann | Medic     | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 4           | NPC Ann | Medic     | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |
| 4           | NPC Ann | Medic     | reveal    | Player: NPC Dan is not possessed                             |
| 4           | NPC Ann | Medic     | reveal    | Player: NPC Bob is not possessed                             |
| 4           | NPC Ann | Medic     | reveal    | Player: NPC Cal is not possessed                             |
| 4           | NPC Bob | Thief     | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 4           | NPC Bob | Thief     | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed    |
| 4           | NPC Bob | Thief     | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 4           | NPC Bob | Thief     | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed    |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |
| 4           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 4           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed    |
| 4           | NPC Dan | Inspector | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 4           | NPC Dan | Inspector | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |
| 4           | NPC Dan | Inspector | reveal    | Reporter is Innocent                                         |
| 4           | NPC Ed  | Trader    | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 4           | NPC Ed  | Trader    | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed    |
| 4           | NPC Ed  | Trader    | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 4           | NPC Ed  | Trader    | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |
| 4           | NPC Fae | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 4           | NPC Fae | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed    |
| 4           | NPC Fae | Psychic   | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 4           | NPC Fae | Psychic   | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |
| 4           | NPC Gia | Judge     | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed   |
| 4           | NPC Gia | Judge     | broadcast | I (NPC Ann) am the Psychic and the Thief is not possessed    |
| 4           | NPC Gia | Judge     | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 4           | NPC Gia | Judge     | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed     |

#### Actions Round 5
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 5           | NPC Ann | Medic    | NPC Fae  |          | successful  |
| 5           | NPC Cal | Reporter | NPC Ed   |          | successful  |
| 5           | NPC Fae | Psychic  |          |          | successful  |
| 5           | NPC Gia | Judge    | Trader   |          | successful  |

#### States Round 5
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Bob | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Dan | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Gia | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Trader    | False      | False     | True       | 3         | True   | 0              | 0                  |
| 5           | NPC Ann | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Cal | Reporter  | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Fae | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role      | message   | details                                                       |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------ |
| 5           | NPC Ann | Medic     | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Trader          |
| 5           | NPC Ann | Medic     | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ann | Medic     | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed     |
| 5           | NPC Ann | Medic     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed     |
| 5           | NPC Bob | Thief     | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Trader          |
| 5           | NPC Bob | Thief     | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Bob | Thief     | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed     |
| 5           | NPC Bob | Thief     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed     |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Trader          |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed     |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed     |
| 5           | NPC Cal | Reporter  | reveal    | NPC Ed is Trader                                              |
| 5           | NPC Dan | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Trader          |
| 5           | NPC Dan | Inspector | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Dan | Inspector | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed     |
| 5           | NPC Dan | Inspector | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed     |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Trader          |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed     |
| 5           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed     |
| 5           | NPC Fae | Psychic   | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Trader          |
| 5           | NPC Fae | Psychic   | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Fae | Psychic   | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed     |
| 5           | NPC Fae | Psychic   | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed     |
| 5           | NPC Fae | Psychic   | reveal    | Player: NPC Ed is not possessed                               |
| 5           | NPC Fae | Psychic   | reveal    | Player: NPC Dan is not possessed                              |
| 5           | NPC Gia | Judge     | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Trader          |
| 5           | NPC Gia | Judge     | broadcast | I (NPC Fae) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Gia | Judge     | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed     |
| 5           | NPC Gia | Judge     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed     |

#### Actions Round 6
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 6           | NPC Ann | Medic     | NPC Bob  |          | successful  |
| 6           | NPC Bob | Thief     | NPC Dan  |          | successful  |
| 6           | NPC Dan | Inspector | NPC Ed   |          | successful  |
| 6           | NPC Fae | Psychic   |          |          | successful  |
| 6           | NPC Gia | Judge     | Psychic  |          | successful  |

#### States Round 6
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Bob | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan | Inspector | False      | False     | True       | 2         | True   | 0              | 0                  |
| 6           | NPC Gia | Judge     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ed  | Trader    | False      | False     | True       | 2         | True   | 0              | 0                  |
| 6           | NPC Ann | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Reporter  | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Fae | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 6           | NPC Ann | Medic     | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 6           | NPC Ann | Medic     | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed      |
| 6           | NPC Ann | Medic     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed    |
| 6           | NPC Ann | Medic     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed   |
| 6           | NPC Ann | Medic     | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed    |
| 6           | NPC Bob | Thief     | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 6           | NPC Bob | Thief     | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed      |
| 6           | NPC Bob | Thief     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed    |
| 6           | NPC Bob | Thief     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed   |
| 6           | NPC Bob | Thief     | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed    |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed      |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed    |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed   |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed    |
| 6           | NPC Dan | Inspector | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 6           | NPC Dan | Inspector | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed      |
| 6           | NPC Dan | Inspector | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed    |
| 6           | NPC Dan | Inspector | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed   |
| 6           | NPC Dan | Inspector | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed    |
| 6           | NPC Dan | Inspector | reveal    | Trader is Innocent                                           |
| 6           | NPC Ed  | Trader    | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 6           | NPC Ed  | Trader    | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed      |
| 6           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed    |
| 6           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed   |
| 6           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed    |
| 6           | NPC Fae | Psychic   | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 6           | NPC Fae | Psychic   | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed      |
| 6           | NPC Fae | Psychic   | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed    |
| 6           | NPC Fae | Psychic   | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed   |
| 6           | NPC Fae | Psychic   | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed    |
| 6           | NPC Fae | Psychic   | reveal    | Player: NPC Dan is not possessed                             |
| 6           | NPC Fae | Psychic   | reveal    | Player: NPC Ed is not possessed                              |
| 6           | NPC Fae | Psychic   | reveal    | Player: NPC Cal is not possessed                             |
| 6           | NPC Gia | Judge     | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 6           | NPC Gia | Judge     | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed      |
| 6           | NPC Gia | Judge     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed    |
| 6           | NPC Gia | Judge     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed   |
| 6           | NPC Gia | Judge     | broadcast | I (NPC Fae) am the Psychic and the Medic is not possessed    |

#### Actions Round 7
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 7           | NPC Ann | Medic    | NPC Dan  |          | successful  |
| 7           | NPC Bob | Thief    | NPC Gia  |          | successful  |
| 7           | NPC Cal | Reporter | NPC Bob  |          | successful  |
| 7           | NPC Fae | Psychic  |          |          | successful  |
| 7           | NPC Gia | Judge    | Thief    |          | successful  |

#### States Round 7
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Bob | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Dan | Inspector | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Gia | Judge     | False      | True      | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Ed  | Trader    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 7           | NPC Ann | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Cal | Reporter  | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Fae | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 7           | NPC Ann | Medic     | broadcast | I (NPC Bob) am the Thief and I have made NPC Gia vulnerable    |
| 7           | NPC Ann | Medic     | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Thief           |
| 7           | NPC Ann | Medic     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 7           | NPC Ann | Medic     | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Bob | Thief     | broadcast | I (NPC Bob) am the Thief and I have made NPC Gia vulnerable    |
| 7           | NPC Bob | Thief     | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Thief           |
| 7           | NPC Bob | Thief     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 7           | NPC Bob | Thief     | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Cal | Reporter  | broadcast | I (NPC Bob) am the Thief and I have made NPC Gia vulnerable    |
| 7           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Thief           |
| 7           | NPC Cal | Reporter  | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 7           | NPC Cal | Reporter  | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Cal | Reporter  | reveal    | NPC Bob is Thief                                               |
| 7           | NPC Dan | Inspector | broadcast | I (NPC Bob) am the Thief and I have made NPC Gia vulnerable    |
| 7           | NPC Dan | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Thief           |
| 7           | NPC Dan | Inspector | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 7           | NPC Dan | Inspector | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Bob) am the Thief and I have made NPC Gia vulnerable    |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Thief           |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 7           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Fae | Psychic   | broadcast | I (NPC Bob) am the Thief and I have made NPC Gia vulnerable    |
| 7           | NPC Fae | Psychic   | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Thief           |
| 7           | NPC Fae | Psychic   | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 7           | NPC Fae | Psychic   | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Fae | Psychic   | reveal    | Player: NPC Cal is not possessed                               |
| 7           | NPC Fae | Psychic   | reveal    | Player: NPC Ed is not possessed                                |
| 7           | NPC Fae | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 7           | NPC Gia | Judge     | broadcast | I (NPC Bob) am the Thief and I have made NPC Gia vulnerable    |
| 7           | NPC Gia | Judge     | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Thief           |
| 7           | NPC Gia | Judge     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 7           | NPC Gia | Judge     | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |

#### Actions Round 8
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 8           | NPC Ann | Medic     | NPC Gia  |          | successful  |
| 8           | NPC Dan | Inspector | NPC Fae  |          | successful  |
| 8           | NPC Ed  | Trader    | NPC Cal  | NPC Fae  | successful  |
| 8           | NPC Fae | Psychic   |          |          | successful  |
| 8           | NPC Gia | Judge     | Medic    |          | successful  |

#### States Round 8
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Bob | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Dan | Inspector | False      | False     | True       | 2         | True   | 0              | 0                  |
| 8           | NPC Gia | Judge     | False      | True      | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Ed  | Trader    | False      | False     | True       | 4         | True   | 0              | 0                  |
| 8           | NPC Ann | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Cal | Psychic   | False      | False     | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Fae | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 8           | NPC Ann | Medic     | broadcast | I (NPC Dan) inspected NPC Fae and they are not possessed       |
| 8           | NPC Ann | Medic     | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Ann | Medic     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 8           | NPC Ann | Medic     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 8           | NPC Bob | Thief     | broadcast | I (NPC Dan) inspected NPC Fae and they are not possessed       |
| 8           | NPC Bob | Thief     | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Bob | Thief     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 8           | NPC Bob | Thief     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 8           | NPC Cal | Psychic   | broadcast | I (NPC Dan) inspected NPC Fae and they are not possessed       |
| 8           | NPC Cal | Psychic   | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Cal | Psychic   | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 8           | NPC Cal | Psychic   | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 8           | NPC Dan | Inspector | broadcast | I (NPC Dan) inspected NPC Fae and they are not possessed       |
| 8           | NPC Dan | Inspector | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Dan | Inspector | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 8           | NPC Dan | Inspector | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 8           | NPC Dan | Inspector | reveal    | Psychic is Innocent                                            |
| 8           | NPC Ed  | Trader    | broadcast | I (NPC Dan) inspected NPC Fae and they are not possessed       |
| 8           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 8           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 8           | NPC Fae | Reporter  | broadcast | I (NPC Dan) inspected NPC Fae and they are not possessed       |
| 8           | NPC Fae | Reporter  | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Fae | Reporter  | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 8           | NPC Fae | Reporter  | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |
| 8           | NPC Fae | Reporter  | reveal    | Player: NPC Bob is not possessed                               |
| 8           | NPC Fae | Reporter  | reveal    | Player: NPC Dan is not possessed                               |
| 8           | NPC Gia | Judge     | broadcast | I (NPC Dan) inspected NPC Fae and they are not possessed       |
| 8           | NPC Gia | Judge     | broadcast | I (NPC Fae) am the Psychic and the Inspector is not possessed  |
| 8           | NPC Gia | Judge     | broadcast | I (NPC Fae) am the Psychic and the Trader is not possessed     |
| 8           | NPC Gia | Judge     | broadcast | I (NPC Fae) am the Psychic and the Thief is not possessed      |

#### Actions Round 9
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 9           | NPC Ann | Medic    | NPC Ed   |          | successful  |
| 9           | NPC Bob | Thief    | NPC Fae  |          | successful  |
| 9           | NPC Cal | Psychic  |          |          | successful  |
| 9           | NPC Fae | Reporter | NPC Ed   |          | successful  |
| 9           | NPC Gia | Judge    | Thief    |          | successful  |

#### States Round 9
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 9           | NPC Bob | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 9           | NPC Dan | Inspector | False      | False     | True       | 1         | True   | 0              | 0                  |
| 9           | NPC Gia | Judge     | False      | True      | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Ed  | Trader    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Ann | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Cal | Psychic   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 9           | NPC Fae | Reporter  | False      | False     | True       | 2         | True   | 0              | 0                  |

#### Notifications Round 9
| round_index | Player  | Role      | message   | details                                                       |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------ |
| 9           | NPC Ann | Medic     | broadcast | I (NPC Bob) am the Thief and I have made NPC Fae vulnerable   |
| 9           | NPC Ann | Medic     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 9           | NPC Ann | Medic     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 9           | NPC Ann | Medic     | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader          |
| 9           | NPC Bob | Thief     | broadcast | I (NPC Bob) am the Thief and I have made NPC Fae vulnerable   |
| 9           | NPC Bob | Thief     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 9           | NPC Bob | Thief     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 9           | NPC Bob | Thief     | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader          |
| 9           | NPC Cal | Psychic   | broadcast | I (NPC Bob) am the Thief and I have made NPC Fae vulnerable   |
| 9           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 9           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 9           | NPC Cal | Psychic   | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader          |
| 9           | NPC Cal | Psychic   | reveal    | Player: NPC Dan is not possessed                              |
| 9           | NPC Cal | Psychic   | reveal    | Player: NPC Bob is not possessed                              |
| 9           | NPC Cal | Psychic   | reveal    | Player: NPC Ann is not possessed                              |
| 9           | NPC Dan | Inspector | broadcast | I (NPC Bob) am the Thief and I have made NPC Fae vulnerable   |
| 9           | NPC Dan | Inspector | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 9           | NPC Dan | Inspector | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 9           | NPC Dan | Inspector | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader          |
| 9           | NPC Ed  | Trader    | broadcast | I (NPC Bob) am the Thief and I have made NPC Fae vulnerable   |
| 9           | NPC Ed  | Trader    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 9           | NPC Ed  | Trader    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 9           | NPC Ed  | Trader    | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader          |
| 9           | NPC Fae | Reporter  | broadcast | I (NPC Bob) am the Thief and I have made NPC Fae vulnerable   |
| 9           | NPC Fae | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 9           | NPC Fae | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 9           | NPC Fae | Reporter  | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader          |
| 9           | NPC Fae | Reporter  | reveal    | NPC Ed is Trader                                              |
| 9           | NPC Gia | Judge     | broadcast | I (NPC Bob) am the Thief and I have made NPC Fae vulnerable   |
| 9           | NPC Gia | Judge     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed     |
| 9           | NPC Gia | Judge     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 9           | NPC Gia | Judge     | broadcast | I (NPC Fae) am the Reporter and NPC Ed is the Trader          |