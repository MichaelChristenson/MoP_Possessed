#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 9    | 6       | 6       |

#### Roles
| Role       |
| :--------- |
| Thief      |
| Inspector  |
| Judge      |
| Medic      |
| Trader     |
| Reporter   |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Trader    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Thief     | role change | Your Role is Thief      |
| 0           | NPC Ann | Thief     | possessed   | You are Not Possessed   |
| 0           | NPC Bob | Judge     | role change | Your Role is Judge      |
| 0           | NPC Bob | Judge     | possessed   | You are Not Possessed   |
| 0           | NPC Cal | Trader    | role change | Your Role is Trader     |
| 0           | NPC Cal | Trader    | possessed   | You are Possessed       |
| 0           | NPC Dan | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Dan | Reporter  | possessed   | You are Not Possessed   |
| 0           | NPC Ed  | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Ed  | Inspector | possessed   | You are Not Possessed   |
| 0           | NPC Fae | Medic     | role change | Your Role is Medic      |
| 0           | NPC Fae | Medic     | possessed   | You are Not Possessed   |