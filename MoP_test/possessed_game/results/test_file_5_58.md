#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 58   | 5       | 8       |

#### Roles
| Role         |
| :----------- |
| Medic        |
| Prophet      |
| Inspector    |
| Trader       |
| Executioner  |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Trader      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Trader      | role change | Your Role is Trader       |
| 0           | NPC Ann | Trader      | possessed   | You are Possessed         |
| 0           | NPC Bob | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Bob | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Medic       | role change | Your Role is Medic        |
| 0           | NPC Cal | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Dan | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Ed  | Prophet     | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Trader    | NPC Cal  | NPC Bob  | successful  |
| 1           | NPC Bob | Inspector | NPC Dan  |          | successful  |
| 1           | NPC Cal | Medic     | NPC Bob  |          | successful  |
| 1           | NPC Ed  | Prophet   | NPC Ann  |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Trader      | False      | True      | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                   |
| :-----------| :-------| :-----------| :---------| :-------------------------------------------------------- |
| 1           | NPC Ann | Trader      | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |
| 1           | NPC Bob | Medic       | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |
| 1           | NPC Bob | Medic       | reveal    | Executioner is Innocent                                   |
| 1           | NPC Cal | Inspector   | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |
| 1           | NPC Dan | Executioner | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |
| 1           | NPC Ed  | Prophet     | broadcast | I (NPC Bob) inspected NPC Dan and they are not possessed  |

#### Actions Round 2
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 2           | NPC Bob | Medic     | NPC Ann  |          | successful  |
| 2           | NPC Cal | Inspector | NPC Dan  |          | successful  |
| 2           | NPC Ed  | Prophet   | NPC Cal  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Ed  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Trader      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                   |
| :-----------| :-------| :-----------| :---------| :-------------------------------------------------------- |
| 2           | NPC Ann | Trader      | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| 2           | NPC Bob | Medic       | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| 2           | NPC Cal | Inspector   | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| 2           | NPC Cal | Inspector   | reveal    | Executioner is Innocent                                   |
| 2           | NPC Dan | Executioner | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |
| 2           | NPC Ed  | Prophet     | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed  |

#### Actions Round 3
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 3           | NPC Ann | Trader  | NPC Ed   | NPC Cal  | successful  |
| 3           | NPC Bob | Medic   | NPC Dan  |          | successful  |
| 3           | NPC Ed  | Prophet | NPC Ann  |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Trader      | False      | True      | False      | 4         | True   | 0              | 0                  |
| 3           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |