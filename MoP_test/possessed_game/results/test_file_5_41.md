#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 41   | 5       | 7       |

#### Roles
| Role      |
| :-------- |
| Medic     |
| Reporter  |
| Thief     |
| Priest    |
| Silencer  |

#### States Round 0
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Reporter | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Thief    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Priest   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Silencer | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role     | message     | details                |
| :-----------| :-------| :--------| :-----------| :--------------------- |
| 0           | NPC Ann | Priest   | role change | Your Role is Priest    |
| 0           | NPC Ann | Priest   | possessed   | You are Possessed      |
| 0           | NPC Bob | Thief    | role change | Your Role is Thief     |
| 0           | NPC Bob | Thief    | possessed   | You are Not Possessed  |
| 0           | NPC Cal | Medic    | role change | Your Role is Medic     |
| 0           | NPC Cal | Medic    | possessed   | You are Not Possessed  |
| 0           | NPC Dan | Silencer | role change | Your Role is Silencer  |
| 0           | NPC Dan | Silencer | possessed   | You are Not Possessed  |
| 0           | NPC Ed  | Reporter | role change | Your Role is Reporter  |
| 0           | NPC Ed  | Reporter | possessed   | You are Not Possessed  |