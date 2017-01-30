#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 38   | 6       | 7       |

#### Roles
| Role         |
| :----------- |
| Inspector    |
| Judge        |
| Medic        |
| Executioner  |
| Reporter     |
| Thief        |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Reporter    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Ann | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Medic       | role change | Your Role is Medic        |
| 0           | NPC Bob | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Cal | Reporter    | possessed   | You are Possessed         |
| 0           | NPC Dan | Thief       | role change | Your Role is Thief        |
| 0           | NPC Dan | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Ed  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Fae | Executioner | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Inspector | NPC Cal  |          | successful  |
| 1           | NPC Bob | Medic     | NPC Ed   |          | successful  |
| 1           | NPC Cal | Reporter  | NPC Ed   |          | successful  |
| 1           | NPC Dan | Thief     | NPC Fae  |          | successful  |
| 1           | NPC Ed  | Judge     | Medic    |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Reporter    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Inspector   | broadcast | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 1           | NPC Ann | Inspector   | broadcast | I (NPC Dan) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Ann | Inspector   | reveal    | Reporter is Possessed                                        |
| 1           | NPC Bob | Medic       | broadcast | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 1           | NPC Bob | Medic       | broadcast | I (NPC Dan) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Cal | Reporter    | broadcast | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 1           | NPC Cal | Reporter    | broadcast | I (NPC Dan) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Cal | Reporter    | reveal    | NPC Ed is Judge                                              |
| 1           | NPC Dan | Thief       | broadcast | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 1           | NPC Dan | Thief       | broadcast | I (NPC Dan) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Ed  | Judge       | broadcast | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 1           | NPC Ed  | Judge       | broadcast | I (NPC Dan) am the Thief and I have made NPC Fae vulnerable  |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Dan) am the Thief and I have made NPC Fae vulnerable  |

#### Actions Round 2
| round_index | Player  | action      | Target 1 | Target 2 | status                        |
| :-----------| :-------| :-----------| :--------| :--------| :---------------------------- |
| 2           | NPC Bob | Medic       | NPC Fae  |          | successful                    |
| 2           | NPC Ed  | Judge       | Thief    |          | successful                    |
| 2           | NPC Fae | Executioner | NPC Cal  |          | failed because of no support  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ann | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Reporter    | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message       | details  |
| :-----------| :-------| :-----------| :-------------| :------- |
| 2           | NPC Fae | Executioner | action failed |          |

#### Actions Round 3
| round_index | Player  | action      | Target 1 | Target 2 | status      |
| :-----------| :-------| :-----------| :--------| :--------| :---------- |
| 3           | NPC Ann | Inspector   | NPC Cal  |          | successful  |
| 3           | NPC Bob | Medic       | NPC Cal  |          | successful  |
| 3           | NPC Cal | Reporter    | NPC Bob  |          | successful  |
| 3           | NPC Dan | Thief       | NPC Bob  |          | successful  |
| 3           | NPC Ed  | Judge       | Reporter |          | successful  |
| 3           | NPC Fae | Executioner | NPC Cal  |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ann | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Fae | Executioner | False      | False     | True       | 4         | True   | 0              | 0                  |
| 3           | NPC Cal | Reporter    | True       | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message     | details                                                      |
| :-----------| :-------| :-----------| :-----------| :----------------------------------------------------------- |
| 3           | NPC Ann | Inspector   | broadcast   | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 3           | NPC Ann | Inspector   | broadcast   | I (NPC Cal) am the Reporter and NPC Bob is the Medic         |
| 3           | NPC Ann | Inspector   | broadcast   | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Ann | Inspector   | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 3           | NPC Ann | Inspector   | elimination | NPC Cal has been eliminated                                  |
| 3           | NPC Ann | Inspector   | reveal      | Reporter is Possessed                                        |
| 3           | NPC Bob | Medic       | broadcast   | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 3           | NPC Bob | Medic       | broadcast   | I (NPC Cal) am the Reporter and NPC Bob is the Medic         |
| 3           | NPC Bob | Medic       | broadcast   | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Bob | Medic       | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 3           | NPC Bob | Medic       | elimination | NPC Cal has been eliminated                                  |
| 3           | NPC Cal | Reporter    | broadcast   | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 3           | NPC Cal | Reporter    | broadcast   | I (NPC Cal) am the Reporter and NPC Bob is the Medic         |
| 3           | NPC Cal | Reporter    | broadcast   | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Cal | Reporter    | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 3           | NPC Cal | Reporter    | elimination | NPC Cal has been eliminated                                  |
| 3           | NPC Cal | Reporter    | reveal      | NPC Bob is Medic                                             |
| 3           | NPC Dan | Thief       | broadcast   | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 3           | NPC Dan | Thief       | broadcast   | I (NPC Cal) am the Reporter and NPC Bob is the Medic         |
| 3           | NPC Dan | Thief       | broadcast   | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Dan | Thief       | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 3           | NPC Dan | Thief       | elimination | NPC Cal has been eliminated                                  |
| 3           | NPC Ed  | Judge       | broadcast   | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 3           | NPC Ed  | Judge       | broadcast   | I (NPC Cal) am the Reporter and NPC Bob is the Medic         |
| 3           | NPC Ed  | Judge       | broadcast   | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Ed  | Judge       | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 3           | NPC Ed  | Judge       | elimination | NPC Cal has been eliminated                                  |
| 3           | NPC Fae | Executioner | broadcast   | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 3           | NPC Fae | Executioner | broadcast   | I (NPC Cal) am the Reporter and NPC Bob is the Medic         |
| 3           | NPC Fae | Executioner | broadcast   | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable  |
| 3           | NPC Fae | Executioner | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 3           | NPC Fae | Executioner | elimination | NPC Cal has been eliminated                                  |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 4           | NPC Bob | Medic    | NPC Ann  |          | successful  |
| 4           | NPC Cal | Reporter | NPC Ann  |          | successful  |
| 4           | NPC Ed  | Judge    | Reporter |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ann | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Fae | Executioner | False      | False     | True       | 3         | True   | 0              | 0                  |
| 4           | NPC Cal | Reporter    | True       | True      | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Dan | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                   |
| :-----------| :-------| :-----------| :---------| :-------------------------------------------------------- |
| 4           | NPC Ann | Inspector   | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Inspector  |
| 4           | NPC Ann | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!          |
| 4           | NPC Bob | Medic       | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Inspector  |
| 4           | NPC Bob | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!          |
| 4           | NPC Cal | Reporter    | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Inspector  |
| 4           | NPC Cal | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!          |
| 4           | NPC Cal | Reporter    | reveal    | NPC Ann is Inspector                                      |
| 4           | NPC Dan | Thief       | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Inspector  |
| 4           | NPC Dan | Thief       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!          |
| 4           | NPC Ed  | Judge       | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Inspector  |
| 4           | NPC Ed  | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!          |
| 4           | NPC Fae | Executioner | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Inspector  |
| 4           | NPC Fae | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!          |

#### Actions Round 5
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 5           | NPC Ann | Inspector | NPC Dan  |          | successful  |
| 5           | NPC Bob | Medic     | NPC Ed   |          | successful  |
| 5           | NPC Dan | Thief     | NPC Ann  |          | successful  |
| 5           | NPC Ed  | Judge     | Thief    |          | successful  |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ann | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Fae | Executioner | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Cal | Reporter    | True       | True      | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Dan | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 5           | NPC Ann | Inspector   | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed     |
| 5           | NPC Ann | Inspector   | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Ann | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 5           | NPC Ann | Inspector   | reveal    | Thief is Innocent                                            |
| 5           | NPC Bob | Medic       | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed     |
| 5           | NPC Bob | Medic       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Bob | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 5           | NPC Cal | Reporter    | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed     |
| 5           | NPC Cal | Reporter    | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Cal | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 5           | NPC Dan | Thief       | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed     |
| 5           | NPC Dan | Thief       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Dan | Thief       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 5           | NPC Ed  | Judge       | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed     |
| 5           | NPC Ed  | Judge       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Ed  | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |
| 5           | NPC Fae | Executioner | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed     |
| 5           | NPC Fae | Executioner | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 5           | NPC Fae | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!             |

#### Actions Round 6
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 6           | NPC Bob | Medic    | NPC Fae  |          | successful  |
| 6           | NPC Cal | Reporter | NPC Dan  |          | successful  |
| 6           | NPC Ed  | Judge    | Thief    |          | successful  |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Ann | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Fae | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Reporter    | True       | True      | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Dan | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role        | message   | details                                               |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------- |
| 6           | NPC Ann | Inspector   | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Thief  |
| 6           | NPC Ann | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!      |
| 6           | NPC Bob | Medic       | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Thief  |
| 6           | NPC Bob | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!      |
| 6           | NPC Cal | Reporter    | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Thief  |
| 6           | NPC Cal | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!      |
| 6           | NPC Cal | Reporter    | reveal    | NPC Dan is Thief                                      |
| 6           | NPC Dan | Thief       | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Thief  |
| 6           | NPC Dan | Thief       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!      |
| 6           | NPC Ed  | Judge       | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Thief  |
| 6           | NPC Ed  | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!      |
| 6           | NPC Fae | Executioner | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Thief  |
| 6           | NPC Fae | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!      |

#### Actions Round 7
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 7           | NPC Ann | Inspector | NPC Bob  |          | successful  |
| 7           | NPC Bob | Medic     | NPC Dan  |          | successful  |
| 7           | NPC Dan | Thief     | NPC Ed   |          | successful  |
| 7           | NPC Ed  | Judge     | Thief    |          | successful  |

#### States Round 7
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Ann | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Ed  | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Bob | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Fae | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Cal | Reporter    | True       | True      | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Dan | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 7           | NPC Ann | Inspector   | broadcast | I (NPC Ann) inspected NPC Bob and they are not possessed    |
| 7           | NPC Ann | Inspector   | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 7           | NPC Ann | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!            |
| 7           | NPC Ann | Inspector   | reveal    | Medic is Innocent                                           |
| 7           | NPC Bob | Medic       | broadcast | I (NPC Ann) inspected NPC Bob and they are not possessed    |
| 7           | NPC Bob | Medic       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 7           | NPC Bob | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!            |
| 7           | NPC Cal | Reporter    | broadcast | I (NPC Ann) inspected NPC Bob and they are not possessed    |
| 7           | NPC Cal | Reporter    | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 7           | NPC Cal | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!            |
| 7           | NPC Dan | Thief       | broadcast | I (NPC Ann) inspected NPC Bob and they are not possessed    |
| 7           | NPC Dan | Thief       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 7           | NPC Dan | Thief       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!            |
| 7           | NPC Ed  | Judge       | broadcast | I (NPC Ann) inspected NPC Bob and they are not possessed    |
| 7           | NPC Ed  | Judge       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 7           | NPC Ed  | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!            |
| 7           | NPC Fae | Executioner | broadcast | I (NPC Ann) inspected NPC Bob and they are not possessed    |
| 7           | NPC Fae | Executioner | broadcast | I (NPC Dan) am the Thief and I have made NPC Ed vulnerable  |
| 7           | NPC Fae | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!            |