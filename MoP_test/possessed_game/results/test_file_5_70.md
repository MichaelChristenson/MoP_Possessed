#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 70   | 5       | 3       |

#### Roles
| Role         |
| :----------- |
| Executioner  |
| Jailer       |
| Trader       |
| Demagog      |
| Priest       |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Demagog     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Ann | Demagog     | possessed   | You are Possessed         |
| 0           | NPC Bob | Trader      | role change | Your Role is Trader       |
| 0           | NPC Bob | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Cal | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Priest      | role change | Your Role is Priest       |
| 0           | NPC Dan | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Ed  | Jailer      | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action  | Target 1    | Target 2 | status                         |
| :-----------| :-------| :-------| :-----------| :--------| :----------------------------- |
| 1           | NPC Ann | Demagog | Executioner |          | voting in progress             |
| 1           | NPC Bob | Trader  | NPC Ed      | NPC Dan  | failed because not vulnerable  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Ann | Demagog     | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message | details                                                  |
| :-----------| :-------| :-----------| :-------| :------------------------------------------------------- |
| 1           | NPC Ann | Demagog     | vote    | Demagog has initiated a vote on eliminating Executioner  |
| 1           | NPC Bob | Trader      | vote    | Demagog has initiated a vote on eliminating Executioner  |
| 1           | NPC Cal | Executioner | vote    | Demagog has initiated a vote on eliminating Executioner  |
| 1           | NPC Dan | Priest      | vote    | Demagog has initiated a vote on eliminating Executioner  |
| 1           | NPC Ed  | Jailer      | vote    | Demagog has initiated a vote on eliminating Executioner  |

#### Actions Round 2
| round_index | Player | action | Target 1 | Target 2 | status  |
| :-----------| :------| :------| :--------| :--------| :------ |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Ann | Demagog     | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |

#### Actions Round 3
| round_index | Player  | action  | Target 1 | Target 2 | status              |
| :-----------| :-------| :-------| :--------| :--------| :------------------ |
| 3           | NPC Ann | Demagog | Trader   |          | voting in progress  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann | Demagog     | False      | True      | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message | details                                             |
| :-----------| :-------| :-----------| :-------| :-------------------------------------------------- |
| 3           | NPC Ann | Demagog     | vote    | Demagog has initiated a vote on eliminating Trader  |
| 3           | NPC Bob | Trader      | vote    | Demagog has initiated a vote on eliminating Trader  |
| 3           | NPC Cal | Executioner | vote    | Demagog has initiated a vote on eliminating Trader  |
| 3           | NPC Dan | Priest      | vote    | Demagog has initiated a vote on eliminating Trader  |
| 3           | NPC Ed  | Jailer      | vote    | Demagog has initiated a vote on eliminating Trader  |