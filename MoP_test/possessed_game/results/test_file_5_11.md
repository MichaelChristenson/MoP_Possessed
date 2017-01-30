#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 11   | 5       | 7       |

#### Roles
| Role         |
| :----------- |
| Psychic      |
| Reporter     |
| Judge        |
| Executioner  |
| Assassin     |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Executioner | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ann | Executioner | possessed   | You are Possessed         |
| 0           | NPC Bob | Judge       | role change | Your Role is Judge        |
| 0           | NPC Bob | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Cal | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Dan | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Ed  | Reporter    | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action      | Target 1 | Target 2 | status                        |
| :-----------| :-------| :-----------| :--------| :--------| :---------------------------- |
| 1           | NPC Ann | Executioner | NPC Cal  |          | failed because of no support  |
| 1           | NPC Bob | Judge       | Reporter |          | successful                    |
| 1           | NPC Cal | Psychic     |          |          | successful                    |
| 1           | NPC Dan | Assassin    | Psychic  |          | successful                    |
| 1           | NPC Ed  | Reporter    | NPC Bob  |          | successful                    |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ed  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Executioner | False      | True      | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Dan | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message       | details                                                       |
| :-----------| :-------| :-----------| :-------------| :------------------------------------------------------------ |
| 1           | NPC Ann | Executioner | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 1           | NPC Ann | Executioner | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Ann | Executioner | action failed |                                                               |
| 1           | NPC Bob | Judge       | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 1           | NPC Bob | Judge       | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Cal | Psychic     | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 1           | NPC Cal | Psychic     | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Cal | Psychic     | reveal        | Player: NPC Ed is not possessed                               |
| 1           | NPC Dan | Assassin    | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 1           | NPC Dan | Assassin    | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Ed  | Reporter    | broadcast     | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 1           | NPC Ed  | Reporter    | broadcast     | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Ed  | Reporter    | reveal        | NPC Bob is Judge                                              |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Bob | Judge   | Psychic  |          | successful  |
| 2           | NPC Cal | Psychic |          |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Executioner | False      | True      | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Dan | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                       |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------ |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Cal | Psychic     | reveal    | Player: NPC Bob is not possessed                              |
| 2           | NPC Dan | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Dan | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Ed  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Ed  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |

#### Actions Round 3
| round_index | Player  | action   | Target 1    | Target 2 | status      |
| :-----------| :-------| :--------| :-----------| :--------| :---------- |
| 3           | NPC Bob | Judge    | Assassin    |          | successful  |
| 3           | NPC Cal | Psychic  |             |          | successful  |
| 3           | NPC Dan | Assassin | Executioner |          | successful  |
| 3           | NPC Ed  | Reporter | NPC Dan     |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ed  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Executioner | False      | True      | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                       |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------ |
| 3           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ann | Executioner | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Assassin        |
| 3           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Bob | Judge       | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Assassin        |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Cal | Psychic     | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Assassin        |
| 3           | NPC Cal | Psychic     | reveal    | Player: NPC Ed is not possessed                               |
| 3           | NPC Cal | Psychic     | reveal    | Player: NPC Bob is not possessed                              |
| 3           | NPC Dan | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Dan | Assassin    | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Assassin        |
| 3           | NPC Ed  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ed  | Reporter    | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Assassin        |
| 3           | NPC Ed  | Reporter    | reveal    | NPC Dan is Assassin                                           |

#### Actions Round 4
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 4           | NPC Bob | Judge   | Assassin |          | successful  |
| 4           | NPC Cal | Psychic |          |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Bob | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Executioner | False      | True      | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                       |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------ |
| 4           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Cal | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 4           | NPC Dan | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Dan | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ed  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ed  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |

#### Actions Round 5
| round_index | Player  | action      | Target 1    | Target 2 | status      |
| :-----------| :-------| :-----------| :-----------| :--------| :---------- |
| 5           | NPC Ann | Executioner | NPC Bob     |          | successful  |
| 5           | NPC Bob | Judge       | Psychic     |          | successful  |
| 5           | NPC Cal | Psychic     |             |          | successful  |
| 5           | NPC Dan | Assassin    | Executioner |          | successful  |
| 5           | NPC Ed  | Reporter    | NPC Cal     |          | successful  |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Ed  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Bob | Judge       | True       | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ann | Executioner | False      | True      | False      | 4         | True   | 0              | 0                  |
| 5           | NPC Dan | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message     | details                                                       |
| :-----------| :-------| :-----------| :-----------| :------------------------------------------------------------ |
| 5           | NPC Ann | Executioner | broadcast   | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 5           | NPC Ann | Executioner | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ann | Executioner | broadcast   | I (NPC Ed) am the Reporter and NPC Cal is the Psychic         |
| 5           | NPC Ann | Executioner | elimination | NPC Bob has been eliminated                                   |
| 5           | NPC Bob | Judge       | broadcast   | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 5           | NPC Bob | Judge       | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Bob | Judge       | broadcast   | I (NPC Ed) am the Reporter and NPC Cal is the Psychic         |
| 5           | NPC Bob | Judge       | elimination | NPC Bob has been eliminated                                   |
| 5           | NPC Cal | Psychic     | broadcast   | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 5           | NPC Cal | Psychic     | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Cal | Psychic     | broadcast   | I (NPC Ed) am the Reporter and NPC Cal is the Psychic         |
| 5           | NPC Cal | Psychic     | elimination | NPC Bob has been eliminated                                   |
| 5           | NPC Cal | Psychic     | reveal      | Player: NPC Dan is not possessed                              |
| 5           | NPC Dan | Assassin    | broadcast   | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 5           | NPC Dan | Assassin    | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Dan | Assassin    | broadcast   | I (NPC Ed) am the Reporter and NPC Cal is the Psychic         |
| 5           | NPC Dan | Assassin    | elimination | NPC Bob has been eliminated                                   |
| 5           | NPC Ed  | Reporter    | broadcast   | I (NPC Cal) am the Psychic and the Judge is not possessed     |
| 5           | NPC Ed  | Reporter    | broadcast   | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ed  | Reporter    | broadcast   | I (NPC Ed) am the Reporter and NPC Cal is the Psychic         |
| 5           | NPC Ed  | Reporter    | elimination | NPC Bob has been eliminated                                   |
| 5           | NPC Ed  | Reporter    | reveal      | NPC Cal is Psychic                                            |

#### Actions Round 6
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 6           | NPC Bob | Judge   | Psychic  |          | successful  |
| 6           | NPC Cal | Psychic |          |          | successful  |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ed  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Bob | Judge       | True       | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ann | Executioner | False      | True      | False      | 3         | True   | 0              | 0                  |
| 6           | NPC Dan | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role        | message   | details                                                       |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------ |
| 6           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Cal | Psychic     | reveal    | Player: NPC Bob is not possessed                              |
| 6           | NPC Dan | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Dan | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Ed  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Ed  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |

#### Actions Round 7
| round_index | Player  | action   | Target 1    | Target 2 | status      |
| :-----------| :-------| :--------| :-----------| :--------| :---------- |
| 7           | NPC Bob | Judge    | Psychic     |          | successful  |
| 7           | NPC Cal | Psychic  |             |          | successful  |
| 7           | NPC Dan | Assassin | Executioner |          | successful  |
| 7           | NPC Ed  | Reporter | NPC Ann     |          | successful  |

#### States Round 7
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Ed  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Bob | Judge       | True       | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Ann | Executioner | False      | True      | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Dan | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role        | message   | details                                                       |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------ |
| 7           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Ann | Executioner | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Bob | Judge       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Cal | Psychic     | reveal    | Player: NPC Ed is not possessed                               |
| 7           | NPC Cal | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 7           | NPC Dan | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Dan | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Ed  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Ed  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Ed  | Reporter    | reveal    | NPC Ann is Executioner                                        |