#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 73   | 7       | 4       |

#### Roles
| Role         |
| :----------- |
| Psychic      |
| Thief        |
| Medic        |
| Reporter     |
| Judge        |
| Inspector    |
| Executioner  |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Judge       | role change | Your Role is Judge        |
| 0           | NPC Ann | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Bob | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Cal | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Thief       | role change | Your Role is Thief        |
| 0           | NPC Dan | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Ed  | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Fae | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Gia | Medic       | role change | Your Role is Medic        |
| 0           | NPC Gia | Medic       | possessed   | You are Possessed         |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Judge     | Psychic  |          | successful  |
| 1           | NPC Bob | Psychic   |          |          | successful  |
| 1           | NPC Cal | Inspector | NPC Gia  |          | successful  |
| 1           | NPC Dan | Thief     | NPC Cal  |          | successful  |
| 1           | NPC Ed  | Reporter  | NPC Bob  |          | successful  |
| 1           | NPC Gia | Medic     | NPC Dan  |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Dan | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                       |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------ |
| 1           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 1           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Ann | Judge       | broadcast | I (NPC Cal) inspected NPC Gia and they are possessed          |
| 1           | NPC Ann | Judge       | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable   |
| 1           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Psychic         |
| 1           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 1           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Bob | Psychic     | broadcast | I (NPC Cal) inspected NPC Gia and they are possessed          |
| 1           | NPC Bob | Psychic     | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable   |
| 1           | NPC Bob | Psychic     | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Psychic         |
| 1           | NPC Bob | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 1           | NPC Bob | Psychic     | reveal    | Player: NPC Ann is not possessed                              |
| 1           | NPC Bob | Psychic     | reveal    | Player: NPC Fae is not possessed                              |
| 1           | NPC Cal | Inspector   | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 1           | NPC Cal | Inspector   | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Cal | Inspector   | broadcast | I (NPC Cal) inspected NPC Gia and they are possessed          |
| 1           | NPC Cal | Inspector   | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable   |
| 1           | NPC Cal | Inspector   | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Psychic         |
| 1           | NPC Cal | Inspector   | reveal    | Medic is Possessed                                            |
| 1           | NPC Dan | Thief       | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 1           | NPC Dan | Thief       | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Dan | Thief       | broadcast | I (NPC Cal) inspected NPC Gia and they are possessed          |
| 1           | NPC Dan | Thief       | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable   |
| 1           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Psychic         |
| 1           | NPC Ed  | Reporter    | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 1           | NPC Ed  | Reporter    | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Ed  | Reporter    | broadcast | I (NPC Cal) inspected NPC Gia and they are possessed          |
| 1           | NPC Ed  | Reporter    | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable   |
| 1           | NPC Ed  | Reporter    | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Psychic         |
| 1           | NPC Ed  | Reporter    | reveal    | NPC Bob is Psychic                                            |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Cal) inspected NPC Gia and they are possessed          |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable   |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Psychic         |
| 1           | NPC Gia | Medic       | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 1           | NPC Gia | Medic       | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Gia | Medic       | broadcast | I (NPC Cal) inspected NPC Gia and they are possessed          |
| 1           | NPC Gia | Medic       | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable   |
| 1           | NPC Gia | Medic       | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Psychic         |

#### Actions Round 2
| round_index | Player  | action      | Target 1 | Target 2 | status                        |
| :-----------| :-------| :-----------| :--------| :--------| :---------------------------- |
| 2           | NPC Ann | Judge       | Psychic  |          | successful                    |
| 2           | NPC Bob | Psychic     |          |          | successful                    |
| 2           | NPC Dan | Thief       | NPC Bob  |          | successful                    |
| 2           | NPC Fae | Executioner | NPC Gia  |          | failed because of no support  |
| 2           | NPC Gia | Medic       | NPC Ed   |          | successful                    |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Psychic     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Gia | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Fae | Executioner | False      | False     | False      | 4         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message       | details                                                          |
| :-----------| :-------| :-----------| :-------------| :--------------------------------------------------------------- |
| 2           | NPC Ann | Judge       | broadcast     | I (NPC Bob) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Ann | Judge       | broadcast     | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ann | Judge       | broadcast     | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable      |
| 2           | NPC Bob | Psychic     | broadcast     | I (NPC Bob) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Bob | Psychic     | broadcast     | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Bob | Psychic     | broadcast     | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable      |
| 2           | NPC Bob | Psychic     | reveal        | Player: NPC Ann is not possessed                                 |
| 2           | NPC Bob | Psychic     | reveal        | Player: NPC Dan is not possessed                                 |
| 2           | NPC Cal | Inspector   | broadcast     | I (NPC Bob) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Cal | Inspector   | broadcast     | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Cal | Inspector   | broadcast     | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable      |
| 2           | NPC Dan | Thief       | broadcast     | I (NPC Bob) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Dan | Thief       | broadcast     | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Dan | Thief       | broadcast     | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable      |
| 2           | NPC Ed  | Reporter    | broadcast     | I (NPC Bob) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Ed  | Reporter    | broadcast     | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ed  | Reporter    | broadcast     | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable      |
| 2           | NPC Fae | Executioner | broadcast     | I (NPC Bob) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Fae | Executioner | broadcast     | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Fae | Executioner | broadcast     | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable      |
| 2           | NPC Fae | Executioner | action failed |                                                                  |
| 2           | NPC Gia | Medic       | broadcast     | I (NPC Bob) am the Psychic and the Reporter is not possessed     |
| 2           | NPC Gia | Medic       | broadcast     | I (NPC Bob) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Gia | Medic       | broadcast     | I (NPC Dan) am the Thief and I have made NPC Bob vulnerable      |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 3           | NPC Ann | Judge     | Medic    |          | successful  |
| 3           | NPC Bob | Psychic   |          |          | successful  |
| 3           | NPC Cal | Inspector | NPC Dan  |          | successful  |
| 3           | NPC Ed  | Reporter  | NPC Cal  |          | successful  |
| 3           | NPC Gia | Medic     | NPC Ann  |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Psychic     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 3           | NPC Dan | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Gia | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Fae | Executioner | False      | False     | False      | 3         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                       |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------ |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed      |
| 3           | NPC Ann | Judge       | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Inspector       |
| 3           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 3           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Bob | Psychic     | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed      |
| 3           | NPC Bob | Psychic     | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Inspector       |
| 3           | NPC Bob | Psychic     | reveal    | Player: NPC Cal is not possessed                              |
| 3           | NPC Bob | Psychic     | reveal    | Player: NPC Fae is not possessed                              |
| 3           | NPC Bob | Psychic     | reveal    | Player: NPC Ed is not possessed                               |
| 3           | NPC Cal | Inspector   | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 3           | NPC Cal | Inspector   | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Cal | Inspector   | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed      |
| 3           | NPC Cal | Inspector   | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Inspector       |
| 3           | NPC Cal | Inspector   | reveal    | Thief is Innocent                                             |
| 3           | NPC Dan | Thief       | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 3           | NPC Dan | Thief       | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Dan | Thief       | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed      |
| 3           | NPC Dan | Thief       | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Inspector       |
| 3           | NPC Ed  | Reporter    | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 3           | NPC Ed  | Reporter    | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ed  | Reporter    | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed      |
| 3           | NPC Ed  | Reporter    | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Inspector       |
| 3           | NPC Ed  | Reporter    | reveal    | NPC Cal is Inspector                                          |
| 3           | NPC Fae | Executioner | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 3           | NPC Fae | Executioner | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Fae | Executioner | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed      |
| 3           | NPC Fae | Executioner | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Inspector       |
| 3           | NPC Gia | Medic       | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 3           | NPC Gia | Medic       | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Gia | Medic       | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed      |
| 3           | NPC Gia | Medic       | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Inspector       |

#### Actions Round 4
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 4           | NPC Ann | Judge   | Medic    |          | successful  |
| 4           | NPC Bob | Psychic |          |          | successful  |
| 4           | NPC Dan | Thief   | NPC Ann  |          | successful  |
| 4           | NPC Gia | Medic   | NPC Cal  |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Bob | Psychic     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Gia | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann | Judge       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Inspector   | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Fae | Executioner | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                       |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------ |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ann | Judge       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable   |
| 4           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 4           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 4           | NPC Bob | Psychic     | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Bob | Psychic     | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable   |
| 4           | NPC Bob | Psychic     | reveal    | Player: NPC Fae is not possessed                              |
| 4           | NPC Bob | Psychic     | reveal    | Player: NPC Ed is not possessed                               |
| 4           | NPC Bob | Psychic     | reveal    | Player: NPC Ann is not possessed                              |
| 4           | NPC Cal | Inspector   | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 4           | NPC Cal | Inspector   | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 4           | NPC Cal | Inspector   | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Cal | Inspector   | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable   |
| 4           | NPC Dan | Thief       | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 4           | NPC Dan | Thief       | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 4           | NPC Dan | Thief       | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Dan | Thief       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable   |
| 4           | NPC Ed  | Reporter    | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 4           | NPC Ed  | Reporter    | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 4           | NPC Ed  | Reporter    | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ed  | Reporter    | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable   |
| 4           | NPC Fae | Executioner | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 4           | NPC Fae | Executioner | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 4           | NPC Fae | Executioner | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Fae | Executioner | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable   |
| 4           | NPC Gia | Medic       | broadcast | I (NPC Bob) am the Psychic and the Thief is not possessed     |
| 4           | NPC Gia | Medic       | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 4           | NPC Gia | Medic       | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Gia | Medic       | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable   |