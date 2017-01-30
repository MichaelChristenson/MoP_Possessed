#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 12   | 8       | 2       |

#### Roles
| Role         |
| :----------- |
| Assassin     |
| Prophet      |
| Inspector    |
| Executioner  |
| Silencer     |
| Trader       |
| Reporter     |
| Psychic      |

#### States Round 0
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Fae | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player  | Role        | message     | details                   |
| :-----------| :-------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Ann | Prophet     | possessed   | You are Possessed         |
| 0           | NPC Bob | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Bob | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Cal | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Cal | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Dan | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Dan | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Ed  | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Ed  | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Fae | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Fae | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Gia | Trader      | role change | Your Role is Trader       |
| 0           | NPC Gia | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Han | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Han | Executioner | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player  | action    | Target 1  | Target 2 | status      |
| :-----------| :-------| :---------| :---------| :--------| :---------- |
| 1           | NPC Ann | Prophet   | NPC Ed    |          | successful  |
| 1           | NPC Bob | Reporter  | NPC Han   |          | successful  |
| 1           | NPC Cal | Inspector | NPC Ed    |          | successful  |
| 1           | NPC Dan | Psychic   |           |          | successful  |
| 1           | NPC Ed  | Silencer  | NPC Fae   |          | successful  |
| 1           | NPC Fae | Assassin  | Inspector |          | successful  |
| 1           | NPC Gia | Trader    | NPC Cal   | NPC Dan  | successful  |

#### States Round 1
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Fae | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Cal | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Gia | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Bob | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player  | Role        | message   | details                                                        |
| :-----------| :-------| :-----------| :---------| :------------------------------------------------------------- |
| 1           | NPC Ann | Prophet     | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 1           | NPC Ann | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 1           | NPC Ann | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Ann | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Bob | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob | Reporter    | reveal    | NPC Han is Executioner                                         |
| 1           | NPC Cal | Psychic     | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 1           | NPC Cal | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 1           | NPC Cal | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Cal | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Cal | Psychic     | reveal    | Silencer is Innocent                                           |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Dan | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Dan | Inspector   | reveal    | Player: NPC Fae is not possessed                               |
| 1           | NPC Dan | Inspector   | reveal    | Player: NPC Cal is not possessed                               |
| 1           | NPC Dan | Inspector   | reveal    | Player: NPC Bob is not possessed                               |
| 1           | NPC Ed  | Silencer    | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 1           | NPC Ed  | Silencer    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 1           | NPC Ed  | Silencer    | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Ed  | Silencer    | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Fae | Assassin    | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 1           | NPC Fae | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 1           | NPC Fae | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Fae | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Fae | Assassin    | silenced  | You have been silenced                                         |
| 1           | NPC Gia | Trader      | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 1           | NPC Gia | Trader      | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 1           | NPC Gia | Trader      | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Gia | Trader      | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Han | Executioner | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 1           | NPC Han | Executioner | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed     |
| 1           | NPC Han | Executioner | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed   |
| 1           | NPC Han | Executioner | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed  |

#### Actions Round 2
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 2           | NPC Ann | Prophet   | NPC Ed   |          | successful  |
| 2           | NPC Cal | Psychic   |          |          | successful  |
| 2           | NPC Dan | Inspector | NPC Bob  |          | successful  |
| 2           | NPC Ed  | Silencer  | NPC Han  |          | successful  |

#### States Round 2
| round_index | Player  | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :-------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Fae | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Cal | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Han | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Bob | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player  | Role        | message   | details                                                          |
| :-----------| :-------| :-----------| :---------| :--------------------------------------------------------------- |
| 2           | NPC Ann | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Ann | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Ann | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Ann | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ann | Prophet     | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed         |
| 2           | NPC Bob | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Bob | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Bob | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Bob | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Bob | Reporter    | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed         |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Cal | Psychic     | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed         |
| 2           | NPC Cal | Psychic     | reveal    | Player: NPC Han is not possessed                                 |
| 2           | NPC Cal | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 2           | NPC Cal | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 2           | NPC Dan | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Dan | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Dan | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Dan | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Dan | Inspector   | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed         |
| 2           | NPC Dan | Inspector   | reveal    | Reporter is Innocent                                             |
| 2           | NPC Ed  | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Ed  | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Ed  | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Ed  | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ed  | Silencer    | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed         |
| 2           | NPC Fae | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Fae | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Fae | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Fae | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Fae | Assassin    | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed         |
| 2           | NPC Gia | Trader      | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Gia | Trader      | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Gia | Trader      | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Gia | Trader      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Gia | Trader      | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed         |
| 2           | NPC Han | Executioner | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 2           | NPC Han | Executioner | broadcast | I (NPC Cal) am the Psychic and the Silencer is not possessed     |
| 2           | NPC Han | Executioner | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Han | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Han | Executioner | broadcast | I (NPC Dan) inspected NPC Bob and they are not possessed         |
| 2           | NPC Han | Executioner | silenced  | You have been silenced                                           |