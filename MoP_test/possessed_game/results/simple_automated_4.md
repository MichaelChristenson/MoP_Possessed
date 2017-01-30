#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 1    | 4       | 10      |

#### Roles
| Role         |
| :----------- |
| Reporter     |
| Inspector    |
| Thief        |
| Medic        |
| Judge        |
| Executioner  |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Reporter  | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Thief     | role change | Your Role is Thief      |
| 0           | NPC Ann | Thief     | possessed   | You are Not Possessed   |
| 0           | NPC Bob | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Bob | Reporter  | possessed   | You are Possessed       |
| 0           | NPC Cal | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Cal | Inspector | possessed   | You are Not Possessed   |
| 0           | NPC Dan | Medic     | role change | Your Role is Medic      |
| 0           | NPC Dan | Medic     | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Thief     | NPC Cal  |          | successful  |
| 1           | NPC Bob | Reporter  | NPC Dan  |          | successful  |
| 1           | NPC Cal | Inspector | NPC Dan  |          | successful  |
| 1           | NPC Dan | Medic     | NPC Cal  |          | successful  |

#### States Round 1
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Reporter  | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal | Inspector | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Thief     | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ann | Thief     | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Ann | Thief     | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| 1           | NPC Bob | Reporter  | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Bob | Reporter  | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Bob | Reporter  | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| 1           | NPC Bob | Reporter  | reveal    | NPC Dan is Medic                                             |
| 1           | NPC Cal | Inspector | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Cal | Inspector | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Cal | Inspector | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| 1           | NPC Cal | Inspector | reveal    | Medic is Innocent                                            |
| 1           | NPC Dan | Medic     | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Dan | Medic     | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Medic         |
| 1           | NPC Dan | Medic     | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |

#### Actions Round 2
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 2           | NPC Cal | Inspector | NPC Dan  |          | successful  |
| 2           | NPC Dan | Medic     | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Reporter  | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal | Inspector | False      | False     | True       | 2         | True   | 0              | 0                  |
| 2           | NPC Ann | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role      | message   | details                                                   |
| :-----------| :-------| :---------| :---------| :-------------------------------------------------------- |
| 2           | NPC Ann | Thief     | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| 2           | NPC Bob | Reporter  | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| 2           | NPC Cal | Inspector | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| 2           | NPC Cal | Inspector | reveal    | Medic is Innocent                                         |
| 2           | NPC Dan | Medic     | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 3           | NPC Ann | Thief    | NPC Bob  |          | successful  |
| 3           | NPC Bob | Reporter | NPC Ann  |          | successful  |
| 3           | NPC Dan | Medic    | NPC Bob  |          | successful  |

#### States Round 3
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Reporter  | False      | True      | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Inspector | False      | False     | True       | 1         | True   | 0              | 0                  |
| 3           | NPC Ann | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann | Thief     | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Ann | Thief     | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Thief         |
| 3           | NPC Bob | Reporter  | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Bob | Reporter  | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Thief         |
| 3           | NPC Bob | Reporter  | reveal    | NPC Ann is Thief                                             |
| 3           | NPC Cal | Inspector | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Cal | Inspector | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Thief         |
| 3           | NPC Dan | Medic     | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Dan | Medic     | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Thief         |

#### Actions Round 4
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 4           | NPC Bob | Reporter  | NPC Cal  |          | successful  |
| 4           | NPC Cal | Inspector | NPC Bob  |          | successful  |
| 4           | NPC Dan | Medic     | NPC Cal  |          | successful  |

#### States Round 4
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Bob | Reporter  | False      | True      | True       | 2         | True   | 0              | 0                  |
| 4           | NPC Cal | Inspector | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role      | message   | details                                                   |
| :-----------| :-------| :---------| :---------| :-------------------------------------------------------- |
| 4           | NPC Ann | Thief     | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Inspector  |
| 4           | NPC Ann | Thief     | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed      |
| 4           | NPC Bob | Reporter  | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Inspector  |
| 4           | NPC Bob | Reporter  | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed      |
| 4           | NPC Bob | Reporter  | reveal    | NPC Cal is Inspector                                      |
| 4           | NPC Cal | Inspector | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Inspector  |
| 4           | NPC Cal | Inspector | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed      |
| 4           | NPC Cal | Inspector | reveal    | Reporter is Possessed                                     |
| 4           | NPC Dan | Medic     | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Inspector  |
| 4           | NPC Dan | Medic     | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed      |

#### Actions Round 5
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 5           | NPC Ann | Thief     | NPC Dan  |          | successful  |
| 5           | NPC Cal | Inspector | NPC Bob  |          | successful  |
| 5           | NPC Dan | Medic     | NPC Ann  |          | successful  |

#### States Round 5
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Bob | Reporter  | False      | True      | True       | 1         | True   | 0              | 0                  |
| 5           | NPC Cal | Inspector | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Ann | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 5           | NPC Ann | Thief     | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| 5           | NPC Ann | Thief     | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed         |
| 5           | NPC Bob | Reporter  | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| 5           | NPC Bob | Reporter  | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed         |
| 5           | NPC Cal | Inspector | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| 5           | NPC Cal | Inspector | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed         |
| 5           | NPC Cal | Inspector | reveal    | Reporter is Possessed                                        |
| 5           | NPC Dan | Medic     | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| 5           | NPC Dan | Medic     | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed         |

#### Actions Round 6
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 6           | NPC Ann | Steal  | NPC Dan  | Medic    | successful  |
| 6           | NPC Dan | Medic  | NPC Bob  |          | successful  |

#### States Round 6
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Bob | Reporter  | False      | True      | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Inspector | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Ann | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan | Thief     | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |

#### Actions Round 7
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 7           | NPC Ann | Medic     | NPC Cal  |          | successful  |
| 7           | NPC Cal | Inspector | NPC Dan  |          | successful  |
| 7           | NPC Dan | Thief     | NPC Ann  |          | successful  |

#### States Round 7
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Bob | Reporter  | False      | True      | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Cal | Inspector | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Ann | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Dan | Thief     | False      | False     | True       | 2         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 7           | NPC Ann | Medic     | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| 7           | NPC Ann | Medic     | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 7           | NPC Bob | Reporter  | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| 7           | NPC Bob | Reporter  | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 7           | NPC Cal | Inspector | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| 7           | NPC Cal | Inspector | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 7           | NPC Cal | Inspector | reveal    | Thief is Innocent                                            |
| 7           | NPC Dan | Thief     | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| 7           | NPC Dan | Thief     | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |

#### Actions Round 8
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 8           | NPC Ann | Medic     | NPC Dan  |          | successful  |
| 8           | NPC Cal | Inspector | NPC Dan  |          | successful  |

#### States Round 8
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Bob | Reporter  | False      | True      | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Cal | Inspector | False      | False     | True       | 2         | True   | 0              | 0                  |
| 8           | NPC Ann | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Dan | Thief     | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player  | Role      | message   | details                                                   |
| :-----------| :-------| :---------| :---------| :-------------------------------------------------------- |
| 8           | NPC Ann | Medic     | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| 8           | NPC Bob | Reporter  | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| 8           | NPC Cal | Inspector | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| 8           | NPC Cal | Inspector | reveal    | Thief is Innocent                                         |
| 8           | NPC Dan | Thief     | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |

#### Actions Round 9
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 9           | NPC Ann | Medic  | NPC Bob  |          | successful  |
| 9           | NPC Dan | Steal  | NPC Bob  | Reporter | successful  |

#### States Round 9
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 9           | NPC Bob | Thief     | False      | True      | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Cal | Inspector | False      | False     | True       | 1         | True   | 0              | 0                  |
| 9           | NPC Ann | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Dan | Reporter  | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 9
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |

#### Actions Round 10
| round_index | Player  | action    | Target 1 | Target 2  | status      |
| :-----------| :-------| :---------| :--------| :---------| :---------- |
| 10          | NPC Ann | Medic     | NPC Cal  |           | successful  |
| 10          | NPC Bob | Steal     | NPC Cal  | Inspector | successful  |
| 10          | NPC Cal | Inspector | NPC Ann  |           | successful  |
| 10          | NPC Dan | Reporter  | NPC Ann  |           | successful  |

#### States Round 10
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 10          | NPC Bob | Inspector | False      | True      | True       | 0         | True   | 0              | 0                  |
| 10          | NPC Cal | Thief     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 10          | NPC Ann | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 10          | NPC Dan | Reporter  | False      | False     | True       | 2         | True   | 0              | 0                  |

#### Notifications Round 10
| round_index | Player  | Role      | message   | details                                                   |
| :-----------| :-------| :---------| :---------| :-------------------------------------------------------- |
| 10          | NPC Ann | Medic     | broadcast | I (NPC Cal) inspected NPC Ann and they are not possessed  |
| 10          | NPC Ann | Medic     | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Medic      |
| 10          | NPC Bob | Inspector | broadcast | I (NPC Cal) inspected NPC Ann and they are not possessed  |
| 10          | NPC Bob | Inspector | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Medic      |
| 10          | NPC Cal | Thief     | broadcast | I (NPC Cal) inspected NPC Ann and they are not possessed  |
| 10          | NPC Cal | Thief     | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Medic      |
| 10          | NPC Cal | Thief     | reveal    | Medic is Innocent                                         |
| 10          | NPC Dan | Reporter  | broadcast | I (NPC Cal) inspected NPC Ann and they are not possessed  |
| 10          | NPC Dan | Reporter  | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Medic      |
| 10          | NPC Dan | Reporter  | reveal    | NPC Ann is Medic                                          |