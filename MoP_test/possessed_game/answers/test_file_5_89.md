#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 89   | 5       | 2       |

#### Roles
| Role         |
| :----------- |
| Thief        |
| Executioner  |
| Medic        |
| Inspector    |
| Reporter     |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Inspector   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Ann | Inspector   | possessed   | You are Possessed         |
| 0           | NPC Bob | Medic       | role change | Your Role is Medic        |
| 0           | NPC Bob | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Thief       | role change | Your Role is Thief        |
| 0           | NPC Cal | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Dan | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ed  | Executioner | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 1           | NPC Bob | Medic    | NPC Ed   |          | successful  |
| 1           | NPC Cal | Thief    | NPC Bob  |          | successful  |
| 1           | NPC Dan | Reporter | NPC Ann  |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Inspector   | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Inspector   | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed        |
| 1           | NPC Ann | Inspector   | broadcast | I (NPC Cal) am the Thief and I have made NPC Bob vulnerable  |
| 1           | NPC Ann | Inspector   | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Inspector     |
| 1           | NPC Bob | Medic       | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed        |
| 1           | NPC Bob | Medic       | broadcast | I (NPC Cal) am the Thief and I have made NPC Bob vulnerable  |
| 1           | NPC Bob | Medic       | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Inspector     |
| 1           | NPC Cal | Thief       | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed        |
| 1           | NPC Cal | Thief       | broadcast | I (NPC Cal) am the Thief and I have made NPC Bob vulnerable  |
| 1           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Inspector     |
| 1           | NPC Dan | Reporter    | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed        |
| 1           | NPC Dan | Reporter    | broadcast | I (NPC Cal) am the Thief and I have made NPC Bob vulnerable  |
| 1           | NPC Dan | Reporter    | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Inspector     |
| 1           | NPC Dan | Reporter    | reveal    | NPC Ann is Inspector                                         |
| 1           | NPC Ed  | Executioner | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed        |
| 1           | NPC Ed  | Executioner | broadcast | I (NPC Cal) am the Thief and I have made NPC Bob vulnerable  |
| 1           | NPC Ed  | Executioner | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Inspector     |

#### Actions Round 2
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 2           | NPC Bob | Medic  | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Inspector   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |