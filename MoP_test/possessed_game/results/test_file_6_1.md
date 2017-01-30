#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 1    | 6       | 7       |

#### Roles
| Role       |
| :--------- |
| Inspector  |
| Demagog    |
| Jailer     |
| Prophet    |
| Psychic    |
| Judge      |

#### States Round 0
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Ann | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Demagog   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Psychic   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role      | message     | details                 |
| :-----------| :-------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Ann | Inspector | possessed   | You are Not Possessed   |
| 0           | NPC Bob | Jailer    | role change | Your Role is Jailer     |
| 0           | NPC Bob | Jailer    | possessed   | You are Not Possessed   |
| 0           | NPC Cal | Psychic   | role change | Your Role is Psychic    |
| 0           | NPC Cal | Psychic   | possessed   | You are Possessed       |
| 0           | NPC Dan | Judge     | role change | Your Role is Judge      |
| 0           | NPC Dan | Judge     | possessed   | You are Not Possessed   |
| 0           | NPC Ed  | Demagog   | role change | Your Role is Demagog    |
| 0           | NPC Ed  | Demagog   | possessed   | You are Not Possessed   |
| 0           | NPC Fae | Prophet   | role change | Your Role is Prophet    |
| 0           | NPC Fae | Prophet   | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player  | action    | Target 1 | Target 2 | status              |
| :-----------| :-------| :---------| :--------| :--------| :------------------ |
| 1           | NPC Ann | Inspector | NPC Cal  |          | successful          |
| 1           | NPC Cal | Psychic   |          |          | successful          |
| 1           | NPC Dan | Judge     | Psychic  |          | successful          |
| 1           | NPC Ed  | Demagog   | Psychic  |          | voting in progress  |
| 1           | NPC Fae | Prophet   | NPC Bob  |          | successful          |

#### States Round 1
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Ann | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed  | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Psychic   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 1           | NPC Ann | Inspector | broadcast | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 1           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 1           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 1           | NPC Ann | Inspector | reveal    | Psychic is Possessed                                         |
| 1           | NPC Ann | Inspector | vote      | Demagog has initiated a vote on eliminating Psychic          |
| 1           | NPC Bob | Jailer    | broadcast | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 1           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 1           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 1           | NPC Bob | Jailer    | vote      | Demagog has initiated a vote on eliminating Psychic          |
| 1           | NPC Cal | Psychic   | broadcast | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 1           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 1           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 1           | NPC Cal | Psychic   | reveal    | Player: NPC Dan is not possessed                             |
| 1           | NPC Cal | Psychic   | reveal    | Player: NPC Fae is not possessed                             |
| 1           | NPC Cal | Psychic   | vote      | Demagog has initiated a vote on eliminating Psychic          |
| 1           | NPC Dan | Judge     | broadcast | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 1           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 1           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 1           | NPC Dan | Judge     | vote      | Demagog has initiated a vote on eliminating Psychic          |
| 1           | NPC Ed  | Demagog   | broadcast | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 1           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 1           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 1           | NPC Ed  | Demagog   | vote      | Demagog has initiated a vote on eliminating Psychic          |
| 1           | NPC Fae | Prophet   | broadcast | I (NPC Ann) inspected NPC Cal and they are possessed         |
| 1           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 1           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 1           | NPC Fae | Prophet   | vote      | Demagog has initiated a vote on eliminating Psychic          |

#### Actions Round 2
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 2           | NPC Cal | Psychic |          |          | successful  |
| 2           | NPC Dan | Judge   | Psychic  |          | successful  |
| 2           | NPC Fae | Prophet | NPC Bob  |          | successful  |

#### States Round 2
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Ann | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed  | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Bob | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Psychic   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 2           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 2           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Cal | Psychic   | reveal    | Player: NPC Ed is not possessed                                |
| 2           | NPC Cal | Psychic   | reveal    | Player: NPC Bob is not possessed                               |
| 2           | NPC Cal | Psychic   | reveal    | Player: NPC Fae is not possessed                               |
| 2           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 2           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 2           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |
| 2           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 2           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed      |

#### Actions Round 3
| round_index | Player  | action    | Target 1 | Target 2 | status              |
| :-----------| :-------| :---------| :--------| :--------| :------------------ |
| 3           | NPC Ann | Inspector | NPC Dan  |          | successful          |
| 3           | NPC Cal | Psychic   |          |          | successful          |
| 3           | NPC Dan | Judge     | Psychic  |          | successful          |
| 3           | NPC Ed  | Demagog   | Judge    |          | voting in progress  |
| 3           | NPC Fae | Prophet   | NPC Ann  |          | successful          |

#### States Round 3
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Ann | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ed  | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Bob | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Fae | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Cal | Psychic   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed     |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 3           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed    |
| 3           | NPC Ann | Inspector | reveal    | Judge is Innocent                                            |
| 3           | NPC Ann | Inspector | vote      | Demagog has initiated a vote on eliminating Judge            |
| 3           | NPC Bob | Jailer    | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed     |
| 3           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 3           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed    |
| 3           | NPC Bob | Jailer    | vote      | Demagog has initiated a vote on eliminating Judge            |
| 3           | NPC Cal | Psychic   | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed     |
| 3           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 3           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed    |
| 3           | NPC Cal | Psychic   | reveal    | Player: NPC Ann is not possessed                             |
| 3           | NPC Cal | Psychic   | reveal    | Player: NPC Dan is not possessed                             |
| 3           | NPC Cal | Psychic   | reveal    | Player: NPC Fae is not possessed                             |
| 3           | NPC Cal | Psychic   | vote      | Demagog has initiated a vote on eliminating Judge            |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed     |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 3           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed    |
| 3           | NPC Dan | Judge     | vote      | Demagog has initiated a vote on eliminating Judge            |
| 3           | NPC Ed  | Demagog   | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed     |
| 3           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 3           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed    |
| 3           | NPC Ed  | Demagog   | vote      | Demagog has initiated a vote on eliminating Judge            |
| 3           | NPC Fae | Prophet   | broadcast | I (NPC Ann) inspected NPC Dan and they are not possessed     |
| 3           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 3           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Judge is not possessed    |
| 3           | NPC Fae | Prophet   | vote      | Demagog has initiated a vote on eliminating Judge            |

#### Actions Round 4
| round_index | Player  | action  | Target 1  | Target 2 | status      |
| :-----------| :-------| :-------| :---------| :--------| :---------- |
| 4           | NPC Cal | Psychic |           |          | successful  |
| 4           | NPC Dan | Judge   | Inspector |          | successful  |
| 4           | NPC Fae | Prophet | NPC Ed    |          | successful  |

#### States Round 4
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Ann | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed  | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Bob | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Cal | Psychic   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 4           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 4           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 4           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 4           | NPC Cal | Psychic   | reveal    | Player: NPC Ann is not possessed                               |
| 4           | NPC Cal | Psychic   | reveal    | Player: NPC Ed is not possessed                                |
| 4           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 4           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |
| 4           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed     |

#### Actions Round 5
| round_index | Player  | action    | Target 1  | Target 2 | status              |
| :-----------| :-------| :---------| :---------| :--------| :------------------ |
| 5           | NPC Ann | Inspector | NPC Bob   |          | successful          |
| 5           | NPC Cal | Psychic   |           |          | successful          |
| 5           | NPC Dan | Judge     | Psychic   |          | successful          |
| 5           | NPC Ed  | Demagog   | Inspector |          | voting in progress  |
| 5           | NPC Fae | Prophet   | NPC Bob   |          | successful          |

#### States Round 5
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Ann | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Ed  | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Bob | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Fae | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Cal | Psychic   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player  | Role      | message   | details                                                        |
| :-----------| :-------| :---------| :---------| :------------------------------------------------------------- |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Ann) inspected NPC Bob and they are not possessed       |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ann | Inspector | reveal    | Jailer is Innocent                                             |
| 5           | NPC Ann | Inspector | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 5           | NPC Bob | Jailer    | broadcast | I (NPC Ann) inspected NPC Bob and they are not possessed       |
| 5           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Bob | Jailer    | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 5           | NPC Cal | Psychic   | broadcast | I (NPC Ann) inspected NPC Bob and they are not possessed       |
| 5           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Cal | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 5           | NPC Cal | Psychic   | reveal    | Player: NPC Bob is not possessed                               |
| 5           | NPC Cal | Psychic   | reveal    | Player: NPC Ed is not possessed                                |
| 5           | NPC Cal | Psychic   | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 5           | NPC Dan | Judge     | broadcast | I (NPC Ann) inspected NPC Bob and they are not possessed       |
| 5           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Dan | Judge     | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 5           | NPC Ed  | Demagog   | broadcast | I (NPC Ann) inspected NPC Bob and they are not possessed       |
| 5           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ed  | Demagog   | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 5           | NPC Fae | Prophet   | broadcast | I (NPC Ann) inspected NPC Bob and they are not possessed       |
| 5           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Fae | Prophet   | vote      | Demagog has initiated a vote on eliminating Inspector          |

#### Actions Round 6
| round_index | Player  | action  | Target 1 | Target 2 | status      |
| :-----------| :-------| :-------| :--------| :--------| :---------- |
| 6           | NPC Cal | Psychic |          |          | successful  |
| 6           | NPC Dan | Judge   | Prophet  |          | successful  |
| 6           | NPC Fae | Prophet | NPC Bob  |          | successful  |

#### States Round 6
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Ann | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ed  | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Bob | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Fae | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Cal | Psychic   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 6           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 6           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 6           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 6           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 6           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 6           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 6           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 6           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 6           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 6           | NPC Cal | Psychic   | reveal    | Player: NPC Ann is not possessed                             |
| 6           | NPC Cal | Psychic   | reveal    | Player: NPC Bob is not possessed                             |
| 6           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 6           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 6           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 6           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 6           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 6           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 6           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed  |
| 6           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 6           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |

#### Actions Round 7
| round_index | Player  | action    | Target 1 | Target 2 | status              |
| :-----------| :-------| :---------| :--------| :--------| :------------------ |
| 7           | NPC Ann | Inspector | NPC Fae  |          | successful          |
| 7           | NPC Cal | Psychic   |          |          | successful          |
| 7           | NPC Dan | Judge     | Psychic  |          | successful          |
| 7           | NPC Ed  | Demagog   | Jailer   |          | voting in progress  |
| 7           | NPC Fae | Prophet   | NPC Bob  |          | successful          |

#### States Round 7
| round_index | Player  | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Ann | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Ed  | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Bob | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Fae | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Cal | Psychic   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Dan | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player  | Role      | message   | details                                                      |
| :-----------| :-------| :---------| :---------| :----------------------------------------------------------- |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 7           | NPC Ann | Inspector | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 7           | NPC Ann | Inspector | reveal    | Prophet is Innocent                                          |
| 7           | NPC Ann | Inspector | vote      | Demagog has initiated a vote on eliminating Jailer           |
| 7           | NPC Bob | Jailer    | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 7           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 7           | NPC Bob | Jailer    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 7           | NPC Bob | Jailer    | vote      | Demagog has initiated a vote on eliminating Jailer           |
| 7           | NPC Cal | Psychic   | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 7           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 7           | NPC Cal | Psychic   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 7           | NPC Cal | Psychic   | reveal    | Player: NPC Fae is not possessed                             |
| 7           | NPC Cal | Psychic   | reveal    | Player: NPC Dan is not possessed                             |
| 7           | NPC Cal | Psychic   | vote      | Demagog has initiated a vote on eliminating Jailer           |
| 7           | NPC Dan | Judge     | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 7           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 7           | NPC Dan | Judge     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 7           | NPC Dan | Judge     | vote      | Demagog has initiated a vote on eliminating Jailer           |
| 7           | NPC Ed  | Demagog   | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 7           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 7           | NPC Ed  | Demagog   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 7           | NPC Ed  | Demagog   | vote      | Demagog has initiated a vote on eliminating Jailer           |
| 7           | NPC Fae | Prophet   | broadcast | I (NPC Ann) inspected NPC Fae and they are not possessed     |
| 7           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed  |
| 7           | NPC Fae | Prophet   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed   |
| 7           | NPC Fae | Prophet   | vote      | Demagog has initiated a vote on eliminating Jailer           |