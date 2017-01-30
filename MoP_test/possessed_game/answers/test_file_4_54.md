#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 54   | 4       | 6       |

#### Roles
| Role       |
| :--------- |
| Trader     |
| Psychic    |
| Medic      |
| Inspector  |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Trader    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Medic     | role change | Your Role is Medic      |
| 0           | NPC Ann | Medic     | possessed   | You are Not Possessed   |
| 0           | NPC Bob | Trader    | role change | Your Role is Trader     |
| 0           | NPC Bob | Trader    | possessed   | You are Possessed       |
| 0           | NPC Cal | Psychic   | role change | Your Role is Psychic    |
| 0           | NPC Cal | Psychic   | possessed   | You are Not Possessed   |
| 0           | NPC Dan | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Dan | Inspector | possessed   | You are Not Possessed   |