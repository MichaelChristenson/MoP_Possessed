#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 27   | 4       | 7       |

#### Roles
| Role       |
| :--------- |
| Medic      |
| Reporter   |
| Psychic    |
| Inspector  |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Psychic   | role change | Your Role is Psychic    |
| 0           | NPC Ann | Psychic   | possessed   | You are Not Possessed   |
| 0           | NPC Bob | Medic     | role change | Your Role is Medic      |
| 0           | NPC Bob | Medic     | possessed   | You are Possessed       |
| 0           | NPC Cal | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Cal | Reporter  | possessed   | You are Not Possessed   |
| 0           | NPC Dan | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Dan | Inspector | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Psychic   |          |          | successful  |
| 1           | NPC Bob | Medic     | NPC Ann  |          | successful  |
| 1           | NPC Cal | Reporter  | NPC Dan  |          | successful  |
| 1           | NPC Dan | Inspector | NPC Ann  |          | successful  |

#### States Round 1
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 1           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ann | Psychic   | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Inspector       |
| 1           | NPC Ann | Psychic   | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed       |
| 1           | NPC Ann | Psychic   | reveal    | Player: NPC Cal is not possessed                               |
| 1           | NPC Bob | Medic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob | Medic     | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Inspector       |
| 1           | NPC Bob | Medic     | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed       |
| 1           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Inspector       |
| 1           | NPC Cal | Reporter  | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed       |
| 1           | NPC Cal | Reporter  | reveal    | NPC Dan is Inspector                                           |
| 1           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Dan | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Dan is the Inspector       |
| 1           | NPC Dan | Inspector | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed       |
| 1           | NPC Dan | Inspector | reveal    | Psychic is Innocent                                            |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Ann | Psychic |          |          | successful  |
| 2           | NPC Bob | Medic   | NPC Dan  |          | successful  |

#### States Round 2
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role      | message   | details                                                       |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------ |
| 2           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Ann | Psychic   | reveal    | Player: NPC Cal is not possessed                              |
| 2           | NPC Bob | Medic     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 3           | NPC Ann | Psychic   |          |          | successful  |
| 3           | NPC Bob | Medic     | NPC Cal  |          | successful  |
| 3           | NPC Cal | Reporter  | NPC Ann  |          | successful  |
| 3           | NPC Dan | Inspector | NPC Ann  |          | successful  |

#### States Round 3
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Dan | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role      | message   | details                                                       |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------ |
| 3           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ann | Psychic   | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Psychic        |
| 3           | NPC Ann | Psychic   | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed      |
| 3           | NPC Ann | Psychic   | reveal    | Player: NPC Dan is not possessed                              |
| 3           | NPC Bob | Medic     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Bob | Medic     | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Psychic        |
| 3           | NPC Bob | Medic     | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed      |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Psychic        |
| 3           | NPC Cal | Reporter  | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed      |
| 3           | NPC Cal | Reporter  | reveal    | NPC Ann is Psychic                                            |
| 3           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Dan | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Psychic        |
| 3           | NPC Dan | Inspector | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed      |
| 3           | NPC Dan | Inspector | reveal    | Psychic is Innocent                                           |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 4           | NPC Ann | Psychic  |          |          | successful  |
| 4           | NPC Bob | Medic    | NPC Ann  |          | successful  |
| 4           | NPC Cal | Reporter | NPC Bob  |          | successful  |

#### States Round 4
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Bob | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Ann | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 4           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 4           | NPC Ann | Psychic   | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Medic           |
| 4           | NPC Ann | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 4           | NPC Bob | Medic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Bob | Medic     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 4           | NPC Bob | Medic     | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Medic           |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 4           | NPC Cal | Reporter  | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Medic           |
| 4           | NPC Cal | Reporter  | reveal    | NPC Bob is Medic                                               |
| 4           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 4           | NPC Dan | Inspector | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Medic           |

#### Actions Round 5
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 5           | NPC Ann | Psychic   |          |          | successful  |
| 5           | NPC Bob | Medic     | NPC Dan  |          | successful  |
| 5           | NPC Dan | Inspector | NPC Cal  |          | successful  |

#### States Round 5
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Bob | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Cal | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Ann | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Dan | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 5           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ann | Psychic   | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Ann | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 5           | NPC Bob | Medic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Bob | Medic     | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Cal | Reporter  | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Dan | Inspector | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 5           | NPC Dan | Inspector | reveal    | Reporter is Innocent                                           |

#### Actions Round 6
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 6           | NPC Ann | Psychic   |          |          | successful  |
| 6           | NPC Bob | Medic     | NPC Cal  |          | successful  |
| 6           | NPC Dan | Inspector | NPC Bob  |          | successful  |

#### States Round 6
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Bob | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ann | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Dan | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 6           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 6           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Ann | Psychic   | broadcast | I (NPC Dan) inspected NPC Bob and they are possessed           |
| 6           | NPC Ann | Psychic   | reveal    | Player: NPC Cal is not possessed                               |
| 6           | NPC Bob | Medic     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 6           | NPC Bob | Medic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Bob | Medic     | broadcast | I (NPC Dan) inspected NPC Bob and they are possessed           |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Cal | Reporter  | broadcast | I (NPC Dan) inspected NPC Bob and they are possessed           |
| 6           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 6           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Dan | Inspector | broadcast | I (NPC Dan) inspected NPC Bob and they are possessed           |
| 6           | NPC Dan | Inspector | reveal    | Medic is Possessed                                             |

#### Actions Round 7
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 7           | NPC Ann | Psychic |          |          | successful  |
| 7           | NPC Bob | Medic   | NPC Ann  |          | successful  |

#### States Round 7
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Bob | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Cal | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Ann | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Dan | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 7           | NPC Ann | Psychic   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Ann | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 7           | NPC Bob | Medic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Cal | Reporter  | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Dan | Inspector | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |