#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 19   | 15      | 4       |

#### Roles
| Role         |
| :----------- |
| Trader       |
| Psychic      |
| Jailer       |
| Thief        |
| Prophet      |
| Executioner  |
| Priest       |
| Inspector    |
| Medic        |
| Spy          |
| Silencer     |
| Demagog      |
| Reporter     |
| Assassin     |
| Judge        |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Igi  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Mark | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Norm | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ozie | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Judge       | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Ann  | Judge       | possessed   | You are Possessed         |
| 0           | NPC Bob  | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Bob  | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Cal  | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Cal  | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Dan  | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Ed   | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Fae  | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Priest      | role change | Your Role is Priest       |
| 0           | NPC Gia  | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Thief       | role change | Your Role is Thief        |
| 0           | NPC Han  | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Trader      | role change | Your Role is Trader       |
| 0           | NPC Igi  | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Jeff | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Ken  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Lee  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Mark | Medic       | role change | Your Role is Medic        |
| 0           | NPC Mark | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Norm | Spy         | role change | Your Role is Spy          |
| 0           | NPC Norm | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Ozie | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Ozie | Demagog     | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player   | action    | Target 1  | Target 2 | status              |
| :-----------| :--------| :---------| :---------| :--------| :------------------ |
| 1           | NPC Ann  | Judge     | Reporter  |          | successful          |
| 1           | NPC Bob  | Prophet   | NPC Ed    |          | successful          |
| 1           | NPC Cal  | Reporter  | NPC Ozie  |          | successful          |
| 1           | NPC Dan  | Psychic   |           |          | successful          |
| 1           | NPC Ed   | Assassin  | Inspector |          | successful          |
| 1           | NPC Han  | Thief     | NPC Gia   |          | successful          |
| 1           | NPC Igi  | Trader    | NPC Mark  | NPC Ann  | successful          |
| 1           | NPC Jeff | Silencer  | NPC Norm  |          | successful          |
| 1           | NPC Ken  | Inspector | NPC Lee   |          | successful          |
| 1           | NPC Mark | Medic     | NPC Dan   |          | successful          |
| 1           | NPC Norm | Spy       |           |          | successful          |
| 1           | NPC Ozie | Demagog   | Assassin  |          | voting in progress  |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Igi  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Dan  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Lee  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia  | Priest      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Ken  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Mark | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Norm | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Jeff | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ozie | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Cal  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed   | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ann  | Medic       | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Ann  | Medic       | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Ann  | Medic       | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Bob  | Prophet     | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Bob  | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Bob  | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Bob  | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Bob  | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Bob  | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Bob  | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Bob  | Prophet     | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Bob  | Prophet     | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Bob  | Prophet     | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Cal  | Reporter    | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Cal  | Reporter    | reveal    | NPC Ozie is Demagog                                              |
| 1           | NPC Cal  | Reporter    | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Dan  | Psychic     | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Dan  | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Dan  | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Dan  | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Dan  | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Dan  | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Dan  | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Dan  | Psychic     | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Dan  | Psychic     | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Dan  | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 1           | NPC Dan  | Psychic     | reveal    | Player: NPC Ozie is not possessed                                |
| 1           | NPC Dan  | Psychic     | reveal    | Player: NPC Han is not possessed                                 |
| 1           | NPC Dan  | Psychic     | reveal    | Player: NPC Mark is not possessed                                |
| 1           | NPC Dan  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 1           | NPC Dan  | Psychic     | reveal    | Player: NPC Norm is not possessed                                |
| 1           | NPC Dan  | Psychic     | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Ed   | Assassin    | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Fae  | Jailer      | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Fae  | Jailer      | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Fae  | Jailer      | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Fae  | Jailer      | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Fae  | Jailer      | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Gia  | Priest      | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Gia  | Priest      | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Han  | Thief       | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Han  | Thief       | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Igi  | Trader      | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Igi  | Trader      | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Igi  | Trader      | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Igi  | Trader      | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Igi  | Trader      | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Igi  | Trader      | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Igi  | Trader      | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Igi  | Trader      | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Igi  | Trader      | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Igi  | Trader      | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Jeff | Silencer    | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Jeff | Silencer    | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Ken  | Inspector   | reveal    | Executioner is Innocent                                          |
| 1           | NPC Ken  | Inspector   | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Lee  | Executioner | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Lee  | Executioner | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Mark | Judge       | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Mark | Judge       | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Norm | Spy         | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Norm | Spy         | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Norm | Spy         | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Norm | Spy         | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Norm | Spy         | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Norm | Spy         | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Norm | Spy         | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Norm | Spy         | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Norm | Spy         | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Norm | Spy         | silenced  | You have been silenced                                           |
| 1           | NPC Norm | Spy         | reveal    | NPC Han is targeting NPC Gia                                     |
| 1           | NPC Norm | Spy         | reveal    | NPC Ken is targeting NPC Lee                                     |
| 1           | NPC Norm | Spy         | reveal    | NPC Jeff is targeting NPC Norm                                   |
| 1           | NPC Norm | Spy         | reveal    | NPC Cal is targeting NPC Ozie                                    |
| 1           | NPC Norm | Spy         | reveal    | NPC Ann is targeting NPC Cal                                     |
| 1           | NPC Norm | Spy         | vote      | Demagog has initiated a vote on eliminating Assassin             |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Cal) am the Reporter and NPC Ozie is the Demagog          |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Dan) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Dan) am the Psychic and the Thief is not possessed        |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Dan) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed       |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Han) am the Thief and I have made NPC Gia vulnerable      |
| 1           | NPC Ozie | Demagog     | broadcast | I (NPC Ken) inspected NPC Lee and they are not possessed         |
| 1           | NPC Ozie | Demagog     | vote      | Demagog has initiated a vote on eliminating Assassin             |