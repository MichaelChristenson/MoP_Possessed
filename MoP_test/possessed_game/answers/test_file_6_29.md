#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 29   | 6       | 8       |

#### Roles
| Role      |
| :-------- |
| Trader    |
| Thief     |
| Judge     |
| Medic     |
| Reporter  |
| Psychic   |

#### States Round 0
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Trader   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Thief    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Reporter | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Psychic  | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role     | message     | details                |
| :-----------| :-------| :--------| :-----------| :--------------------- |
| 0           | NPC Ann | Trader   | role change | Your Role is Trader    |
| 0           | NPC Ann | Trader   | possessed   | You are Not Possessed  |
| 0           | NPC Bob | Judge    | role change | Your Role is Judge     |
| 0           | NPC Bob | Judge    | possessed   | You are Not Possessed  |
| 0           | NPC Cal | Reporter | role change | Your Role is Reporter  |
| 0           | NPC Cal | Reporter | possessed   | You are Possessed      |
| 0           | NPC Dan | Psychic  | role change | Your Role is Psychic   |
| 0           | NPC Dan | Psychic  | possessed   | You are Not Possessed  |
| 0           | NPC Ed  | Thief    | role change | Your Role is Thief     |
| 0           | NPC Ed  | Thief    | possessed   | You are Not Possessed  |
| 0           | NPC Fae | Medic    | role change | Your Role is Medic     |
| 0           | NPC Fae | Medic    | possessed   | You are Not Possessed  |