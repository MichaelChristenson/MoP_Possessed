#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 48   | 5       | 6       |

#### Roles
| Role         |
| :----------- |
| Inspector    |
| Executioner  |
| Judge        |
| Medic        |
| Reporter     |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Medic       | role change | Your Role is Medic        |
| 0           | NPC Ann | Medic       | possessed   | You are Possessed         |
| 0           | NPC Bob | Judge       | role change | Your Role is Judge        |
| 0           | NPC Bob | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Cal | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Dan | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ed  | Executioner | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1  | Target 2 | status      |
| :-----------| :-------| :---------| :---------| :--------| :---------- |
| 1           | NPC Ann | Medic     | NPC Ed    |          | successful  |
| 1           | NPC Bob | Judge     | Inspector |          | successful  |
| 1           | NPC Cal | Inspector | NPC Bob   |          | successful  |
| 1           | NPC Dan | Reporter  | NPC Ann   |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                   |
| :-----------| :-------| :-----------| :---------| :-------------------------------------------------------- |
| 1           | NPC Ann | Medic       | broadcast | I (NPC Cal) inspected NPC Bob and they are not possessed  |
| 1           | NPC Ann | Medic       | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Medic      |
| 1           | NPC Bob | Judge       | broadcast | I (NPC Cal) inspected NPC Bob and they are not possessed  |
| 1           | NPC Bob | Judge       | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Medic      |
| 1           | NPC Cal | Inspector   | broadcast | I (NPC Cal) inspected NPC Bob and they are not possessed  |
| 1           | NPC Cal | Inspector   | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Medic      |
| 1           | NPC Cal | Inspector   | reveal    | Judge is Innocent                                         |
| 1           | NPC Dan | Reporter    | broadcast | I (NPC Cal) inspected NPC Bob and they are not possessed  |
| 1           | NPC Dan | Reporter    | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Medic      |
| 1           | NPC Dan | Reporter    | reveal    | NPC Ann is Medic                                          |
| 1           | NPC Ed  | Executioner | broadcast | I (NPC Cal) inspected NPC Bob and they are not possessed  |
| 1           | NPC Ed  | Executioner | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Medic      |

#### Actions Round 2
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 2           | NPC Ann | Medic  | NPC Bob  |          | successful  |
| 2           | NPC Bob | Judge  | Medic    |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 3           | NPC Ann | Medic     | NPC Dan  |          | successful  |
| 3           | NPC Bob | Judge     | Reporter |          | successful  |
| 3           | NPC Cal | Inspector | NPC Ed   |          | successful  |
| 3           | NPC Dan | Reporter  | NPC Ed   |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 3           | NPC Ann | Medic       | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed  |
| 3           | NPC Bob | Judge       | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed  |
| 3           | NPC Cal | Inspector   | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed  |
| 3           | NPC Cal | Inspector   | reveal    | Executioner is Innocent                                  |
| 3           | NPC Dan | Reporter    | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed  |
| 3           | NPC Dan | Reporter    | reveal    | NPC Ed is Executioner                                    |
| 3           | NPC Ed  | Executioner | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed  |

#### Actions Round 4
| round_index | Player  | action   | Target 1  | Target 2 | status      |
| :-----------| :-------| :--------| :---------| :--------| :---------- |
| 4           | NPC Ann | Medic    | NPC Cal   |          | successful  |
| 4           | NPC Bob | Judge    | Inspector |          | successful  |
| 4           | NPC Dan | Reporter | NPC Bob   |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role     | message | details           |
| :-----------| :-------| :--------| :-------| :---------------- |
| 4           | NPC Dan | Reporter | reveal  | NPC Bob is Judge  |

#### Actions Round 5
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 5           | NPC Ann | Medic     | NPC Ed   |          | successful  |
| 5           | NPC Bob | Judge     | Medic    |          | successful  |
| 5           | NPC Cal | Inspector | NPC Ed   |          | successful  |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 5           | NPC Ann | Medic       | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed  |
| 5           | NPC Bob | Judge       | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed  |
| 5           | NPC Cal | Inspector   | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed  |
| 5           | NPC Cal | Inspector   | reveal    | Executioner is Innocent                                  |
| 5           | NPC Dan | Reporter    | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed  |
| 5           | NPC Ed  | Executioner | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed  |

#### Actions Round 6
| round_index | Player  | action   | Target 1  | Target 2 | status      |
| :-----------| :-------| :--------| :---------| :--------| :---------- |
| 6           | NPC Ann | Medic    | NPC Bob   |          | successful  |
| 6           | NPC Bob | Judge    | Inspector |          | successful  |
| 6           | NPC Dan | Reporter | NPC Cal   |          | successful  |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Cal | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role        | message   | details                                                   |
| :-----------| :-------| :-----------| :---------| :-------------------------------------------------------- |
| 6           | NPC Ann | Medic       | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Inspector  |
| 6           | NPC Bob | Judge       | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Inspector  |
| 6           | NPC Cal | Inspector   | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Inspector  |
| 6           | NPC Dan | Reporter    | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Inspector  |
| 6           | NPC Dan | Reporter    | reveal    | NPC Cal is Inspector                                      |
| 6           | NPC Ed  | Executioner | broadcast | I (NPC Dan) am the Reporter and NPC Cal is the Inspector  |