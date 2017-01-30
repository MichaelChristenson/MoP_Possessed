#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 76   | 5       | 4       |

#### Roles
| Role         |
| :----------- |
| Psychic      |
| Spy          |
| Judge        |
| Reporter     |
| Executioner  |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Reporter    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Ann | Reporter    | possessed   | You are Possessed         |
| 0           | NPC Bob | Judge       | role change | Your Role is Judge        |
| 0           | NPC Bob | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Cal | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Dan | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Ed  | Spy         | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 1           | NPC Ann | Reporter | NPC Cal  |          | successful  |
| 1           | NPC Bob | Judge    | Spy      |          | successful  |
| 1           | NPC Cal | Psychic  |          |          | successful  |
| 1           | NPC Ed  | Spy      |          |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ed  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Reporter    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 1           | NPC Ann | Reporter    | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic           |
| 1           | NPC Ann | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed        |
| 1           | NPC Ann | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ann | Reporter    | reveal    | NPC Cal is Psychic                                               |
| 1           | NPC Bob | Judge       | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic           |
| 1           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed        |
| 1           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal | Psychic     | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic           |
| 1           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed        |
| 1           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 1           | NPC Cal | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 1           | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic           |
| 1           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed        |
| 1           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ed  | Spy         | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Psychic           |
| 1           | NPC Ed  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed        |
| 1           | NPC Ed  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ed  | Spy         | reveal    | NPC Bob is targeting NPC Ed                                      |
| 1           | NPC Ed  | Spy         | reveal    | NPC Ann is targeting NPC Cal                                     |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Bob | Judge   | Psychic  |          | successful  |
| 2           | NPC Cal | Psychic |          |          | successful  |
| 2           | NPC Ed  | Spy     |          |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Reporter    | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 2           | NPC Ann | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ann | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Ed            |
| 2           | NPC Ann | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Cal           |
| 2           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Bob | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Ed            |
| 2           | NPC Bob | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Cal           |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Ed            |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Cal           |
| 2           | NPC Cal | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 2           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Dan | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Ed            |
| 2           | NPC Dan | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Cal           |
| 2           | NPC Ed  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Ed            |
| 2           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Cal           |
| 2           | NPC Ed  | Spy         | reveal    | NPC Bob is targeting NPC Cal                                     |
| 2           | NPC Ed  | Spy         | reveal    | NPC Ann is targeting NPC Cal                                     |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 3           | NPC Ann | Reporter | NPC Ed   |          | successful  |
| 3           | NPC Bob | Judge    | Psychic  |          | successful  |
| 3           | NPC Cal | Psychic  |          |          | successful  |
| 3           | NPC Ed  | Spy      |          |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ed  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Reporter    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                    |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------- |
| 3           | NPC Ann | Reporter    | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Spy          |
| 3           | NPC Ann | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed    |
| 3           | NPC Ann | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed  |
| 3           | NPC Ann | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal     |
| 3           | NPC Ann | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Cal     |
| 3           | NPC Ann | Reporter    | reveal    | NPC Ed is Spy                                              |
| 3           | NPC Bob | Judge       | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Spy          |
| 3           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed    |
| 3           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed  |
| 3           | NPC Bob | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal     |
| 3           | NPC Bob | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Cal     |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Spy          |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed    |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed  |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal     |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Cal     |
| 3           | NPC Cal | Psychic     | reveal    | Player: NPC Bob is not possessed                           |
| 3           | NPC Cal | Psychic     | reveal    | Player: NPC Ed is not possessed                            |
| 3           | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Spy          |
| 3           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed    |
| 3           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed  |
| 3           | NPC Dan | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal     |
| 3           | NPC Dan | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Cal     |
| 3           | NPC Ed  | Spy         | broadcast | I (NPC Ann) am the Reporter and NPC Ed is the Spy          |
| 3           | NPC Ed  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed    |
| 3           | NPC Ed  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed  |
| 3           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal     |
| 3           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Cal     |
| 3           | NPC Ed  | Spy         | reveal    | NPC Bob is targeting NPC Cal                               |
| 3           | NPC Ed  | Spy         | reveal    | NPC Ann is targeting NPC Ed                                |

#### Actions Round 4
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 4           | NPC Bob | Judge   | Psychic  |          | successful  |
| 4           | NPC Cal | Psychic |          |          | successful  |
| 4           | NPC Ed  | Spy     |          |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Reporter    | False      | True      | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 4           | NPC Ann | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ann | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed        |
| 4           | NPC Ann | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 4           | NPC Ann | Reporter    | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Ed            |
| 4           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed        |
| 4           | NPC Bob | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 4           | NPC Bob | Judge       | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Ed            |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed        |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Ed            |
| 4           | NPC Cal | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 4           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Dan | Executioner | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed        |
| 4           | NPC Dan | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 4           | NPC Dan | Executioner | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Ed            |
| 4           | NPC Ed  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ed  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed        |
| 4           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Bob is targeting NPC Cal           |
| 4           | NPC Ed  | Spy         | broadcast | I (NPC Ed) am the Spy and NPC Ann is targeting NPC Ed            |
| 4           | NPC Ed  | Spy         | reveal    | NPC Bob is targeting NPC Cal                                     |
| 4           | NPC Ed  | Spy         | reveal    | NPC Ann is targeting NPC Ed                                      |