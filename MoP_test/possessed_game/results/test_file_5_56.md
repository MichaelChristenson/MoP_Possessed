#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 56   | 5       | 9       |

#### Roles
| Role      |
| :-------- |
| Reporter  |
| Judge     |
| Psychic   |
| Assassin  |
| Silencer  |

#### States Round 0
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Reporter | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Psychic  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Assassin | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Silencer | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role     | message     | details                |
| :-----------| :-------| :--------| :-----------| :--------------------- |
| 0           | NPC Ann | Assassin | role change | Your Role is Assassin  |
| 0           | NPC Ann | Assassin | possessed   | You are Possessed      |
| 0           | NPC Bob | Psychic  | role change | Your Role is Psychic   |
| 0           | NPC Bob | Psychic  | possessed   | You are Not Possessed  |
| 0           | NPC Cal | Reporter | role change | Your Role is Reporter  |
| 0           | NPC Cal | Reporter | possessed   | You are Not Possessed  |
| 0           | NPC Dan | Silencer | role change | Your Role is Silencer  |
| 0           | NPC Dan | Silencer | possessed   | You are Not Possessed  |
| 0           | NPC Ed  | Judge    | role change | Your Role is Judge     |
| 0           | NPC Ed  | Judge    | possessed   | You are Not Possessed  |

#### Actions Round 1
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 1           | NPC Ann | Assassin | Reporter |          | successful  |
| 1           | NPC Bob | Psychic  |          |          | successful  |
| 1           | NPC Cal | Reporter | NPC Ann  |          | successful  |
| 1           | NPC Dan | Silencer | NPC Dan  |          | successful  |
| 1           | NPC Ed  | Judge    | Reporter |          | successful  |

#### States Round 1
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Reporter | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed  | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ann | Assassin | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Silencer | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 1           | NPC Ann | Assassin | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Ann | Assassin | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Assassin       |
| 1           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Bob | Psychic  | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Assassin       |
| 1           | NPC Bob | Psychic  | reveal    | Player: NPC Ed is not possessed                               |
| 1           | NPC Bob | Psychic  | reveal    | Player: NPC Cal is not possessed                              |
| 1           | NPC Cal | Reporter | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Cal | Reporter | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Assassin       |
| 1           | NPC Cal | Reporter | reveal    | NPC Ann is Assassin                                           |
| 1           | NPC Dan | Silencer | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Dan | Silencer | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Assassin       |
| 1           | NPC Dan | Silencer | silenced  | You have been silenced                                        |
| 1           | NPC Ed  | Judge    | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Ed  | Judge    | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Assassin       |

#### Actions Round 2
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 2           | NPC Bob | Psychic  |          |          | successful  |
| 2           | NPC Dan | Silencer | NPC Ann  |          | successful  |
| 2           | NPC Ed  | Judge    | Reporter |          | successful  |

#### States Round 2
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Reporter | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann | Assassin | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Silencer | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 2           | NPC Ann | Assassin | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Ann | Assassin | silenced  | You have been silenced                                        |
| 2           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Bob | Psychic  | reveal    | Player: NPC Ed is not possessed                               |
| 2           | NPC Cal | Reporter | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Dan | Silencer | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 2           | NPC Ed  | Judge    | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 3           | NPC Ann | Assassin | Silencer |          | successful  |
| 3           | NPC Bob | Psychic  |          |          | successful  |
| 3           | NPC Cal | Reporter | NPC Dan  |          | successful  |
| 3           | NPC Dan | Silencer | NPC Dan  |          | successful  |
| 3           | NPC Ed  | Judge    | Psychic  |          | successful  |

#### States Round 3
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal | Reporter | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ed  | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ann | Assassin | False      | True      | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Silencer | True       | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role     | message     | details                                                       |
| :-----------| :-------| :--------| :-----------| :------------------------------------------------------------ |
| 3           | NPC Ann | Assassin | broadcast   | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ann | Assassin | broadcast   | I (NPC Cal) am the Reporter and NPC Dan is the Silencer       |
| 3           | NPC Ann | Assassin | elimination | NPC Dan has been eliminated                                   |
| 3           | NPC Bob | Psychic  | broadcast   | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Bob | Psychic  | broadcast   | I (NPC Cal) am the Reporter and NPC Dan is the Silencer       |
| 3           | NPC Bob | Psychic  | reveal      | Player: NPC Cal is not possessed                              |
| 3           | NPC Bob | Psychic  | elimination | NPC Dan has been eliminated                                   |
| 3           | NPC Cal | Reporter | broadcast   | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Cal | Reporter | broadcast   | I (NPC Cal) am the Reporter and NPC Dan is the Silencer       |
| 3           | NPC Cal | Reporter | reveal      | NPC Dan is Silencer                                           |
| 3           | NPC Cal | Reporter | elimination | NPC Dan has been eliminated                                   |
| 3           | NPC Dan | Silencer | broadcast   | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Dan | Silencer | broadcast   | I (NPC Cal) am the Reporter and NPC Dan is the Silencer       |
| 3           | NPC Dan | Silencer | silenced    | You have been silenced                                        |
| 3           | NPC Dan | Silencer | elimination | NPC Dan has been eliminated                                   |
| 3           | NPC Ed  | Judge    | broadcast   | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ed  | Judge    | broadcast   | I (NPC Cal) am the Reporter and NPC Dan is the Silencer       |
| 3           | NPC Ed  | Judge    | elimination | NPC Dan has been eliminated                                   |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 4           | NPC Bob | Psychic  |          |          | successful  |
| 4           | NPC Dan | Silencer | NPC Ed   |          | successful  |
| 4           | NPC Ed  | Judge    | Psychic  |          | successful  |

#### States Round 4
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal | Reporter | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed  | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann | Assassin | False      | True      | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Silencer | True       | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 4           | NPC Ann | Assassin | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Ann | Assassin | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 4           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 4           | NPC Bob | Psychic  | reveal    | Player: NPC Ed is not possessed                               |
| 4           | NPC Cal | Reporter | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Cal | Reporter | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 4           | NPC Dan | Silencer | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Dan | Silencer | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 4           | NPC Ed  | Judge    | broadcast | I (NPC Bob) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Ed  | Judge    | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 4           | NPC Ed  | Judge    | silenced  | You have been silenced                                        |

#### Actions Round 5
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 5           | NPC Ann | Assassin | Reporter |          | successful  |
| 5           | NPC Bob | Psychic  |          |          | successful  |
| 5           | NPC Cal | Reporter | NPC Bob  |          | successful  |
| 5           | NPC Dan | Silencer | NPC Bob  |          | successful  |
| 5           | NPC Ed  | Judge    | Psychic  |          | successful  |

#### States Round 5
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal | Reporter | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Ed  | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Ann | Assassin | False      | True      | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Dan | Silencer | True       | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 5           | NPC Ann | Assassin | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 5           | NPC Ann | Assassin | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ann | Assassin | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Psychic        |
| 5           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 5           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Bob | Psychic  | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Psychic        |
| 5           | NPC Bob | Psychic  | silenced  | You have been silenced                                        |
| 5           | NPC Bob | Psychic  | reveal    | Player: NPC Dan is not possessed                              |
| 5           | NPC Bob | Psychic  | reveal    | Player: NPC Ed is not possessed                               |
| 5           | NPC Cal | Reporter | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 5           | NPC Cal | Reporter | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Cal | Reporter | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Psychic        |
| 5           | NPC Cal | Reporter | reveal    | NPC Bob is Psychic                                            |
| 5           | NPC Dan | Silencer | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 5           | NPC Dan | Silencer | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Dan | Silencer | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Psychic        |
| 5           | NPC Ed  | Judge    | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 5           | NPC Ed  | Judge    | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ed  | Judge    | broadcast | I (NPC Cal) am the Reporter and NPC Bob is the Psychic        |

#### Actions Round 6
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 6           | NPC Bob | Psychic  |          |          | successful  |
| 6           | NPC Dan | Silencer | NPC Ed   |          | successful  |
| 6           | NPC Ed  | Judge    | Assassin |          | successful  |

#### States Round 6
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Cal | Reporter | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ed  | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ann | Assassin | False      | True      | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Dan | Silencer | True       | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role    | message  | details                           |
| :-----------| :-------| :-------| :--------| :-------------------------------- |
| 6           | NPC Bob | Psychic | reveal   | Player: NPC Cal is not possessed  |
| 6           | NPC Bob | Psychic | reveal   | Player: NPC Dan is not possessed  |
| 6           | NPC Ed  | Judge   | silenced | You have been silenced            |

#### Actions Round 7
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 7           | NPC Ann | Assassin | Psychic  |          | successful  |
| 7           | NPC Bob | Psychic  |          |          | successful  |
| 7           | NPC Cal | Reporter | NPC Ed   |          | successful  |
| 7           | NPC Dan | Silencer | NPC Ann  |          | successful  |
| 7           | NPC Ed  | Judge    | Reporter |          | successful  |

#### States Round 7
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Cal | Reporter | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Ed  | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Bob | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Ann | Assassin | False      | True      | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Dan | Silencer | True       | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 7           | NPC Ann | Assassin | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 7           | NPC Ann | Assassin | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Ann | Assassin | silenced  | You have been silenced                                        |
| 7           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 7           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Bob | Psychic  | reveal    | Player: NPC Dan is not possessed                              |
| 7           | NPC Cal | Reporter | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 7           | NPC Cal | Reporter | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Cal | Reporter | reveal    | NPC Ed is Judge                                               |
| 7           | NPC Dan | Silencer | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 7           | NPC Dan | Silencer | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 7           | NPC Ed  | Judge    | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed     |
| 7           | NPC Ed  | Judge    | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |

#### Actions Round 8
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 8           | NPC Bob | Psychic  |          |          | successful  |
| 8           | NPC Dan | Silencer | NPC Ann  |          | successful  |
| 8           | NPC Ed  | Judge    | Silencer |          | successful  |

#### States Round 8
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Cal | Reporter | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Ed  | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Bob | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Ann | Assassin | False      | True      | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Dan | Silencer | True       | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player  | Role     | message   | details                                                    |
| :-----------| :-------| :--------| :---------| :--------------------------------------------------------- |
| 8           | NPC Ann | Assassin | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed  |
| 8           | NPC Ann | Assassin | silenced  | You have been silenced                                     |
| 8           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed  |
| 8           | NPC Bob | Psychic  | reveal    | Player: NPC Cal is not possessed                           |
| 8           | NPC Cal | Reporter | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed  |
| 8           | NPC Dan | Silencer | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed  |
| 8           | NPC Ed  | Judge    | broadcast | I (NPC Bob) am the Psychic and the Judge is not possessed  |

#### Actions Round 9
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 9           | NPC Ann | Assassin | Reporter |          | successful  |
| 9           | NPC Bob | Psychic  |          |          | successful  |
| 9           | NPC Dan | Silencer | NPC Ann  |          | successful  |
| 9           | NPC Ed  | Judge    | Silencer |          | successful  |

#### States Round 9
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 9           | NPC Cal | Reporter | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Ed  | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 9           | NPC Bob | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 9           | NPC Ann | Assassin | False      | True      | False      | 2         | True   | 0              | 0                  |
| 9           | NPC Dan | Silencer | True       | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 9
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 9           | NPC Ann | Assassin | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 9           | NPC Ann | Assassin | silenced  | You have been silenced                                        |
| 9           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 9           | NPC Bob | Psychic  | reveal    | Player: NPC Cal is not possessed                              |
| 9           | NPC Bob | Psychic  | reveal    | Player: NPC Ed is not possessed                               |
| 9           | NPC Cal | Reporter | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 9           | NPC Dan | Silencer | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 9           | NPC Ed  | Judge    | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |