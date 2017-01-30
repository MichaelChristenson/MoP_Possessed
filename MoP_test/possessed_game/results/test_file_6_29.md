#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 29   | 6       | 8       |

#### Roles
| Role      |
| :-------- |
| Trader    |
| Thief     |
| Judge     |
| Medic     |
| Reporter  |
| Psychic   |

#### States Round 0
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Trader   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Thief    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Reporter | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Psychic  | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role     | message     | details                |
| :-----------| :-------| :--------| :-----------| :--------------------- |
| 0           | NPC Ann | Trader   | role change | Your Role is Trader    |
| 0           | NPC Ann | Trader   | possessed   | You are Not Possessed  |
| 0           | NPC Bob | Judge    | role change | Your Role is Judge     |
| 0           | NPC Bob | Judge    | possessed   | You are Not Possessed  |
| 0           | NPC Cal | Reporter | role change | Your Role is Reporter  |
| 0           | NPC Cal | Reporter | possessed   | You are Possessed      |
| 0           | NPC Dan | Psychic  | role change | Your Role is Psychic   |
| 0           | NPC Dan | Psychic  | possessed   | You are Not Possessed  |
| 0           | NPC Ed  | Thief    | role change | Your Role is Thief     |
| 0           | NPC Ed  | Thief    | possessed   | You are Not Possessed  |
| 0           | NPC Fae | Medic    | role change | Your Role is Medic     |
| 0           | NPC Fae | Medic    | possessed   | You are Not Possessed  |

#### Actions Round 1
| round_index | Player  | action   | Target 1 | Target 2 | status                         |
| :-----------| :-------| :--------| :--------| :--------| :----------------------------- |
| 1           | NPC Ann | Trader   | NPC Cal  | NPC Bob  | failed because not vulnerable  |
| 1           | NPC Bob | Judge    | Reporter |          | successful                     |
| 1           | NPC Cal | Reporter | NPC Ed   |          | successful                     |
| 1           | NPC Dan | Psychic  |          |          | successful                     |
| 1           | NPC Ed  | Thief    | NPC Cal  |          | successful                     |
| 1           | NPC Fae | Medic    | NPC Ed   |          | successful                     |

#### States Round 1
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Trader   | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Ed  | Thief    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Judge    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Reporter | False      | True      | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role     | message   | details                                                     |
| :-----------| :-------| :--------| :---------| :---------------------------------------------------------- |
| 1           | NPC Ann | Trader   | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Thief         |
| 1           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 1           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed   |
| 1           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 1           | NPC Ann | Trader   | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Bob | Judge    | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Thief         |
| 1           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 1           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed   |
| 1           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 1           | NPC Bob | Judge    | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Cal | Reporter | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Thief         |
| 1           | NPC Cal | Reporter | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 1           | NPC Cal | Reporter | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed   |
| 1           | NPC Cal | Reporter | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 1           | NPC Cal | Reporter | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Cal | Reporter | reveal    | NPC Ed is Thief                                             |
| 1           | NPC Dan | Psychic  | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Thief         |
| 1           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 1           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed   |
| 1           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 1           | NPC Dan | Psychic  | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Dan | Psychic  | reveal    | Player: NPC Ed is not possessed                             |
| 1           | NPC Dan | Psychic  | reveal    | Player: NPC Bob is not possessed                            |
| 1           | NPC Ed  | Thief    | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Thief         |
| 1           | NPC Ed  | Thief    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 1           | NPC Ed  | Thief    | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed   |
| 1           | NPC Ed  | Thief    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 1           | NPC Ed  | Thief    | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |
| 1           | NPC Fae | Medic    | broadcast | I (NPC Cal) am the Reporter and NPC Ed is the Thief         |
| 1           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 1           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed   |
| 1           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 1           | NPC Fae | Medic    | broadcast | I (NPC Ed) am the Thief and I have made NPC Cal vulnerable  |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Bob | Judge   | Thief    |          | successful  |
| 2           | NPC Dan | Psychic |          |          | successful  |
| 2           | NPC Ed  | Thief   | NPC Bob  |          | successful  |
| 2           | NPC Fae | Medic   | NPC Bob  |          | successful  |

#### States Round 2
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ann | Trader   | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Ed  | Thief    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Bob | Judge    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 2           | NPC Fae | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Reporter | False      | True      | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role     | message   | details                                                     |
| :-----------| :-------| :--------| :---------| :---------------------------------------------------------- |
| 2           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 2           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 2           | NPC Ann | Trader   | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 2           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 2           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 2           | NPC Bob | Judge    | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 2           | NPC Cal | Reporter | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 2           | NPC Cal | Reporter | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 2           | NPC Cal | Reporter | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 2           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 2           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 2           | NPC Dan | Psychic  | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 2           | NPC Dan | Psychic  | reveal    | Player: NPC Fae is not possessed                            |
| 2           | NPC Dan | Psychic  | reveal    | Player: NPC Ann is not possessed                            |
| 2           | NPC Ed  | Thief    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 2           | NPC Ed  | Thief    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 2           | NPC Ed  | Thief    | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |
| 2           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 2           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 2           | NPC Fae | Medic    | broadcast | I (NPC Ed) am the Thief and I have made NPC Bob vulnerable  |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 3           | NPC Bob | Judge    | Reporter |          | successful  |
| 3           | NPC Cal | Reporter | NPC Bob  |          | successful  |
| 3           | NPC Dan | Psychic  |          |          | successful  |
| 3           | NPC Fae | Medic    | NPC Cal  |          | successful  |

#### States Round 3
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ann | Trader   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ed  | Thief    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Bob | Judge    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Fae | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Reporter | False      | True      | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role     | message   | details                                                    |
| :-----------| :-------| :--------| :---------| :--------------------------------------------------------- |
| 3           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed  |
| 3           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed  |
| 3           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed  |
| 3           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed  |
| 3           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed  |
| 3           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed  |
| 3           | NPC Cal | Reporter | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed  |
| 3           | NPC Cal | Reporter | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed  |
| 3           | NPC Cal | Reporter | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed  |
| 3           | NPC Cal | Reporter | reveal    | NPC Bob is Judge                                           |
| 3           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed  |
| 3           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed  |
| 3           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed  |
| 3           | NPC Dan | Psychic  | reveal    | Player: NPC Ed is not possessed                            |
| 3           | NPC Dan | Psychic  | reveal    | Player: NPC Fae is not possessed                           |
| 3           | NPC Ed  | Thief    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed  |
| 3           | NPC Ed  | Thief    | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed  |
| 3           | NPC Ed  | Thief    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed  |
| 3           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed  |
| 3           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed  |
| 3           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed  |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 4           | NPC Bob | Judge    | Medic    |          | successful  |
| 4           | NPC Cal | Reporter | NPC Ann  |          | successful  |
| 4           | NPC Dan | Psychic  |          |          | successful  |
| 4           | NPC Ed  | Thief    | NPC Ann  |          | successful  |
| 4           | NPC Fae | Medic    | NPC Dan  |          | successful  |

#### States Round 4
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ann | Trader   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Ed  | Thief    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Bob | Judge    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Fae | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Reporter | False      | True      | True       | 2         | True   | 0              | 0                  |
| 4           | NPC Dan | Psychic  | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role     | message   | details                                                     |
| :-----------| :-------| :--------| :---------| :---------------------------------------------------------- |
| 4           | NPC Ann | Trader   | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Trader       |
| 4           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 4           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed  |
| 4           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 4           | NPC Ann | Trader   | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 4           | NPC Bob | Judge    | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Trader       |
| 4           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 4           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed  |
| 4           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 4           | NPC Bob | Judge    | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 4           | NPC Cal | Reporter | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Trader       |
| 4           | NPC Cal | Reporter | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 4           | NPC Cal | Reporter | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed  |
| 4           | NPC Cal | Reporter | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 4           | NPC Cal | Reporter | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 4           | NPC Cal | Reporter | reveal    | NPC Ann is Trader                                           |
| 4           | NPC Dan | Psychic  | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Trader       |
| 4           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 4           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed  |
| 4           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 4           | NPC Dan | Psychic  | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 4           | NPC Dan | Psychic  | reveal    | Player: NPC Fae is not possessed                            |
| 4           | NPC Dan | Psychic  | reveal    | Player: NPC Bob is not possessed                            |
| 4           | NPC Ed  | Thief    | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Trader       |
| 4           | NPC Ed  | Thief    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 4           | NPC Ed  | Thief    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed  |
| 4           | NPC Ed  | Thief    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 4           | NPC Ed  | Thief    | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |
| 4           | NPC Fae | Medic    | broadcast | I (NPC Cal) am the Reporter and NPC Ann is the Trader       |
| 4           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 4           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed  |
| 4           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed   |
| 4           | NPC Fae | Medic    | broadcast | I (NPC Ed) am the Thief and I have made NPC Ann vulnerable  |

#### Actions Round 5
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 5           | NPC Ann | Trader  | NPC Cal  | NPC Ed   | successful  |
| 5           | NPC Bob | Judge   | Thief    |          | successful  |
| 5           | NPC Dan | Psychic |          |          | successful  |
| 5           | NPC Fae | Medic   | NPC Ann  |          | successful  |

#### States Round 5
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ann | Trader   | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Reporter | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob | Judge    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Fae | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Cal | Thief    | False      | True      | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role     | message   | details                                                     |
| :-----------| :-------| :--------| :---------| :---------------------------------------------------------- |
| 5           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 5           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed  |
| 5           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed   |
| 5           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 5           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed  |
| 5           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed   |
| 5           | NPC Cal | Thief    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 5           | NPC Cal | Thief    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed  |
| 5           | NPC Cal | Thief    | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed   |
| 5           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 5           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed  |
| 5           | NPC Dan | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed   |
| 5           | NPC Dan | Psychic  | reveal    | Player: NPC Ann is not possessed                            |
| 5           | NPC Dan | Psychic  | reveal    | Player: NPC Ed is not possessed                             |
| 5           | NPC Ed  | Reporter | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 5           | NPC Ed  | Reporter | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed  |
| 5           | NPC Ed  | Reporter | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed   |
| 5           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed   |
| 5           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed  |
| 5           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed   |

#### Actions Round 6
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 6           | NPC Ann | Trader   | NPC Dan  | NPC Ed   | successful  |
| 6           | NPC Bob | Judge    | Psychic  |          | successful  |
| 6           | NPC Cal | Thief    | NPC Dan  |          | successful  |
| 6           | NPC Dan | Psychic  |          |          | successful  |
| 6           | NPC Ed  | Reporter | NPC Cal  |          | successful  |
| 6           | NPC Fae | Medic    | NPC Ed   |          | successful  |

#### States Round 6
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Ann | Trader   | False      | False     | True       | 4         | True   | 0              | 0                  |
| 6           | NPC Ed  | Psychic  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Judge    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Fae | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Thief    | False      | True      | True       | 2         | True   | 0              | 0                  |
| 6           | NPC Dan | Reporter | False      | False     | True       | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 6           | NPC Ann | Trader   | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable   |
| 6           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed     |
| 6           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed     |
| 6           | NPC Ann | Trader   | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Thief           |
| 6           | NPC Bob | Judge    | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable   |
| 6           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed     |
| 6           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed     |
| 6           | NPC Bob | Judge    | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Thief           |
| 6           | NPC Cal | Thief    | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable   |
| 6           | NPC Cal | Thief    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed     |
| 6           | NPC Cal | Thief    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Cal | Thief    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed     |
| 6           | NPC Cal | Thief    | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Thief           |
| 6           | NPC Dan | Reporter | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable   |
| 6           | NPC Dan | Reporter | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed     |
| 6           | NPC Dan | Reporter | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Dan | Reporter | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed     |
| 6           | NPC Dan | Reporter | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Thief           |
| 6           | NPC Dan | Reporter | reveal    | Player: NPC Ann is not possessed                              |
| 6           | NPC Dan | Reporter | reveal    | Player: NPC Fae is not possessed                              |
| 6           | NPC Ed  | Psychic  | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable   |
| 6           | NPC Ed  | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed     |
| 6           | NPC Ed  | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Ed  | Psychic  | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed     |
| 6           | NPC Ed  | Psychic  | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Thief           |
| 6           | NPC Ed  | Psychic  | reveal    | NPC Cal is Thief                                              |
| 6           | NPC Fae | Medic    | broadcast | I (NPC Cal) am the Thief and I have made NPC Dan vulnerable   |
| 6           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Medic is not possessed     |
| 6           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 6           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Psychic and the Judge is not possessed     |
| 6           | NPC Fae | Medic    | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Thief           |

#### Actions Round 7
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 7           | NPC Bob | Judge    | Medic    |          | successful  |
| 7           | NPC Dan | Reporter | NPC Fae  |          | successful  |
| 7           | NPC Ed  | Psychic  |          |          | successful  |
| 7           | NPC Fae | Medic    | NPC Bob  |          | successful  |

#### States Round 7
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Ann | Trader   | False      | False     | True       | 3         | True   | 0              | 0                  |
| 7           | NPC Ed  | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Bob | Judge    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Fae | Medic    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Cal | Thief    | False      | True      | True       | 1         | True   | 0              | 0                  |
| 7           | NPC Dan | Reporter | False      | False     | True       | 2         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role     | message   | details                                                    |
| :-----------| :-------| :--------| :---------| :--------------------------------------------------------- |
| 7           | NPC Ann | Trader   | broadcast | I (NPC Dan) am the Reporter and NPC Fae is the Medic       |
| 7           | NPC Ann | Trader   | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed  |
| 7           | NPC Ann | Trader   | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed   |
| 7           | NPC Bob | Judge    | broadcast | I (NPC Dan) am the Reporter and NPC Fae is the Medic       |
| 7           | NPC Bob | Judge    | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed  |
| 7           | NPC Bob | Judge    | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed   |
| 7           | NPC Cal | Thief    | broadcast | I (NPC Dan) am the Reporter and NPC Fae is the Medic       |
| 7           | NPC Cal | Thief    | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed  |
| 7           | NPC Cal | Thief    | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed   |
| 7           | NPC Dan | Reporter | broadcast | I (NPC Dan) am the Reporter and NPC Fae is the Medic       |
| 7           | NPC Dan | Reporter | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed  |
| 7           | NPC Dan | Reporter | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed   |
| 7           | NPC Dan | Reporter | reveal    | NPC Fae is Medic                                           |
| 7           | NPC Ed  | Psychic  | broadcast | I (NPC Dan) am the Reporter and NPC Fae is the Medic       |
| 7           | NPC Ed  | Psychic  | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed  |
| 7           | NPC Ed  | Psychic  | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed   |
| 7           | NPC Ed  | Psychic  | reveal    | Player: NPC Bob is not possessed                           |
| 7           | NPC Ed  | Psychic  | reveal    | Player: NPC Dan is not possessed                           |
| 7           | NPC Fae | Medic    | broadcast | I (NPC Dan) am the Reporter and NPC Fae is the Medic       |
| 7           | NPC Fae | Medic    | broadcast | I (NPC Ed) am the Psychic and the Trader is not possessed  |
| 7           | NPC Fae | Medic    | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed   |

#### Actions Round 8
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 8           | NPC Bob | Judge   | Reporter |          | successful  |
| 8           | NPC Cal | Thief   | NPC Fae  |          | successful  |
| 8           | NPC Ed  | Psychic |          |          | successful  |
| 8           | NPC Fae | Medic   | NPC Cal  |          | successful  |

#### States Round 8
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 8           | NPC Ann | Trader   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 8           | NPC Ed  | Psychic  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 8           | NPC Bob | Judge    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Fae | Medic    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Cal | Thief    | False      | True      | True       | 0         | True   | 0              | 0                  |
| 8           | NPC Dan | Reporter | False      | False     | True       | 1         | True   | 0              | 0                  |

#### Notifications Round 8
| round_index | Player  | Role     | message   | details                                                      |
| :-----------| :-------| :--------| :---------| :----------------------------------------------------------- |
| 8           | NPC Ann | Trader   | broadcast | I (NPC Cal) am the Thief and I have made NPC Fae vulnerable  |
| 8           | NPC Ann | Trader   | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed     |
| 8           | NPC Ann | Trader   | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 8           | NPC Bob | Judge    | broadcast | I (NPC Cal) am the Thief and I have made NPC Fae vulnerable  |
| 8           | NPC Bob | Judge    | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed     |
| 8           | NPC Bob | Judge    | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 8           | NPC Cal | Thief    | broadcast | I (NPC Cal) am the Thief and I have made NPC Fae vulnerable  |
| 8           | NPC Cal | Thief    | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed     |
| 8           | NPC Cal | Thief    | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 8           | NPC Dan | Reporter | broadcast | I (NPC Cal) am the Thief and I have made NPC Fae vulnerable  |
| 8           | NPC Dan | Reporter | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed     |
| 8           | NPC Dan | Reporter | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 8           | NPC Ed  | Psychic  | broadcast | I (NPC Cal) am the Thief and I have made NPC Fae vulnerable  |
| 8           | NPC Ed  | Psychic  | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed     |
| 8           | NPC Ed  | Psychic  | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |
| 8           | NPC Ed  | Psychic  | reveal    | Player: NPC Bob is not possessed                             |
| 8           | NPC Ed  | Psychic  | reveal    | Player: NPC Dan is not possessed                             |
| 8           | NPC Fae | Medic    | broadcast | I (NPC Cal) am the Thief and I have made NPC Fae vulnerable  |
| 8           | NPC Fae | Medic    | broadcast | I (NPC Ed) am the Psychic and the Judge is not possessed     |
| 8           | NPC Fae | Medic    | broadcast | I (NPC Ed) am the Psychic and the Medic is not possessed     |