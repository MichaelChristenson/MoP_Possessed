#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 61   | 7       | 3       |

#### Roles
| Role         |
| :----------- |
| Inspector    |
| Psychic      |
| Thief        |
| Judge        |
| Reporter     |
| Medic        |
| Executioner  |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Thief       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Ann | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Bob | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Medic       | role change | Your Role is Medic        |
| 0           | NPC Cal | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Dan | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Ed  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Fae | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Gia | Thief       | role change | Your Role is Thief        |
| 0           | NPC Gia | Thief       | possessed   | You are Possessed         |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Reporter  | NPC Bob  |          | successful  |
| 1           | NPC Bob | Inspector | NPC Ed   |          | successful  |
| 1           | NPC Cal | Medic     | NPC Dan  |          | successful  |
| 1           | NPC Dan | Psychic   |          |          | successful  |
| 1           | NPC Ed  | Judge     | Medic    |          | successful  |
| 1           | NPC Gia | Thief     | NPC Bob  |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia | Thief       | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 1           | NPC Ann | Reporter    | broadcast | I (NPC Ann) am the Reporter and NPC Bob is the Inspector       |
| 1           | NPC Ann | Reporter    | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed        |
| 1           | NPC Ann | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ann | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ann | Reporter    | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable    |
| 1           | NPC Ann | Reporter    | reveal    | NPC Bob is Inspector                                           |
| 1           | NPC Bob | Inspector   | broadcast | I (NPC Ann) am the Reporter and NPC Bob is the Inspector       |
| 1           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed        |
| 1           | NPC Bob | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Bob | Inspector   | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable    |
| 1           | NPC Bob | Inspector   | reveal    | Judge is Innocent                                              |
| 1           | NPC Cal | Medic       | broadcast | I (NPC Ann) am the Reporter and NPC Bob is the Inspector       |
| 1           | NPC Cal | Medic       | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed        |
| 1           | NPC Cal | Medic       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Cal | Medic       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Cal | Medic       | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable    |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Ann) am the Reporter and NPC Bob is the Inspector       |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed        |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable    |
| 1           | NPC Dan | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 1           | NPC Dan | Psychic     | reveal    | Player: NPC Ann is not possessed                               |
| 1           | NPC Dan | Psychic     | reveal    | Player: NPC Fae is not possessed                               |
| 1           | NPC Ed  | Judge       | broadcast | I (NPC Ann) am the Reporter and NPC Bob is the Inspector       |
| 1           | NPC Ed  | Judge       | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed        |
| 1           | NPC Ed  | Judge       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ed  | Judge       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ed  | Judge       | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable    |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Reporter and NPC Bob is the Inspector       |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed        |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable    |
| 1           | NPC Gia | Thief       | broadcast | I (NPC Ann) am the Reporter and NPC Bob is the Inspector       |
| 1           | NPC Gia | Thief       | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed        |
| 1           | NPC Gia | Thief       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Gia | Thief       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Gia | Thief       | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable    |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Cal | Medic   | NPC Gia  |          | successful  |
| 2           | NPC Dan | Psychic |          |          | successful  |
| 2           | NPC Ed  | Judge   | Medic    |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia | Thief       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 2           | NPC Ann | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ann | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Bob | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Bob | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal | Medic       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Dan | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 2           | NPC Dan | Psychic     | reveal    | Player: NPC Cal is not possessed                               |
| 2           | NPC Ed  | Judge       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ed  | Judge       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Fae | Executioner | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Fae | Executioner | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Gia | Thief       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Gia | Thief       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 3           | NPC Ann | Reporter  | NPC Cal  |          | successful  |
| 3           | NPC Bob | Inspector | NPC Ed   |          | successful  |
| 3           | NPC Cal | Medic     | NPC Ed   |          | successful  |
| 3           | NPC Dan | Psychic   |          |          | successful  |
| 3           | NPC Ed  | Judge     | Psychic  |          | successful  |
| 3           | NPC Gia | Thief     | NPC Cal  |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Gia | Thief       | False      | True      | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ed  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Cal | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                       |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------ |
| 3           | NPC Ann | Reporter    | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Medic          |
| 3           | NPC Ann | Reporter    | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed       |
| 3           | NPC Ann | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ann | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed     |
| 3           | NPC Ann | Reporter    | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Ann | Reporter    | reveal    | NPC Cal is Medic                                              |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Medic          |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed       |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed     |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Bob | Inspector   | reveal    | Judge is Innocent                                             |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Medic          |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed       |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed     |
| 3           | NPC Cal | Medic       | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Dan | Psychic     | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Medic          |
| 3           | NPC Dan | Psychic     | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed       |
| 3           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed     |
| 3           | NPC Dan | Psychic     | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Dan | Psychic     | reveal    | Player: NPC Cal is not possessed                              |
| 3           | NPC Dan | Psychic     | reveal    | Player: NPC Fae is not possessed                              |
| 3           | NPC Dan | Psychic     | reveal    | Player: NPC Ed is not possessed                               |
| 3           | NPC Ed  | Judge       | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Medic          |
| 3           | NPC Ed  | Judge       | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed       |
| 3           | NPC Ed  | Judge       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ed  | Judge       | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed     |
| 3           | NPC Ed  | Judge       | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Medic          |
| 3           | NPC Fae | Executioner | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed       |
| 3           | NPC Fae | Executioner | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Fae | Executioner | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed     |
| 3           | NPC Fae | Executioner | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Gia | Thief       | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Medic          |
| 3           | NPC Gia | Thief       | broadcast | I (NPC Bob) inspected NPC Ed and they are not possessed       |
| 3           | NPC Gia | Thief       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Gia | Thief       | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed     |
| 3           | NPC Gia | Thief       | broadcast | I (NPC Gia) am the Thief and I have made NPC Cal vulnerable   |