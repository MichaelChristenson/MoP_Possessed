#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 26   | 4       | 6       |

#### Roles
| Role     |
| :------- |
| Prophet  |
| Priest   |
| Thief    |
| Medic    |

#### States Round 0
| round_index | Player  | Role    | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Prophet | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Priest  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Thief   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Medic   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role    | message     | details                |
| :-----------| :-------| :-------| :-----------| :--------------------- |
| 0           | NPC Ann | Thief   | role change | Your Role is Thief     |
| 0           | NPC Ann | Thief   | possessed   | You are Not Possessed  |
| 0           | NPC Bob | Prophet | role change | Your Role is Prophet   |
| 0           | NPC Bob | Prophet | possessed   | You are Possessed      |
| 0           | NPC Cal | Priest  | role change | Your Role is Priest    |
| 0           | NPC Cal | Priest  | possessed   | You are Not Possessed  |
| 0           | NPC Dan | Medic   | role change | Your Role is Medic     |
| 0           | NPC Dan | Medic   | possessed   | You are Not Possessed  |

#### Actions Round 1
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 1           | NPC Ann | Thief   | NPC Cal  |          | successful  |
| 1           | NPC Bob | Prophet | NPC Dan  |          | successful  |
| 1           | NPC Dan | Medic   | NPC Cal  |          | successful  |

#### States Round 1
| round_index | Player  | Role    | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Prophet | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Priest  | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Thief   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Medic   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role    | message   | details                                                      |
| :-----------| :-------| :-------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Thief   | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Bob | Prophet | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Cal | Priest  | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Dan | Medic   | broadcast | I (NPC Ann) am the Thief and I have made NPC Cal vulnerable  |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Bob | Prophet | NPC Dan  |          | successful  |
| 2           | NPC Dan | Medic   | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player  | Role    | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Prophet | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Priest  | False      | False     | True       | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Thief   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Medic   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |

#### Actions Round 3
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 3           | NPC Ann | Thief   | NPC Dan  |          | successful  |
| 3           | NPC Bob | Prophet | NPC Cal  |          | successful  |
| 3           | NPC Dan | Medic   | NPC Bob  |          | successful  |

#### States Round 3
| round_index | Player  | Role    | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Prophet | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Priest  | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Thief   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Medic   | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role    | message   | details                                                      |
| :-----------| :-------| :-------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann | Thief   | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| 3           | NPC Bob | Prophet | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| 3           | NPC Cal | Priest  | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |
| 3           | NPC Dan | Medic   | broadcast | I (NPC Ann) am the Thief and I have made NPC Dan vulnerable  |

#### Actions Round 4
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 4           | NPC Bob | Prophet | NPC Ann  |          | successful  |
| 4           | NPC Dan | Medic   | NPC Cal  |          | successful  |

#### States Round 4
| round_index | Player  | Role    | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Bob | Prophet | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Priest  | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Thief   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Medic   | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |

#### Actions Round 5
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 5           | NPC Ann | Thief   | NPC Bob  |          | successful  |
| 5           | NPC Bob | Prophet | NPC Cal  |          | successful  |
| 5           | NPC Dan | Medic   | NPC Ann  |          | successful  |

#### States Round 5
| round_index | Player  | Role    | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Bob | Prophet | False      | True      | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Cal | Priest  | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Ann | Thief   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Medic   | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role    | message   | details                                                      |
| :-----------| :-------| :-------| :---------| :----------------------------------------------------------- |
| 5           | NPC Ann | Thief   | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| 5           | NPC Bob | Prophet | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| 5           | NPC Cal | Priest  | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |
| 5           | NPC Dan | Medic   | broadcast | I (NPC Ann) am the Thief and I have made NPC Bob vulnerable  |

#### Actions Round 6
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 6           | NPC Ann | Steal   | NPC Bob  | Prophet  | successful  |
| 6           | NPC Bob | Prophet | NPC Cal  |          | successful  |
| 6           | NPC Dan | Medic   | NPC Bob  |          | successful  |

#### States Round 6
| round_index | Player  | Role    | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Bob | Thief   | False      | True      | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Priest  | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Ann | Prophet | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan | Medic   | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |