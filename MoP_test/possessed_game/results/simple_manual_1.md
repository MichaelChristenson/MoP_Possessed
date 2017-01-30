#### Setup
| Seed | Rounds  |
| :----| :------ |
| 1    | 4       |

#### Initial State
| Player | Role        | Password       |
| :------| :-----------| :------------- |
| Ann    | Executioner | test_password        |
| Bob    | Judge       | test_password  |
| Cal    | Inspector   | test_password  |
| Dan    | Thief       | test_password  |
| Ed     | Reporter    | test_password  |
| Fin    | Trader      | test_password  |

#### Actions Round 1
| round_index | Player | action    | Target 1  | Target 2 | status   |
| :-----------| :------| :---------| :---------| :--------| :------- |
| 1           | Dan    | Thief     | Ann       |          | Success  |
| 1           | Bob    | Judge     | Inspector |          | Fail     |
| 1           | Cal    | Inspector | Ann       |          | Success  |
| 1           | Ed     | Reporter  | Cal       |          | Success  |
| 1           | Fin    | Trader    | Cal       | Ed       | Success  |

#### Actions Round 2
| round_index | Player | action      | Target 1  | Target 2  | status   |
| :-----------| :------| :-----------| :---------| :---------| :------- |
| 2           | Ann    | Executioner | Ed        |           | Success  |
| 2           | Fin    | Steal       | Dan       | Inspector | Fail     |
| 2           | Bob    | Judge       | Inspector |           | Success  |

#### Actions Round 3
| round_index | Player | action | Target 1 | Target 2 | status   |
| :-----------| :------| :------| :--------| :--------| :------- |
| 3           | Cal    | Steal  | Ed       |          | Success  |
| 3           | Dan    | Trader | Bob      | Cal      | Success  |

#### Actions Round 4
| round_index | Player | action      | Target 1 | Target 2 | status   |
| :-----------| :------| :-----------| :--------| :--------| :------- |
| 4           | Cal    | Inspector   | Dan      |          | Success  |
| 4           | Fin    | Executioner | Dan      |          | Success  |
| 4           | Cal    | Judge       | Trader   |          | Success  |

#### States Round 0
| round_index | Player | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | Ann    | Executioner | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | Bob    | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Cal    | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Dan    | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Ed     | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Fin    | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### States Round 1
| round_index | Player | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | Ann    | Executioner | False      | True      | True       | 0         | True   | 0              | 0                  |
| 1           | Bob    | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | Cal    | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | Dan    | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | Ed     | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | Fin    | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |

#### States Round 2
| round_index | Player | Role | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :----| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |

#### States Round 3
| round_index | Player | Role | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :----| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |

#### States Round 4
| round_index | Player | Role | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :----| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |

#### Notifications Round 0
| Player | Role        | round_index | message     | details                   |
| :------| :-----------| :-----------| :-----------| :------------------------ |
| Ann    | Executioner | 0           | role change | Your Role is Executioner  |
| Ann    | Executioner | 0           | possessed   | You are Possessed         |
| Bob    | Judge       | 0           | role change | Your Role is Judge        |
| Bob    | Judge       | 0           | possessed   | You are Not Possessed     |
| Cal    | Inspector   | 0           | role change | Your Role is Inspector    |
| Cal    | Inspector   | 0           | possessed   | You are Not Possessed     |
| Dan    | Thief       | 0           | role change | Your Role is Thief        |
| Dan    | Thief       | 0           | possessed   | You are Not Possessed     |
| Ed     | Reporter    | 0           | role change | Your Role is Reporter     |
| Ed     | Reporter    | 0           | possessed   | You are Not Possessed     |
| Fin    | Trader      | 0           | role change | Your Role is Trader       |
| Fin    | Trader      | 0           | possessed   | You are Not Possessed     |

#### Notifications Round 1
| Player | Role      | round_index | message | details                   |
| :------| :---------| :-----------| :-------| :------------------------ |
| Cal    | Inspector | 1           | reveal  | Executioner is Possessed  |
| Ed     | Reporter  | 1           | reveal  | Cal is Inspector          |

#### Notifications Round 2
| Player | Role | round_index | message | details  |
| :------| :----| :-----------| :-------| :------- |

#### Notifications Round 3
| Player | Role | round_index | message | details  |
| :------| :----| :-----------| :-------| :------- |

#### Notifications Round 4
| Player | Role | round_index | message | details  |
| :------| :----| :-----------| :-------| :------- |