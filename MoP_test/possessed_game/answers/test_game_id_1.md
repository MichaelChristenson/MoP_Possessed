#### Actions Round 0
| round_index | Player  | Role | action     | Target 1 | Target 2 | status      |
| :-----------| :-------| :----| :----------| :--------| :--------| :---------- |
| 0           | NPC Ann |      | Start Game |          |          | successful  |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Reporter  | False      | True      | False      | 0         | False  | 0              | 0                  |
| 0           | NPC Cal | Inspector | False      | False     | False      | 0         | False  | 0              | 0                  |
| 0           | NPC Ann | Thief     | False      | False     | False      | 0         | False  | 0              | 0                  |
| 0           | NPC Dan | Medic     | False      | False     | False      | 0         | False  | 0              | 0                  |

#### Notifications Round 0
| Player  | Role      | round_index | message     | details                 |
| :-------| :---------| :-----------| :-----------| :---------------------- |
| NPC Ann | Thief     | 0           | role change | Your Role is Thief      |
| NPC Ann | Thief     | 0           | possessed   | You are Not Possessed   |
| NPC Bob | Reporter  | 0           | role change | Your Role is Reporter   |
| NPC Bob | Reporter  | 0           | possessed   | You are Possessed       |
| NPC Cal | Inspector | 0           | role change | Your Role is Inspector  |
| NPC Cal | Inspector | 0           | possessed   | You are Not Possessed   |
| NPC Dan | Medic     | 0           | role change | Your Role is Medic      |
| NPC Dan | Medic     | 0           | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player  | Role | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :----| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann |      | Thief     | NPC Cal  |          | successful  |
| 1           | NPC Bob |      | Reporter  | NPC Dan  |          | successful  |
| 1           | NPC Cal |      | Inspector | NPC Dan  |          | successful  |
| 1           | NPC Dan |      | Medic     | NPC Cal  |          | successful  |

#### States Round 1
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Reporter  | False      | True      | False      | 2         | False  | 0              | 0                  |
| 1           | NPC Cal | Inspector | False      | False     | True       | 0         | False  | 0              | 0                  |
| 1           | NPC Ann | Thief     | False      | False     | False      | 2         | False  | 0              | 0                  |
| 1           | NPC Dan | Medic     | False      | False     | False      | 0         | False  | 0              | 0                  |

#### Notifications Round 1
| Player  | Role      | round_index | message   | details                                                      |
| :-------| :---------| :-----------| :---------| :----------------------------------------------------------- |
| NPC Ann | Thief     | 1           | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| NPC Bob | Reporter  | 1           | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| NPC Cal | Inspector | 1           | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| NPC Dan | Medic     | 1           | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| NPC Ann | Thief     | 1           | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Medic         |
| NPC Bob | Reporter  | 1           | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Medic         |
| NPC Cal | Inspector | 1           | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Medic         |
| NPC Dan | Medic     | 1           | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Medic         |
| NPC Ann | Thief     | 1           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| NPC Bob | Reporter  | 1           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| NPC Cal | Inspector | 1           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| NPC Dan | Medic     | 1           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| NPC Bob | Reporter  | 1           | reveal    | NPC Dan is Medic                                             |
| NPC Cal | Inspector | 1           | reveal    | Medic is Innocent                                            |

#### Actions Round 2
| round_index | Player  | Role | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :----| :---------| :--------| :--------| :---------- |
| 2           | NPC Cal |      | Inspector | NPC Dan  |          | successful  |
| 2           | NPC Dan |      | Medic     | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Reporter  | False      | True      | False      | 1         | False  | 0              | 0                  |
| 2           | NPC Cal | Inspector | False      | False     | True       | 2         | False  | 0              | 0                  |
| 2           | NPC Ann | Thief     | False      | False     | False      | 0         | False  | 0              | 0                  |
| 2           | NPC Dan | Medic     | False      | False     | False      | 0         | False  | 0              | 0                  |

#### Notifications Round 2
| Player  | Role      | round_index | message   | details                                                   |
| :-------| :---------| :-----------| :---------| :-------------------------------------------------------- |
| NPC Ann | Thief     | 2           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| NPC Bob | Reporter  | 2           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| NPC Cal | Inspector | 2           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| NPC Dan | Medic     | 2           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| NPC Cal | Inspector | 2           | reveal    | Medic is Innocent                                         |

#### Actions Round 3
| round_index | Player  | Role | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :----| :--------| :--------| :--------| :---------- |
| 3           | NPC Ann |      | Thief    | NPC Bob  |          | successful  |
| 3           | NPC Bob |      | Reporter | NPC Ann  |          | successful  |
| 3           | NPC Dan |      | Medic    | NPC Bob  |          | successful  |

#### States Round 3
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Reporter  | False      | True      | True       | 0         | False  | 0              | 0                  |
| 3           | NPC Cal | Inspector | False      | False     | True       | 1         | False  | 0              | 0                  |
| 3           | NPC Ann | Thief     | False      | False     | False      | 2         | False  | 0              | 0                  |
| 3           | NPC Dan | Medic     | False      | False     | False      | 0         | False  | 0              | 0                  |

#### Notifications Round 3
| Player  | Role      | round_index | message   | details                                                      |
| :-------| :---------| :-----------| :---------| :----------------------------------------------------------- |
| NPC Ann | Thief     | 3           | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| NPC Bob | Reporter  | 3           | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| NPC Cal | Inspector | 3           | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| NPC Dan | Medic     | 3           | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| NPC Ann | Thief     | 3           | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Thief         |
| NPC Bob | Reporter  | 3           | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Thief         |
| NPC Cal | Inspector | 3           | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Thief         |
| NPC Dan | Medic     | 3           | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Thief         |
| NPC Bob | Reporter  | 3           | reveal    | NPC Ann is Thief                                             |

#### Actions Round 4
| round_index | Player  | Role | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :----| :---------| :--------| :--------| :---------- |
| 4           | NPC Bob |      | Reporter  | NPC Cal  |          | successful  |
| 4           | NPC Cal |      | Inspector | NPC Bob  |          | successful  |
| 4           | NPC Dan |      | Medic     | NPC Cal  |          | successful  |

#### States Round 4
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Bob | Reporter  | False      | True      | True       | 2         | False  | 0              | 0                  |
| 4           | NPC Cal | Inspector | False      | False     | True       | 0         | False  | 0              | 0                  |
| 4           | NPC Ann | Thief     | False      | False     | False      | 1         | False  | 0              | 0                  |
| 4           | NPC Dan | Medic     | False      | False     | False      | 0         | False  | 0              | 0                  |

#### Notifications Round 4
| Player  | Role      | round_index | message   | details                                                   |
| :-------| :---------| :-----------| :---------| :-------------------------------------------------------- |
| NPC Ann | Thief     | 4           | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Inspector  |
| NPC Bob | Reporter  | 4           | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Inspector  |
| NPC Cal | Inspector | 4           | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Inspector  |
| NPC Dan | Medic     | 4           | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Inspector  |
| NPC Ann | Thief     | 4           | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed      |
| NPC Bob | Reporter  | 4           | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed      |
| NPC Cal | Inspector | 4           | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed      |
| NPC Dan | Medic     | 4           | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed      |
| NPC Bob | Reporter  | 4           | reveal    | NPC Cal is Inspector                                      |
| NPC Cal | Inspector | 4           | reveal    | Reporter is Possessed                                     |

#### Actions Round 5
| round_index | Player  | Role | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :----| :---------| :--------| :--------| :---------- |
| 5           | NPC Ann |      | Thief     | NPC Dan  |          | successful  |
| 5           | NPC Cal |      | Inspector | NPC Bob  |          | successful  |
| 5           | NPC Dan |      | Medic     | NPC Ann  |          | successful  |

#### States Round 5
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Bob | Reporter  | False      | True      | True       | 1         | False  | 0              | 0                  |
| 5           | NPC Cal | Inspector | False      | False     | True       | 2         | False  | 0              | 0                  |
| 5           | NPC Ann | Thief     | False      | False     | False      | 0         | False  | 0              | 0                  |
| 5           | NPC Dan | Medic     | False      | False     | True       | 0         | False  | 0              | 0                  |

#### Notifications Round 5
| Player  | Role      | round_index | message   | details                                                      |
| :-------| :---------| :-----------| :---------| :----------------------------------------------------------- |
| NPC Ann | Thief     | 5           | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| NPC Bob | Reporter  | 5           | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| NPC Cal | Inspector | 5           | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| NPC Dan | Medic     | 5           | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| NPC Ann | Thief     | 5           | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed         |
| NPC Bob | Reporter  | 5           | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed         |
| NPC Cal | Inspector | 5           | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed         |
| NPC Dan | Medic     | 5           | broadcast | I (NPC Cal) inspected NPC Bob and they are possessed         |
| NPC Cal | Inspector | 5           | reveal    | Reporter is Possessed                                        |

#### Actions Round 6
| round_index | Player  | Role | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :----| :------| :--------| :--------| :---------- |
| 6           | NPC Ann |      | Steal  | NPC Dan  | Medic    | successful  |
| 6           | NPC Dan |      | Medic  | NPC Bob  |          | successful  |

#### States Round 6
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Bob | Reporter  | False      | True      | True       | 0         | False  | 0              | 0                  |
| 6           | NPC Cal | Inspector | False      | False     | True       | 1         | False  | 0              | 0                  |
| 6           | NPC Ann | Medic     | False      | False     | False      | 0         | False  | 0              | 0                  |
| 6           | NPC Dan | Thief     | False      | False     | True       | 0         | False  | 0              | 0                  |

#### Notifications Round 6
| Player | Role | round_index | message | details  |
| :------| :----| :-----------| :-------| :------- |

#### Actions Round 7
| round_index | Player  | Role | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :----| :---------| :--------| :--------| :---------- |
| 7           | NPC Ann |      | Medic     | NPC Cal  |          | successful  |
| 7           | NPC Cal |      | Inspector | NPC Dan  |          | successful  |
| 7           | NPC Dan |      | Thief     | NPC Ann  |          | successful  |

#### States Round 7
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Bob | Reporter  | False      | True      | True       | 0         | False  | 0              | 0                  |
| 7           | NPC Cal | Inspector | False      | False     | True       | 0         | False  | 0              | 0                  |
| 7           | NPC Ann | Medic     | False      | False     | True       | 0         | False  | 0              | 0                  |
| 7           | NPC Dan | Thief     | False      | False     | True       | 2         | False  | 0              | 0                  |

#### Notifications Round 7
| Player  | Role      | round_index | message   | details                                                      |
| :-------| :---------| :-----------| :---------| :----------------------------------------------------------- |
| NPC Ann | Medic     | 7           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| NPC Bob | Reporter  | 7           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| NPC Cal | Inspector | 7           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| NPC Dan | Thief     | 7           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed     |
| NPC Ann | Medic     | 7           | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| NPC Bob | Reporter  | 7           | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| NPC Cal | Inspector | 7           | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| NPC Dan | Thief     | 7           | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| NPC Cal | Inspector | 7           | reveal    | Thief is Innocent                                            |

#### Actions Round 8
| round_index | Player  | Role | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :----| :---------| :--------| :--------| :---------- |
| 8           | NPC Ann |      | Medic     | NPC Dan  |          | successful  |
| 8           | NPC Cal |      | Inspector | NPC Dan  |          | successful  |

#### States Round 8
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Bob | Reporter  | False      | True      | True       | 0         | False  | 0              | 0                  |
| 8           | NPC Cal | Inspector | False      | False     | True       | 2         | False  | 0              | 0                  |
| 8           | NPC Ann | Medic     | False      | False     | True       | 0         | False  | 0              | 0                  |
| 8           | NPC Dan | Thief     | False      | False     | True       | 0         | False  | 0              | 0                  |

#### Notifications Round 8
| Player  | Role      | round_index | message   | details                                                   |
| :-------| :---------| :-----------| :---------| :-------------------------------------------------------- |
| NPC Ann | Medic     | 8           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| NPC Bob | Reporter  | 8           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| NPC Cal | Inspector | 8           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| NPC Dan | Thief     | 8           | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| NPC Cal | Inspector | 8           | reveal    | Thief is Innocent                                         |

#### Actions Round 9
| round_index | Player  | Role | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :----| :------| :--------| :--------| :---------- |
| 9           | NPC Ann |      | Medic  | NPC Bob  |          | successful  |
| 9           | NPC Dan |      | Steal  | NPC Bob  | Reporter | successful  |

#### States Round 9
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 9           | NPC Bob | Thief     | False      | True      | True       | 0         | False  | 0              | 0                  |
| 9           | NPC Cal | Inspector | False      | False     | True       | 1         | False  | 0              | 0                  |
| 9           | NPC Ann | Medic     | False      | False     | True       | 0         | False  | 0              | 0                  |
| 9           | NPC Dan | Reporter  | False      | False     | True       | 0         | False  | 0              | 0                  |

#### Notifications Round 9
| Player | Role | round_index | message | details  |
| :------| :----| :-----------| :-------| :------- |

#### Actions Round 10
| round_index | Player  | Role | action    | Target 1 | Target 2  | status      |
| :-----------| :-------| :----| :---------| :--------| :---------| :---------- |
| 10          | NPC Ann |      | Medic     | NPC Cal  |           | successful  |
| 10          | NPC Bob |      | Steal     | NPC Cal  | Inspector | successful  |
| 10          | NPC Cal |      | Inspector | NPC Ann  |           | successful  |
| 10          | NPC Dan |      | Reporter  | NPC Ann  |           | successful  |

#### States Round 10
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 10          | NPC Bob | Inspector | False      | True      | True       | 0         | True   | 0              | 0                  |
| 10          | NPC Cal | Thief     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 10          | NPC Ann | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 10          | NPC Dan | Reporter  | False      | False     | True       | 2         | True   | 0              | 0                  |

#### Notifications Round 10
| Player  | Role      | round_index | message   | details                                                   |
| :-------| :---------| :-----------| :---------| :-------------------------------------------------------- |
| NPC Ann | Medic     | 10          | broadcast | I (NPC Cal) inspected NPC Ann and they are not possessed  |
| NPC Bob | Inspector | 10          | broadcast | I (NPC Cal) inspected NPC Ann and they are not possessed  |
| NPC Cal | Thief     | 10          | broadcast | I (NPC Cal) inspected NPC Ann and they are not possessed  |
| NPC Dan | Reporter  | 10          | broadcast | I (NPC Cal) inspected NPC Ann and they are not possessed  |
| NPC Ann | Medic     | 10          | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Medic      |
| NPC Bob | Inspector | 10          | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Medic      |
| NPC Cal | Thief     | 10          | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Medic      |
| NPC Dan | Reporter  | 10          | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Medic      |
| NPC Cal | Thief     | 10          | reveal    | Medic is Innocent                                         |
| NPC Dan | Reporter  | 10          | reveal    | NPC Ann is Medic                                          |