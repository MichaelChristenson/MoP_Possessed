#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 81   | 4       | 7       |

#### Roles
| Role         |
| :----------- |
| Inspector    |
| Judge        |
| Psychic      |
| Executioner  |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Inspector   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Ann | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Bob | Inspector   | possessed   | You are Possessed         |
| 0           | NPC Cal | Judge       | role change | Your Role is Judge        |
| 0           | NPC Cal | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Dan | Executioner | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 1           | NPC Ann | Psychic |          |          | successful  |
| 1           | NPC Cal | Judge   | Psychic  |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Inspector   | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 1           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ann | Psychic     | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed            |
| 1           | NPC Ann | Psychic     | reveal    | Player: NPC Cal is not possessed                                 |
| 1           | NPC Bob | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed            |
| 1           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal | Judge       | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed            |
| 1           | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Dan | Executioner | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed            |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Ann | Psychic |          |          | successful  |
| 2           | NPC Cal | Judge   | Psychic  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Inspector   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                    |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------- |
| 2           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed  |
| 2           | NPC Ann | Psychic     | reveal    | Player: NPC Dan is not possessed                           |
| 2           | NPC Bob | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed  |
| 2           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed  |
| 2           | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed  |

#### Actions Round 3
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 3           | NPC Ann | Psychic |          |          | successful  |
| 3           | NPC Cal | Judge   | Psychic  |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Inspector   | False      | True      | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 3           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Ann | Psychic     | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed            |
| 3           | NPC Ann | Psychic     | reveal    | Player: NPC Cal is not possessed                                 |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed            |
| 3           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Cal | Judge       | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed            |
| 3           | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Dan | Executioner | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed            |

#### Actions Round 4
| round_index | Player  | action  | Target 1  | Target 2 | status      |
| :-----------| :-------| :-------| :---------| :--------| :---------- |
| 4           | NPC Ann | Psychic |           |          | successful  |
| 4           | NPC Cal | Judge   | Inspector |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Bob | Inspector   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 4           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed        |
| 4           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ann | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 4           | NPC Bob | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed        |
| 4           | NPC Bob | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed        |
| 4           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed        |
| 4           | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |

#### Actions Round 5
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 5           | NPC Ann | Psychic |          |          | successful  |
| 5           | NPC Cal | Judge   | Psychic  |          | successful  |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Bob | Inspector   | False      | True      | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 5           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed        |
| 5           | NPC Ann | Psychic     | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed            |
| 5           | NPC Ann | Psychic     | reveal    | Player: NPC Cal is not possessed                                 |
| 5           | NPC Bob | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Bob | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed        |
| 5           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed            |
| 5           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed        |
| 5           | NPC Cal | Judge       | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed            |
| 5           | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed        |
| 5           | NPC Dan | Executioner | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed            |

#### Actions Round 6
| round_index | Player  | action  | Target 1  | Target 2 | status      |
| :-----------| :-------| :-------| :---------| :--------| :---------- |
| 6           | NPC Ann | Psychic |           |          | successful  |
| 6           | NPC Cal | Judge   | Inspector |          | successful  |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Bob | Inspector   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 6           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Ann | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 6           | NPC Bob | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 6           | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |

#### Actions Round 7
| round_index | Player  | action  | Target 1  | Target 2 | status      |
| :-----------| :-------| :-------| :---------| :--------| :---------- |
| 7           | NPC Ann | Psychic |           |          | successful  |
| 7           | NPC Cal | Judge   | Inspector |          | successful  |

#### States Round 7
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Bob | Inspector   | False      | True      | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Dan | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role        | message   | details                                                    |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------- |
| 7           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed  |
| 7           | NPC Ann | Psychic     | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed      |
| 7           | NPC Ann | Psychic     | reveal    | Player: NPC Dan is not possessed                           |
| 7           | NPC Bob | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed  |
| 7           | NPC Bob | Inspector   | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed      |
| 7           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed  |
| 7           | NPC Cal | Judge       | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed      |
| 7           | NPC Dan | Executioner | broadcast | I (NPC Ann) am the Psychic and the Judge is not possessed  |
| 7           | NPC Dan | Executioner | broadcast | I (NPC Bob) inspected NPC Dan and they are posssessed      |