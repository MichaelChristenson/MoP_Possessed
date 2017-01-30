#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 20   | 4       | 3       |

#### Roles
| Role      |
| :-------- |
| Psychic   |
| Demagog   |
| Reporter  |
| Jailer    |

#### States Round 0
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Bob | Psychic  | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Demagog  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Reporter | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Jailer   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role     | message     | details                |
| :-----------| :-------| :--------| :-----------| :--------------------- |
| 0           | NPC Ann | Reporter | role change | Your Role is Reporter  |
| 0           | NPC Ann | Reporter | possessed   | You are Not Possessed  |
| 0           | NPC Bob | Psychic  | role change | Your Role is Psychic   |
| 0           | NPC Bob | Psychic  | possessed   | You are Possessed      |
| 0           | NPC Cal | Demagog  | role change | Your Role is Demagog   |
| 0           | NPC Cal | Demagog  | possessed   | You are Not Possessed  |
| 0           | NPC Dan | Jailer   | role change | Your Role is Jailer    |
| 0           | NPC Dan | Jailer   | possessed   | You are Not Possessed  |

#### Actions Round 1
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 1           | NPC Ann | Reporter | NPC Cal  |          | successful          |
| 1           | NPC Bob | Psychic  |          |          | successful          |
| 1           | NPC Cal | Demagog  | Psychic  |          | voting in progress  |

#### States Round 1
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Bob | Psychic  | False      | True      | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Cal | Demagog  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann | Reporter | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Jailer   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 1           | NPC Ann | Reporter | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Demagog        |
| 1           | NPC Ann | Reporter | broadcast | I (NPC Bob) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Ann | Reporter | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Ann | Reporter | reveal    | NPC Cal is Demagog                                            |
| 1           | NPC Ann | Reporter | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 1           | NPC Bob | Psychic  | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Demagog        |
| 1           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Bob | Psychic  | reveal    | Player: NPC Dan is not possessed                              |
| 1           | NPC Bob | Psychic  | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 1           | NPC Cal | Demagog  | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Demagog        |
| 1           | NPC Cal | Demagog  | broadcast | I (NPC Bob) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Cal | Demagog  | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Cal | Demagog  | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 1           | NPC Dan | Jailer   | broadcast | I (NPC Ann) am the Reporter and NPC Cal is the Demagog        |
| 1           | NPC Dan | Jailer   | broadcast | I (NPC Bob) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Dan | Jailer   | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Dan | Jailer   | vote      | Demagog has initiated a vote on eliminating Psychic           |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Bob | Psychic |          |          | successful  |

#### States Round 2
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Bob | Psychic  | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Cal | Demagog  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann | Reporter | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Jailer   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 2           | NPC Ann | Reporter | broadcast | I (NPC Bob) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Ann | Reporter | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Bob | Psychic  | reveal    | Player: NPC Cal is not possessed                              |
| 2           | NPC Bob | Psychic  | reveal    | Player: NPC Dan is not possessed                              |
| 2           | NPC Cal | Demagog  | broadcast | I (NPC Bob) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Cal | Demagog  | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Dan | Jailer   | broadcast | I (NPC Bob) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Dan | Jailer   | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |

#### Actions Round 3
| round_index | Player  | action   | Target 1 | Target 2 | status              |
| :-----------| :-------| :--------| :--------| :--------| :------------------ |
| 3           | NPC Ann | Reporter | NPC Dan  |          | successful          |
| 3           | NPC Bob | Psychic  |          |          | successful          |
| 3           | NPC Cal | Demagog  | Jailer   |          | voting in progress  |

#### States Round 3
| round_index | Player  | Role     | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :--------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Bob | Psychic  | False      | True      | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Cal | Demagog  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ann | Reporter | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan | Jailer   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role     | message   | details                                                       |
| :-----------| :-------| :--------| :---------| :------------------------------------------------------------ |
| 3           | NPC Ann | Reporter | broadcast | I (NPC Ann) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Ann | Reporter | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Ann | Reporter | reveal    | NPC Dan is Jailer                                             |
| 3           | NPC Ann | Reporter | vote      | Demagog has initiated a vote on eliminating Jailer            |
| 3           | NPC Bob | Psychic  | broadcast | I (NPC Ann) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Bob | Psychic  | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Bob | Psychic  | reveal    | Player: NPC Cal is not possessed                              |
| 3           | NPC Bob | Psychic  | vote      | Demagog has initiated a vote on eliminating Jailer            |
| 3           | NPC Cal | Demagog  | broadcast | I (NPC Ann) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Cal | Demagog  | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Cal | Demagog  | vote      | Demagog has initiated a vote on eliminating Jailer            |
| 3           | NPC Dan | Jailer   | broadcast | I (NPC Ann) am the Reporter and NPC Dan is the Jailer         |
| 3           | NPC Dan | Jailer   | broadcast | I (NPC Bob) am the Psychic and the Reporter is not possessed  |
| 3           | NPC Dan | Jailer   | vote      | Demagog has initiated a vote on eliminating Jailer            |