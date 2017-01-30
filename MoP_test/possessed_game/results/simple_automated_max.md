#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 1    | 6       | 10      |

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
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Ann | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Thief       | role change | Your Role is Thief        |
| 0           | NPC Bob | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Judge       | role change | Your Role is Judge        |
| 0           | NPC Cal | Judge       | possessed   | You are Possessed         |
| 0           | NPC Dan | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Dan | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Ed  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Medic       | role change | Your Role is Medic        |
| 0           | NPC Fae | Medic       | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Reporter  | NPC Cal  |          | successful  |
| 1           | NPC Bob | Thief     | NPC Ed   |          | successful  |
| 1           | NPC Cal | Judge     | Medic    |          | successful  |
| 1           | NPC Ed  | Inspector | NPC Bob  |          | successful  |
| 1           | NPC Fae | Medic     | NPC Ed   |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed  | Inspector   | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 1           | NPC Ann | Reporter    | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 1           | NPC Ann | Reporter    | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed     |
| 1           | NPC Ann | Reporter    | reveal    | NPC Cal is Judge                                            |
| 1           | NPC Bob | Thief       | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 1           | NPC Bob | Thief       | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed     |
| 1           | NPC Cal | Judge       | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 1           | NPC Cal | Judge       | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed     |
| 1           | NPC Dan | Executioner | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 1           | NPC Dan | Executioner | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed     |
| 1           | NPC Ed  | Inspector   | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 1           | NPC Ed  | Inspector   | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed     |
| 1           | NPC Ed  | Inspector   | reveal    | Thief is Innocent                                           |
| 1           | NPC Fae | Medic       | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 1           | NPC Fae | Medic       | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed     |

#### Actions Round 2
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 2           | NPC Cal | Judge     | Medic    |          | successful  |
| 2           | NPC Ed  | Inspector | NPC Cal  |          | successful  |
| 2           | NPC Fae | Medic     | NPC Bob  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ann | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 2           | NPC Bob | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                              |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------- |
| 2           | NPC Ann | Reporter    | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed  |
| 2           | NPC Bob | Thief       | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed  |
| 2           | NPC Cal | Judge       | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed  |
| 2           | NPC Dan | Executioner | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed  |
| 2           | NPC Ed  | Inspector   | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed  |
| 2           | NPC Ed  | Inspector   | reveal    | Judge is Possessed                                   |
| 2           | NPC Fae | Medic       | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed  |

#### Actions Round 3
| round_index | Player  | action      | Target 1 | Target 2 | status      |
| :-----------| :-------| :-----------| :--------| :--------| :---------- |
| 3           | NPC Ann | Reporter    | NPC Bob  |          | successful  |
| 3           | NPC Bob | Thief       | NPC Cal  |          | successful  |
| 3           | NPC Cal | Judge       | Thief    |          | successful  |
| 3           | NPC Dan | Executioner | NPC Cal  |          | successful  |
| 3           | NPC Fae | Medic       | NPC Cal  |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ann | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ed  | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 3           | NPC Bob | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Judge       | True       | True      | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Executioner | False      | False     | False      | 4         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message     | details                                                      |
| :-----------| :-------| :-----------| :-----------| :----------------------------------------------------------- |
| 3           | NPC Ann | Reporter    | broadcast   | I (NPC Ann) am the Reporter and NPC Bob is the Thief         |
| 3           | NPC Ann | Reporter    | broadcast   | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 3           | NPC Ann | Reporter    | elimination | NPC Cal has been eliminated                                  |
| 3           | NPC Ann | Reporter    | reveal      | NPC Bob is Thief                                             |
| 3           | NPC Ann | Reporter    | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 3           | NPC Bob | Thief       | broadcast   | I (NPC Ann) am the Reporter and NPC Bob is the Thief         |
| 3           | NPC Bob | Thief       | broadcast   | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 3           | NPC Bob | Thief       | elimination | NPC Cal has been eliminated                                  |
| 3           | NPC Bob | Thief       | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 3           | NPC Cal | Judge       | broadcast   | I (NPC Ann) am the Reporter and NPC Bob is the Thief         |
| 3           | NPC Cal | Judge       | broadcast   | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 3           | NPC Cal | Judge       | elimination | NPC Cal has been eliminated                                  |
| 3           | NPC Cal | Judge       | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 3           | NPC Dan | Executioner | broadcast   | I (NPC Ann) am the Reporter and NPC Bob is the Thief         |
| 3           | NPC Dan | Executioner | broadcast   | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 3           | NPC Dan | Executioner | elimination | NPC Cal has been eliminated                                  |
| 3           | NPC Dan | Executioner | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 3           | NPC Ed  | Inspector   | broadcast   | I (NPC Ann) am the Reporter and NPC Bob is the Thief         |
| 3           | NPC Ed  | Inspector   | broadcast   | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 3           | NPC Ed  | Inspector   | elimination | NPC Cal has been eliminated                                  |
| 3           | NPC Ed  | Inspector   | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 3           | NPC Fae | Medic       | broadcast   | I (NPC Ann) am the Reporter and NPC Bob is the Thief         |
| 3           | NPC Fae | Medic       | broadcast   | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 3           | NPC Fae | Medic       | elimination | NPC Cal has been eliminated                                  |
| 3           | NPC Fae | Medic       | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |

#### Actions Round 4
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 4           | NPC Cal | Judge     | Reporter |          | successful  |
| 4           | NPC Ed  | Inspector | NPC Fae  |          | successful  |
| 4           | NPC Fae | Medic     | NPC Ann  |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ann | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 4           | NPC Bob | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Judge       | True       | True      | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Executioner | False      | False     | False      | 3         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 4           | NPC Ann | Reporter    | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 4           | NPC Ann | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 4           | NPC Bob | Thief       | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 4           | NPC Bob | Thief       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 4           | NPC Cal | Judge       | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 4           | NPC Cal | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 4           | NPC Dan | Executioner | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 4           | NPC Dan | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 4           | NPC Ed  | Inspector   | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 4           | NPC Ed  | Inspector   | reveal    | Medic is Innocent                                        |
| 4           | NPC Ed  | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 4           | NPC Fae | Medic       | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 4           | NPC Fae | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |

#### Actions Round 5
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 5           | NPC Ann | Reporter | NPC Dan  |          | successful  |
| 5           | NPC Bob | Thief    | NPC Ann  |          | successful  |
| 5           | NPC Cal | Judge    | Medic    |          | successful  |
| 5           | NPC Fae | Medic    | NPC Ed   |          | successful  |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ann | Reporter    | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Ed  | Inspector   | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Bob | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Cal | Judge       | True       | True      | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Executioner | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 5           | NPC Ann | Reporter    | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Ann | Reporter    | reveal    | NPC Dan is Executioner                                       |
| 5           | NPC Ann | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 5           | NPC Bob | Thief       | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Bob | Thief       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 5           | NPC Cal | Judge       | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Cal | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 5           | NPC Dan | Executioner | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Dan | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 5           | NPC Ed  | Inspector   | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Ed  | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 5           | NPC Fae | Medic       | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Fae | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |

#### Actions Round 6
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 6           | NPC Cal | Judge     | Thief    |          | successful  |
| 6           | NPC Ed  | Inspector | NPC Dan  |          | successful  |
| 6           | NPC Fae | Medic     | NPC Bob  |          | successful  |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Ann | Reporter    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Ed  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 6           | NPC Bob | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Judge       | True       | True      | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Dan | Executioner | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 6           | NPC Ann | Reporter    | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed  |
| 6           | NPC Ann | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 6           | NPC Bob | Thief       | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed  |
| 6           | NPC Bob | Thief       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 6           | NPC Cal | Judge       | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed  |
| 6           | NPC Cal | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 6           | NPC Dan | Executioner | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed  |
| 6           | NPC Dan | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 6           | NPC Ed  | Inspector   | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed  |
| 6           | NPC Ed  | Inspector   | reveal    | Executioner is Innocent                                  |
| 6           | NPC Ed  | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 6           | NPC Fae | Medic       | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed  |
| 6           | NPC Fae | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |

#### Actions Round 7
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 7           | NPC Ann | Reporter | NPC Ed   |          | successful  |
| 7           | NPC Bob | Thief    | NPC Fae  |          | successful  |
| 7           | NPC Cal | Judge    | Medic    |          | successful  |
| 7           | NPC Fae | Medic    | NPC Dan  |          | successful  |

#### States Round 7
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Ann | Reporter    | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Ed  | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 7           | NPC Bob | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Fae | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Cal | Judge       | True       | True      | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 7           | NPC Ann | Reporter    | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Inspector      |
| 7           | NPC Ann | Reporter    | broadcast | I (NPC Bob) am the Thief and I have made NPC Fae vulnerable  |
| 7           | NPC Ann | Reporter    | reveal    | NPC Ed is Inspector                                          |
| 7           | NPC Ann | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 7           | NPC Bob | Thief       | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Inspector      |
| 7           | NPC Bob | Thief       | broadcast | I (NPC Bob) am the Thief and I have made NPC Fae vulnerable  |
| 7           | NPC Bob | Thief       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 7           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Inspector      |
| 7           | NPC Cal | Judge       | broadcast | I (NPC Bob) am the Thief and I have made NPC Fae vulnerable  |
| 7           | NPC Cal | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 7           | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Inspector      |
| 7           | NPC Dan | Executioner | broadcast | I (NPC Bob) am the Thief and I have made NPC Fae vulnerable  |
| 7           | NPC Dan | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 7           | NPC Ed  | Inspector   | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Inspector      |
| 7           | NPC Ed  | Inspector   | broadcast | I (NPC Bob) am the Thief and I have made NPC Fae vulnerable  |
| 7           | NPC Ed  | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 7           | NPC Fae | Medic       | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Inspector      |
| 7           | NPC Fae | Medic       | broadcast | I (NPC Bob) am the Thief and I have made NPC Fae vulnerable  |
| 7           | NPC Fae | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |

#### Actions Round 8
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 8           | NPC Cal | Judge     | Medic    |          | successful  |
| 8           | NPC Ed  | Inspector | NPC Fae  |          | successful  |
| 8           | NPC Fae | Medic     | NPC Ann  |          | successful  |

#### States Round 8
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Ann | Reporter    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Ed  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 8           | NPC Bob | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Fae | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Cal | Judge       | True       | True      | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 8           | NPC Ann | Reporter    | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 8           | NPC Ann | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 8           | NPC Bob | Thief       | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 8           | NPC Bob | Thief       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 8           | NPC Cal | Judge       | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 8           | NPC Cal | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 8           | NPC Dan | Executioner | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 8           | NPC Dan | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 8           | NPC Ed  | Inspector   | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 8           | NPC Ed  | Inspector   | reveal    | Medic is Innocent                                        |
| 8           | NPC Ed  | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 8           | NPC Fae | Medic       | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 8           | NPC Fae | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |

#### Actions Round 9
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 9           | NPC Ann | Reporter | NPC Fae  |          | successful  |
| 9           | NPC Bob | Thief    | NPC Dan  |          | successful  |
| 9           | NPC Cal | Judge    | Thief    |          | successful  |
| 9           | NPC Fae | Medic    | NPC Ed   |          | successful  |

#### States Round 9
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 9           | NPC Ann | Reporter    | False      | False     | True       | 2         | True   | 0              | 0                  |
| 9           | NPC Ed  | Inspector   | False      | False     | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Bob | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 9           | NPC Fae | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Cal | Judge       | True       | True      | True       | 0         | True   | 0              | 0                  |
| 9           | NPC Dan | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 9
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 9           | NPC Ann | Reporter    | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Medic         |
| 9           | NPC Ann | Reporter    | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 9           | NPC Ann | Reporter    | reveal    | NPC Fae is Medic                                             |
| 9           | NPC Ann | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 9           | NPC Bob | Thief       | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Medic         |
| 9           | NPC Bob | Thief       | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 9           | NPC Bob | Thief       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 9           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Medic         |
| 9           | NPC Cal | Judge       | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 9           | NPC Cal | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 9           | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Medic         |
| 9           | NPC Dan | Executioner | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 9           | NPC Dan | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 9           | NPC Ed  | Inspector   | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Medic         |
| 9           | NPC Ed  | Inspector   | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 9           | NPC Ed  | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 9           | NPC Fae | Medic       | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Medic         |
| 9           | NPC Fae | Medic       | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 9           | NPC Fae | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |

#### Actions Round 10
| round_index | Player  | action    | Target 1  | Target 2 | status      |
| :-----------| :-------| :---------| :---------| :--------| :---------- |
| 10          | NPC Cal | Judge     | Inspector |          | successful  |
| 10          | NPC Ed  | Inspector | NPC Dan   |          | successful  |
| 10          | NPC Fae | Medic     | NPC Bob   |          | successful  |

#### States Round 10
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 10          | NPC Ann | Reporter    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 10          | NPC Ed  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 10          | NPC Bob | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 10          | NPC Fae | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 10          | NPC Cal | Judge       | True       | True      | True       | 0         | True   | 0              | 0                  |
| 10          | NPC Dan | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 10
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 10          | NPC Ann | Reporter    | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed  |
| 10          | NPC Ann | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 10          | NPC Bob | Thief       | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed  |
| 10          | NPC Bob | Thief       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 10          | NPC Cal | Judge       | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed  |
| 10          | NPC Cal | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 10          | NPC Dan | Executioner | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed  |
| 10          | NPC Dan | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 10          | NPC Ed  | Inspector   | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed  |
| 10          | NPC Ed  | Inspector   | reveal    | Executioner is Innocent                                  |
| 10          | NPC Ed  | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |
| 10          | NPC Fae | Medic       | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed  |
| 10          | NPC Fae | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!         |