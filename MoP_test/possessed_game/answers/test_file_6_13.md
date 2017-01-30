#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 13   | 6       | 6       |

#### Roles
| Role         |
| :----------- |
| Executioner  |
| Inspector    |
| Reporter     |
| Medic        |
| Thief        |
| Psychic      |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Thief       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ann | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Bob | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Thief       | role change | Your Role is Thief        |
| 0           | NPC Cal | Thief       | possessed   | You are Possessed         |
| 0           | NPC Dan | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Dan | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Ed  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Medic       | role change | Your Role is Medic        |
| 0           | NPC Fae | Medic       | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Bob | Reporter  | NPC Cal  |          | successful  |
| 1           | NPC Cal | Thief     | NPC Ed   |          | successful  |
| 1           | NPC Dan | Psychic   |          |          | successful  |
| 1           | NPC Ed  | Inspector | NPC Fae  |          | successful  |
| 1           | NPC Fae | Medic     | NPC Ed   |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Inspector   | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Thief       | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 1           | NPC Ann | Executioner | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Thief           |
| 1           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Thief and I have made NPC Ed vulnerable     |
| 1           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 1           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ann | Executioner | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed        |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Thief           |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Cal) am the Thief and I have made NPC Ed vulnerable     |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed        |
| 1           | NPC Bob | Reporter    | reveal    | NPC Cal is Thief                                               |
| 1           | NPC Cal | Thief       | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Thief           |
| 1           | NPC Cal | Thief       | broadcast | I (NPC Cal) am the Thief and I have made NPC Ed vulnerable     |
| 1           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 1           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Cal | Thief       | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed        |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Thief           |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Cal) am the Thief and I have made NPC Ed vulnerable     |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Dan | Psychic     | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed        |
| 1           | NPC Dan | Psychic     | reveal    | Player: NPC Ann is not possessed                               |
| 1           | NPC Dan | Psychic     | reveal    | Player: NPC Ed is not possessed                                |
| 1           | NPC Ed  | Inspector   | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Thief           |
| 1           | NPC Ed  | Inspector   | broadcast | I (NPC Cal) am the Thief and I have made NPC Ed vulnerable     |
| 1           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 1           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ed  | Inspector   | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed        |
| 1           | NPC Ed  | Inspector   | reveal    | Medic is Innocent                                              |
| 1           | NPC Fae | Medic       | broadcast | I (NPC Bob) am the Reporter and NPC Cal is the Thief           |
| 1           | NPC Fae | Medic       | broadcast | I (NPC Cal) am the Thief and I have made NPC Ed vulnerable     |
| 1           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 1           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Fae | Medic       | broadcast | I (NPC Ed) inspected NPC Fae and they are not possessed        |

#### Actions Round 2
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 2           | NPC Dan | Psychic   |          |          | successful  |
| 2           | NPC Ed  | Inspector | NPC Dan  |          | successful  |
| 2           | NPC Fae | Medic     | NPC Bob  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ann | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 2           | NPC Bob | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Thief       | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed          |
| 2           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 2           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Bob | Reporter    | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed          |
| 2           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 2           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Cal | Thief       | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed          |
| 2           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 2           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Dan | Psychic     | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed          |
| 2           | NPC Dan | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 2           | NPC Dan | Psychic     | reveal    | Player: NPC Ann is not possessed                                 |
| 2           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 2           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ed  | Inspector   | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed          |
| 2           | NPC Ed  | Inspector   | reveal    | Psychic is Innocent                                              |
| 2           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 2           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Fae | Medic       | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed          |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 3           | NPC Bob | Reporter | NPC Fae  |          | successful  |
| 3           | NPC Cal | Thief    | NPC Ann  |          | successful  |
| 3           | NPC Dan | Psychic  |          |          | successful  |
| 3           | NPC Fae | Medic    | NPC Cal  |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ann | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 3           | NPC Bob | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Fae | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Thief       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 3           | NPC Ann | Executioner | broadcast | I (NPC Bob) am the Reporter and NPC Fae is the Medic           |
| 3           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Thief and I have made NPC Ann vulnerable    |
| 3           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 3           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Bob | Reporter    | broadcast | I (NPC Bob) am the Reporter and NPC Fae is the Medic           |
| 3           | NPC Bob | Reporter    | broadcast | I (NPC Cal) am the Thief and I have made NPC Ann vulnerable    |
| 3           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 3           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Bob | Reporter    | reveal    | NPC Fae is Medic                                               |
| 3           | NPC Cal | Thief       | broadcast | I (NPC Bob) am the Reporter and NPC Fae is the Medic           |
| 3           | NPC Cal | Thief       | broadcast | I (NPC Cal) am the Thief and I have made NPC Ann vulnerable    |
| 3           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 3           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Dan | Psychic     | broadcast | I (NPC Bob) am the Reporter and NPC Fae is the Medic           |
| 3           | NPC Dan | Psychic     | broadcast | I (NPC Cal) am the Thief and I have made NPC Ann vulnerable    |
| 3           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 3           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Dan | Psychic     | reveal    | Player: NPC Ann is not possessed                               |
| 3           | NPC Dan | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 3           | NPC Ed  | Inspector   | broadcast | I (NPC Bob) am the Reporter and NPC Fae is the Medic           |
| 3           | NPC Ed  | Inspector   | broadcast | I (NPC Cal) am the Thief and I have made NPC Ann vulnerable    |
| 3           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 3           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Fae | Medic       | broadcast | I (NPC Bob) am the Reporter and NPC Fae is the Medic           |
| 3           | NPC Fae | Medic       | broadcast | I (NPC Cal) am the Thief and I have made NPC Ann vulnerable    |
| 3           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed      |
| 3           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed   |

#### Actions Round 4
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 4           | NPC Cal | Thief     | NPC Fae  |          | successful  |
| 4           | NPC Dan | Psychic   |          |          | successful  |
| 4           | NPC Ed  | Inspector | NPC Dan  |          | successful  |
| 4           | NPC Fae | Medic     | NPC Dan  |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ann | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 4           | NPC Bob | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Fae | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Thief       | False      | True      | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Dan | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 4           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Thief and I have made NPC Fae vulnerable      |
| 4           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ann | Executioner | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed          |
| 4           | NPC Bob | Reporter    | broadcast | I (NPC Cal) am the Thief and I have made NPC Fae vulnerable      |
| 4           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Bob | Reporter    | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed          |
| 4           | NPC Cal | Thief       | broadcast | I (NPC Cal) am the Thief and I have made NPC Fae vulnerable      |
| 4           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Cal | Thief       | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed          |
| 4           | NPC Dan | Psychic     | broadcast | I (NPC Cal) am the Thief and I have made NPC Fae vulnerable      |
| 4           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Dan | Psychic     | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed          |
| 4           | NPC Dan | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 4           | NPC Dan | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 4           | NPC Ed  | Inspector   | broadcast | I (NPC Cal) am the Thief and I have made NPC Fae vulnerable      |
| 4           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ed  | Inspector   | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed          |
| 4           | NPC Ed  | Inspector   | reveal    | Psychic is Innocent                                              |
| 4           | NPC Fae | Medic       | broadcast | I (NPC Cal) am the Thief and I have made NPC Fae vulnerable      |
| 4           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Fae | Medic       | broadcast | I (NPC Ed) inspected NPC Dan and they are not possessed          |

#### Actions Round 5
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 5           | NPC Bob | Reporter | NPC Ann  |          | successful  |
| 5           | NPC Dan | Psychic  |          |          | successful  |
| 5           | NPC Fae | Medic    | NPC Ann  |          | successful  |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ann | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 5           | NPC Bob | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Fae | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Cal | Thief       | False      | True      | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Dan | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 5           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 5           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 5           | NPC Bob | Reporter    | reveal    | NPC Ann is Executioner                                           |
| 5           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 5           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 5           | NPC Dan | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 5           | NPC Dan | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 5           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 5           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 5           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |

#### Actions Round 6
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 6           | NPC Cal | Thief     | NPC Bob  |          | successful  |
| 6           | NPC Dan | Psychic   |          |          | successful  |
| 6           | NPC Ed  | Inspector | NPC Bob  |          | successful  |
| 6           | NPC Fae | Medic     | NPC Ed   |          | successful  |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Ann | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Ed  | Inspector   | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Reporter    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Fae | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Thief       | False      | True      | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Dan | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 6           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Thief and I have made NPC Bob vulnerable      |
| 6           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Ann | Executioner | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 6           | NPC Ann | Executioner | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed          |
| 6           | NPC Bob | Reporter    | broadcast | I (NPC Cal) am the Thief and I have made NPC Bob vulnerable      |
| 6           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 6           | NPC Bob | Reporter    | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed          |
| 6           | NPC Cal | Thief       | broadcast | I (NPC Cal) am the Thief and I have made NPC Bob vulnerable      |
| 6           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Cal | Thief       | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 6           | NPC Cal | Thief       | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed          |
| 6           | NPC Dan | Psychic     | broadcast | I (NPC Cal) am the Thief and I have made NPC Bob vulnerable      |
| 6           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Dan | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 6           | NPC Dan | Psychic     | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed          |
| 6           | NPC Dan | Psychic     | reveal    | Player: NPC Ann is not possessed                                 |
| 6           | NPC Dan | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 6           | NPC Ed  | Inspector   | broadcast | I (NPC Cal) am the Thief and I have made NPC Bob vulnerable      |
| 6           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Ed  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 6           | NPC Ed  | Inspector   | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed          |
| 6           | NPC Ed  | Inspector   | reveal    | Reporter is Innocent                                             |
| 6           | NPC Fae | Medic       | broadcast | I (NPC Cal) am the Thief and I have made NPC Bob vulnerable      |
| 6           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed     |
| 6           | NPC Fae | Medic       | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed        |
| 6           | NPC Fae | Medic       | broadcast | I (NPC Ed) inspected NPC Bob and they are not possessed          |