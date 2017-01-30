#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 25   | 5       | 5       |

#### Roles
| Role      |
| :-------- |
| Priest    |
| Reporter  |
| Silencer  |
| Trader    |
| Medic     |

#### States Round 0
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Reporter | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Silencer | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Trader   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role     | message     | details                |
| :-----------| :-------| :--------| :-----------| :--------------------- |
| 0           | NPC Ann | Trader   | role change | Your Role is Trader    |
| 0           | NPC Ann | Trader   | possessed   | You are Possessed      |
| 0           | NPC Bob | Silencer | role change | Your Role is Silencer  |
| 0           | NPC Bob | Silencer | possessed   | You are Not Possessed  |
| 0           | NPC Cal | Priest   | role change | Your Role is Priest    |
| 0           | NPC Cal | Priest   | possessed   | You are Not Possessed  |
| 0           | NPC Dan | Medic    | role change | Your Role is Medic     |
| 0           | NPC Dan | Medic    | possessed   | You are Not Possessed  |
| 0           | NPC Ed  | Reporter | role change | Your Role is Reporter  |
| 0           | NPC Ed  | Reporter | possessed   | You are Not Possessed  |

#### Actions Round 1
| round_index | Player  | action   | Target 1 | Target 2 | status                         |
| :-----------| :-------| :--------| :--------| :--------| :----------------------------- |
| 1           | NPC Ann | Trader   | NPC Cal  | NPC Bob  | failed because not vulnerable  |
| 1           | NPC Bob | Silencer | NPC Dan  |          | successful                     |
| 1           | NPC Dan | Medic    | NPC Ed   |          | successful                     |
| 1           | NPC Ed  | Reporter | NPC Ann  |          | successful                     |

#### States Round 1
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Reporter | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Silencer | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ann | Trader   | False      | True      | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Dan | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role     | message   | details                                               |
| :-----------| :-------| :--------| :---------| :---------------------------------------------------- |
| 1           | NPC Ann | Trader   | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Trader  |
| 1           | NPC Bob | Silencer | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Trader  |
| 1           | NPC Cal | Priest   | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Trader  |
| 1           | NPC Dan | Medic    | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Trader  |
| 1           | NPC Dan | Medic    | silenced  | You have been silenced                                |
| 1           | NPC Ed  | Reporter | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Trader  |
| 1           | NPC Ed  | Reporter | reveal    | NPC Ann is Trader                                     |

#### Actions Round 2
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 2           | NPC Bob | Silencer | NPC Dan  |          | successful  |
| 2           | NPC Dan | Medic    | NPC Bob  |          | successful  |
| 2           | NPC Ed  | Reporter | NPC Cal  |          | successful  |

#### States Round 2
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Reporter | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Bob | Silencer | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Trader   | False      | True      | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Dan | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role     | message   | details                                               |
| :-----------| :-------| :--------| :---------| :---------------------------------------------------- |
| 2           | NPC Ann | Trader   | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Priest  |
| 2           | NPC Bob | Silencer | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Priest  |
| 2           | NPC Cal | Priest   | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Priest  |
| 2           | NPC Dan | Medic    | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Priest  |
| 2           | NPC Dan | Medic    | silenced  | You have been silenced                                |
| 2           | NPC Ed  | Reporter | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Priest  |
| 2           | NPC Ed  | Reporter | reveal    | NPC Cal is Priest                                     |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 3           | NPC Bob | Silencer | NPC Bob  |          | successful  |
| 3           | NPC Dan | Medic    | NPC Ann  |          | successful  |

#### States Round 3
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Reporter | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Bob | Silencer | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ann | Trader   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role     | message  | details                 |
| :-----------| :-------| :--------| :--------| :---------------------- |
| 3           | NPC Bob | Silencer | silenced | You have been silenced  |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status                         |
| :-----------| :-------| :--------| :--------| :--------| :----------------------------- |
| 4           | NPC Ann | Trader   | NPC Cal  | NPC Bob  | failed because not vulnerable  |
| 4           | NPC Bob | Silencer | NPC Bob  |          | successful                     |
| 4           | NPC Dan | Medic    | NPC Cal  |          | successful                     |
| 4           | NPC Ed  | Reporter | NPC Bob  |          | successful                     |

#### States Round 4
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Reporter | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Bob | Silencer | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann | Trader   | False      | True      | False      | 4         | True   | 0              | 0                  |
| 4           | NPC Dan | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role     | message   | details                                                 |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------ |
| 4           | NPC Ann | Trader   | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Silencer  |
| 4           | NPC Bob | Silencer | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Silencer  |
| 4           | NPC Bob | Silencer | silenced  | You have been silenced                                  |
| 4           | NPC Cal | Priest   | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Silencer  |
| 4           | NPC Dan | Medic    | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Silencer  |
| 4           | NPC Ed  | Reporter | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Silencer  |
| 4           | NPC Ed  | Reporter | reveal    | NPC Bob is Silencer                                     |

#### Actions Round 5
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 5           | NPC Bob | Silencer | NPC Ed   |          | successful  |
| 5           | NPC Dan | Medic    | NPC Ed   |          | successful  |

#### States Round 5
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Reporter | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob | Silencer | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Ann | Trader   | False      | True      | False      | 3         | True   | 0              | 0                  |
| 5           | NPC Dan | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player | Role     | message  | details                 |
| :-----------| :------| :--------| :--------| :---------------------- |
| 5           | NPC Ed | Reporter | silenced | You have been silenced  |