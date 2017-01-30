#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 56   | 5       | 10      |

#### Roles
| Role         |
| :----------- |
| Trader       |
| Thief        |
| Inspector    |
| Judge        |
| Executioner  |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Judge       | role change | Your Role is Judge        |
| 0           | NPC Ann | Judge       | possessed   | You are Possessed         |
| 0           | NPC Bob | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Bob | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Trader      | role change | Your Role is Trader       |
| 0           | NPC Cal | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Dan | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Thief       | role change | Your Role is Thief        |
| 0           | NPC Ed  | Thief       | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Judge     | Trader   |          | successful  |
| 1           | NPC Bob | Inspector | NPC Ed   |          | successful  |
| 1           | NPC Cal | Trader    | NPC Dan  | NPC Bob  | successful  |
| 1           | NPC Ed  | Thief     | NPC Dan  |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Ed  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Inspector   | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 1           | NPC Ann | Judge       | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed     |
| 1           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Bob | Executioner | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed     |
| 1           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Bob | Executioner | reveal    | Thief is Innocent                                           |
| 1           | NPC Cal | Trader      | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed     |
| 1           | NPC Cal | Trader      | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed     |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Ed  | Thief       | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed     |
| 1           | NPC Ed  | Thief       | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |

#### Actions Round 2
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 2           | NPC Ann | Judge     | Trader   |          | successful  |
| 2           | NPC Dan | Inspector | NPC Ed   |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Ed  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 2           | NPC Ann | Judge       | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed  |
| 2           | NPC Bob | Executioner | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed  |
| 2           | NPC Cal | Trader      | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed  |
| 2           | NPC Dan | Inspector   | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed  |
| 2           | NPC Dan | Inspector   | reveal    | Thief is Innocent                                        |
| 2           | NPC Ed  | Thief       | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed  |

#### Actions Round 3
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 3           | NPC Ann | Judge  | Trader   |          | successful  |
| 3           | NPC Ed  | Thief  | NPC Bob  |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ed  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Bob | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Cal | Trader      | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Ed  | Thief       | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |

#### Actions Round 4
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 4           | NPC Ann | Judge     | Thief    |          | successful  |
| 4           | NPC Dan | Inspector | NPC Cal  |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal | Trader      | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Bob | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                   |
| :-----------| :-------| :-----------| :---------| :-------------------------------------------------------- |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed  |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed  |
| 4           | NPC Cal | Trader      | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed  |
| 4           | NPC Dan | Inspector   | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed  |
| 4           | NPC Dan | Inspector   | reveal    | Trader is Innocent                                        |
| 4           | NPC Ed  | Thief       | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed  |

#### Actions Round 5
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 5           | NPC Ann | Judge  | Trader   |          | successful  |
| 5           | NPC Cal | Trader | NPC Bob  | NPC Dan  | successful  |
| 5           | NPC Ed  | Thief  | NPC Ann  |          | successful  |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 5           | NPC Ed  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Bob | Inspector   | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Ann | Judge       | False      | True      | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Cal | Trader      | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Dan | Executioner | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Ed  | Thief       | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |

#### Actions Round 6
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 6           | NPC Ann | Judge     | Trader   |          | successful  |
| 6           | NPC Bob | Inspector | NPC Dan  |          | successful  |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Cal | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 6           | NPC Ed  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Bob | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 6           | NPC Ann | Judge       | False      | True      | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Dan | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role        | message   | details                                                   |
| :-----------| :-------| :-----------| :---------| :-------------------------------------------------------- |
| 6           | NPC Ann | Judge       | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |
| 6           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |
| 6           | NPC Bob | Inspector   | reveal    | Executioner is Innocent                                   |
| 6           | NPC Cal | Trader      | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |
| 6           | NPC Dan | Executioner | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |
| 6           | NPC Ed  | Thief       | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |

#### Actions Round 7
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 7           | NPC Ann | Judge  | Trader   |          | successful  |
| 7           | NPC Ed  | Thief  | NPC Cal  |          | successful  |

#### States Round 7
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Cal | Trader      | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Ed  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Bob | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 7           | NPC Ann | Judge       | False      | True      | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Dan | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 7           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 7           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 7           | NPC Cal | Trader      | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 7           | NPC Dan | Executioner | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 7           | NPC Ed  | Thief       | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |

#### Actions Round 8
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 8           | NPC Ann | Judge     | Trader   |          | successful  |
| 8           | NPC Bob | Inspector | NPC Cal  |          | successful  |

#### States Round 8
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Cal | Trader      | False      | False     | True       | 1         | True   | 0              | 0                  |
| 8           | NPC Ed  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Bob | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 8           | NPC Ann | Judge       | False      | True      | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Dan | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player  | Role        | message   | details                                                   |
| :-----------| :-------| :-----------| :---------| :-------------------------------------------------------- |
| 8           | NPC Ann | Judge       | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |
| 8           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |
| 8           | NPC Bob | Inspector   | reveal    | Trader is Innocent                                        |
| 8           | NPC Cal | Trader      | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |
| 8           | NPC Dan | Executioner | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |
| 8           | NPC Ed  | Thief       | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |

#### Actions Round 9
| round_index | Player  | action | Target 1  | Target 2    | status      |
| :-----------| :-------| :------| :---------| :-----------| :---------- |
| 9           | NPC Ann | Judge  | Inspector |             | successful  |
| 9           | NPC Cal | Trader | NPC Ed    | NPC Bob     | successful  |
| 9           | NPC Ed  | Steal  | NPC Dan   | Executioner | successful  |

#### States Round 9
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 9           | NPC Cal | Trader      | False      | False     | True       | 4         | True   | 0              | 0                  |
| 9           | NPC Ed  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Bob | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Ann | Judge       | False      | True      | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Dan | Thief       | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 9
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |

#### Actions Round 10
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 10          | NPC Ann | Judge     | Thief    |          | successful  |
| 10          | NPC Dan | Thief     | NPC Ed   |          | successful  |
| 10          | NPC Ed  | Inspector | NPC Dan  |          | successful  |

#### States Round 10
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 10          | NPC Cal | Trader      | False      | False     | True       | 3         | True   | 0              | 0                  |
| 10          | NPC Ed  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 10          | NPC Bob | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 10          | NPC Ann | Judge       | False      | True      | True       | 0         | True   | 0              | 0                  |
| 10          | NPC Dan | Thief       | False      | False     | True       | 2         | True   | 0              | 0                  |

#### Notifications Round 10
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 10          | NPC Ann | Judge       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 10          | NPC Ann | Judge       | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed     |
| 10          | NPC Bob | Executioner | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 10          | NPC Bob | Executioner | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed     |
| 10          | NPC Cal | Trader      | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 10          | NPC Cal | Trader      | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed     |
| 10          | NPC Dan | Thief       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 10          | NPC Dan | Thief       | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed     |
| 10          | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 10          | NPC Ed  | Inspector   | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed     |
| 10          | NPC Ed  | Inspector   | reveal    | Thief is Innocent                                           |