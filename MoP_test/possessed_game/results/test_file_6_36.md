#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 36   | 6       | 7       |

#### Roles
| Role         |
| :----------- |
| Psychic      |
| Medic        |
| Reporter     |
| Executioner  |
| Judge        |
| Inspector    |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Ann | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Bob | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Bob | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Judge       | role change | Your Role is Judge        |
| 0           | NPC Cal | Judge       | possessed   | You are Possessed         |
| 0           | NPC Dan | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Dan | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Ed  | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Fae | Executioner | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 1           | NPC Ann | Psychic   |          |          | successful  |
| 1           | NPC Bob | Reporter  | NPC Dan  |          | successful  |
| 1           | NPC Cal | Judge     | Reporter |          | successful  |
| 1           | NPC Dan | Inspector | NPC Bob  |          | successful  |
| 1           | NPC Ed  | Medic     | NPC Bob  |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ed  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 1           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 1           | NPC Ann | Psychic     | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Inspector       |
| 1           | NPC Ann | Psychic     | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed       |
| 1           | NPC Ann | Psychic     | reveal    | Player: NPC Ed is not possessed                                |
| 1           | NPC Ann | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Inspector       |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed       |
| 1           | NPC Bob | Reporter    | reveal    | NPC Dan is Inspector                                           |
| 1           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 1           | NPC Cal | Judge       | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Inspector       |
| 1           | NPC Cal | Judge       | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed       |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Inspector       |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed       |
| 1           | NPC Dan | Inspector   | reveal    | Reporter is Innocent                                           |
| 1           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 1           | NPC Ed  | Medic       | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Inspector       |
| 1           | NPC Ed  | Medic       | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed       |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Bob) am the Reporter and NPC Dan is the Inspector       |
| 1           | NPC Fae | Executioner | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed       |

#### Actions Round 2
| round_index | Player  | action   | Target 1  | Target 2 | status      |
| :-----------| :-------| :--------| :---------| :--------| :---------- |
| 2           | NPC Ann | Psychic  |           |          | successful  |
| 2           | NPC Bob | Reporter | NPC Cal   |          | successful  |
| 2           | NPC Cal | Judge    | Inspector |          | successful  |
| 2           | NPC Ed  | Medic    | NPC Fae   |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 2           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 2           | NPC Ann | Psychic     | reveal    | Player: NPC Dan is not possessed                               |
| 2           | NPC Ann | Psychic     | reveal    | Player: NPC Fae is not possessed                               |
| 2           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 2           | NPC Bob | Reporter    | reveal    | NPC Cal is Judge                                               |
| 2           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 2           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 2           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |
| 2           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed      |

#### Actions Round 3
| round_index | Player  | action    | Target 1  | Target 2 | status      |
| :-----------| :-------| :---------| :---------| :--------| :---------- |
| 3           | NPC Ann | Psychic   |           |          | successful  |
| 3           | NPC Cal | Judge     | Inspector |          | successful  |
| 3           | NPC Dan | Inspector | NPC Cal   |          | successful  |
| 3           | NPC Ed  | Medic     | NPC Cal   |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ed  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 3           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Ann | Psychic     | broadcast | I (NPC Dan) inspected NPC Cal and they are possessed             |
| 3           | NPC Ann | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 3           | NPC Ann | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 3           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Bob | Reporter    | broadcast | I (NPC Dan) inspected NPC Cal and they are possessed             |
| 3           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Cal | Judge       | broadcast | I (NPC Dan) inspected NPC Cal and they are possessed             |
| 3           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Dan | Inspector   | broadcast | I (NPC Dan) inspected NPC Cal and they are possessed             |
| 3           | NPC Dan | Inspector   | reveal    | Judge is Possessed                                               |
| 3           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Ed  | Medic       | broadcast | I (NPC Dan) inspected NPC Cal and they are possessed             |
| 3           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Fae | Executioner | broadcast | I (NPC Dan) inspected NPC Cal and they are possessed             |

#### Actions Round 4
| round_index | Player  | action      | Target 1 | Target 2 | status      |
| :-----------| :-------| :-----------| :--------| :--------| :---------- |
| 4           | NPC Ann | Psychic     |          |          | successful  |
| 4           | NPC Bob | Reporter    | NPC Fae  |          | successful  |
| 4           | NPC Cal | Judge       | Reporter |          | successful  |
| 4           | NPC Ed  | Medic       | NPC Dan  |          | successful  |
| 4           | NPC Fae | Executioner | NPC Cal  |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Fae | Executioner | False      | False     | False      | 4         | True   | 0              | 0                  |
| 4           | NPC Cal | Judge       | True       | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message     | details                                                          |
| :-----------| :-------| :-----------| :-----------| :--------------------------------------------------------------- |
| 4           | NPC Ann | Psychic     | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Ann | Psychic     | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ann | Psychic     | broadcast   | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 4           | NPC Ann | Psychic     | elimination | NPC Cal has been eliminated                                      |
| 4           | NPC Ann | Psychic     | reveal      | Player: NPC Ed is not possessed                                  |
| 4           | NPC Ann | Psychic     | reveal      | Player: NPC Dan is not possessed                                 |
| 4           | NPC Ann | Psychic     | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 4           | NPC Bob | Reporter    | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Bob | Reporter    | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Bob | Reporter    | broadcast   | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 4           | NPC Bob | Reporter    | elimination | NPC Cal has been eliminated                                      |
| 4           | NPC Bob | Reporter    | reveal      | NPC Fae is Executioner                                           |
| 4           | NPC Bob | Reporter    | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 4           | NPC Cal | Judge       | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Cal | Judge       | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Cal | Judge       | broadcast   | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 4           | NPC Cal | Judge       | elimination | NPC Cal has been eliminated                                      |
| 4           | NPC Cal | Judge       | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 4           | NPC Dan | Inspector   | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Dan | Inspector   | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Dan | Inspector   | broadcast   | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 4           | NPC Dan | Inspector   | elimination | NPC Cal has been eliminated                                      |
| 4           | NPC Dan | Inspector   | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 4           | NPC Ed  | Medic       | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Ed  | Medic       | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ed  | Medic       | broadcast   | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 4           | NPC Ed  | Medic       | elimination | NPC Cal has been eliminated                                      |
| 4           | NPC Ed  | Medic       | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 4           | NPC Fae | Executioner | broadcast   | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 4           | NPC Fae | Executioner | broadcast   | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Fae | Executioner | broadcast   | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 4           | NPC Fae | Executioner | elimination | NPC Cal has been eliminated                                      |
| 4           | NPC Fae | Executioner | game over   | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |

#### Actions Round 5
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 5           | NPC Ann | Psychic   |          |          | successful  |
| 5           | NPC Cal | Judge     | Psychic  |          | successful  |
| 5           | NPC Dan | Inspector | NPC Ed   |          | successful  |
| 5           | NPC Ed  | Medic     | NPC Bob  |          | successful  |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Ed  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Fae | Executioner | False      | False     | False      | 3         | True   | 0              | 0                  |
| 5           | NPC Cal | Judge       | True       | True      | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 5           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 5           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 5           | NPC Ann | Psychic     | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 5           | NPC Ann | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 5           | NPC Ann | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 5           | NPC Ann | Psychic     | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 5           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 5           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 5           | NPC Bob | Reporter    | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 5           | NPC Bob | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 5           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 5           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 5           | NPC Cal | Judge       | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 5           | NPC Cal | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 5           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 5           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 5           | NPC Dan | Inspector   | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 5           | NPC Dan | Inspector   | reveal    | Medic is Innocent                                                |
| 5           | NPC Dan | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 5           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 5           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 5           | NPC Ed  | Medic       | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 5           | NPC Ed  | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 5           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 5           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 5           | NPC Fae | Executioner | broadcast | I (NPC Dan) inspected NPC Ed and they are not possessed          |
| 5           | NPC Fae | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |

#### Actions Round 6
| round_index | Player  | action   | Target 1  | Target 2 | status      |
| :-----------| :-------| :--------| :---------| :--------| :---------- |
| 6           | NPC Ann | Psychic  |           |          | successful  |
| 6           | NPC Bob | Reporter | NPC Ann   |          | successful  |
| 6           | NPC Cal | Judge    | Inspector |          | successful  |
| 6           | NPC Ed  | Medic    | NPC Fae   |          | successful  |

#### States Round 6
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ed  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Judge       | True       | True      | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Dan | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 6           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 6           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Ann | Psychic     | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Psychic         |
| 6           | NPC Ann | Psychic     | reveal    | Player: NPC Dan is not possessed                               |
| 6           | NPC Ann | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 6           | NPC Ann | Psychic     | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!               |
| 6           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 6           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Bob | Reporter    | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Psychic         |
| 6           | NPC Bob | Reporter    | reveal    | NPC Ann is Psychic                                             |
| 6           | NPC Bob | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!               |
| 6           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 6           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Cal | Judge       | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Psychic         |
| 6           | NPC Cal | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!               |
| 6           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 6           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Dan | Inspector   | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Psychic         |
| 6           | NPC Dan | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!               |
| 6           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 6           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Ed  | Medic       | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Psychic         |
| 6           | NPC Ed  | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!               |
| 6           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed   |
| 6           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed  |
| 6           | NPC Fae | Executioner | broadcast | I (NPC Bob) am the Reporter and NPC Ann is the Psychic         |
| 6           | NPC Fae | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!               |

#### Actions Round 7
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 7           | NPC Ann | Psychic   |          |          | successful  |
| 7           | NPC Cal | Judge     | Medic    |          | successful  |
| 7           | NPC Dan | Inspector | NPC Ann  |          | successful  |
| 7           | NPC Ed  | Medic     | NPC Dan  |          | successful  |

#### States Round 7
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Ann | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Ed  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Bob | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Fae | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Cal | Judge       | True       | True      | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Dan | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 7           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 7           | NPC Ann | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 7           | NPC Ann | Psychic     | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed         |
| 7           | NPC Ann | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 7           | NPC Ann | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 7           | NPC Ann | Psychic     | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 7           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 7           | NPC Bob | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 7           | NPC Bob | Reporter    | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed         |
| 7           | NPC Bob | Reporter    | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 7           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 7           | NPC Cal | Judge       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 7           | NPC Cal | Judge       | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed         |
| 7           | NPC Cal | Judge       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 7           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 7           | NPC Dan | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 7           | NPC Dan | Inspector   | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed         |
| 7           | NPC Dan | Inspector   | reveal    | Psychic is Innocent                                              |
| 7           | NPC Dan | Inspector   | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 7           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 7           | NPC Ed  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 7           | NPC Ed  | Medic       | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed         |
| 7           | NPC Ed  | Medic       | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |
| 7           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 7           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Reporter is not possessed     |
| 7           | NPC Fae | Executioner | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 7           | NPC Fae | Executioner | broadcast | I (NPC Dan) inspected NPC Ann and they are not possessed         |
| 7           | NPC Fae | Executioner | game over | NPC Ann, NPC Ed, NPC Bob, NPC Fae, NPC Dan Wins!                 |