#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 63   | 4       | 3       |

#### Roles
| Role       |
| :--------- |
| Thief      |
| Medic      |
| Jailer     |
| Inspector  |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Thief     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Jailer    | role change | Your Role is Jailer     |
| 0           | NPC Ann | Jailer    | possessed   | You are Not Possessed   |
| 0           | NPC Bob | Thief     | role change | Your Role is Thief      |
| 0           | NPC Bob | Thief     | possessed   | You are Possessed       |
| 0           | NPC Cal | Medic     | role change | Your Role is Medic      |
| 0           | NPC Cal | Medic     | possessed   | You are Not Possessed   |
| 0           | NPC Dan | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Dan | Inspector | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Bob | Thief     | NPC Ann  |          | successful  |
| 1           | NPC Cal | Medic     | NPC Ann  |          | successful  |
| 1           | NPC Dan | Inspector | NPC Ann  |          | successful  |

#### States Round 1
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Thief     | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Jailer    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Jailer    | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Ann | Jailer    | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed     |
| 1           | NPC Bob | Thief     | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Bob | Thief     | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed     |
| 1           | NPC Cal | Medic     | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Cal | Medic     | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed     |
| 1           | NPC Dan | Inspector | broadcast | I (NPC Bob) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Dan | Inspector | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed     |
| 1           | NPC Dan | Inspector | reveal    | Jailer is Innocent                                           |

#### Actions Round 2
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 2           | NPC Cal | Medic  | NPC Dan  |          | successful  |

#### States Round 2
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Thief     | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Jailer    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 3           | NPC Bob | Thief     | NPC Dan  |          | successful  |
| 3           | NPC Cal | Medic     | NPC Bob  |          | successful  |
| 3           | NPC Dan | Inspector | NPC Ann  |          | successful  |

#### States Round 3
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Thief     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Jailer    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Inspector | False      | False     | True       | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann | Jailer    | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 3           | NPC Ann | Jailer    | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed     |
| 3           | NPC Bob | Thief     | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 3           | NPC Bob | Thief     | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed     |
| 3           | NPC Cal | Medic     | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 3           | NPC Cal | Medic     | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed     |
| 3           | NPC Dan | Inspector | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable  |
| 3           | NPC Dan | Inspector | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed     |
| 3           | NPC Dan | Inspector | reveal    | Jailer is Innocent                                           |