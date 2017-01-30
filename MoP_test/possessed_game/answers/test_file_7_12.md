#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 12   | 7       | 9       |

#### Roles
| Role       |
| :--------- |
| Judge      |
| Inspector  |
| Thief      |
| Trader     |
| Psychic    |
| Reporter   |
| Medic      |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Thief     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Trader    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Psychic   | role change | Your Role is Psychic    |
| 0           | NPC Ann | Psychic   | possessed   | You are Not Possessed   |
| 0           | NPC Bob | Judge     | role change | Your Role is Judge      |
| 0           | NPC Bob | Judge     | possessed   | You are Not Possessed   |
| 0           | NPC Cal | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Cal | Reporter  | possessed   | You are Not Possessed   |
| 0           | NPC Dan | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Dan | Inspector | possessed   | You are Not Possessed   |
| 0           | NPC Ed  | Trader    | role change | Your Role is Trader     |
| 0           | NPC Ed  | Trader    | possessed   | You are Not Possessed   |
| 0           | NPC Fae | Medic     | role change | Your Role is Medic      |
| 0           | NPC Fae | Medic     | possessed   | You are Not Possessed   |
| 0           | NPC Gia | Thief     | role change | Your Role is Thief      |
| 0           | NPC Gia | Thief     | possessed   | You are Possessed       |