#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 67   | 4       | 4       |

#### Roles
| Role      |
| :-------- |
| Thief     |
| Silencer  |
| Judge     |
| Medic     |

#### States Round 0
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Thief    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Silencer | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role     | message     | details                |
| :-----------| :-------| :--------| :-----------| :--------------------- |
| 0           | NPC Ann | Judge    | role change | Your Role is Judge     |
| 0           | NPC Ann | Judge    | possessed   | You are Not Possessed  |
| 0           | NPC Bob | Thief    | role change | Your Role is Thief     |
| 0           | NPC Bob | Thief    | possessed   | You are Possessed      |
| 0           | NPC Cal | Silencer | role change | Your Role is Silencer  |
| 0           | NPC Cal | Silencer | possessed   | You are Not Possessed  |
| 0           | NPC Dan | Medic    | role change | Your Role is Medic     |
| 0           | NPC Dan | Medic    | possessed   | You are Not Possessed  |

#### Actions Round 1
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 1           | NPC Ann | Judge    | Silencer |          | successful  |
| 1           | NPC Bob | Thief    | NPC Dan  |          | successful  |
| 1           | NPC Cal | Silencer | NPC Dan  |          | successful  |
| 1           | NPC Dan | Medic    | NPC Cal  |          | successful  |

#### States Round 1
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Thief    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal | Silencer | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Medic    | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role     | message   | details                                                      |
| :-----------| :-------| :--------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Judge    | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Bob | Thief    | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Cal | Silencer | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Dan | Medic    | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 1           | NPC Dan | Medic    | silenced  | You have been silenced                                       |

#### Actions Round 2
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 2           | NPC Ann | Judge    | Medic    |          | successful  |
| 2           | NPC Cal | Silencer | NPC Bob  |          | successful  |
| 2           | NPC Dan | Medic    | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Thief    | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal | Silencer | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Medic    | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role  | message  | details                 |
| :-----------| :-------| :-----| :--------| :---------------------- |
| 2           | NPC Bob | Thief | silenced | You have been silenced  |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 3           | NPC Ann | Judge    | Silencer |          | successful  |
| 3           | NPC Bob | Thief    | NPC Cal  |          | successful  |
| 3           | NPC Cal | Silencer | NPC Bob  |          | successful  |
| 3           | NPC Dan | Medic    | NPC Bob  |          | successful  |

#### States Round 3
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Thief    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Silencer | False      | False     | True       | 1         | True   | 0              | 0                  |
| 3           | NPC Ann | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Medic    | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role  | message  | details                 |
| :-----------| :-------| :-----| :--------| :---------------------- |
| 3           | NPC Bob | Thief | silenced | You have been silenced  |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 4           | NPC Ann | Judge    | Thief    |          | successful  |
| 4           | NPC Bob | Thief    | NPC Ann  |          | successful  |
| 4           | NPC Cal | Silencer | NPC Dan  |          | successful  |
| 4           | NPC Dan | Medic    | NPC Cal  |          | successful  |

#### States Round 4
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Bob | Thief    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Cal | Silencer | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Judge    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Medic    | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role  | message  | details                 |
| :-----------| :-------| :-----| :--------| :---------------------- |
| 4           | NPC Dan | Medic | silenced | You have been silenced  |