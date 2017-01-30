#### Setup
| Seed | Rounds  |
| :----| :------ |
| 1    | 2       |

#### Initial State
| Player | Role        | Password       |
| :------| :-----------| :------------- |
| Ann    | Thief       | test_password  |
| Bob    | Judge       | test_password  |
| Cal    | Executioner | test_password  |

#### Actions Round 1
| round_index | Player | Role        | Action | Target     | Motive                                        | Result   |
| :-----------| :------| :-----------| :------| :----------| :---------------------------------------------| :------- |
| 1           | Ann    | Thief       | Steal  | Bob,Judge  | Shakeup                                       | Success  |
| 1           | Bob    | Judge       | Class  | Thief      | Trying to kill bob                            | Fail     |
| 1           | Cal    | Executioner |        |            | Waiting                                       | Success  |

#### Actions Round 2
| round_index | Player | Role        | Action | Target     | Motive                                        | Result   |
| :-----------| :------| :-----------| :------| :----------| :---------------------------------------------| :------- |
| 2           | Ann    | Judge       | Class  | Bob        | Hoping he is Possessed                        | Success  |
| 2           | Bob    | Thief       | Class  | Cal        | Elimination                                   | Success  |
| 2           | Cal    | Executioner | Class  | Ann, Judge | Knows Ann is the Judge because Bob complained | Success  |

#### States Round 0
| round_index | Player | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | Ann    | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Bob    | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Cal    | Executioner | False      | True      | False      | 0         | True   | 0              | 0                  |

#### States Round 1
| round_index | Player | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | Ann    | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | Bob    | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | Cal    | Executioner | False      | True      | False      | 0         | True   | 0              | 0                  |

#### States Round 2
| round_index | Player | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | Ann    | Judge       | True       | False     | False      | 0         | True   | 0              | 0                  |
| 2           | Bob    | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | Cal    | Executioner | False      | True      | True       | 4         | True   | 0              | 0                  |

#### Notifications Round 0
| Player | round_index | message     | details                   |
| :------| :-----------| :-----------| :------------------------ |
| Ann    | 0           | role change | Your Role is Thief        |
| Ann    | 0           | possessed   | You are Not Possessed     |
| Bob    | 0           | role change | Your Role is Judge        |
| Bob    | 0           | possessed   | You are Not Possessed     |
| Cal    | 0           | role change | Your Role is Executioner  |
| Cal    | 0           | possessed   | You are Possessed         |

#### Notifications Round 1
| Player | round_index | message     | details                   |
| :------| :-----------| :-----------| :------------------------ |
| Ann    | 1           | role change | Your Role is Judge        |
| Bob    | 1           | role change | Your Role is Thief        |

#### Notifications Round 2
| Player | round_index | message     | details                   |
| :------| :-----------| :-----------| :------------------------ |
| Ann    | 2           | elimination | Ann has been eliminated   |
| Ann    | 2           | game over   | Cal Wins!                 |
| Bob    | 2           | elimination | Ann has been eliminated   |
| Bob    | 2           | game over   | Cal Wins!                 |
| Cal    | 2           | elimination | Ann has been eliminated   |
| Cal    | 2           | game over   | Cal Wins!                 |