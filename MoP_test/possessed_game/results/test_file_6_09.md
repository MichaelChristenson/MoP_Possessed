#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 9    | 6       | 6       |

#### Roles
| Role       |
| :--------- |
| Thief      |
| Inspector  |
| Judge      |
| Medic      |
| Trader     |
| Reporter   |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Trader    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Thief     | role change | Your Role is Thief      |
| 0           | NPC Ann | Thief     | possessed   | You are Not Possessed   |
| 0           | NPC Bob | Judge     | role change | Your Role is Judge      |
| 0           | NPC Bob | Judge     | possessed   | You are Not Possessed   |
| 0           | NPC Cal | Trader    | role change | Your Role is Trader     |
| 0           | NPC Cal | Trader    | possessed   | You are Possessed       |
| 0           | NPC Dan | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Dan | Reporter  | possessed   | You are Not Possessed   |
| 0           | NPC Ed  | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Ed  | Inspector | possessed   | You are Not Possessed   |
| 0           | NPC Fae | Medic     | role change | Your Role is Medic      |
| 0           | NPC Fae | Medic     | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player  | action    | Target 1  | Target 2 | status                         |
| :-----------| :-------| :---------| :---------| :--------| :----------------------------- |
| 1           | NPC Ann | Thief     | NPC Cal   |          | successful                     |
| 1           | NPC Bob | Judge     | Inspector |          | successful                     |
| 1           | NPC Cal | Trader    | NPC Fae   | NPC Ed   | failed because not vulnerable  |
| 1           | NPC Dan | Reporter  | NPC Cal   |          | successful                     |
| 1           | NPC Ed  | Inspector | NPC Cal   |          | successful                     |
| 1           | NPC Fae | Medic     | NPC Ed    |          | successful                     |

#### States Round 1
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed  | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Trader    | False      | True      | True       | 4         | True   | 0              | 0                  |
| 1           | NPC Dan | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Thief     | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ann | Thief     | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader        |
| 1           | NPC Ann | Thief     | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed          |
| 1           | NPC Bob | Judge     | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Bob | Judge     | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader        |
| 1           | NPC Bob | Judge     | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed          |
| 1           | NPC Cal | Trader    | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Cal | Trader    | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader        |
| 1           | NPC Cal | Trader    | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed          |
| 1           | NPC Dan | Reporter  | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Dan | Reporter  | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader        |
| 1           | NPC Dan | Reporter  | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed          |
| 1           | NPC Dan | Reporter  | reveal    | NPC Cal is Trader                                            |
| 1           | NPC Ed  | Inspector | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ed  | Inspector | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader        |
| 1           | NPC Ed  | Inspector | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed          |
| 1           | NPC Ed  | Inspector | reveal    | Trader is Possessed                                          |
| 1           | NPC Fae | Medic     | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Fae | Medic     | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Trader        |
| 1           | NPC Fae | Medic     | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed          |

#### Actions Round 2
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 2           | NPC Bob | Judge     | Medic    |          | successful  |
| 2           | NPC Ed  | Inspector | NPC Fae  |          | successful  |
| 2           | NPC Fae | Medic     | NPC Bob  |          | successful  |

#### States Round 2
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ann | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Trader    | False      | True      | True       | 3         | True   | 0              | 0                  |
| 2           | NPC Dan | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role      | message   | details                                                  |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------- |
| 2           | NPC Ann | Thief     | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 2           | NPC Bob | Judge     | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 2           | NPC Cal | Trader    | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 2           | NPC Dan | Reporter  | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 2           | NPC Ed  | Inspector | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |
| 2           | NPC Ed  | Inspector | reveal    | Medic is Innocent                                        |
| 2           | NPC Fae | Medic     | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed  |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 3           | NPC Ann | Thief    | NPC Fae  |          | successful  |
| 3           | NPC Bob | Judge    | Thief    |          | successful  |
| 3           | NPC Dan | Reporter | NPC Bob  |          | successful  |
| 3           | NPC Fae | Medic    | NPC Cal  |          | successful  |

#### States Round 3
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ann | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ed  | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Fae | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Trader    | False      | True      | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann | Thief     | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable  |
| 3           | NPC Bob | Judge     | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable  |
| 3           | NPC Cal | Trader    | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable  |
| 3           | NPC Dan | Reporter  | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable  |
| 3           | NPC Dan | Reporter  | reveal    | NPC Bob is Judge                                             |
| 3           | NPC Ed  | Inspector | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable  |
| 3           | NPC Fae | Medic     | broadcast | I (NPC Ann) am the Thief and I have made NPC Fae vulnerable  |

#### Actions Round 4
| round_index | Player  | action    | Target 1 | Target 2 | status                         |
| :-----------| :-------| :---------| :--------| :--------| :----------------------------- |
| 4           | NPC Bob | Judge     | Reporter |          | successful                     |
| 4           | NPC Cal | Trader    | NPC Ed   | NPC Dan  | failed because not vulnerable  |
| 4           | NPC Ed  | Inspector | NPC Cal  |          | successful                     |
| 4           | NPC Fae | Medic     | NPC Dan  |          | successful                     |

#### States Round 4
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ann | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Trader    | False      | True      | True       | 4         | True   | 0              | 0                  |
| 4           | NPC Dan | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role      | message   | details                                              |
| :-----------| :-------| :---------| :---------| :--------------------------------------------------- |
| 4           | NPC Ann | Thief     | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed  |
| 4           | NPC Bob | Judge     | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed  |
| 4           | NPC Cal | Trader    | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed  |
| 4           | NPC Dan | Reporter  | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed  |
| 4           | NPC Ed  | Inspector | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed  |
| 4           | NPC Ed  | Inspector | reveal    | Trader is Possessed                                  |
| 4           | NPC Fae | Medic     | broadcast | I (NPC Ed) inspected NPC Cal and they are possessed  |

#### Actions Round 5
| round_index | Player  | action   | Target 1  | Target 2 | status      |
| :-----------| :-------| :--------| :---------| :--------| :---------- |
| 5           | NPC Ann | Thief    | NPC Dan   |          | successful  |
| 5           | NPC Bob | Judge    | Inspector |          | successful  |
| 5           | NPC Dan | Reporter | NPC Ann   |          | successful  |
| 5           | NPC Fae | Medic    | NPC Ann   |          | successful  |

#### States Round 5
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ann | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Fae | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Cal | Trader    | False      | True      | True       | 3         | True   | 0              | 0                  |
| 5           | NPC Dan | Reporter  | False      | False     | True       | 2         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 5           | NPC Ann | Thief     | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| 5           | NPC Ann | Thief     | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Thief         |
| 5           | NPC Bob | Judge     | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| 5           | NPC Bob | Judge     | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Thief         |
| 5           | NPC Cal | Trader    | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| 5           | NPC Cal | Trader    | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Thief         |
| 5           | NPC Dan | Reporter  | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| 5           | NPC Dan | Reporter  | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Thief         |
| 5           | NPC Dan | Reporter  | reveal    | NPC Ann is Thief                                             |
| 5           | NPC Ed  | Inspector | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| 5           | NPC Ed  | Inspector | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Thief         |
| 5           | NPC Fae | Medic     | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| 5           | NPC Fae | Medic     | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Thief         |

#### Actions Round 6
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 6           | NPC Ann | Thief     | NPC Bob  |          | successful  |
| 6           | NPC Bob | Judge     | Reporter |          | successful  |
| 6           | NPC Ed  | Inspector | NPC Fae  |          | successful  |
| 6           | NPC Fae | Medic     | NPC Ed   |          | successful  |

#### States Round 6
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Ann | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Ed  | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Judge     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Fae | Medic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Trader    | False      | True      | True       | 2         | True   | 0              | 0                  |
| 6           | NPC Dan | Reporter  | False      | False     | True       | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 6           | NPC Ann | Thief     | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| 6           | NPC Ann | Thief     | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed      |
| 6           | NPC Bob | Judge     | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| 6           | NPC Bob | Judge     | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed      |
| 6           | NPC Cal | Trader    | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| 6           | NPC Cal | Trader    | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed      |
| 6           | NPC Dan | Reporter  | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| 6           | NPC Dan | Reporter  | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed      |
| 6           | NPC Ed  | Inspector | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| 6           | NPC Ed  | Inspector | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed      |
| 6           | NPC Ed  | Inspector | reveal    | Medic is Innocent                                            |
| 6           | NPC Fae | Medic     | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| 6           | NPC Fae | Medic     | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed      |