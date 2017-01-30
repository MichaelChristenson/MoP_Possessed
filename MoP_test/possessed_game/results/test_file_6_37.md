#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 37   | 6       | 9       |

#### Roles
| Role         |
| :----------- |
| Executioner  |
| Jailer       |
| Demagog      |
| Judge        |
| Assassin     |
| Medic        |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Assassin    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ann | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Bob | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Cal | Assassin    | possessed   | You are Possessed         |
| 0           | NPC Dan | Medic       | role change | Your Role is Medic        |
| 0           | NPC Dan | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Ed  | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Judge       | role change | Your Role is Judge        |
| 0           | NPC Fae | Judge       | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 1           | NPC Bob | Demagog  | Assassin |          | voting in progress  |
| 1           | NPC Cal | Assassin | Jailer   |          | successful          |
| 1           | NPC Dan | Medic    | NPC Ed   |          | successful          |
| 1           | NPC Fae | Judge    | Medic    |          | successful          |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Fae | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Assassin    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message | details                                               |
| :-----------| :-------| :-----------| :-------| :---------------------------------------------------- |
| 1           | NPC Ann | Executioner | vote    | Demagog has initiated a vote on eliminating Assassin  |
| 1           | NPC Bob | Demagog     | vote    | Demagog has initiated a vote on eliminating Assassin  |
| 1           | NPC Cal | Assassin    | vote    | Demagog has initiated a vote on eliminating Assassin  |
| 1           | NPC Dan | Medic       | vote    | Demagog has initiated a vote on eliminating Assassin  |
| 1           | NPC Ed  | Jailer      | vote    | Demagog has initiated a vote on eliminating Assassin  |
| 1           | NPC Fae | Judge       | vote    | Demagog has initiated a vote on eliminating Assassin  |

#### Actions Round 2
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 2           | NPC Dan | Medic  | NPC Bob  |          | successful  |
| 2           | NPC Fae | Judge  | Demagog  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Assassin    | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 3           | NPC Bob | Demagog  | Medic    |          | voting in progress  |
| 3           | NPC Cal | Assassin | Judge    |          | successful          |
| 3           | NPC Dan | Medic    | NPC Fae  |          | successful          |
| 3           | NPC Fae | Judge    | Demagog  |          | successful          |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Fae | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Assassin    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message | details                                            |
| :-----------| :-------| :-----------| :-------| :------------------------------------------------- |
| 3           | NPC Ann | Executioner | vote    | Demagog has initiated a vote on eliminating Medic  |
| 3           | NPC Bob | Demagog     | vote    | Demagog has initiated a vote on eliminating Medic  |
| 3           | NPC Cal | Assassin    | vote    | Demagog has initiated a vote on eliminating Medic  |
| 3           | NPC Dan | Medic       | vote    | Demagog has initiated a vote on eliminating Medic  |
| 3           | NPC Ed  | Jailer      | vote    | Demagog has initiated a vote on eliminating Medic  |
| 3           | NPC Fae | Judge       | vote    | Demagog has initiated a vote on eliminating Medic  |

#### Actions Round 4
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 4           | NPC Dan | Medic  | NPC Cal  |          | successful  |
| 4           | NPC Fae | Judge  | Assassin |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Fae | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Assassin    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |

#### Actions Round 5
| round_index | Player  | action   | Target 1    | Target 2 | status              |
| :-----------| :-------| :--------| :-----------| :--------| :------------------ |
| 5           | NPC Bob | Demagog  | Assassin    |          | voting in progress  |
| 5           | NPC Cal | Assassin | Executioner |          | successful          |
| 5           | NPC Dan | Medic    | NPC Ann     |          | successful          |
| 5           | NPC Fae | Judge    | Assassin    |          | successful          |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Fae | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Cal | Assassin    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message | details                                               |
| :-----------| :-------| :-----------| :-------| :---------------------------------------------------- |
| 5           | NPC Ann | Executioner | vote    | Demagog has initiated a vote on eliminating Assassin  |
| 5           | NPC Bob | Demagog     | vote    | Demagog has initiated a vote on eliminating Assassin  |
| 5           | NPC Cal | Assassin    | vote    | Demagog has initiated a vote on eliminating Assassin  |
| 5           | NPC Dan | Medic       | vote    | Demagog has initiated a vote on eliminating Assassin  |
| 5           | NPC Ed  | Jailer      | vote    | Demagog has initiated a vote on eliminating Assassin  |
| 5           | NPC Fae | Judge       | vote    | Demagog has initiated a vote on eliminating Assassin  |

#### Actions Round 6
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 6           | NPC Dan | Medic  | NPC Ed   |          | successful  |
| 6           | NPC Fae | Judge  | Medic    |          | successful  |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Fae | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Assassin    | False      | True      | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |

#### Actions Round 7
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 7           | NPC Bob | Demagog  | Jailer   |          | voting in progress  |
| 7           | NPC Cal | Assassin | Medic    |          | successful          |
| 7           | NPC Dan | Medic    | NPC Bob  |          | successful          |
| 7           | NPC Fae | Judge    | Assassin |          | successful          |

#### States Round 7
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Bob | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Fae | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Cal | Assassin    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role        | message | details                                             |
| :-----------| :-------| :-----------| :-------| :-------------------------------------------------- |
| 7           | NPC Ann | Executioner | vote    | Demagog has initiated a vote on eliminating Jailer  |
| 7           | NPC Bob | Demagog     | vote    | Demagog has initiated a vote on eliminating Jailer  |
| 7           | NPC Cal | Assassin    | vote    | Demagog has initiated a vote on eliminating Jailer  |
| 7           | NPC Dan | Medic       | vote    | Demagog has initiated a vote on eliminating Jailer  |
| 7           | NPC Ed  | Jailer      | vote    | Demagog has initiated a vote on eliminating Jailer  |
| 7           | NPC Fae | Judge       | vote    | Demagog has initiated a vote on eliminating Jailer  |

#### Actions Round 8
| round_index | Player  | action  | Target 1 | Target 2 | status              |
| :-----------| :-------| :-------| :--------| :--------| :------------------ |
| 8           | NPC Bob | Demagog | Medic    |          | voting in progress  |
| 8           | NPC Dan | Medic   | NPC Fae  |          | successful          |
| 8           | NPC Fae | Judge   | Demagog  |          | successful          |

#### States Round 8
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Bob | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 8           | NPC Fae | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Cal | Assassin    | False      | True      | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player  | Role        | message | details                                            |
| :-----------| :-------| :-----------| :-------| :------------------------------------------------- |
| 8           | NPC Ann | Executioner | vote    | Demagog has initiated a vote on eliminating Medic  |
| 8           | NPC Bob | Demagog     | vote    | Demagog has initiated a vote on eliminating Medic  |
| 8           | NPC Cal | Assassin    | vote    | Demagog has initiated a vote on eliminating Medic  |
| 8           | NPC Dan | Medic       | vote    | Demagog has initiated a vote on eliminating Medic  |
| 8           | NPC Ed  | Jailer      | vote    | Demagog has initiated a vote on eliminating Medic  |
| 8           | NPC Fae | Judge       | vote    | Demagog has initiated a vote on eliminating Medic  |

#### Actions Round 9
| round_index | Player  | action   | Target 1    | Target 2 | status      |
| :-----------| :-------| :--------| :-----------| :--------| :---------- |
| 9           | NPC Cal | Assassin | Executioner |          | successful  |
| 9           | NPC Dan | Medic    | NPC Cal     |          | successful  |
| 9           | NPC Fae | Judge    | Medic       |          | successful  |

#### States Round 9
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 9           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Bob | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 9           | NPC Fae | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Cal | Assassin    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 9
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |