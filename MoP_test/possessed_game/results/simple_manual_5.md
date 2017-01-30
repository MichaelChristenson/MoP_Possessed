#### Setup
| Seed | Rounds  |
| :----| :------ |
| 9    | 5       |

#### Initial State
| Player | Role      | Password       |
| :------| :---------| :------------- |
| Ann    | Medic     | test_password        |
| Bob    | Thief     | test_password  |
| Cal    | Reporter  | test_password  |
| Dan    | Judge     | test_password  |
| Ed     | Inspector | test_password  |

#### Actions Round 1
| round_index | Player | action    | Target 1 | Target 2 | status      |
| :-----------| :------| :---------| :--------| :--------| :---------- |
| 1           | Ann    | Medic     | Ed       |          | successful  |
| 1           | Bob    | Thief     | Ann      |          | successful  |
| 1           | Cal    | Reporter  | Bob      |          | successful  |
| 1           | Dan    | Judge     | Medic    |          | successful  |
| 1           | Ed     | Inspector | Cal      |          | successful  |

#### Actions Round 2
| round_index | Player | action    | Target 1 | Target 2 | status      |
| :-----------| :------| :---------| :--------| :--------| :---------- |
| 2           | Ann    | Medic     | Bob      |          | successful  |
| 2           | Dan    | Judge     | Thief    |          | successful  |
| 2           | Ed     | Inspector | Ann      |          | successful  |

#### Actions Round 3
| round_index | Player | action | Target 1 | Target 2 | status      |
| :-----------| :------| :------| :--------| :--------| :---------- |
| 3           | Ann    | Medic  | Dan      |          | successful  |
| 3           | Bob    | Thief  | Dan      |          | successful  |
| 3           | Dan    | Judge  | Judge    |          | successful  |

#### Actions Round 4
| round_index | Player | action | Target 1 | Target 2 | status      |
| :-----------| :------| :------| :--------| :--------| :---------- |
| 4           | Ann    | Medic  | Cal      |          | successful  |
| 4           | Cal    | Steal  | Dan      |          | successful  |
| 4           | Dan    | Judge  | Medic    |          | successful  |
| 5           | Ann    | Medic  | Ed       |          | successful  |

#### Actions Round 5
| round_index | Player | action    | Target 1 | Target 2 | status      |
| :-----------| :------| :---------| :--------| :--------| :---------- |
| 5           | Bob    | Steal     | Ann      | Medic    | successful  |
| 5           | Cal    | Judge     | Reporter |          | successful  |
| 5           | Dan    | Reporter  | Judge    |          | successful  |
| 5           | Ed     | Inspector | Cal      |          | successful  |

#### States Round 0
| round_index | Player | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | Ann    | Medic     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | Bob    | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Cal    | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Dan    | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Ed     | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |

#### States Round 1
| round_index | Player | Role | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :----| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |

#### States Round 2
| round_index | Player | Role | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :----| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |

#### States Round 3
| round_index | Player | Role | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :----| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |

#### States Round 4
| round_index | Player | Role | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :----| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |

#### States Round 5
| round_index | Player | Role | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :----| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |

#### Notifications Round 0
| Player | Role      | round_index | message     | details                 |
| :------| :---------| :-----------| :-----------| :---------------------- |
| Ann    | Medic     | 0           | role change | Your Role is Medic      |
| Ann    | Medic     | 0           | possessed   | You are Possessed       |
| Bob    | Thief     | 0           | role change | Your Role is Thief      |
| Bob    | Thief     | 0           | possessed   | You are Not Possessed   |
| Cal    | Reporter  | 0           | role change | Your Role is Reporter   |
| Cal    | Reporter  | 0           | possessed   | You are Not Possessed   |
| Dan    | Judge     | 0           | role change | Your Role is Judge      |
| Dan    | Judge     | 0           | possessed   | You are Not Possessed   |
| Ed     | Inspector | 0           | role change | Your Role is Inspector  |
| Ed     | Inspector | 0           | possessed   | You are Not Possessed   |

#### Notifications Round 1
| Player | Role | round_index | message | details  |
| :------| :----| :-----------| :-------| :------- |

#### Notifications Round 2
| Player | Role | round_index | message | details  |
| :------| :----| :-----------| :-------| :------- |

#### Notifications Round 3
| Player | Role | round_index | message | details  |
| :------| :----| :-----------| :-------| :------- |

#### Notifications Round 4
| Player | Role | round_index | message | details  |
| :------| :----| :-----------| :-------| :------- |

#### Notifications Round 5
| Player | Role | round_index | message | details  |
| :------| :----| :-----------| :-------| :------- |