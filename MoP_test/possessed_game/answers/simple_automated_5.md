#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 1    | 5       | 5       |

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
| 0           | NPC Cal | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Medic     | role change | Your Role is Medic      |
| 0           | NPC Ann | Medic     | possessed   | You are Possessed       |
| 0           | NPC Bob | Thief     | role change | Your Role is Thief      |
| 0           | NPC Bob | Thief     | possessed   | You are Not Possessed   |
| 0           | NPC Cal | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Cal | Reporter  | possessed   | You are Not Possessed   |
| 0           | NPC Dan | Judge     | role change | Your Role is Judge      |
| 0           | NPC Dan | Judge     | possessed   | You are Not Possessed   |
| 0           | NPC Ed  | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Ed  | Inspector | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Medic     | NPC Ed   |          | successful  |
| 1           | NPC Bob | Thief     | NPC Cal  |          | successful  |
| 1           | NPC Cal | Reporter  | NPC Bob  |          | successful  |
| 1           | NPC Dan | Judge     | Medic    |          | successful  |
| 1           | NPC Ed  | Inspector | NPC Ann  |          | successful  |

#### States Round 1
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Reporter  | False      | False     | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Ed  | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Medic     | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ann | Medic     | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Thief         |
| 1           | NPC Ann | Medic     | broadcast | I (NPC Ed) inspected NPC Ann and they are possessed          |
| 1           | NPC Bob | Thief     | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Bob | Thief     | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Thief         |
| 1           | NPC Bob | Thief     | broadcast | I (NPC Ed) inspected NPC Ann and they are possessed          |
| 1           | NPC Cal | Reporter  | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Thief         |
| 1           | NPC Cal | Reporter  | broadcast | I (NPC Ed) inspected NPC Ann and they are possessed          |
| 1           | NPC Cal | Reporter  | reveal    | NPC Bob is Thief                                             |
| 1           | NPC Dan | Judge     | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Thief         |
| 1           | NPC Dan | Judge     | broadcast | I (NPC Ed) inspected NPC Ann and they are possessed          |
| 1           | NPC Ed  | Inspector | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Thief         |
| 1           | NPC Ed  | Inspector | broadcast | I (NPC Ed) inspected NPC Ann and they are possessed          |
| 1           | NPC Ed  | Inspector | reveal    | Medic is Possessed                                           |

#### Actions Round 2
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 2           | NPC Ann | Medic     | NPC Bob  |          | successful  |
| 2           | NPC Dan | Judge     | Medic    |          | successful  |
| 2           | NPC Ed  | Inspector | NPC Cal  |          | successful  |

#### States Round 2
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Reporter  | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Bob | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role      | message   | details                                                  |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------- |
| 2           | NPC Ann | Medic     | broadcast | I (NPC Ed) inspected NPC Cal and they are not possessed  |
| 2           | NPC Bob | Thief     | broadcast | I (NPC Ed) inspected NPC Cal and they are not possessed  |
| 2           | NPC Cal | Reporter  | broadcast | I (NPC Ed) inspected NPC Cal and they are not possessed  |
| 2           | NPC Dan | Judge     | broadcast | I (NPC Ed) inspected NPC Cal and they are not possessed  |
| 2           | NPC Ed  | Inspector | broadcast | I (NPC Ed) inspected NPC Cal and they are not possessed  |
| 2           | NPC Ed  | Inspector | reveal    | Reporter is Innocent                                     |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 3           | NPC Ann | Medic    | NPC Dan  |          | successful  |
| 3           | NPC Bob | Thief    | NPC Ann  |          | successful  |
| 3           | NPC Cal | Reporter | NPC Ed   |          | successful  |
| 3           | NPC Dan | Judge    | Thief    |          | successful  |

#### States Round 3
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal | Reporter  | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Ed  | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Bob | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann | Medic     | False      | True      | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann | Medic     | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Ann | Medic     | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Inspector      |
| 3           | NPC Bob | Thief     | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Bob | Thief     | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Inspector      |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Inspector      |
| 3           | NPC Cal | Reporter  | reveal    | NPC Ed is Inspector                                          |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Inspector      |
| 3           | NPC Ed  | Inspector | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 3           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Inspector      |

#### Actions Round 4
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 4           | NPC Ann | Medic     | NPC Cal  |          | successful  |
| 4           | NPC Dan | Judge     | Thief    |          | successful  |
| 4           | NPC Ed  | Inspector | NPC Cal  |          | successful  |

#### States Round 4
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal | Reporter  | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Bob | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann | Medic     | False      | True      | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role      | message   | details                                                  |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------- |
| 4           | NPC Ann | Medic     | broadcast | I (NPC Ed) inspected NPC Cal and they are not possessed  |
| 4           | NPC Bob | Thief     | broadcast | I (NPC Ed) inspected NPC Cal and they are not possessed  |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Ed) inspected NPC Cal and they are not possessed  |
| 4           | NPC Dan | Judge     | broadcast | I (NPC Ed) inspected NPC Cal and they are not possessed  |
| 4           | NPC Ed  | Inspector | broadcast | I (NPC Ed) inspected NPC Cal and they are not possessed  |
| 4           | NPC Ed  | Inspector | reveal    | Reporter is Innocent                                     |

#### Actions Round 5
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 5           | NPC Ann | Medic    | NPC Ed   |          | successful  |
| 5           | NPC Bob | Thief    | NPC Ed   |          | successful  |
| 5           | NPC Cal | Reporter | NPC Ann  |          | successful  |
| 5           | NPC Dan | Judge    | Medic    |          | successful  |

#### States Round 5
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal | Reporter  | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Ed  | Inspector | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Bob | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Ann | Medic     | False      | True      | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role      | message   | details                                                     |
| :-----------| :-------| :---------| :---------| :---------------------------------------------------------- |
| 5           | NPC Ann | Medic     | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 5           | NPC Ann | Medic     | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Medic        |
| 5           | NPC Bob | Thief     | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 5           | NPC Bob | Thief     | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Medic        |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Medic        |
| 5           | NPC Cal | Reporter  | reveal    | NPC Ann is Medic                                            |
| 5           | NPC Dan | Judge     | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 5           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Medic        |
| 5           | NPC Ed  | Inspector | broadcast | I (NPC Bob) am the Thief and I have made NPC Ed vulnerable  |
| 5           | NPC Ed  | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Medic        |