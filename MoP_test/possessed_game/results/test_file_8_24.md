#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 24   | 8       | 9       |

#### Roles
| Role         |
| :----------- |
| Reporter     |
| Executioner  |
| Medic        |
| Judge        |
| Trader       |
| Prophet      |
| Spy          |
| Demagog      |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Fae | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Executioner | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ann | Executioner | possessed   | You are Possessed         |
| 0           | NPC Bob | Spy         | role change | Your Role is Spy          |
| 0           | NPC Bob | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Medic       | role change | Your Role is Medic        |
| 0           | NPC Cal | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Dan | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Trader      | role change | Your Role is Trader       |
| 0           | NPC Ed  | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Fae | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Gia | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Gia | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Han | Judge       | role change | Your Role is Judge        |
| 0           | NPC Han | Judge       | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action      | Target 1 | Target 2 | status                        |
| :-----------| :-------| :-----------| :--------| :--------| :---------------------------- |
| 1           | NPC Ann | Executioner | NPC Ed   |          | failed because of no support  |
| 1           | NPC Bob | Spy         |          |          | successful                    |
| 1           | NPC Cal | Medic       | NPC Ann  |          | successful                    |
| 1           | NPC Dan | Demagog     | Judge    |          | voting in progress            |
| 1           | NPC Ed  | Trader      | NPC Han  | NPC Ann  | successful                    |
| 1           | NPC Fae | Reporter    | NPC Bob  |          | successful                    |
| 1           | NPC Gia | Prophet     | NPC Fae  |          | successful                    |
| 1           | NPC Han | Judge       | Medic    |          | successful                    |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Fae | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Gia | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message       | details                                             |
| :-----------| :-------| :-----------| :-------------| :-------------------------------------------------- |
| 1           | NPC Ann | Judge       | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Spy  |
| 1           | NPC Ann | Judge       | action failed |                                                     |
| 1           | NPC Ann | Judge       | vote          | Demagog has initiated a vote on eliminating Judge   |
| 1           | NPC Bob | Spy         | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Spy  |
| 1           | NPC Bob | Spy         | reveal        | NPC Fae is targeting NPC Bob                        |
| 1           | NPC Bob | Spy         | reveal        | NPC Ann is targeting NPC Ed                         |
| 1           | NPC Bob | Spy         | reveal        | NPC Han is targeting NPC Cal                        |
| 1           | NPC Bob | Spy         | vote          | Demagog has initiated a vote on eliminating Judge   |
| 1           | NPC Cal | Medic       | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Spy  |
| 1           | NPC Cal | Medic       | vote          | Demagog has initiated a vote on eliminating Judge   |
| 1           | NPC Dan | Demagog     | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Spy  |
| 1           | NPC Dan | Demagog     | vote          | Demagog has initiated a vote on eliminating Judge   |
| 1           | NPC Ed  | Trader      | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Spy  |
| 1           | NPC Ed  | Trader      | vote          | Demagog has initiated a vote on eliminating Judge   |
| 1           | NPC Fae | Reporter    | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Spy  |
| 1           | NPC Fae | Reporter    | reveal        | NPC Bob is Spy                                      |
| 1           | NPC Fae | Reporter    | vote          | Demagog has initiated a vote on eliminating Judge   |
| 1           | NPC Gia | Prophet     | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Spy  |
| 1           | NPC Gia | Prophet     | vote          | Demagog has initiated a vote on eliminating Judge   |
| 1           | NPC Han | Executioner | broadcast     | I (NPC Fae) am the Reporter and NPC Bob is the Spy  |
| 1           | NPC Han | Executioner | vote          | Demagog has initiated a vote on eliminating Judge   |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Ann | Judge   | Reporter |          | successful  |
| 2           | NPC Bob | Spy     |          |          | successful  |
| 2           | NPC Cal | Medic   | NPC Han  |          | successful  |
| 2           | NPC Gia | Prophet | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Fae | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Gia | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 2           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 2           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 2           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 2           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 2           | NPC Bob | Spy         | reveal    | NPC Fae is targeting NPC Bob                             |
| 2           | NPC Bob | Spy         | reveal    | NPC Ann is targeting NPC Fae                             |
| 2           | NPC Bob | Spy         | reveal    | NPC Cal is targeting NPC Ann                             |
| 2           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Han                              |
| 2           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Han                              |
| 2           | NPC Bob | Spy         | reveal    | NPC Gia is targeting NPC Fae                             |
| 2           | NPC Bob | Spy         | reveal    | NPC Dan is targeting NPC Ann                             |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 2           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 2           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 2           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 2           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 2           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 2           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 2           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 2           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 2           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 2           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 2           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 2           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 2           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 3           | NPC Ann | Judge    | Trader   |          | successful          |
| 3           | NPC Bob | Spy      |          |          | successful          |
| 3           | NPC Cal | Medic    | NPC Ed   |          | successful          |
| 3           | NPC Dan | Demagog  | Spy      |          | voting in progress  |
| 3           | NPC Fae | Reporter | NPC Han  |          | successful          |
| 3           | NPC Gia | Prophet  | NPC Fae  |          | successful          |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Fae | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Han | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Gia | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae  |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Han  |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ann  |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 3           | NPC Ann | Judge       | vote      | Demagog has initiated a vote on eliminating Spy          |
| 3           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 3           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae  |
| 3           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Han  |
| 3           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ann  |
| 3           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 3           | NPC Bob | Spy         | reveal    | NPC Fae is targeting NPC Han                             |
| 3           | NPC Bob | Spy         | reveal    | NPC Ann is targeting NPC Ed                              |
| 3           | NPC Bob | Spy         | reveal    | NPC Cal is targeting NPC Han                             |
| 3           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Han                              |
| 3           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Han                              |
| 3           | NPC Bob | Spy         | reveal    | NPC Gia is targeting NPC Ann                             |
| 3           | NPC Bob | Spy         | reveal    | NPC Dan is targeting NPC Ann                             |
| 3           | NPC Bob | Spy         | vote      | Demagog has initiated a vote on eliminating Spy          |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae  |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Han  |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ann  |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 3           | NPC Cal | Medic       | vote      | Demagog has initiated a vote on eliminating Spy          |
| 3           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 3           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae  |
| 3           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Han  |
| 3           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ann  |
| 3           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 3           | NPC Dan | Demagog     | vote      | Demagog has initiated a vote on eliminating Spy          |
| 3           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 3           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae  |
| 3           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Han  |
| 3           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ann  |
| 3           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 3           | NPC Ed  | Trader      | vote      | Demagog has initiated a vote on eliminating Spy          |
| 3           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 3           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae  |
| 3           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Han  |
| 3           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ann  |
| 3           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 3           | NPC Fae | Reporter    | reveal    | NPC Han is Executioner                                   |
| 3           | NPC Fae | Reporter    | vote      | Demagog has initiated a vote on eliminating Spy          |
| 3           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 3           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae  |
| 3           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Han  |
| 3           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ann  |
| 3           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 3           | NPC Gia | Prophet     | vote      | Demagog has initiated a vote on eliminating Spy          |
| 3           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Bob  |
| 3           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Fae  |
| 3           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Han  |
| 3           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 3           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ann  |
| 3           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 3           | NPC Han | Executioner | vote      | Demagog has initiated a vote on eliminating Spy          |

#### Actions Round 4
| round_index | Player  | action  | Target 1 | Target 2 | status                         |
| :-----------| :-------| :-------| :--------| :--------| :----------------------------- |
| 4           | NPC Ann | Judge   | Medic    |          | successful                     |
| 4           | NPC Bob | Spy     |          |          | successful                     |
| 4           | NPC Cal | Medic   | NPC Gia  |          | successful                     |
| 4           | NPC Ed  | Trader  | NPC Dan  | NPC Fae  | failed because not vulnerable  |
| 4           | NPC Gia | Prophet | NPC Ed   |          | successful                     |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Fae | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Han | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 4           | NPC Gia | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 4           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 4           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 4           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Bob | Spy         | reveal    | NPC Fae is targeting NPC Han                             |
| 4           | NPC Bob | Spy         | reveal    | NPC Ann is targeting NPC Cal                             |
| 4           | NPC Bob | Spy         | reveal    | NPC Cal is targeting NPC Ed                              |
| 4           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Han                              |
| 4           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Han                              |
| 4           | NPC Bob | Spy         | reveal    | NPC Gia is targeting NPC Fae                             |
| 4           | NPC Bob | Spy         | reveal    | NPC Dan is targeting NPC Bob                             |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 4           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 4           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 4           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 4           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 4           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 4           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 4           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 4           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 4           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 4           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 4           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 4           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 4           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 4           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 4           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 4           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ed   |
| 4           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 4           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 4           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |

#### Actions Round 5
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 5           | NPC Ann | Judge    | Trader   |          | successful          |
| 5           | NPC Bob | Spy      |          |          | successful          |
| 5           | NPC Cal | Medic    | NPC Bob  |          | successful          |
| 5           | NPC Dan | Demagog  | Trader   |          | voting in progress  |
| 5           | NPC Fae | Reporter | NPC Cal  |          | successful          |
| 5           | NPC Gia | Prophet  | NPC Ed   |          | successful          |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Fae | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Han | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 5           | NPC Gia | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Cal  |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia  |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 5           | NPC Ann | Judge       | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic     |
| 5           | NPC Ann | Judge       | vote      | Demagog has initiated a vote on eliminating Trader       |
| 5           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 5           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Cal  |
| 5           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia  |
| 5           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 5           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 5           | NPC Bob | Spy         | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic     |
| 5           | NPC Bob | Spy         | reveal    | NPC Fae is targeting NPC Cal                             |
| 5           | NPC Bob | Spy         | reveal    | NPC Ann is targeting NPC Ed                              |
| 5           | NPC Bob | Spy         | reveal    | NPC Cal is targeting NPC Gia                             |
| 5           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Dan                              |
| 5           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Dan                              |
| 5           | NPC Bob | Spy         | reveal    | NPC Gia is targeting NPC Ed                              |
| 5           | NPC Bob | Spy         | reveal    | NPC Dan is targeting NPC Bob                             |
| 5           | NPC Bob | Spy         | vote      | Demagog has initiated a vote on eliminating Trader       |
| 5           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 5           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Cal  |
| 5           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia  |
| 5           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 5           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 5           | NPC Cal | Medic       | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic     |
| 5           | NPC Cal | Medic       | vote      | Demagog has initiated a vote on eliminating Trader       |
| 5           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 5           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Cal  |
| 5           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia  |
| 5           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 5           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 5           | NPC Dan | Demagog     | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic     |
| 5           | NPC Dan | Demagog     | vote      | Demagog has initiated a vote on eliminating Trader       |
| 5           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 5           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Cal  |
| 5           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia  |
| 5           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 5           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 5           | NPC Ed  | Trader      | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic     |
| 5           | NPC Ed  | Trader      | vote      | Demagog has initiated a vote on eliminating Trader       |
| 5           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 5           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Cal  |
| 5           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia  |
| 5           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 5           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 5           | NPC Fae | Reporter    | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic     |
| 5           | NPC Fae | Reporter    | reveal    | NPC Cal is Medic                                         |
| 5           | NPC Fae | Reporter    | vote      | Demagog has initiated a vote on eliminating Trader       |
| 5           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 5           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Cal  |
| 5           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia  |
| 5           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 5           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 5           | NPC Gia | Prophet     | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic     |
| 5           | NPC Gia | Prophet     | vote      | Demagog has initiated a vote on eliminating Trader       |
| 5           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Han  |
| 5           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Cal  |
| 5           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Gia  |
| 5           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 5           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 5           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Bob  |
| 5           | NPC Han | Executioner | broadcast | I (NPC Fae) am the Reporter and NPC Cal is the Medic     |
| 5           | NPC Han | Executioner | vote      | Demagog has initiated a vote on eliminating Trader       |

#### Actions Round 6
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 6           | NPC Ann | Judge   | Trader   |          | successful  |
| 6           | NPC Bob | Spy     |          |          | successful  |
| 6           | NPC Cal | Medic   | NPC Dan  |          | successful  |
| 6           | NPC Gia | Prophet | NPC Ed   |          | successful  |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Fae | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Han | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ed  | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Gia | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 6           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 6           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 6           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Bob  |
| 6           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 6           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 6           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 6           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 6           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Bob  |
| 6           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 6           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 6           | NPC Bob | Spy         | reveal    | NPC Fae is targeting NPC Cal                             |
| 6           | NPC Bob | Spy         | reveal    | NPC Ann is targeting NPC Ed                              |
| 6           | NPC Bob | Spy         | reveal    | NPC Cal is targeting NPC Bob                             |
| 6           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Dan                              |
| 6           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Dan                              |
| 6           | NPC Bob | Spy         | reveal    | NPC Gia is targeting NPC Ed                              |
| 6           | NPC Bob | Spy         | reveal    | NPC Dan is targeting NPC Ed                              |
| 6           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 6           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 6           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Bob  |
| 6           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 6           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 6           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 6           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 6           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Bob  |
| 6           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 6           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 6           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 6           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 6           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Bob  |
| 6           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 6           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 6           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 6           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 6           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Bob  |
| 6           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 6           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 6           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 6           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 6           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Bob  |
| 6           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 6           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 6           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 6           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 6           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Bob  |
| 6           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 6           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 6           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |

#### Actions Round 7
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 7           | NPC Ann | Judge    | Demagog  |          | successful          |
| 7           | NPC Bob | Spy      |          |          | successful          |
| 7           | NPC Cal | Medic    | NPC Fae  |          | successful          |
| 7           | NPC Dan | Demagog  | Trader   |          | voting in progress  |
| 7           | NPC Fae | Reporter | NPC Ann  |          | successful          |
| 7           | NPC Gia | Prophet  | NPC Fae  |          | successful          |

#### States Round 7
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Fae | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Ann | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Han | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Ed  | Trader      | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Gia | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Bob | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Dan | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 7           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 7           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 7           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan  |
| 7           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 7           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 7           | NPC Ann | Judge       | vote      | Demagog has initiated a vote on eliminating Trader       |
| 7           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 7           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 7           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan  |
| 7           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 7           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 7           | NPC Bob | Spy         | reveal    | NPC Fae is targeting NPC Ann                             |
| 7           | NPC Bob | Spy         | reveal    | NPC Ann is targeting NPC Dan                             |
| 7           | NPC Bob | Spy         | reveal    | NPC Cal is targeting NPC Dan                             |
| 7           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Dan                              |
| 7           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Dan                              |
| 7           | NPC Bob | Spy         | reveal    | NPC Gia is targeting NPC Ed                              |
| 7           | NPC Bob | Spy         | reveal    | NPC Dan is targeting NPC Ed                              |
| 7           | NPC Bob | Spy         | vote      | Demagog has initiated a vote on eliminating Trader       |
| 7           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 7           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 7           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan  |
| 7           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 7           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 7           | NPC Cal | Medic       | vote      | Demagog has initiated a vote on eliminating Trader       |
| 7           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 7           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 7           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan  |
| 7           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 7           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 7           | NPC Dan | Demagog     | vote      | Demagog has initiated a vote on eliminating Trader       |
| 7           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 7           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 7           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan  |
| 7           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 7           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 7           | NPC Ed  | Trader      | vote      | Demagog has initiated a vote on eliminating Trader       |
| 7           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 7           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 7           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan  |
| 7           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 7           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 7           | NPC Fae | Reporter    | reveal    | NPC Ann is Judge                                         |
| 7           | NPC Fae | Reporter    | vote      | Demagog has initiated a vote on eliminating Trader       |
| 7           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 7           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 7           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan  |
| 7           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 7           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 7           | NPC Gia | Prophet     | vote      | Demagog has initiated a vote on eliminating Trader       |
| 7           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Cal  |
| 7           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Ed   |
| 7           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan  |
| 7           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 7           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 7           | NPC Han | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 7           | NPC Han | Executioner | vote      | Demagog has initiated a vote on eliminating Trader       |

#### Actions Round 8
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 8           | NPC Ann | Judge    | Demagog  |          | successful  |
| 8           | NPC Bob | Spy      |          |          | successful  |
| 8           | NPC Cal | Medic    | NPC Ann  |          | successful  |
| 8           | NPC Ed  | Trader   | NPC Han  | NPC Ann  | successful  |
| 8           | NPC Fae | Reporter | NPC Dan  |          | successful  |
| 8           | NPC Gia | Prophet  | NPC Ed   |          | successful  |

#### States Round 8
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Fae | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 8           | NPC Ann | Executioner | False      | True      | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Han | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Ed  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 8           | NPC Gia | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Bob | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Dan | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 8           | NPC Ann | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann  |
| 8           | NPC Ann | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan  |
| 8           | NPC Ann | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Fae  |
| 8           | NPC Ann | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Ann | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Ann | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 8           | NPC Ann | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 8           | NPC Ann | Executioner | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Demagog   |
| 8           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann  |
| 8           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan  |
| 8           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Fae  |
| 8           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 8           | NPC Bob | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 8           | NPC Bob | Spy         | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Demagog   |
| 8           | NPC Bob | Spy         | reveal    | NPC Fae is targeting NPC Dan                             |
| 8           | NPC Bob | Spy         | reveal    | NPC Ann is targeting NPC Dan                             |
| 8           | NPC Bob | Spy         | reveal    | NPC Cal is targeting NPC Fae                             |
| 8           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Dan                              |
| 8           | NPC Bob | Spy         | reveal    | NPC Ed is targeting NPC Dan                              |
| 8           | NPC Bob | Spy         | reveal    | NPC Gia is targeting NPC Fae                             |
| 8           | NPC Bob | Spy         | reveal    | NPC Dan is targeting NPC Ed                              |
| 8           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann  |
| 8           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan  |
| 8           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Fae  |
| 8           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 8           | NPC Cal | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 8           | NPC Cal | Medic       | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Demagog   |
| 8           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann  |
| 8           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan  |
| 8           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Fae  |
| 8           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 8           | NPC Dan | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 8           | NPC Dan | Demagog     | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Demagog   |
| 8           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann  |
| 8           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan  |
| 8           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Fae  |
| 8           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 8           | NPC Ed  | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 8           | NPC Ed  | Trader      | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Demagog   |
| 8           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann  |
| 8           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan  |
| 8           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Fae  |
| 8           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 8           | NPC Fae | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 8           | NPC Fae | Reporter    | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Demagog   |
| 8           | NPC Fae | Reporter    | reveal    | NPC Dan is Demagog                                       |
| 8           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann  |
| 8           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan  |
| 8           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Fae  |
| 8           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 8           | NPC Gia | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 8           | NPC Gia | Prophet     | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Demagog   |
| 8           | NPC Han | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ann  |
| 8           | NPC Han | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ann is targeting NPC Dan  |
| 8           | NPC Han | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Fae  |
| 8           | NPC Han | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Han | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Dan   |
| 8           | NPC Han | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Fae  |
| 8           | NPC Han | Judge       | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 8           | NPC Han | Judge       | broadcast | I (NPC Fae) am the Reporter and NPC Dan is the Demagog   |

#### Actions Round 9
| round_index | Player  | action      | Target 1 | Target 2 | status                        |
| :-----------| :-------| :-----------| :--------| :--------| :---------------------------- |
| 9           | NPC Ann | Executioner | NPC Bob  |          | failed because of no support  |
| 9           | NPC Bob | Spy         |          |          | successful                    |
| 9           | NPC Cal | Medic       | NPC Han  |          | successful                    |
| 9           | NPC Dan | Demagog     | Spy      |          | voting in progress            |
| 9           | NPC Gia | Prophet     | NPC Ann  |          | successful                    |
| 9           | NPC Han | Judge       | Trader   |          | successful                    |

#### States Round 9
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 9           | NPC Fae | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 9           | NPC Ann | Executioner | False      | True      | False      | 4         | True   | 0              | 0                  |
| 9           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Han | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Ed  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 9           | NPC Gia | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Bob | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Dan | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 9
| round_index | Player  | Role        | message       | details                                                  |
| :-----------| :-------| :-----------| :-------------| :------------------------------------------------------- |
| 9           | NPC Ann | Executioner | broadcast     | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Dan  |
| 9           | NPC Ann | Executioner | broadcast     | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 9           | NPC Ann | Executioner | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Ann | Executioner | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Ann | Executioner | broadcast     | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 9           | NPC Ann | Executioner | broadcast     | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 9           | NPC Ann | Executioner | action failed |                                                          |
| 9           | NPC Ann | Executioner | vote          | Demagog has initiated a vote on eliminating Spy          |
| 9           | NPC Bob | Spy         | broadcast     | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Dan  |
| 9           | NPC Bob | Spy         | broadcast     | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 9           | NPC Bob | Spy         | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Bob | Spy         | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Bob | Spy         | broadcast     | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 9           | NPC Bob | Spy         | broadcast     | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 9           | NPC Bob | Spy         | reveal        | NPC Fae is targeting NPC Dan                             |
| 9           | NPC Bob | Spy         | reveal        | NPC Ann is targeting NPC Bob                             |
| 9           | NPC Bob | Spy         | reveal        | NPC Cal is targeting NPC Ann                             |
| 9           | NPC Bob | Spy         | reveal        | NPC Han is targeting NPC Ed                              |
| 9           | NPC Bob | Spy         | reveal        | NPC Ed is targeting NPC Han                              |
| 9           | NPC Bob | Spy         | reveal        | NPC Ed is targeting NPC Han                              |
| 9           | NPC Bob | Spy         | reveal        | NPC Gia is targeting NPC Ed                              |
| 9           | NPC Bob | Spy         | reveal        | NPC Dan is targeting NPC Ed                              |
| 9           | NPC Bob | Spy         | vote          | Demagog has initiated a vote on eliminating Spy          |
| 9           | NPC Cal | Medic       | broadcast     | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Dan  |
| 9           | NPC Cal | Medic       | broadcast     | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 9           | NPC Cal | Medic       | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Cal | Medic       | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Cal | Medic       | broadcast     | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 9           | NPC Cal | Medic       | broadcast     | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 9           | NPC Cal | Medic       | vote          | Demagog has initiated a vote on eliminating Spy          |
| 9           | NPC Dan | Demagog     | broadcast     | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Dan  |
| 9           | NPC Dan | Demagog     | broadcast     | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 9           | NPC Dan | Demagog     | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Dan | Demagog     | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Dan | Demagog     | broadcast     | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 9           | NPC Dan | Demagog     | broadcast     | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 9           | NPC Dan | Demagog     | vote          | Demagog has initiated a vote on eliminating Spy          |
| 9           | NPC Ed  | Trader      | broadcast     | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Dan  |
| 9           | NPC Ed  | Trader      | broadcast     | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 9           | NPC Ed  | Trader      | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Ed  | Trader      | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Ed  | Trader      | broadcast     | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 9           | NPC Ed  | Trader      | broadcast     | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 9           | NPC Ed  | Trader      | vote          | Demagog has initiated a vote on eliminating Spy          |
| 9           | NPC Fae | Reporter    | broadcast     | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Dan  |
| 9           | NPC Fae | Reporter    | broadcast     | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 9           | NPC Fae | Reporter    | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Fae | Reporter    | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Fae | Reporter    | broadcast     | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 9           | NPC Fae | Reporter    | broadcast     | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 9           | NPC Fae | Reporter    | vote          | Demagog has initiated a vote on eliminating Spy          |
| 9           | NPC Gia | Prophet     | broadcast     | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Dan  |
| 9           | NPC Gia | Prophet     | broadcast     | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 9           | NPC Gia | Prophet     | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Gia | Prophet     | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Gia | Prophet     | broadcast     | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 9           | NPC Gia | Prophet     | broadcast     | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 9           | NPC Gia | Prophet     | vote          | Demagog has initiated a vote on eliminating Spy          |
| 9           | NPC Han | Judge       | broadcast     | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Dan  |
| 9           | NPC Han | Judge       | broadcast     | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 9           | NPC Han | Judge       | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Han | Judge       | broadcast     | I (NPC Bob) am the Spy and NPC Ed is targeting NPC Han   |
| 9           | NPC Han | Judge       | broadcast     | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ed   |
| 9           | NPC Han | Judge       | broadcast     | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ed   |
| 9           | NPC Han | Judge       | vote          | Demagog has initiated a vote on eliminating Spy          |