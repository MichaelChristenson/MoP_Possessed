#### Setup
| Seed | Rounds  |
| :----| :------ |
| 1    | 4       |

#### Initial State
| Player | Role        | Password       |
| :------| :-----------| :------------- |
| Ann    | Judge       | test_password        |
| Bob    | Reporter    | test_password  |
| Cal    | Executioner | test_password  |
| Dan    | Inspector   | test_password  |
| Ed     | Thief       | test_password  |
| Fin    | Psychic     | test_password  |

#### Actions Round 1
| round_index | Player | action    | Target 1 | Target 2 | status   |
| :-----------| :------| :---------| :--------| :--------| :------- |
| 1           | Ann    | Judge     | Reporter |          | Success  |
| 1           | Bob    | Reporter  | Ann      |          | Fail     |
| 1           | Dan    | Inspector | Bob      |          | Success  |
| 1           | Ed     | Thief     | Cal      |          | Success  |
| 1           | Fin    | Psychic   |          |          | Success  |

#### Actions Round 2
| round_index | Player | action      | Target 1 | Target 2 | status   |
| :-----------| :------| :-----------| :--------| :--------| :------- |
| 2           | Ann    | Judge       | Thief    |          | Fail     |
| 2           | Cal    | Executioner | Ann      |          | Success  |

#### Actions Round 3
| round_index | Player | action  | Target 1 | Target 2 | status   |
| :-----------| :------| :-------| :--------| :--------| :------- |
| 3           | Ann    | Judge   | Thief    |          | Fail     |
| 3           | Fin    | Psychic | Ann      |          | Success  |

#### Actions Round 4
| round_index | Player | action | Target 1    | Target 2 | status  |
| :-----------| :------| :------| :-----------| :--------| :------ |
| 4           | Ann    | Judge  | Executioner |          | Fail    |

#### States Round 0
| round_index | Player | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | Ann    | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Bob    | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Cal    | Executioner | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | Dan    | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Ed     | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | Fin    | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### States Round 1
| round_index | Player | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | Ann    | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | Bob    | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | Cal    | Executioner | False      | True      | True       | 0         | True   | 0              | 0                  |
| 1           | Dan    | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | Ed     | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | Fin    | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |

#### States Round 2
| round_index | Player | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | Ann    | Judge       | True       | False     | False      | 0         | True   | 0              | 0                  |
| 2           | Bob    | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | Cal    | Executioner | False      | True      | True       | 4         | True   | 0              | 0                  |
| 2           | Dan    | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | Ed     | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | Fin    | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### States Round 3
| round_index | Player | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | Ann    | Judge       | True       | False     | False      | 0         | True   | 0              | 0                  |
| 3           | Bob    | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | Cal    | Executioner | False      | True      | True       | 3         | True   | 0              | 0                  |
| 3           | Dan    | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | Ed     | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | Fin    | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |

#### States Round 4
| round_index | Player | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | Ann    | Judge       | True       | False     | False      | 0         | True   | 0              | 0                  |
| 4           | Bob    | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | Cal    | Executioner | False      | True      | True       | 2         | True   | 0              | 0                  |
| 4           | Dan    | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | Ed     | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | Fin    | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| Player | Role        | round_index | message     | details                   |
| :------| :-----------| :-----------| :-----------| :------------------------ |
| Ann    | Judge       | 0           | role change | Your Role is Judge        |
| Ann    | Judge       | 0           | possessed   | You are Not Possessed     |
| Bob    | Reporter    | 0           | role change | Your Role is Reporter     |
| Bob    | Reporter    | 0           | possessed   | You are Not Possessed     |
| Cal    | Executioner | 0           | role change | Your Role is Executioner  |
| Cal    | Executioner | 0           | possessed   | You are Possessed         |
| Dan    | Inspector   | 0           | role change | Your Role is Inspector    |
| Dan    | Inspector   | 0           | possessed   | You are Not Possessed     |
| Ed     | Thief       | 0           | role change | Your Role is Thief        |
| Ed     | Thief       | 0           | possessed   | You are Not Possessed     |
| Fin    | Psychic     | 0           | role change | Your Role is Psychic      |
| Fin    | Psychic     | 0           | possessed   | You are Not Possessed     |

#### Notifications Round 1
| Player | Role      | round_index | message | details                       |
| :------| :---------| :-----------| :-------| :---------------------------- |
| Bob    | Reporter  | 1           | reveal  | Ann is Judge                  |
| Dan    | Inspector | 1           | reveal  | Reporter is Innocent          |
| Fin    | Psychic   | 1           | reveal  | Player: Ed is not possessed   |
| Fin    | Psychic   | 1           | reveal  | Player: Bob is not possessed  |

#### Notifications Round 2
| Player | Role        | round_index | message     | details                  |
| :------| :-----------| :-----------| :-----------| :----------------------- |
| Ann    | Judge       | 2           | elimination | Ann has been eliminated  |
| Bob    | Reporter    | 2           | elimination | Ann has been eliminated  |
| Cal    | Executioner | 2           | elimination | Ann has been eliminated  |
| Dan    | Inspector   | 2           | elimination | Ann has been eliminated  |
| Ed     | Thief       | 2           | elimination | Ann has been eliminated  |
| Fin    | Psychic     | 2           | elimination | Ann has been eliminated  |

#### Notifications Round 3
| Player | Role    | round_index | message | details                       |
| :------| :-------| :-----------| :-------| :---------------------------- |
| Fin    | Psychic | 3           | reveal  | Player: Bob is not possessed  |
| Fin    | Psychic | 3           | reveal  | Player: Dan is not possessed  |

#### Notifications Round 4
| Player | Role | round_index | message | details  |
| :------| :----| :-----------| :-------| :------- |