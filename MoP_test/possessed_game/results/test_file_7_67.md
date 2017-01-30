#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 67   | 7       | 7       |

#### Roles
| Role         |
| :----------- |
| Medic        |
| Jailer       |
| Executioner  |
| Inspector    |
| Trader       |
| Thief        |
| Spy          |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Executioner | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Trader      | role change | Your Role is Trader       |
| 0           | NPC Ann | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Medic       | role change | Your Role is Medic        |
| 0           | NPC Bob | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Thief       | role change | Your Role is Thief        |
| 0           | NPC Cal | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Dan | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Ed  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Spy         | role change | Your Role is Spy          |
| 0           | NPC Fae | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Gia | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Gia | Executioner | possessed   | You are Possessed         |