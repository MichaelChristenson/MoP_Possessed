#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 80   | 4       | 4       |

#### Roles
| Role     |
| :------- |
| Spy      |
| Demagog  |
| Priest   |
| Thief    |

#### States Round 0
| round_index | Player  | Role    | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Spy     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Demagog | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Priest  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Thief   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role    | message     | details                |
| :-----------| :-------| :-------| :-----------| :--------------------- |
| 0           | NPC Ann | Priest  | role change | Your Role is Priest    |
| 0           | NPC Ann | Priest  | possessed   | You are Not Possessed  |
| 0           | NPC Bob | Spy     | role change | Your Role is Spy       |
| 0           | NPC Bob | Spy     | possessed   | You are Possessed      |
| 0           | NPC Cal | Demagog | role change | Your Role is Demagog   |
| 0           | NPC Cal | Demagog | possessed   | You are Not Possessed  |
| 0           | NPC Dan | Thief   | role change | Your Role is Thief     |
| 0           | NPC Dan | Thief   | possessed   | You are Not Possessed  |

#### Actions Round 1
| round_index | Player  | action  | Target 1 | Target 2 | status              |
| :-----------| :-------| :-------| :--------| :--------| :------------------ |
| 1           | NPC Bob | Spy     |          |          | successful          |
| 1           | NPC Cal | Demagog | Priest   |          | voting in progress  |
| 1           | NPC Dan | Thief   | NPC Ann  |          | successful          |

#### States Round 1
| round_index | Player  | Role    | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Spy     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Demagog | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann | Priest  | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Dan | Thief   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role    | message   | details                                                      |
| :-----------| :-------| :-------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Priest  | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Ann | Priest  | vote      | Demagog has initiated a vote on eliminating Priest           |
| 1           | NPC Bob | Spy     | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Bob | Spy     | reveal    | NPC Dan is targeting NPC Ann                                 |
| 1           | NPC Bob | Spy     | vote      | Demagog has initiated a vote on eliminating Priest           |
| 1           | NPC Cal | Demagog | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Cal | Demagog | vote      | Demagog has initiated a vote on eliminating Priest           |
| 1           | NPC Dan | Thief   | broadcast | I (NPC Dan) am the Thief and I have made NPC Ann vulnerable  |
| 1           | NPC Dan | Thief   | vote      | Demagog has initiated a vote on eliminating Priest           |

#### Actions Round 2
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 2           | NPC Bob | Spy    |          |          | successful  |

#### States Round 2
| round_index | Player  | Role    | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Spy     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Demagog | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann | Priest  | False      | False     | True       | 0         | True   | 0              | 0                  |
| 2           | NPC Dan | Thief   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role    | message   | details                                                  |
| :-----------| :-------| :-------| :---------| :------------------------------------------------------- |
| 2           | NPC Ann | Priest  | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 2           | NPC Ann | Priest  | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 2           | NPC Bob | Spy     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 2           | NPC Bob | Spy     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 2           | NPC Bob | Spy     | reveal    | NPC Cal is targeting NPC Ann                             |
| 2           | NPC Bob | Spy     | reveal    | NPC Dan is targeting NPC Ann                             |
| 2           | NPC Cal | Demagog | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 2           | NPC Cal | Demagog | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |
| 2           | NPC Dan | Thief   | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann  |
| 2           | NPC Dan | Thief   | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann  |

#### Actions Round 3
| round_index | Player  | action  | Target 1 | Target 2 | status              |
| :-----------| :-------| :-------| :--------| :--------| :------------------ |
| 3           | NPC Bob | Spy     |          |          | successful          |
| 3           | NPC Cal | Demagog | Thief    |          | voting in progress  |
| 3           | NPC Dan | Thief   | NPC Cal  |          | successful          |

#### States Round 3
| round_index | Player  | Role    | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Spy     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Demagog | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Ann | Priest  | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Thief   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role    | message   | details                                                      |
| :-----------| :-------| :-------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann | Priest  | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann      |
| 3           | NPC Ann | Priest  | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann      |
| 3           | NPC Ann | Priest  | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable  |
| 3           | NPC Ann | Priest  | vote      | Demagog has initiated a vote on eliminating Thief            |
| 3           | NPC Bob | Spy     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann      |
| 3           | NPC Bob | Spy     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann      |
| 3           | NPC Bob | Spy     | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable  |
| 3           | NPC Bob | Spy     | reveal    | NPC Cal is targeting NPC Ann                                 |
| 3           | NPC Bob | Spy     | reveal    | NPC Dan is targeting NPC Cal                                 |
| 3           | NPC Bob | Spy     | vote      | Demagog has initiated a vote on eliminating Thief            |
| 3           | NPC Cal | Demagog | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann      |
| 3           | NPC Cal | Demagog | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann      |
| 3           | NPC Cal | Demagog | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable  |
| 3           | NPC Cal | Demagog | vote      | Demagog has initiated a vote on eliminating Thief            |
| 3           | NPC Dan | Thief   | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Ann      |
| 3           | NPC Dan | Thief   | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Ann      |
| 3           | NPC Dan | Thief   | broadcast | I (NPC Dan) am the Thief and I have made NPC Cal vulnerable  |
| 3           | NPC Dan | Thief   | vote      | Demagog has initiated a vote on eliminating Thief            |

#### Actions Round 4
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 4           | NPC Bob | Spy    |          |          | successful  |

#### States Round 4
| round_index | Player  | Role    | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Bob | Spy     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Demagog | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Ann | Priest  | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Dan | Thief   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role    | message   | details                                                  |
| :-----------| :-------| :-------| :---------| :------------------------------------------------------- |
| 4           | NPC Ann | Priest  | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan  |
| 4           | NPC Ann | Priest  | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Cal  |
| 4           | NPC Bob | Spy     | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan  |
| 4           | NPC Bob | Spy     | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Cal  |
| 4           | NPC Bob | Spy     | reveal    | NPC Cal is targeting NPC Dan                             |
| 4           | NPC Bob | Spy     | reveal    | NPC Dan is targeting NPC Cal                             |
| 4           | NPC Cal | Demagog | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan  |
| 4           | NPC Cal | Demagog | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Cal  |
| 4           | NPC Dan | Thief   | broadcast | I (NPC Bob) am the Spy and NPC Cal is targeting NPC Dan  |
| 4           | NPC Dan | Thief   | broadcast | I (NPC Bob) am the Spy and NPC Dan is targeting NPC Cal  |