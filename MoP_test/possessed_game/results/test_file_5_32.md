#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 32   | 5       | 5       |

#### Roles
| Role         |
| :----------- |
| Judge        |
| Reporter     |
| Executioner  |
| Inspector    |
| Medic        |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Inspector   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Ann | Inspector   | possessed   | You are Possessed         |
| 0           | NPC Bob | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Bob | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Judge       | role change | Your Role is Judge        |
| 0           | NPC Cal | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Medic       | role change | Your Role is Medic        |
| 0           | NPC Dan | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Ed  | Reporter    | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action   | Target 1  | Target 2 | status      |
| :-----------| :-------| :--------| :---------| :--------| :---------- |
| 1           | NPC Cal | Judge    | Inspector |          | successful  |
| 1           | NPC Dan | Medic    | NPC Ed    |          | successful  |
| 1           | NPC Ed  | Reporter | NPC Dan   |          | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann | Inspector   | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------- |
| 1           | NPC Ann | Inspector   | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 1           | NPC Ann | Inspector   | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Medic    |
| 1           | NPC Bob | Executioner | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 1           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Medic    |
| 1           | NPC Cal | Judge       | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 1           | NPC Cal | Judge       | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Medic    |
| 1           | NPC Dan | Medic       | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 1           | NPC Dan | Medic       | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Medic    |
| 1           | NPC Ed  | Reporter    | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 1           | NPC Ed  | Reporter    | broadcast | I (NPC Ed) am the Reporter and NPC Dan is the Medic    |
| 1           | NPC Ed  | Reporter    | reveal    | NPC Dan is Medic                                       |

#### Actions Round 2
| round_index | Player  | action   | Target 1  | Target 2 | status      |
| :-----------| :-------| :--------| :---------| :--------| :---------- |
| 2           | NPC Cal | Judge    | Inspector |          | successful  |
| 2           | NPC Dan | Medic    | NPC Bob   |          | successful  |
| 2           | NPC Ed  | Reporter | NPC Ann   |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann | Inspector   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                  |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------- |
| 2           | NPC Ann | Inspector   | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Inspector  |
| 2           | NPC Bob | Executioner | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Inspector  |
| 2           | NPC Cal | Judge       | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Inspector  |
| 2           | NPC Dan | Medic       | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Inspector  |
| 2           | NPC Ed  | Reporter    | broadcast | I (NPC Ed) am the Reporter and NPC Ann is the Inspector  |
| 2           | NPC Ed  | Reporter    | reveal    | NPC Ann is Inspector                                     |

#### Actions Round 3
| round_index | Player  | action | Target 1  | Target 2 | status      |
| :-----------| :-------| :------| :---------| :--------| :---------- |
| 3           | NPC Cal | Judge  | Inspector |          | successful  |
| 3           | NPC Dan | Medic  | NPC Ann   |          | successful  |

#### States Round 3
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann | Inspector   | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player  | Role        | message   | details                                                |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------- |
| 3           | NPC Ann | Inspector   | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 3           | NPC Bob | Executioner | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 3           | NPC Cal | Judge       | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 3           | NPC Dan | Medic       | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 3           | NPC Ed  | Reporter    | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |

#### Actions Round 4
| round_index | Player  | action   | Target 1  | Target 2 | status      |
| :-----------| :-------| :--------| :---------| :--------| :---------- |
| 4           | NPC Cal | Judge    | Inspector |          | successful  |
| 4           | NPC Dan | Medic    | NPC Cal   |          | successful  |
| 4           | NPC Ed  | Reporter | NPC Bob   |          | successful  |

#### States Round 4
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann | Inspector   | False      | True      | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player  | Role        | message   | details                                                |
| :-----------| :-------| :-----------| :---------| :----------------------------------------------------- |
| 4           | NPC Ann | Inspector   | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 4           | NPC Bob | Executioner | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 4           | NPC Cal | Judge       | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 4           | NPC Dan | Medic       | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 4           | NPC Ed  | Reporter    | broadcast | I (NPC Ann) inspected NPC Cal and they are posssessed  |
| 4           | NPC Ed  | Reporter    | reveal    | NPC Bob is Executioner                                 |

#### Actions Round 5
| round_index | Player  | action | Target 1 | Target 2 | status      |
| :-----------| :-------| :------| :--------| :--------| :---------- |
| 5           | NPC Cal | Judge  | Reporter |          | successful  |
| 5           | NPC Dan | Medic  | NPC Ed   |          | successful  |

#### States Round 5
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ann | Inspector   | False      | True      | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Dan | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player | Role | message | details  |
| :-----------| :------| :----| :-------| :------- |