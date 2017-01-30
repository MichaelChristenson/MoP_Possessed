#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 36   | 6       | 7       |

#### Roles
| Role         |
| :----------- |
| Psychic      |
| Medic        |
| Reporter     |
| Executioner  |
| Judge        |
| Inspector    |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Ann | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Bob | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Judge       | role change | Your Role is Judge        |
| 0           | NPC Cal | Judge       | possessed   | You are Possessed         |
| 0           | NPC Dan | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Dan | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Ed  | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Fae | Executioner | possessed   | You are Not Possessed     |