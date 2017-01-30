#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 56   | 6       | 2       |

#### Roles
| Role         |
| :----------- |
| Executioner  |
| Prophet      |
| Judge        |
| Thief        |
| Spy          |
| Reporter     |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ann | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Judge       | role change | Your Role is Judge        |
| 0           | NPC Bob | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Spy         | role change | Your Role is Spy          |
| 0           | NPC Cal | Spy         | possessed   | You are Possessed         |
| 0           | NPC Dan | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Dan | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Ed  | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Thief       | role change | Your Role is Thief        |
| 0           | NPC Fae | Thief       | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 1           | NPC Bob | Judge    | Reporter |          | successful  |
| 1           | NPC Cal | Spy      |          |          | successful  |
| 1           | NPC Dan | Reporter | NPC Ed   |          | successful  |
| 1           | NPC Ed  | Prophet  | NPC Cal  |          | successful  |
| 1           | NPC Fae | Thief    | NPC Ed   |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Prophet     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                     |
| :-----------| :-------| :-----------| :---------| :---------------------------------------------------------- |
| 1           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Reporter and NPC Ed is the Prophet       |
| 1           | NPC Ann | Executioner | broadcast | I (NPC Fae) am the Thief and I have made NPC Ed vulnerable  |
| 1           | NPC Bob | Judge       | broadcast | I (NPC Dan) am the Reporter and NPC Ed is the Prophet       |
| 1           | NPC Bob | Judge       | broadcast | I (NPC Fae) am the Thief and I have made NPC Ed vulnerable  |
| 1           | NPC Cal | Spy         | broadcast | I (NPC Dan) am the Reporter and NPC Ed is the Prophet       |
| 1           | NPC Cal | Spy         | broadcast | I (NPC Fae) am the Thief and I have made NPC Ed vulnerable  |
| 1           | NPC Cal | Spy         | reveal    | NPC Bob is targeting NPC Dan                                |
| 1           | NPC Cal | Spy         | reveal    | NPC Fae is targeting NPC Ed                                 |
| 1           | NPC Cal | Spy         | reveal    | NPC Dan is targeting NPC Ed                                 |
| 1           | NPC Dan | Reporter    | broadcast | I (NPC Dan) am the Reporter and NPC Ed is the Prophet       |
| 1           | NPC Dan | Reporter    | broadcast | I (NPC Fae) am the Thief and I have made NPC Ed vulnerable  |
| 1           | NPC Dan | Reporter    | reveal    | NPC Ed is Prophet                                           |
| 1           | NPC Ed  | Prophet     | broadcast | I (NPC Dan) am the Reporter and NPC Ed is the Prophet       |
| 1           | NPC Ed  | Prophet     | broadcast | I (NPC Fae) am the Thief and I have made NPC Ed vulnerable  |
| 1           | NPC Fae | Thief       | broadcast | I (NPC Dan) am the Reporter and NPC Ed is the Prophet       |
| 1           | NPC Fae | Thief       | broadcast | I (NPC Fae) am the Thief and I have made NPC Ed vulnerable  |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Bob | Judge   | Reporter |          | successful  |
| 2           | NPC Cal | Spy     |          |          | successful  |
| 2           | NPC Ed  | Prophet | NPC Cal  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Prophet     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal   |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan  |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed   |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ed   |
| 2           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal   |
| 2           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan  |
| 2           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed   |
| 2           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ed   |
| 2           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal   |
| 2           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan  |
| 2           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed   |
| 2           | NPC Cal | Spy         | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ed   |
| 2           | NPC Cal | Spy         | reveal    | NPC Ed is targeting NPC Cal                              |
| 2           | NPC Cal | Spy         | reveal    | NPC Bob is targeting NPC Dan                             |
| 2           | NPC Cal | Spy         | reveal    | NPC Fae is targeting NPC Ed                              |
| 2           | NPC Cal | Spy         | reveal    | NPC Dan is targeting NPC Ed                              |
| 2           | NPC Dan | Reporter    | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal   |
| 2           | NPC Dan | Reporter    | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan  |
| 2           | NPC Dan | Reporter    | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed   |
| 2           | NPC Dan | Reporter    | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ed   |
| 2           | NPC Ed  | Prophet     | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal   |
| 2           | NPC Ed  | Prophet     | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan  |
| 2           | NPC Ed  | Prophet     | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed   |
| 2           | NPC Ed  | Prophet     | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ed   |
| 2           | NPC Fae | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal   |
| 2           | NPC Fae | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan  |
| 2           | NPC Fae | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed   |
| 2           | NPC Fae | Thief       | broadcast | I (NPC Cal) am the Spy and NPC Dan is targeting NPC Ed   |