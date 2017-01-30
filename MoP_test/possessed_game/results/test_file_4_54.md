#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 54   | 4       | 6       |

#### Roles
| Role       |
| :--------- |
| Trader     |
| Psychic    |
| Medic      |
| Inspector  |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Trader    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Medic     | role change | Your Role is Medic      |
| 0           | NPC Ann | Medic     | possessed   | You are Not Possessed   |
| 0           | NPC Bob | Trader    | role change | Your Role is Trader     |
| 0           | NPC Bob | Trader    | possessed   | You are Possessed       |
| 0           | NPC Cal | Psychic   | role change | Your Role is Psychic    |
| 0           | NPC Cal | Psychic   | possessed   | You are Not Possessed   |
| 0           | NPC Dan | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Dan | Inspector | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Medic     | NPC Cal  |          | successful  |
| 1           | NPC Bob | Trader    | NPC Ann  | NPC Dan  | successful  |
| 1           | NPC Cal | Psychic   |          |          | successful  |
| 1           | NPC Dan | Inspector | NPC Cal  |          | successful  |

#### States Round 1
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Trader    | False      | True      | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Cal | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 1           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 1           | NPC Ann | Inspector | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 1           | NPC Bob | Trader    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob | Trader    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 1           | NPC Bob | Trader    | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 1           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 1           | NPC Cal | Psychic   | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 1           | NPC Cal | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 1           | NPC Dan | Medic     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Dan | Medic     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 1           | NPC Dan | Medic     | broadcast | I (NPC Dan) inspected NPC Cal and they are not possessed       |
| 1           | NPC Dan | Medic     | reveal    | Psychic is Innocent                                            |

#### Actions Round 2
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 2           | NPC Ann | Inspector | NPC Dan  |          | successful  |
| 2           | NPC Cal | Psychic   |          |          | successful  |
| 2           | NPC Dan | Medic     | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Trader    | False      | True      | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Cal | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed       |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ann | Inspector | reveal    | Medic is Innocent                                              |
| 2           | NPC Bob | Trader    | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed       |
| 2           | NPC Bob | Trader    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 2           | NPC Bob | Trader    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal | Psychic   | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed       |
| 2           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 2           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 2           | NPC Dan | Medic     | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed       |
| 2           | NPC Dan | Medic     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 2           | NPC Dan | Medic     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 3           | NPC Ann | Inspector | NPC Dan  |          | successful  |
| 3           | NPC Cal | Psychic   |          |          | successful  |
| 3           | NPC Dan | Medic     | NPC Bob  |          | successful  |

#### States Round 3
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Trader    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ann | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed       |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 3           | NPC Ann | Inspector | reveal    | Medic is Innocent                                              |
| 3           | NPC Bob | Trader    | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed       |
| 3           | NPC Bob | Trader    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Bob | Trader    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 3           | NPC Cal | Psychic   | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed       |
| 3           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 3           | NPC Cal | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 3           | NPC Dan | Medic     | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed       |
| 3           | NPC Dan | Medic     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Dan | Medic     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |

#### Actions Round 4
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 4           | NPC Bob | Trader  | NPC Cal  | NPC Dan  | successful  |
| 4           | NPC Cal | Psychic |          |          | successful  |
| 4           | NPC Dan | Medic   | NPC Cal  |          | successful  |

#### States Round 4
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Bob | Trader    | False      | True      | False      | 4         | True   | 0              | 0                  |
| 4           | NPC Cal | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 4           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 4           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Bob | Trader    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 4           | NPC Bob | Trader    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Cal | Medic     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 4           | NPC Cal | Medic     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Cal | Medic     | reveal    | Player: NPC Ann is not possessed                               |
| 4           | NPC Dan | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed      |
| 4           | NPC Dan | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |

#### Actions Round 5
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 5           | NPC Ann | Inspector | NPC Cal  |          | successful  |
| 5           | NPC Cal | Medic     | NPC Dan  |          | successful  |
| 5           | NPC Dan | Psychic   |          |          | successful  |

#### States Round 5
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Bob | Trader    | False      | True      | False      | 3         | True   | 0              | 0                  |
| 5           | NPC Cal | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ann | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Dan | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Ann) inspected NPC Cal and they are not possessed       |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ann | Inspector | reveal    | Medic is Innocent                                              |
| 5           | NPC Bob | Trader    | broadcast | I (NPC Ann) inspected NPC Cal and they are not possessed       |
| 5           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Cal | Medic     | broadcast | I (NPC Ann) inspected NPC Cal and they are not possessed       |
| 5           | NPC Cal | Medic     | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Dan | Psychic   | broadcast | I (NPC Ann) inspected NPC Cal and they are not possessed       |
| 5           | NPC Dan | Psychic   | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Dan | Psychic   | reveal    | Player: NPC Cal is not possessed                               |

#### Actions Round 6
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 6           | NPC Cal | Medic   | NPC Bob  |          | successful  |
| 6           | NPC Dan | Psychic |          |          | successful  |

#### States Round 6
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Bob | Trader    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ann | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Dan | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role      | message   | details                                                    |
| :-----------| :-------| :---------| :---------| :--------------------------------------------------------- |
| 6           | NPC Ann | Inspector | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed  |
| 6           | NPC Bob | Trader    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed  |
| 6           | NPC Cal | Medic     | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed  |
| 6           | NPC Dan | Psychic   | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed  |
| 6           | NPC Dan | Psychic   | reveal    | Player: NPC Ann is not possessed                           |