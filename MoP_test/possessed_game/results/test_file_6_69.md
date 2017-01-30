#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 69   | 6       | 8       |

#### Roles
| Role      |
| :-------- |
| Psychic   |
| Reporter  |
| Medic     |
| Assassin  |
| Spy       |
| Priest    |

#### States Round 0
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Psychic  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Reporter | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Assassin | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Spy      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role     | message     | details                |
| :-----------| :-------| :--------| :-----------| :--------------------- |
| 0           | NPC Ann | Psychic  | role change | Your Role is Psychic   |
| 0           | NPC Ann | Psychic  | possessed   | You are Not Possessed  |
| 0           | NPC Bob | Medic    | role change | Your Role is Medic     |
| 0           | NPC Bob | Medic    | possessed   | You are Not Possessed  |
| 0           | NPC Cal | Spy      | role change | Your Role is Spy       |
| 0           | NPC Cal | Spy      | possessed   | You are Possessed      |
| 0           | NPC Dan | Priest   | role change | Your Role is Priest    |
| 0           | NPC Dan | Priest   | possessed   | You are Not Possessed  |
| 0           | NPC Ed  | Reporter | role change | Your Role is Reporter  |
| 0           | NPC Ed  | Reporter | possessed   | You are Not Possessed  |
| 0           | NPC Fae | Assassin | role change | Your Role is Assassin  |
| 0           | NPC Fae | Assassin | possessed   | You are Not Possessed  |

#### Actions Round 1
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 1           | NPC Ann | Psychic  |          |          | successful  |
| 1           | NPC Bob | Medic    | NPC Ed   |          | successful  |
| 1           | NPC Cal | Spy      |          |          | successful  |
| 1           | NPC Ed  | Reporter | NPC Dan  |          | successful  |
| 1           | NPC Fae | Assassin | Spy      |          | successful  |

#### States Round 1
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ed  | Reporter | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae | Assassin | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal | Spy      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 1           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 1           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 1           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Ann | Psychic  | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Priest          |
| 1           | NPC Ann | Psychic  | reveal    | Player: NPC Fae is not possessed                              |
| 1           | NPC Ann | Psychic  | reveal    | Player: NPC Dan is not possessed                              |
| 1           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 1           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 1           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Bob | Medic    | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Priest          |
| 1           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 1           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 1           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Cal | Spy      | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Priest          |
| 1           | NPC Cal | Spy      | reveal    | NPC Ed is targeting NPC Dan                                   |
| 1           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 1           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 1           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Dan | Priest   | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Priest          |
| 1           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 1           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 1           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Ed  | Reporter | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Priest          |
| 1           | NPC Ed  | Reporter | reveal    | NPC Dan is Priest                                             |
| 1           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 1           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 1           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Fae | Assassin | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Priest          |

#### Actions Round 2
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 2           | NPC Ann | Psychic  |          |          | successful  |
| 2           | NPC Bob | Medic    | NPC Fae  |          | successful  |
| 2           | NPC Cal | Spy      |          |          | successful  |
| 2           | NPC Ed  | Reporter | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ann | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Reporter | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Bob | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae | Assassin | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Spy      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 2           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan        |
| 2           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed        |
| 2           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Cal       |
| 2           | NPC Ann | Psychic  | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Psychic         |
| 2           | NPC Ann | Psychic  | reveal    | Player: NPC Ed is not possessed                               |
| 2           | NPC Ann | Psychic  | reveal    | Player: NPC Dan is not possessed                              |
| 2           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan        |
| 2           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed        |
| 2           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Cal       |
| 2           | NPC Bob | Medic    | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Psychic         |
| 2           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan        |
| 2           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed        |
| 2           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Cal       |
| 2           | NPC Cal | Spy      | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Psychic         |
| 2           | NPC Cal | Spy      | reveal    | NPC Ed is targeting NPC Ann                                   |
| 2           | NPC Cal | Spy      | reveal    | NPC Bob is targeting NPC Ed                                   |
| 2           | NPC Cal | Spy      | reveal    | NPC Fae is targeting NPC Cal                                  |
| 2           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan        |
| 2           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed        |
| 2           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Cal       |
| 2           | NPC Dan | Priest   | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Psychic         |
| 2           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan        |
| 2           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed        |
| 2           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Cal       |
| 2           | NPC Ed  | Reporter | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Psychic         |
| 2           | NPC Ed  | Reporter | reveal    | NPC Ann is Psychic                                            |
| 2           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Dan        |
| 2           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed        |
| 2           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Cal       |
| 2           | NPC Fae | Assassin | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Psychic         |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 3           | NPC Ann | Psychic  |          |          | successful  |
| 3           | NPC Bob | Medic    | NPC Cal  |          | successful  |
| 3           | NPC Cal | Spy      |          |          | successful  |
| 3           | NPC Fae | Assassin | Reporter |          | successful  |

#### States Round 3
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ann | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ed  | Reporter | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Bob | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Fae | Assassin | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Cal | Spy      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 3           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 3           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Fae       |
| 3           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Cal       |
| 3           | NPC Ann | Psychic  | reveal    | Player: NPC Ed is not possessed                               |
| 3           | NPC Ann | Psychic  | reveal    | Player: NPC Bob is not possessed                              |
| 3           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 3           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Fae       |
| 3           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Cal       |
| 3           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 3           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Fae       |
| 3           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Cal       |
| 3           | NPC Cal | Spy      | reveal    | NPC Ed is targeting NPC Ann                                   |
| 3           | NPC Cal | Spy      | reveal    | NPC Bob is targeting NPC Fae                                  |
| 3           | NPC Cal | Spy      | reveal    | NPC Fae is targeting NPC Cal                                  |
| 3           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 3           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Fae       |
| 3           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Cal       |
| 3           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 3           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Fae       |
| 3           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Cal       |
| 3           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 3           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 3           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann        |
| 3           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Fae       |
| 3           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Cal       |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 4           | NPC Ann | Psychic  |          |          | successful  |
| 4           | NPC Bob | Medic    | NPC Dan  |          | successful  |
| 4           | NPC Cal | Spy      |          |          | successful  |
| 4           | NPC Ed  | Reporter | NPC Bob  |          | successful  |

#### States Round 4
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ann | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed  | Reporter | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Bob | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae | Assassin | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Cal | Spy      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 4           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 4           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann        |
| 4           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal       |
| 4           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 4           | NPC Ann | Psychic  | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Medic           |
| 4           | NPC Ann | Psychic  | reveal    | Player: NPC Ed is not possessed                               |
| 4           | NPC Ann | Psychic  | reveal    | Player: NPC Bob is not possessed                              |
| 4           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 4           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann        |
| 4           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal       |
| 4           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 4           | NPC Bob | Medic    | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Medic           |
| 4           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 4           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann        |
| 4           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal       |
| 4           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 4           | NPC Cal | Spy      | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Medic           |
| 4           | NPC Cal | Spy      | reveal    | NPC Ed is targeting NPC Bob                                   |
| 4           | NPC Cal | Spy      | reveal    | NPC Bob is targeting NPC Cal                                  |
| 4           | NPC Cal | Spy      | reveal    | NPC Fae is targeting NPC Ed                                   |
| 4           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 4           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann        |
| 4           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal       |
| 4           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 4           | NPC Dan | Priest   | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Medic           |
| 4           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 4           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann        |
| 4           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal       |
| 4           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 4           | NPC Ed  | Reporter | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Medic           |
| 4           | NPC Ed  | Reporter | reveal    | NPC Bob is Medic                                              |
| 4           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 4           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Ann        |
| 4           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Cal       |
| 4           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 4           | NPC Fae | Assassin | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Medic           |

#### Actions Round 5
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 5           | NPC Ann | Psychic  |          |          | successful  |
| 5           | NPC Bob | Medic    | NPC Ann  |          | successful  |
| 5           | NPC Cal | Spy      |          |          | successful  |
| 5           | NPC Fae | Assassin | Reporter |          | successful  |

#### States Round 5
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ann | Psychic  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Reporter | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Bob | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Fae | Assassin | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Cal | Spy      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 5           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 5           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob        |
| 5           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan       |
| 5           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Ann | Psychic  | reveal    | Player: NPC Bob is not possessed                              |
| 5           | NPC Ann | Psychic  | reveal    | Player: NPC Ed is not possessed                               |
| 5           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 5           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob        |
| 5           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan       |
| 5           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 5           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob        |
| 5           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan       |
| 5           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Cal | Spy      | reveal    | NPC Ed is targeting NPC Bob                                   |
| 5           | NPC Cal | Spy      | reveal    | NPC Bob is targeting NPC Dan                                  |
| 5           | NPC Cal | Spy      | reveal    | NPC Fae is targeting NPC Ed                                   |
| 5           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 5           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob        |
| 5           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan       |
| 5           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 5           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob        |
| 5           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan       |
| 5           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 5           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 5           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 5           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob        |
| 5           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Dan       |
| 5           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |

#### Actions Round 6
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 6           | NPC Ann | Psychic  |          |          | successful  |
| 6           | NPC Bob | Medic    | NPC Ed   |          | successful  |
| 6           | NPC Cal | Spy      |          |          | successful  |
| 6           | NPC Ed  | Reporter | NPC Fae  |          | successful  |

#### States Round 6
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Ann | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ed  | Reporter | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Fae | Assassin | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Cal | Spy      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 6           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 6           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob        |
| 6           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 6           | NPC Ann | Psychic  | broadcast | I (NPC Ed) am the Reporter and NPC Fae is the Assassin        |
| 6           | NPC Ann | Psychic  | reveal    | Player: NPC Ed is not possessed                               |
| 6           | NPC Ann | Psychic  | reveal    | Player: NPC Bob is not possessed                              |
| 6           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 6           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob        |
| 6           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 6           | NPC Bob | Medic    | broadcast | I (NPC Ed) am the Reporter and NPC Fae is the Assassin        |
| 6           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 6           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob        |
| 6           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 6           | NPC Cal | Spy      | broadcast | I (NPC Ed) am the Reporter and NPC Fae is the Assassin        |
| 6           | NPC Cal | Spy      | reveal    | NPC Ed is targeting NPC Fae                                   |
| 6           | NPC Cal | Spy      | reveal    | NPC Bob is targeting NPC Ann                                  |
| 6           | NPC Cal | Spy      | reveal    | NPC Fae is targeting NPC Ed                                   |
| 6           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 6           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob        |
| 6           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 6           | NPC Dan | Priest   | broadcast | I (NPC Ed) am the Reporter and NPC Fae is the Assassin        |
| 6           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 6           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob        |
| 6           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 6           | NPC Ed  | Reporter | broadcast | I (NPC Ed) am the Reporter and NPC Fae is the Assassin        |
| 6           | NPC Ed  | Reporter | reveal    | NPC Fae is Assassin                                           |
| 6           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 6           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Bob        |
| 6           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ann       |
| 6           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 6           | NPC Fae | Assassin | broadcast | I (NPC Ed) am the Reporter and NPC Fae is the Assassin        |

#### Actions Round 7
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 7           | NPC Ann | Psychic  |          |          | successful  |
| 7           | NPC Bob | Medic    | NPC Fae  |          | successful  |
| 7           | NPC Cal | Spy      |          |          | successful  |
| 7           | NPC Ed  | Reporter | NPC Cal  |          | successful  |
| 7           | NPC Fae | Assassin | Priest   |          | successful  |

#### States Round 7
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Ann | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Ed  | Reporter | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Bob | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Fae | Assassin | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Cal | Spy      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Dan | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 7           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 7           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 7           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 7           | NPC Ann | Psychic  | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Spy             |
| 7           | NPC Ann | Psychic  | reveal    | Player: NPC Fae is not possessed                              |
| 7           | NPC Ann | Psychic  | reveal    | Player: NPC Ed is not possessed                               |
| 7           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 7           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 7           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 7           | NPC Bob | Medic    | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Spy             |
| 7           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 7           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 7           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 7           | NPC Cal | Spy      | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Spy             |
| 7           | NPC Cal | Spy      | reveal    | NPC Ed is targeting NPC Cal                                   |
| 7           | NPC Cal | Spy      | reveal    | NPC Bob is targeting NPC Ed                                   |
| 7           | NPC Cal | Spy      | reveal    | NPC Fae is targeting NPC Ed                                   |
| 7           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 7           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 7           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 7           | NPC Dan | Priest   | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Spy             |
| 7           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 7           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 7           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 7           | NPC Ed  | Reporter | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Spy             |
| 7           | NPC Ed  | Reporter | reveal    | NPC Cal is Spy                                                |
| 7           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 7           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 7           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Fae        |
| 7           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Ed        |
| 7           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Ed        |
| 7           | NPC Fae | Assassin | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Spy             |

#### Actions Round 8
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 8           | NPC Ann | Psychic  |          |          | successful  |
| 8           | NPC Bob | Medic    | NPC Cal  |          | successful  |
| 8           | NPC Cal | Spy      |          |          | successful  |
| 8           | NPC Fae | Assassin | Psychic  |          | successful  |

#### States Round 8
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Ann | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Ed  | Reporter | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Bob | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Fae | Assassin | False      | False     | False      | 2         | True   | 0              | 0                  |
| 8           | NPC Cal | Spy      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 8           | NPC Dan | Priest   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player  | Role     | message   | details                                                     |
| :-----------| :-------| :--------| :---------| :---------------------------------------------------------- |
| 8           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed   |
| 8           | NPC Ann | Psychic  | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed  |
| 8           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal      |
| 8           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Fae     |
| 8           | NPC Ann | Psychic  | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Dan     |
| 8           | NPC Ann | Psychic  | reveal    | Player: NPC Bob is not possessed                            |
| 8           | NPC Ann | Psychic  | reveal    | Player: NPC Fae is not possessed                            |
| 8           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed   |
| 8           | NPC Bob | Medic    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed  |
| 8           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal      |
| 8           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Fae     |
| 8           | NPC Bob | Medic    | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Dan     |
| 8           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed   |
| 8           | NPC Cal | Spy      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed  |
| 8           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal      |
| 8           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Fae     |
| 8           | NPC Cal | Spy      | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Dan     |
| 8           | NPC Cal | Spy      | reveal    | NPC Ed is targeting NPC Cal                                 |
| 8           | NPC Cal | Spy      | reveal    | NPC Bob is targeting NPC Fae                                |
| 8           | NPC Cal | Spy      | reveal    | NPC Fae is targeting NPC Dan                                |
| 8           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed   |
| 8           | NPC Dan | Priest   | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed  |
| 8           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal      |
| 8           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Fae     |
| 8           | NPC Dan | Priest   | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Dan     |
| 8           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed   |
| 8           | NPC Ed  | Reporter | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed  |
| 8           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal      |
| 8           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Fae     |
| 8           | NPC Ed  | Reporter | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Dan     |
| 8           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed   |
| 8           | NPC Fae | Assassin | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed  |
| 8           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Ed is targeting NPC Cal      |
| 8           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Bob is targeting NPC Fae     |
| 8           | NPC Fae | Assassin | broadcast | I (NPC Cal) am the Spy and NPC Fae is targeting NPC Dan     |