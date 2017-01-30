#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 16   | 4       | 1       |

#### Roles
| Role      |
| :-------- |
| Thief     |
| Psychic   |
| Reporter  |
| Medic     |

#### States Round 0
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Thief    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Psychic  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Reporter | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role     | message     | details                |
| :-----------| :-------| :--------| :-----------| :--------------------- |
| 0           | NPC Ann | Reporter | role change | Your Role is Reporter  |
| 0           | NPC Ann | Reporter | possessed   | You are Not Possessed  |
| 0           | NPC Bob | Thief    | role change | Your Role is Thief     |
| 0           | NPC Bob | Thief    | possessed   | You are Possessed      |
| 0           | NPC Cal | Psychic  | role change | Your Role is Psychic   |
| 0           | NPC Cal | Psychic  | possessed   | You are Not Possessed  |
| 0           | NPC Dan | Medic    | role change | Your Role is Medic     |
| 0           | NPC Dan | Medic    | possessed   | You are Not Possessed  |

#### Actions Round 1
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 1           | NPC Ann | Reporter | NPC Cal  |          | successful  |
| 1           | NPC Bob | Thief    | NPC Dan  |          | successful  |
| 1           | NPC Cal | Psychic  |          |          | successful  |
| 1           | NPC Dan | Medic    | NPC Cal  |          | successful  |

#### States Round 1
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Thief    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal | Psychic  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Reporter | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Medic    | False      | False     | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 1           | NPC Ann | Reporter | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic        |
| 1           | NPC Ann | Reporter | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable   |
| 1           | NPC Ann | Reporter | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 1           | NPC Ann | Reporter | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Ann | Reporter | reveal    | NPC Cal is Psychic                                            |
| 1           | NPC Bob | Thief    | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic        |
| 1           | NPC Bob | Thief    | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable   |
| 1           | NPC Bob | Thief    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 1           | NPC Bob | Thief    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Cal | Psychic  | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic        |
| 1           | NPC Cal | Psychic  | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable   |
| 1           | NPC Cal | Psychic  | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 1           | NPC Cal | Psychic  | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Cal | Psychic  | reveal    | Player: NPC Dan is not possessed                              |
| 1           | NPC Dan | Medic    | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic        |
| 1           | NPC Dan | Medic    | broadcast | I (NPC Bob) am the Thief and I have made NPC Dan vulnerable   |
| 1           | NPC Dan | Medic    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed     |
| 1           | NPC Dan | Medic    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |