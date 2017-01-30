#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 42   | 6       | 6       |

#### Roles
| Role         |
| :----------- |
| Judge        |
| Psychic      |
| Executioner  |
| Reporter     |
| Medic        |
| Inspector    |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Judge       | role change | Your Role is Judge        |
| 0           | NPC Ann | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Bob | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Medic       | role change | Your Role is Medic        |
| 0           | NPC Cal | Medic       | possessed   | You are Possessed         |
| 0           | NPC Dan | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Dan | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Ed  | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Fae | Reporter    | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1  | Target 2 | status        |
| :-----------| :-------| :---------| :---------| :--------| :------------ |
| 1           | NPC Ann | Judge     | Inspector |          | successful    |
| 1           | NPC Cal | Medic     | NPC Ed    |          | successful    |
| 1           | NPC Dan | Inspector | NPC Ed    |          | successful    |
| 1           | NPC Ed  | Psychic   |           |          | not resolved  |
| 1           | NPC Fae | Reporter  | NPC Bob   |          | successful    |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 1           | NPC Ann | Judge       | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 1           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 1           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 1           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 1           | NPC Bob | Executioner | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 1           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 1           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 1           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 1           | NPC Cal | Medic       | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 1           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 1           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 1           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 1           | NPC Dan | Inspector   | reveal    | Psychic is Innocent                                            |
| 1           | NPC Ed  | Psychic     | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 1           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 1           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 1           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 1           | NPC Ed  | Psychic     | reveal    | Player: NPC Ann is not possessed                               |
| 1           | NPC Ed  | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 1           | NPC Fae | Reporter    | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 1           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 1           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 1           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 1           | NPC Fae | Reporter    | reveal    | NPC Bob is Executioner                                         |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status        |
| :-----------| :-------| :-------| :--------| :--------| :------------ |
| 2           | NPC Ann | Judge   | Medic    |          | successful    |
| 2           | NPC Cal | Medic   | NPC Bob  |          | successful    |
| 2           | NPC Ed  | Psychic |          |          | not resolved  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ann | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 2           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 2           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 2           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 2           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 2           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 2           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 2           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 2           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 2           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 2           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 2           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 2           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 2           | NPC Ed  | Psychic     | reveal    | Player: NPC Dan is not possessed                               |
| 2           | NPC Ed  | Psychic     | reveal    | Player: NPC Ann is not possessed                               |
| 2           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 2           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 2           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status        |
| :-----------| :-------| :---------| :--------| :--------| :------------ |
| 3           | NPC Ann | Judge     | Medic    |          | successful    |
| 3           | NPC Cal | Medic     | NPC Fae  |          | successful    |
| 3           | NPC Dan | Inspector | NPC Ed   |          | successful    |
| 3           | NPC Ed  | Psychic   |          |          | not resolved  |
| 3           | NPC Fae | Reporter  | NPC Cal  |          | successful    |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ann | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Fae | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic           |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic           |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic           |
| 3           | NPC Dan | Inspector   | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 3           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 3           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 3           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 3           | NPC Dan | Inspector   | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic           |
| 3           | NPC Dan | Inspector   | reveal    | Psychic is Innocent                                            |
| 3           | NPC Ed  | Psychic     | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 3           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 3           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 3           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 3           | NPC Ed  | Psychic     | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic           |
| 3           | NPC Ed  | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 3           | NPC Ed  | Psychic     | reveal    | Player: NPC Fae is not possessed                               |
| 3           | NPC Fae | Reporter    | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed        |
| 3           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 3           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 3           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 3           | NPC Fae | Reporter    | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic           |
| 3           | NPC Fae | Reporter    | reveal    | NPC Cal is Medic                                               |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status        |
| :-----------| :-------| :--------| :--------| :--------| :------------ |
| 4           | NPC Ann | Judge    | Reporter |          | successful    |
| 4           | NPC Cal | Medic    | NPC Dan  |          | successful    |
| 4           | NPC Ed  | Psychic  |          |          | not resolved  |
| 4           | NPC Fae | Reporter | NPC Ann  |          | successful    |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ann | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Cal | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 4           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 4           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 4           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 4           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 4           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 4           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 4           | NPC Ed  | Psychic     | reveal    | Player: NPC Fae is not possessed                               |
| 4           | NPC Ed  | Psychic     | reveal    | Player: NPC Ann is not possessed                               |
| 4           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 4           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 4           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Fae is not possessed  |
| 4           | NPC Fae | Reporter    | reveal    | NPC Ann is Judge                                               |

#### Actions Round 5
| round_index | Player  | action    | Target 1 | Target 2 | status        |
| :-----------| :-------| :---------| :--------| :--------| :------------ |
| 5           | NPC Ann | Judge     | Medic    |          | successful    |
| 5           | NPC Cal | Medic     | NPC Ann  |          | successful    |
| 5           | NPC Dan | Inspector | NPC Ann  |          | successful    |
| 5           | NPC Ed  | Psychic   |          |          | not resolved  |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ann | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Fae | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Cal | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed       |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 5           | NPC Bob | Executioner | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed       |
| 5           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 5           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 5           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 5           | NPC Cal | Medic       | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed       |
| 5           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 5           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 5           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 5           | NPC Dan | Inspector   | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed       |
| 5           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 5           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 5           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 5           | NPC Dan | Inspector   | reveal    | Judge is Innocent                                              |
| 5           | NPC Ed  | Psychic     | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed       |
| 5           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 5           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 5           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 5           | NPC Ed  | Psychic     | reveal    | Player: NPC Ann is not possessed                               |
| 5           | NPC Ed  | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 5           | NPC Fae | Reporter    | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed       |
| 5           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 5           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 5           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |

#### Actions Round 6
| round_index | Player  | action   | Target 1 | Target 2 | status        |
| :-----------| :-------| :--------| :--------| :--------| :------------ |
| 6           | NPC Ann | Judge    | Reporter |          | successful    |
| 6           | NPC Cal | Medic    | NPC Ed   |          | successful    |
| 6           | NPC Ed  | Psychic  |          |          | not resolved  |
| 6           | NPC Fae | Reporter | NPC Dan  |          | successful    |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Ann | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ed  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Fae | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Cal | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 6           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 6           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 6           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 6           | NPC Ann | Judge       | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Inspector       |
| 6           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 6           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 6           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 6           | NPC Bob | Executioner | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Inspector       |
| 6           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 6           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 6           | NPC Cal | Medic       | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 6           | NPC Cal | Medic       | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Inspector       |
| 6           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 6           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 6           | NPC Dan | Inspector   | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 6           | NPC Dan | Inspector   | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Inspector       |
| 6           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 6           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 6           | NPC Ed  | Psychic     | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 6           | NPC Ed  | Psychic     | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Inspector       |
| 6           | NPC Ed  | Psychic     | reveal    | Player: NPC Ann is not possessed                               |
| 6           | NPC Ed  | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 6           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Bob is not possessed  |
| 6           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Dan is not possessed  |
| 6           | NPC Fae | Reporter    | broadcast | I (NPC Ed) am the Psychic and player NPC Ann is not possessed  |
| 6           | NPC Fae | Reporter    | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Inspector       |
| 6           | NPC Fae | Reporter    | reveal    | NPC Dan is Inspector                                           |