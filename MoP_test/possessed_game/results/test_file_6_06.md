#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 6    | 6       | 7       |

#### Roles
| Role         |
| :----------- |
| Executioner  |
| Thief        |
| Judge        |
| Inspector    |
| Reporter     |
| Medic        |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Reporter    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ann | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Judge       | role change | Your Role is Judge        |
| 0           | NPC Bob | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Cal | Reporter    | possessed   | You are Possessed         |
| 0           | NPC Dan | Medic       | role change | Your Role is Medic        |
| 0           | NPC Dan | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Thief       | role change | Your Role is Thief        |
| 0           | NPC Ed  | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Fae | Inspector   | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Bob | Judge     | Medic    |          | successful  |
| 1           | NPC Cal | Reporter  | NPC Ed   |          | successful  |
| 1           | NPC Dan | Medic     | NPC Ed   |          | successful  |
| 1           | NPC Ed  | Thief     | NPC Cal  |          | successful  |
| 1           | NPC Fae | Inspector | NPC Ed   |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal | Reporter    | False      | True      | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 1           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Thief         |
| 1           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ann | Executioner | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed     |
| 1           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Thief         |
| 1           | NPC Bob | Judge       | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Bob | Judge       | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed     |
| 1           | NPC Cal | Reporter    | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Thief         |
| 1           | NPC Cal | Reporter    | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Cal | Reporter    | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed     |
| 1           | NPC Cal | Reporter    | reveal    | NPC Ed is Thief                                             |
| 1           | NPC Dan | Medic       | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Thief         |
| 1           | NPC Dan | Medic       | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Dan | Medic       | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed     |
| 1           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Thief         |
| 1           | NPC Ed  | Thief       | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ed  | Thief       | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed     |
| 1           | NPC Fae | Inspector   | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Thief         |
| 1           | NPC Fae | Inspector   | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Fae | Inspector   | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed     |
| 1           | NPC Fae | Inspector   | reveal    | Thief is Innocent                                           |

#### Actions Round 2
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 2           | NPC Bob | Judge  | Medic    |          | successful  |
| 2           | NPC Dan | Medic  | NPC Bob  |          | successful  |
| 2           | NPC Ed  | Thief  | NPC Fae  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Cal | Reporter    | False      | True      | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Thief and I have made NPC Fae vulnerable  |
| 2           | NPC Bob | Judge       | broadcast | I (NPC Ed) am the Thief and I have made NPC Fae vulnerable  |
| 2           | NPC Cal | Reporter    | broadcast | I (NPC Ed) am the Thief and I have made NPC Fae vulnerable  |
| 2           | NPC Dan | Medic       | broadcast | I (NPC Ed) am the Thief and I have made NPC Fae vulnerable  |
| 2           | NPC Ed  | Thief       | broadcast | I (NPC Ed) am the Thief and I have made NPC Fae vulnerable  |
| 2           | NPC Fae | Inspector   | broadcast | I (NPC Ed) am the Thief and I have made NPC Fae vulnerable  |

#### Actions Round 3
| round_index | Player  | action    | Target 1  | Target 2 | status      |
| :-----------| :-------| :---------| :---------| :--------| :---------- |
| 3           | NPC Bob | Judge     | Inspector |          | successful  |
| 3           | NPC Cal | Reporter  | NPC Fae   |          | successful  |
| 3           | NPC Dan | Medic     | NPC Fae   |          | successful  |
| 3           | NPC Fae | Inspector | NPC Cal   |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Fae | Inspector   | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Reporter    | False      | True      | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                   |
| :-----------| :-------| :-----------| :---------| :-------------------------------------------------------- |
| 3           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Reporter and NPC Fae is the Inspector  |
| 3           | NPC Ann | Executioner | broadcast | I (NPC Fae) inspected NPC Cal and they are possessed      |
| 3           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Reporter and NPC Fae is the Inspector  |
| 3           | NPC Bob | Judge       | broadcast | I (NPC Fae) inspected NPC Cal and they are possessed      |
| 3           | NPC Cal | Reporter    | broadcast | I (NPC Cal) am the Reporter and NPC Fae is the Inspector  |
| 3           | NPC Cal | Reporter    | broadcast | I (NPC Fae) inspected NPC Cal and they are possessed      |
| 3           | NPC Cal | Reporter    | reveal    | NPC Fae is Inspector                                      |
| 3           | NPC Dan | Medic       | broadcast | I (NPC Cal) am the Reporter and NPC Fae is the Inspector  |
| 3           | NPC Dan | Medic       | broadcast | I (NPC Fae) inspected NPC Cal and they are possessed      |
| 3           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Reporter and NPC Fae is the Inspector  |
| 3           | NPC Ed  | Thief       | broadcast | I (NPC Fae) inspected NPC Cal and they are possessed      |
| 3           | NPC Fae | Inspector   | broadcast | I (NPC Cal) am the Reporter and NPC Fae is the Inspector  |
| 3           | NPC Fae | Inspector   | broadcast | I (NPC Fae) inspected NPC Cal and they are possessed      |
| 3           | NPC Fae | Inspector   | reveal    | Reporter is Possessed                                     |

#### Actions Round 4
| round_index | Player  | action      | Target 1 | Target 2 | status                        |
| :-----------| :-------| :-----------| :--------| :--------| :---------------------------- |
| 4           | NPC Ann | Executioner | NPC Cal  |          | failed because of no support  |
| 4           | NPC Bob | Judge       | Thief    |          | successful                    |
| 4           | NPC Dan | Medic       | NPC Cal  |          | successful                    |
| 4           | NPC Ed  | Thief       | NPC Bob  |          | successful                    |
| 4           | NPC Fae | Inspector   | NPC Dan  |          | successful                    |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ann | Executioner | False      | False     | False      | 4         | True   | 0              | 0                  |
| 4           | NPC Ed  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Bob | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Fae | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 4           | NPC Cal | Reporter    | False      | True      | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message       | details                                                     |
| :-----------| :-------| :-----------| :-------------| :---------------------------------------------------------- |
| 4           | NPC Ann | Executioner | broadcast     | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 4           | NPC Ann | Executioner | broadcast     | I (NPC Fae) inspected NPC Dan and they are not possessed    |
| 4           | NPC Ann | Executioner | action failed |                                                             |
| 4           | NPC Bob | Judge       | broadcast     | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 4           | NPC Bob | Judge       | broadcast     | I (NPC Fae) inspected NPC Dan and they are not possessed    |
| 4           | NPC Cal | Reporter    | broadcast     | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 4           | NPC Cal | Reporter    | broadcast     | I (NPC Fae) inspected NPC Dan and they are not possessed    |
| 4           | NPC Dan | Medic       | broadcast     | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 4           | NPC Dan | Medic       | broadcast     | I (NPC Fae) inspected NPC Dan and they are not possessed    |
| 4           | NPC Ed  | Thief       | broadcast     | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 4           | NPC Ed  | Thief       | broadcast     | I (NPC Fae) inspected NPC Dan and they are not possessed    |
| 4           | NPC Fae | Inspector   | broadcast     | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 4           | NPC Fae | Inspector   | broadcast     | I (NPC Fae) inspected NPC Dan and they are not possessed    |
| 4           | NPC Fae | Inspector   | reveal        | Medic is Innocent                                           |

#### Actions Round 5
| round_index | Player  | action   | Target 1  | Target 2 | status      |
| :-----------| :-------| :--------| :---------| :--------| :---------- |
| 5           | NPC Bob | Judge    | Inspector |          | successful  |
| 5           | NPC Cal | Reporter | NPC Dan   |          | successful  |
| 5           | NPC Dan | Medic    | NPC Ann   |          | successful  |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Bob | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Fae | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 5           | NPC Cal | Reporter    | False      | True      | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message   | details                                               |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------- |
| 5           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Medic  |
| 5           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Medic  |
| 5           | NPC Cal | Reporter    | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Medic  |
| 5           | NPC Cal | Reporter    | reveal    | NPC Dan is Medic                                      |
| 5           | NPC Dan | Medic       | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Medic  |
| 5           | NPC Ed  | Thief       | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Medic  |
| 5           | NPC Fae | Inspector   | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Medic  |

#### Actions Round 6
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 6           | NPC Bob | Judge     | Reporter |          | successful  |
| 6           | NPC Dan | Medic     | NPC Ed   |          | successful  |
| 6           | NPC Ed  | Thief     | NPC Dan  |          | successful  |
| 6           | NPC Fae | Inspector | NPC Ed   |          | successful  |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ed  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Fae | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 6           | NPC Cal | Reporter    | False      | True      | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Dan | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 6           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 6           | NPC Ann | Executioner | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed     |
| 6           | NPC Bob | Judge       | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 6           | NPC Bob | Judge       | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed     |
| 6           | NPC Cal | Reporter    | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 6           | NPC Cal | Reporter    | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed     |
| 6           | NPC Dan | Medic       | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 6           | NPC Dan | Medic       | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed     |
| 6           | NPC Ed  | Thief       | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 6           | NPC Ed  | Thief       | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed     |
| 6           | NPC Fae | Inspector   | broadcast | I (NPC Ed) am the Thief and I have made NPC Dan vulnerable  |
| 6           | NPC Fae | Inspector   | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed     |
| 6           | NPC Fae | Inspector   | reveal    | Thief is Innocent                                           |

#### Actions Round 7
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 7           | NPC Bob | Judge    | Thief    |          | successful  |
| 7           | NPC Cal | Reporter | NPC Bob  |          | successful  |
| 7           | NPC Dan | Medic    | NPC Bob  |          | successful  |
| 7           | NPC Ed  | Thief    | NPC Ann  |          | successful  |

#### States Round 7
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Ann | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Ed  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Bob | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Fae | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 7           | NPC Cal | Reporter    | False      | True      | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Dan | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 7           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 7           | NPC Bob | Judge       | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 7           | NPC Cal | Reporter    | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 7           | NPC Cal | Reporter    | reveal    | NPC Bob is Judge                                            |
| 7           | NPC Dan | Medic       | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 7           | NPC Ed  | Thief       | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 7           | NPC Fae | Inspector   | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |