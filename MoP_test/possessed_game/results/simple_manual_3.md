#### Setup
| Seed | Rounds  |
| :----| :------ |
| 2    | 1       |

#### Initial State
| Player | Role        | Password       |
| :------| :-----------| :------------- |
| Ann    | Executioner | test_password        |
| Bob    | Judge       | test_password  |

#### Actions Round 1
| round_index | Player | action      | Target 1    | Target 2 | status   |
| :-----------| :------| :-----------| :-----------| :--------| :------- |
| 1           | Ann    | Executioner | Bob         |          | Success  |
| 1           | Bob    | Judge       | Executioner |          | Fail     |

#### States Round 0
| round_index | Player | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | Ann    | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Bob    | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |

#### States Round 1
| round_index | Player | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | Ann    | Executioner | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | Bob    | Judge       | True       | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| Player | Role        | round_index | message     | details                   |
| :------| :-----------| :-----------| :-----------| :------------------------ |
| Ann    | Executioner | 0           | role change | Your Role is Executioner  |
| Ann    | Executioner | 0           | possessed   | You are Not Possessed     |
| Bob    | Judge       | 0           | role change | Your Role is Judge        |
| Bob    | Judge       | 0           | possessed   | You are Possessed         |

#### Notifications Round 1
| Player | Role        | round_index | message     | details                  |
| :------| :-----------| :-----------| :-----------| :----------------------- |
| Ann    | Executioner | 1           | elimination | Bob has been eliminated  |
| Ann    | Executioner | 1           | game over   | Ann Wins!                |
| Bob    | Judge       | 1           | elimination | Bob has been eliminated  |
| Bob    | Judge       | 1           | game over   | Ann Wins!                |