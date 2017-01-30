#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 24   | 6       | 6       |

#### Roles
| Role         |
| :----------- |
| Silencer     |
| Priest       |
| Demagog      |
| Spy          |
| Executioner  |
| Reporter     |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Executioner | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Ann | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Bob | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Cal | Executioner | possessed   | You are Possessed         |
| 0           | NPC Dan | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Dan | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Priest      | role change | Your Role is Priest       |
| 0           | NPC Ed  | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Spy         | role change | Your Role is Spy          |
| 0           | NPC Fae | Spy         | possessed   | You are Not Possessed     |