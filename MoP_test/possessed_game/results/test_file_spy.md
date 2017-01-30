#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 53   | 5       | 10      |

#### Roles
| Role         |
| :----------- |
| Spy          |
| Thief        |
| Inspector    |
| Judge        |
| Executioner  |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
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
| 0           | NPC Cal | Spy         | role change | Your Role is Spy          |
| 0           | NPC Cal | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Dan | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Thief       | role change | Your Role is Thief        |
| 0           | NPC Ed  | Thief       | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Judge     | Spy      |          | successful  |
| 1           | NPC Bob | Inspector | NPC Ed   |          | successful  |
| 1           | NPC Cal | Spy       |          |          | successful  |
| 1           | NPC Ed  | Thief     | NPC Dan  |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 1           | NPC Ann | Judge       | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed     |
| 1           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed     |
| 1           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Bob | Inspector   | reveal    | Thief is Innocent                                           |
| 1           | NPC Cal | Spy         | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed     |
| 1           | NPC Cal | Spy         | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Cal | Spy         | reveal    | NPC Ed is targeting NPC Dan                                 |
| 1           | NPC Cal | Spy         | reveal    | NPC Bob is targeting NPC Ed                                 |
| 1           | NPC Cal | Spy         | reveal    | NPC Ann is targeting NPC Cal                                |
| 1           | NPC Dan | Executioner | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed     |
| 1           | NPC Dan | Executioner | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Ed  | Thief       | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed     |
| 1           | NPC Ed  | Thief       | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |

#### Actions Round 2
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 2           | NPC Ann | Judge  | Thief    |          | successful  |
| 2           | NPC Cal | Spy    |          |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Bob | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 2           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan   |
| 2           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed   |
| 2           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Cal  |
| 2           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan   |
| 2           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed   |
| 2           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Cal  |
| 2           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan   |
| 2           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed   |
| 2           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Cal  |
| 2           | NPC Cal | Spy         | reveal    | NPC Ed is targeting NPC Dan                              |
| 2           | NPC Cal | Spy         | reveal    | NPC Bob is targeting NPC Ed                              |
| 2           | NPC Cal | Spy         | reveal    | NPC Ann is targeting NPC Ed                              |
| 2           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan   |
| 2           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed   |
| 2           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Cal  |
| 2           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan   |
| 2           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed   |
| 2           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Cal  |

#### Actions Round 3
| round_index | Player  | action    | Target 1  | Target 2 | status      |
| :-----------| :-------| :---------| :---------| :--------| :---------- |
| 3           | NPC Ann | Judge     | Inspector |          | successful  |
| 3           | NPC Bob | Inspector | NPC Cal   |          | successful  |
| 3           | NPC Cal | Spy       |           |          | successful  |
| 3           | NPC Ed  | Thief     | NPC Bob   |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Bob | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed    |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan      |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed      |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Ed      |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed    |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan      |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed      |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Ed      |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Bob | Inspector   | reveal    | Spy is Innocent                                             |
| 3           | NPC Cal | Spy         | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed    |
| 3           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan      |
| 3           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed      |
| 3           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Ed      |
| 3           | NPC Cal | Spy         | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Cal | Spy         | reveal    | NPC Ed is targeting NPC Bob                                 |
| 3           | NPC Cal | Spy         | reveal    | NPC Bob is targeting NPC Cal                                |
| 3           | NPC Cal | Spy         | reveal    | NPC Ann is targeting NPC Bob                                |
| 3           | NPC Dan | Executioner | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed    |
| 3           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan      |
| 3           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed      |
| 3           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Ed      |
| 3           | NPC Dan | Executioner | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Ed  | Thief       | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed    |
| 3           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan      |
| 3           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed      |
| 3           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Ed      |
| 3           | NPC Ed  | Thief       | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |

#### Actions Round 4
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 4           | NPC Ann | Judge  | Spy      |          | successful  |
| 4           | NPC Cal | Spy    |          |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Bob | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal  |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Bob  |
| 4           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal  |
| 4           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Bob  |
| 4           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal  |
| 4           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Bob  |
| 4           | NPC Cal | Spy         | reveal    | NPC Ed is targeting NPC Bob                              |
| 4           | NPC Cal | Spy         | reveal    | NPC Bob is targeting NPC Cal                             |
| 4           | NPC Cal | Spy         | reveal    | NPC Ann is targeting NPC Cal                             |
| 4           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal  |
| 4           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Bob  |
| 4           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob   |
| 4           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal  |
| 4           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Bob  |

#### Actions Round 5
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 5           | NPC Ann | Judge     | Thief    |          | successful  |
| 5           | NPC Bob | Inspector | NPC Ann  |          | successful  |
| 5           | NPC Cal | Spy       |          |          | successful  |
| 5           | NPC Ed  | Thief     | NPC Cal  |          | successful  |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Bob | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed        |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob      |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal     |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Cal     |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 5           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed        |
| 5           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob      |
| 5           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal     |
| 5           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Cal     |
| 5           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 5           | NPC Bob | Inspector   | reveal    | Judge is Possessed                                          |
| 5           | NPC Cal | Spy         | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed        |
| 5           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob      |
| 5           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal     |
| 5           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Cal     |
| 5           | NPC Cal | Spy         | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 5           | NPC Cal | Spy         | reveal    | NPC Ed is targeting NPC Cal                                 |
| 5           | NPC Cal | Spy         | reveal    | NPC Bob is targeting NPC Ann                                |
| 5           | NPC Cal | Spy         | reveal    | NPC Ann is targeting NPC Ed                                 |
| 5           | NPC Dan | Executioner | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed        |
| 5           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob      |
| 5           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal     |
| 5           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Cal     |
| 5           | NPC Dan | Executioner | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 5           | NPC Ed  | Thief       | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed        |
| 5           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob      |
| 5           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal     |
| 5           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Cal     |
| 5           | NPC Ed  | Thief       | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |

#### Actions Round 6
| round_index | Player  | action      | Target 1 | Target 2 | status      |
| :-----------| :-------| :-----------| :--------| :--------| :---------- |
| 6           | NPC Ann | Judge       | Spy      |          | successful  |
| 6           | NPC Cal | Spy         |          |          | successful  |
| 6           | NPC Dan | Executioner | NPC Ann  |          | successful  |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Cal | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Ed  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Bob | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Ann | Judge       | True       | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan | Executioner | False      | False     | True       | 4         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role        | message     | details                                                  |
| :-----------| :-------| :-----------| :-----------| :------------------------------------------------------- |
| 6           | NPC Ann | Judge       | broadcast   | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal   |
| 6           | NPC Ann | Judge       | broadcast   | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann  |
| 6           | NPC Ann | Judge       | broadcast   | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Ed   |
| 6           | NPC Ann | Judge       | elimination | NPC Ann has been eliminated                              |
| 6           | NPC Ann | Judge       | game over   | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                  |
| 6           | NPC Bob | Inspector   | broadcast   | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal   |
| 6           | NPC Bob | Inspector   | broadcast   | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann  |
| 6           | NPC Bob | Inspector   | broadcast   | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Ed   |
| 6           | NPC Bob | Inspector   | elimination | NPC Ann has been eliminated                              |
| 6           | NPC Bob | Inspector   | game over   | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                  |
| 6           | NPC Cal | Spy         | broadcast   | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal   |
| 6           | NPC Cal | Spy         | broadcast   | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann  |
| 6           | NPC Cal | Spy         | broadcast   | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Ed   |
| 6           | NPC Cal | Spy         | elimination | NPC Ann has been eliminated                              |
| 6           | NPC Cal | Spy         | reveal      | NPC Ed is targeting NPC Cal                              |
| 6           | NPC Cal | Spy         | reveal      | NPC Bob is targeting NPC Ann                             |
| 6           | NPC Cal | Spy         | reveal      | NPC Dan is targeting NPC Ann                             |
| 6           | NPC Cal | Spy         | game over   | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                  |
| 6           | NPC Dan | Executioner | broadcast   | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal   |
| 6           | NPC Dan | Executioner | broadcast   | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann  |
| 6           | NPC Dan | Executioner | broadcast   | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Ed   |
| 6           | NPC Dan | Executioner | elimination | NPC Ann has been eliminated                              |
| 6           | NPC Dan | Executioner | game over   | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                  |
| 6           | NPC Ed  | Thief       | broadcast   | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal   |
| 6           | NPC Ed  | Thief       | broadcast   | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann  |
| 6           | NPC Ed  | Thief       | broadcast   | I (NPC Cal) am the Spy and NPC Ann is targeting NPC Ed   |
| 6           | NPC Ed  | Thief       | elimination | NPC Ann has been eliminated                              |
| 6           | NPC Ed  | Thief       | game over   | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                  |

#### Actions Round 7
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 7           | NPC Ann | Judge     | Spy      |          | successful  |
| 7           | NPC Bob | Inspector | NPC Dan  |          | successful  |
| 7           | NPC Cal | Spy       |          |          | successful  |
| 7           | NPC Ed  | Thief     | NPC Ann  |          | successful  |

#### States Round 7
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Cal | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Ed  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Bob | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Ann | Judge       | True       | True      | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Dan | Executioner | False      | False     | True       | 3         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 7           | NPC Ann | Judge       | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed    |
| 7           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal      |
| 7           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann     |
| 7           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann     |
| 7           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 7           | NPC Ann | Judge       | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                     |
| 7           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed    |
| 7           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal      |
| 7           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann     |
| 7           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann     |
| 7           | NPC Bob | Inspector   | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 7           | NPC Bob | Inspector   | reveal    | Executioner is Innocent                                     |
| 7           | NPC Bob | Inspector   | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                     |
| 7           | NPC Cal | Spy         | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed    |
| 7           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal      |
| 7           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann     |
| 7           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann     |
| 7           | NPC Cal | Spy         | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 7           | NPC Cal | Spy         | reveal    | NPC Ed is targeting NPC Ann                                 |
| 7           | NPC Cal | Spy         | reveal    | NPC Bob is targeting NPC Dan                                |
| 7           | NPC Cal | Spy         | reveal    | NPC Dan is targeting NPC Ann                                |
| 7           | NPC Cal | Spy         | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                     |
| 7           | NPC Dan | Executioner | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed    |
| 7           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal      |
| 7           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann     |
| 7           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann     |
| 7           | NPC Dan | Executioner | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 7           | NPC Dan | Executioner | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                     |
| 7           | NPC Ed  | Thief       | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed    |
| 7           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal      |
| 7           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann     |
| 7           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann     |
| 7           | NPC Ed  | Thief       | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 7           | NPC Ed  | Thief       | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                     |

#### Actions Round 8
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 8           | NPC Ann | Judge  | Spy      |          | successful  |
| 8           | NPC Cal | Spy    |          |          | successful  |

#### States Round 8
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Cal | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Ed  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Bob | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 8           | NPC Ann | Judge       | True       | True      | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Dan | Executioner | False      | False     | True       | 2         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 8           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann   |
| 8           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan  |
| 8           | NPC Ann | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann  |
| 8           | NPC Ann | Judge       | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                  |
| 8           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann   |
| 8           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan  |
| 8           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann  |
| 8           | NPC Bob | Inspector   | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                  |
| 8           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann   |
| 8           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan  |
| 8           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann  |
| 8           | NPC Cal | Spy         | reveal    | NPC Ed is targeting NPC Ann                              |
| 8           | NPC Cal | Spy         | reveal    | NPC Bob is targeting NPC Dan                             |
| 8           | NPC Cal | Spy         | reveal    | NPC Dan is targeting NPC Ann                             |
| 8           | NPC Cal | Spy         | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                  |
| 8           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann   |
| 8           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan  |
| 8           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann  |
| 8           | NPC Dan | Executioner | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                  |
| 8           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann   |
| 8           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan  |
| 8           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann  |
| 8           | NPC Ed  | Thief       | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                  |

#### Actions Round 9
| round_index | Player  | action    | Target 1  | Target 2 | status      |
| :-----------| :-------| :---------| :---------| :--------| :---------- |
| 9           | NPC Ann | Judge     | Inspector |          | successful  |
| 9           | NPC Bob | Inspector | NPC Cal   |          | successful  |
| 9           | NPC Cal | Spy       |           |          | successful  |
| 9           | NPC Ed  | Steal     | NPC Ann   | Judge    | successful  |

#### States Round 9
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 9           | NPC Cal | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Bob | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 9           | NPC Ann | Thief       | True       | True      | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Dan | Executioner | False      | False     | True       | 1         | True   | 0              | 0                  |

#### Notifications Round 9
| round_index | Player  | Role        | message   | details                                                   |
| :-----------| :-------| :-----------| :---------| :-------------------------------------------------------- |
| 9           | NPC Ann | Thief       | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |
| 9           | NPC Ann | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann    |
| 9           | NPC Ann | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan   |
| 9           | NPC Ann | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann   |
| 9           | NPC Ann | Thief       | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                   |
| 9           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |
| 9           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann    |
| 9           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan   |
| 9           | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann   |
| 9           | NPC Bob | Inspector   | reveal    | Spy is Innocent                                           |
| 9           | NPC Bob | Inspector   | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                   |
| 9           | NPC Cal | Spy         | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |
| 9           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann    |
| 9           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan   |
| 9           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann   |
| 9           | NPC Cal | Spy         | reveal    | NPC Bob is targeting NPC Cal                              |
| 9           | NPC Cal | Spy         | reveal    | NPC Dan is targeting NPC Ann                              |
| 9           | NPC Cal | Spy         | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                   |
| 9           | NPC Dan | Executioner | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |
| 9           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann    |
| 9           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan   |
| 9           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann   |
| 9           | NPC Dan | Executioner | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                   |
| 9           | NPC Ed  | Judge       | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |
| 9           | NPC Ed  | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann    |
| 9           | NPC Ed  | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan   |
| 9           | NPC Ed  | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann   |
| 9           | NPC Ed  | Judge       | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                   |

#### Actions Round 10
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 10          | NPC Ann | Thief  | NPC Ed   |          | successful  |
| 10          | NPC Cal | Spy    |          |          | successful  |
| 10          | NPC Ed  | Judge  | Spy      |          | successful  |

#### States Round 10
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 10          | NPC Cal | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 10          | NPC Ed  | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 10          | NPC Bob | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 10          | NPC Ann | Thief       | True       | True      | True       | 2         | True   | 0              | 0                  |
| 10          | NPC Dan | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 10
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 10          | NPC Ann | Thief       | broadcast | I (NPC Ann) am the Thief and I have made NPC Ed vulnerable  |
| 10          | NPC Ann | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal     |
| 10          | NPC Ann | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann     |
| 10          | NPC Ann | Thief       | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                     |
| 10          | NPC Bob | Inspector   | broadcast | I (NPC Ann) am the Thief and I have made NPC Ed vulnerable  |
| 10          | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal     |
| 10          | NPC Bob | Inspector   | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann     |
| 10          | NPC Bob | Inspector   | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                     |
| 10          | NPC Cal | Spy         | broadcast | I (NPC Ann) am the Thief and I have made NPC Ed vulnerable  |
| 10          | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal     |
| 10          | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann     |
| 10          | NPC Cal | Spy         | reveal    | NPC Ed is targeting NPC Cal                                 |
| 10          | NPC Cal | Spy         | reveal    | NPC Bob is targeting NPC Cal                                |
| 10          | NPC Cal | Spy         | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                     |
| 10          | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Thief and I have made NPC Ed vulnerable  |
| 10          | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal     |
| 10          | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann     |
| 10          | NPC Dan | Executioner | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                     |
| 10          | NPC Ed  | Judge       | broadcast | I (NPC Ann) am the Thief and I have made NPC Ed vulnerable  |
| 10          | NPC Ed  | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal     |
| 10          | NPC Ed  | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ann     |
| 10          | NPC Ed  | Judge       | game over | NPC Cal, NPC Ed, NPC Bob, NPC Dan Wins!                     |