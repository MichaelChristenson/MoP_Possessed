#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 92   | 6       | 1       |

#### Roles
| Role         |
| :----------- |
| Medic        |
| Judge        |
| Thief        |
| Inspector    |
| Reporter     |
| Executioner  |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Reporter    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Medic       | role change | Your Role is Medic        |
| 0           | NPC Ann | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Thief       | role change | Your Role is Thief        |
| 0           | NPC Bob | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Cal | Reporter    | possessed   | You are Possessed         |
| 0           | NPC Dan | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Dan | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Ed  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Fae | Inspector   | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Medic     | NPC Bob  |          | successful  |
| 1           | NPC Bob | Thief     | NPC Cal  |          | successful  |
| 1           | NPC Cal | Reporter  | NPC Ed   |          | successful  |
| 1           | NPC Ed  | Judge     | Reporter |          | successful  |
| 1           | NPC Fae | Inspector | NPC Ed   |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal | Reporter    | False      | True      | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                      |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Medic       | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ann | Medic       | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed      |
| 1           | NPC Bob | Thief       | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Bob | Thief       | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed      |
| 1           | NPC Cal | Reporter    | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Cal | Reporter    | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed      |
| 1           | NPC Cal | Reporter    | reveal    | NPC Ed is Judge                                              |
| 1           | NPC Dan | Executioner | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Dan | Executioner | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed      |
| 1           | NPC Ed  | Judge       | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Ed  | Judge       | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed      |
| 1           | NPC Fae | Inspector   | broadcast | I (NPC Bob) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Fae | Inspector   | broadcast | I (NPC Fae) inspected NPC Ed and they are not possessed      |
| 1           | NPC Fae | Inspector   | reveal    | Judge is Innocent                                            |