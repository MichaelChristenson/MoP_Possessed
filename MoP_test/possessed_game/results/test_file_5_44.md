#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 44   | 5       | 7       |

#### Roles
| Role       |
| :--------- |
| Psychic    |
| Inspector  |
| Judge      |
| Reporter   |
| Thief      |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Reporter  | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Ann | Reporter  | possessed   | You are Possessed       |
| 0           | NPC Bob | Judge     | role change | Your Role is Judge      |
| 0           | NPC Bob | Judge     | possessed   | You are Not Possessed   |
| 0           | NPC Cal | Psychic   | role change | Your Role is Psychic    |
| 0           | NPC Cal | Psychic   | possessed   | You are Not Possessed   |
| 0           | NPC Dan | Thief     | role change | Your Role is Thief      |
| 0           | NPC Dan | Thief     | possessed   | You are Not Possessed   |
| 0           | NPC Ed  | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Ed  | Inspector | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player  | action    | Target 1  | Target 2 | status      |
| :-----------| :-------| :---------| :---------| :--------| :---------- |
| 1           | NPC Ann | Reporter  | NPC Cal   |          | successful  |
| 1           | NPC Bob | Judge     | Inspector |          | successful  |
| 1           | NPC Cal | Psychic   |           |          | successful  |
| 1           | NPC Dan | Thief     | NPC Cal   |          | successful  |
| 1           | NPC Ed  | Inspector | NPC Bob   |          | successful  |

#### States Round 1
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Psychic   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 1           | NPC Ed  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Reporter  | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Reporter  | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic       |
| 1           | NPC Ann | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed    |
| 1           | NPC Ann | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed    |
| 1           | NPC Ann | Reporter  | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ann | Reporter  | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed      |
| 1           | NPC Ann | Reporter  | reveal    | NPC Cal is Psychic                                           |
| 1           | NPC Bob | Judge     | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic       |
| 1           | NPC Bob | Judge     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed    |
| 1           | NPC Bob | Judge     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed    |
| 1           | NPC Bob | Judge     | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Bob | Judge     | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed      |
| 1           | NPC Cal | Psychic   | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic       |
| 1           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed    |
| 1           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed    |
| 1           | NPC Cal | Psychic   | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Cal | Psychic   | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed      |
| 1           | NPC Cal | Psychic   | reveal    | Player: NPC Ed is not possessed                              |
| 1           | NPC Dan | Thief     | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic       |
| 1           | NPC Dan | Thief     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed    |
| 1           | NPC Dan | Thief     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed    |
| 1           | NPC Dan | Thief     | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Dan | Thief     | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed      |
| 1           | NPC Ed  | Inspector | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic       |
| 1           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed    |
| 1           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed    |
| 1           | NPC Ed  | Inspector | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ed  | Inspector | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed      |
| 1           | NPC Ed  | Inspector | reveal    | Judge is Innocent                                            |

#### Actions Round 2
| round_index | Player  | action  | Target 1  | Target 2 | status      |
| :-----------| :-------| :-------| :---------| :--------| :---------- |
| 2           | NPC Bob | Judge   | Inspector |          | successful  |
| 2           | NPC Cal | Psychic |           |          | successful  |

#### States Round 2
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Psychic   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Reporter  | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 2           | NPC Ann | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Ann | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Bob | Judge     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Bob | Judge     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal | Psychic   | reveal    | Player: NPC Bob is not possessed                               |
| 2           | NPC Dan | Thief     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Dan | Thief     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 2           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 3           | NPC Ann | Reporter  | NPC Dan  |          | successful  |
| 3           | NPC Bob | Judge     | Psychic  |          | successful  |
| 3           | NPC Cal | Psychic   |          |          | successful  |
| 3           | NPC Dan | Thief     | NPC Ann  |          | successful  |
| 3           | NPC Ed  | Inspector | NPC Bob  |          | successful  |

#### States Round 3
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal | Psychic   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 3           | NPC Ed  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Reporter  | False      | True      | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann | Reporter  | broadcast | I (NPC Ann) am the Reporter and NPC Dan is the Thief         |
| 3           | NPC Ann | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed    |
| 3           | NPC Ann | Reporter  | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Ann | Reporter  | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed      |
| 3           | NPC Ann | Reporter  | reveal    | NPC Dan is Thief                                             |
| 3           | NPC Bob | Judge     | broadcast | I (NPC Ann) am the Reporter and NPC Dan is the Thief         |
| 3           | NPC Bob | Judge     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed    |
| 3           | NPC Bob | Judge     | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Bob | Judge     | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed      |
| 3           | NPC Cal | Psychic   | broadcast | I (NPC Ann) am the Reporter and NPC Dan is the Thief         |
| 3           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed    |
| 3           | NPC Cal | Psychic   | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Cal | Psychic   | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed      |
| 3           | NPC Cal | Psychic   | reveal    | Player: NPC Ed is not possessed                              |
| 3           | NPC Dan | Thief     | broadcast | I (NPC Ann) am the Reporter and NPC Dan is the Thief         |
| 3           | NPC Dan | Thief     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed    |
| 3           | NPC Dan | Thief     | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Dan | Thief     | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed      |
| 3           | NPC Ed  | Inspector | broadcast | I (NPC Ann) am the Reporter and NPC Dan is the Thief         |
| 3           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed    |
| 3           | NPC Ed  | Inspector | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Ed  | Inspector | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed      |
| 3           | NPC Ed  | Inspector | reveal    | Judge is Innocent                                            |

#### Actions Round 4
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 4           | NPC Bob | Judge   | Reporter |          | successful  |
| 4           | NPC Cal | Psychic |          |          | successful  |

#### States Round 4
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal | Psychic   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Ed  | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Reporter  | False      | True      | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 4           | NPC Ann | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Ann | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Bob | Judge     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Bob | Judge     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Cal | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 4           | NPC Dan | Thief     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Dan | Thief     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 4           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |

#### Actions Round 5
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 5           | NPC Ann | Reporter  | NPC Bob  |          | successful  |
| 5           | NPC Bob | Judge     | Psychic  |          | successful  |
| 5           | NPC Cal | Psychic   |          |          | successful  |
| 5           | NPC Dan | Thief     | NPC Bob  |          | successful  |
| 5           | NPC Ed  | Inspector | NPC Bob  |          | successful  |

#### States Round 5
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal | Psychic   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 5           | NPC Ed  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Bob | Judge     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Ann | Reporter  | False      | True      | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Dan | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 5           | NPC Ann | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 5           | NPC Ann | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ann | Reporter  | broadcast | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable    |
| 5           | NPC Ann | Reporter  | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed        |
| 5           | NPC Ann | Reporter  | reveal    | NPC Bob is Judge                                               |
| 5           | NPC Bob | Judge     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 5           | NPC Bob | Judge     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Bob | Judge     | broadcast | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable    |
| 5           | NPC Bob | Judge     | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed        |
| 5           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 5           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Cal | Psychic   | broadcast | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable    |
| 5           | NPC Cal | Psychic   | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed        |
| 5           | NPC Cal | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 5           | NPC Dan | Thief     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 5           | NPC Dan | Thief     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Dan | Thief     | broadcast | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable    |
| 5           | NPC Dan | Thief     | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed        |
| 5           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 5           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ed  | Inspector | broadcast | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable    |
| 5           | NPC Ed  | Inspector | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed        |
| 5           | NPC Ed  | Inspector | reveal    | Judge is Innocent                                              |

#### Actions Round 6
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 6           | NPC Bob | Judge   | Psychic  |          | successful  |
| 6           | NPC Cal | Psychic |          |          | successful  |

#### States Round 6
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Cal | Psychic   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Ed  | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Bob | Judge     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Ann | Reporter  | False      | True      | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Dan | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 6           | NPC Ann | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Ann | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Bob | Judge     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Bob | Judge     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Cal | Psychic   | reveal    | Player: NPC Bob is not possessed                               |
| 6           | NPC Dan | Thief     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Dan | Thief     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed      |
| 6           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |

#### Actions Round 7
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 7           | NPC Ann | Reporter  | NPC Ed   |          | successful  |
| 7           | NPC Bob | Judge     | Thief    |          | successful  |
| 7           | NPC Cal | Psychic   |          |          | successful  |
| 7           | NPC Dan | Thief     | NPC Ed   |          | successful  |
| 7           | NPC Ed  | Inspector | NPC Dan  |          | successful  |

#### States Round 7
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Cal | Psychic   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 7           | NPC Ed  | Inspector | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Bob | Judge     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Ann | Reporter  | False      | True      | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Dan | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role      | message   | details                                                     |
| :-----------| :-------| :---------| :---------| :---------------------------------------------------------- |
| 7           | NPC Ann | Reporter  | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Inspector     |
| 7           | NPC Ann | Reporter  | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed   |
| 7           | NPC Ann | Reporter  | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 7           | NPC Ann | Reporter  | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed     |
| 7           | NPC Ann | Reporter  | reveal    | NPC Ed is Inspector                                         |
| 7           | NPC Bob | Judge     | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Inspector     |
| 7           | NPC Bob | Judge     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed   |
| 7           | NPC Bob | Judge     | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 7           | NPC Bob | Judge     | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed     |
| 7           | NPC Cal | Psychic   | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Inspector     |
| 7           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed   |
| 7           | NPC Cal | Psychic   | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 7           | NPC Cal | Psychic   | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed     |
| 7           | NPC Cal | Psychic   | reveal    | Player: NPC Ed is not possessed                             |
| 7           | NPC Cal | Psychic   | reveal    | Player: NPC Dan is not possessed                            |
| 7           | NPC Dan | Thief     | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Inspector     |
| 7           | NPC Dan | Thief     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed   |
| 7           | NPC Dan | Thief     | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 7           | NPC Dan | Thief     | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed     |
| 7           | NPC Ed  | Inspector | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Inspector     |
| 7           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed   |
| 7           | NPC Ed  | Inspector | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 7           | NPC Ed  | Inspector | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed     |
| 7           | NPC Ed  | Inspector | reveal    | Thief is Innocent                                           |