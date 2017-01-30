#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 49   | 5       | 6       |

#### Roles
| Role         |
| :----------- |
| Executioner  |
| Judge        |
| Inspector    |
| Medic        |
| Reporter     |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Medic       | role change | Your Role is Medic        |
| 0           | NPC Ann | Medic       | possessed   | You are Possessed         |
| 0           | NPC Bob | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Bob | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Cal | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Dan | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Ed  | Judge       | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Medic     | NPC Ed   |          | successful  |
| 1           | NPC Bob | Inspector | NPC Cal  |          | successful  |
| 1           | NPC Dan | Reporter  | NPC Ed   |          | successful  |
| 1           | NPC Ed  | Judge     | Reporter |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                   |
| :-----------| :-------| :-----------| :---------| :-------------------------------------------------------- |
| 1           | NPC Ann | Medic       | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |
| 1           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |
| 1           | NPC Bob | Inspector   | reveal    | Executioner is Innocent                                   |
| 1           | NPC Cal | Executioner | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |
| 1           | NPC Dan | Reporter    | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |
| 1           | NPC Dan | Reporter    | reveal    | NPC Ed is Judge                                           |
| 1           | NPC Ed  | Judge       | broadcast | I (NPC Bob) inspected NPC Cal and they are not possessed  |

#### Actions Round 2
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 2           | NPC Ann | Medic  | NPC Bob  |          | successful  |
| 2           | NPC Ed  | Judge  | Medic    |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 3           | NPC Ann | Medic     | NPC Dan  |          | successful  |
| 3           | NPC Bob | Inspector | NPC Dan  |          | successful  |
| 3           | NPC Dan | Reporter  | NPC Cal  |          | successful  |
| 3           | NPC Ed  | Judge     | Medic    |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                   |
| :-----------| :-------| :-----------| :---------| :-------------------------------------------------------- |
| 3           | NPC Ann | Medic       | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |
| 3           | NPC Bob | Inspector   | reveal    | Reporter is Innocent                                      |
| 3           | NPC Cal | Executioner | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |
| 3           | NPC Dan | Reporter    | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |
| 3           | NPC Dan | Reporter    | reveal    | NPC Cal is Executioner                                    |
| 3           | NPC Ed  | Judge       | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 4           | NPC Ann | Medic    | NPC Cal  |          | successful  |
| 4           | NPC Dan | Reporter | NPC Bob  |          | successful  |
| 4           | NPC Ed  | Judge    | Medic    |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                   |
| :-----------| :-------| :-----------| :---------| :-------------------------------------------------------- |
| 4           | NPC Ann | Medic       | broadcast | I (NPC Dan) am the Reporter and NPC Bob is the Inspector  |
| 4           | NPC Bob | Inspector   | broadcast | I (NPC Dan) am the Reporter and NPC Bob is the Inspector  |
| 4           | NPC Cal | Executioner | broadcast | I (NPC Dan) am the Reporter and NPC Bob is the Inspector  |
| 4           | NPC Dan | Reporter    | broadcast | I (NPC Dan) am the Reporter and NPC Bob is the Inspector  |
| 4           | NPC Dan | Reporter    | reveal    | NPC Bob is Inspector                                      |
| 4           | NPC Ed  | Judge       | broadcast | I (NPC Dan) am the Reporter and NPC Bob is the Inspector  |

#### Actions Round 5
| round_index | Player  | action    | Target 1  | Target 2 | status      |
| :-----------| :-------| :---------| :---------| :--------| :---------- |
| 5           | NPC Ann | Medic     | NPC Ed    |          | successful  |
| 5           | NPC Bob | Inspector | NPC Ann   |          | successful  |
| 5           | NPC Ed  | Judge     | Inspector |          | successful  |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message   | details                                               |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------- |
| 5           | NPC Ann | Medic       | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed  |
| 5           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed  |
| 5           | NPC Bob | Inspector   | reveal    | Medic is Possessed                                    |
| 5           | NPC Cal | Executioner | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed  |
| 5           | NPC Dan | Reporter    | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed  |
| 5           | NPC Ed  | Judge       | broadcast | I (NPC Bob) inspected NPC Ann and they are possessed  |

#### Actions Round 6
| round_index | Player  | action      | Target 1  | Target 2 | status                        |
| :-----------| :-------| :-----------| :---------| :--------| :---------------------------- |
| 6           | NPC Ann | Medic       | NPC Bob   |          | successful                    |
| 6           | NPC Cal | Executioner | NPC Ann   |          | failed because of no support  |
| 6           | NPC Dan | Reporter    | NPC Ann   |          | successful                    |
| 6           | NPC Ed  | Judge       | Inspector |          | successful                    |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Cal | Executioner | False      | False     | False      | 4         | True   | 0              | 0                  |
| 6           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ann | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role        | message       | details                                               |
| :-----------| :-------| :-----------| :-------------| :---------------------------------------------------- |
| 6           | NPC Ann | Medic       | broadcast     | I (NPC Dan) am the Reporter and NPC Ann is the Medic  |
| 6           | NPC Bob | Inspector   | broadcast     | I (NPC Dan) am the Reporter and NPC Ann is the Medic  |
| 6           | NPC Cal | Executioner | broadcast     | I (NPC Dan) am the Reporter and NPC Ann is the Medic  |
| 6           | NPC Cal | Executioner | action failed |                                                       |
| 6           | NPC Dan | Reporter    | broadcast     | I (NPC Dan) am the Reporter and NPC Ann is the Medic  |
| 6           | NPC Dan | Reporter    | reveal        | NPC Ann is Medic                                      |
| 6           | NPC Ed  | Judge       | broadcast     | I (NPC Dan) am the Reporter and NPC Ann is the Medic  |