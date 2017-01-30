#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 32   | 14      | 5       |

#### Roles
| Role         |
| :----------- |
| Psychic      |
| Silencer     |
| Trader       |
| Spy          |
| Executioner  |
| Reporter     |
| Thief        |
| Demagog      |
| Priest       |
| Prophet      |
| Medic        |
| Assassin     |
| Inspector    |
| Jailer       |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Norm | Silencer    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Mark | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Ann  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Bob  | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Bob  | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Cal  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Cal  | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Dan  | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Ed   | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Fae  | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Thief       | role change | Your Role is Thief        |
| 0           | NPC Gia  | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Han  | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Igi  | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Priest      | role change | Your Role is Priest       |
| 0           | NPC Jeff | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Trader      | role change | Your Role is Trader       |
| 0           | NPC Ken  | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Lee  | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Mark | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Mark | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Norm | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Norm | Silencer    | possessed   | You are Possessed         |

#### Actions Round 1
| round_index | Player   | action    | Target 1    | Target 2 | status                         |
| :-----------| :--------| :---------| :-----------| :--------| :----------------------------- |
| 1           | NPC Bob  | Demagog   | Executioner |          | voting in progress             |
| 1           | NPC Cal  | Psychic   |             |          | successful                     |
| 1           | NPC Dan  | Medic     | NPC Norm    |          | successful                     |
| 1           | NPC Ed   | Assassin  | Priest      |          | successful                     |
| 1           | NPC Fae  | Spy       |             |          | successful                     |
| 1           | NPC Gia  | Thief     | NPC Norm    |          | successful                     |
| 1           | NPC Han  | Prophet   | NPC Ann     |          | successful                     |
| 1           | NPC Igi  | Reporter  | NPC Norm    |          | successful                     |
| 1           | NPC Ken  | Trader    | NPC Fae     | NPC Lee  | failed because not vulnerable  |
| 1           | NPC Mark | Inspector | NPC Igi     |          | successful                     |
| 1           | NPC Norm | Silencer  | NPC Lee     |          | successful                     |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Norm | Silencer    | False      | True      | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Ken  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Igi  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Gia  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed   | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Mark | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Lee  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 1           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ann  | Executioner | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Ann  | Executioner | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Ann  | Executioner | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Ann  | Executioner | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Bob  | Demagog     | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Bob  | Demagog     | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal  | Psychic     | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Cal  | Psychic     | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Cal  | Psychic     | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Cal  | Psychic     | reveal    | Player: NPC Han is not possessed                                 |
| 1           | NPC Cal  | Psychic     | reveal    | Player: NPC Igi is not possessed                                 |
| 1           | NPC Cal  | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 1           | NPC Cal  | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 1           | NPC Cal  | Psychic     | reveal    | Player: NPC Ann is not possessed                                 |
| 1           | NPC Cal  | Psychic     | reveal    | Player: NPC Gia is not possessed                                 |
| 1           | NPC Cal  | Psychic     | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Dan  | Medic       | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Dan  | Medic       | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Dan  | Medic       | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Dan  | Medic       | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Ed   | Assassin    | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Ed   | Assassin    | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Fae  | Spy         | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Fae  | Spy         | reveal    | NPC Norm is targeting NPC Lee                                    |
| 1           | NPC Fae  | Spy         | reveal    | NPC Igi is targeting NPC Norm                                    |
| 1           | NPC Fae  | Spy         | reveal    | NPC Gia is targeting NPC Norm                                    |
| 1           | NPC Fae  | Spy         | reveal    | NPC Mark is targeting NPC Igi                                    |
| 1           | NPC Fae  | Spy         | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Gia  | Thief       | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Gia  | Thief       | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Gia  | Thief       | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Gia  | Thief       | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Han  | Prophet     | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Han  | Prophet     | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Igi  | Reporter    | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Igi  | Reporter    | reveal    | NPC Norm is Silencer                                             |
| 1           | NPC Igi  | Reporter    | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Jeff | Priest      | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Jeff | Priest      | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ken  | Trader      | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Ken  | Trader      | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Ken  | Trader      | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Ken  | Trader      | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Lee  | Jailer      | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Lee  | Jailer      | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Lee  | Jailer      | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Lee  | Jailer      | silenced  | You have been silenced                                           |
| 1           | NPC Lee  | Jailer      | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Mark | Inspector   | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Mark | Inspector   | reveal    | Reporter is Innocent                                             |
| 1           | NPC Mark | Inspector   | vote      | Demagog has initiated a vote on eliminating Executioner          |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Gia) am the Thief and I have made NPC Norm vulnerable     |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Igi) am the Reporter and NPC Norm is the Silencer         |
| 1           | NPC Norm | Silencer    | broadcast | I (NPC Mark) inspected NPC Igi and they are not possessed        |
| 1           | NPC Norm | Silencer    | vote      | Demagog has initiated a vote on eliminating Executioner          |

#### Actions Round 2
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 2           | NPC Cal  | Psychic  |          |          | successful  |
| 2           | NPC Dan  | Medic    | NPC Ken  |          | successful  |
| 2           | NPC Fae  | Spy      |          |          | successful  |
| 2           | NPC Han  | Prophet  | NPC Jeff |          | successful  |
| 2           | NPC Norm | Silencer | NPC Bob  |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Norm | Silencer    | False      | True      | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Ken  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ann  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Igi  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Bob  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed   | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Mark | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Lee  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 2           | NPC Bob  | Demagog     | silenced  | You have been silenced                                           |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 2           | NPC Cal  | Psychic     | reveal    | Player: NPC Ed is not possessed                                  |
| 2           | NPC Cal  | Psychic     | reveal    | Player: NPC Igi is not possessed                                 |
| 2           | NPC Cal  | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 2           | NPC Cal  | Psychic     | reveal    | Player: NPC Ann is not possessed                                 |
| 2           | NPC Cal  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 2           | NPC Cal  | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 2           | NPC Fae  | Spy         | reveal    | NPC Norm is targeting NPC Bob                                    |
| 2           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Fae                                     |
| 2           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Fae                                     |
| 2           | NPC Fae  | Spy         | reveal    | NPC Igi is targeting NPC Norm                                    |
| 2           | NPC Fae  | Spy         | reveal    | NPC Gia is targeting NPC Norm                                    |
| 2           | NPC Fae  | Spy         | reveal    | NPC Bob is targeting NPC Ann                                     |
| 2           | NPC Fae  | Spy         | reveal    | NPC Han is targeting NPC Ann                                     |
| 2           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Norm                                    |
| 2           | NPC Fae  | Spy         | reveal    | NPC Ed is targeting NPC Jeff                                     |
| 2           | NPC Fae  | Spy         | reveal    | NPC Mark is targeting NPC Igi                                    |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Trader is not possessed       |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Assassin is not possessed     |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Spy is not possessed          |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Ann          |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Norm         |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 2           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |

#### Actions Round 3
| round_index | Player   | action    | Target 1 | Target 2 | status                         |
| :-----------| :--------| :---------| :--------| :--------| :----------------------------- |
| 3           | NPC Bob  | Demagog   | Jailer   |          | voting in progress             |
| 3           | NPC Cal  | Psychic   |          |          | successful                     |
| 3           | NPC Dan  | Medic     | NPC Fae  |          | successful                     |
| 3           | NPC Ed   | Assassin  | Psychic  |          | successful                     |
| 3           | NPC Fae  | Spy       |          |          | successful                     |
| 3           | NPC Gia  | Thief     | NPC Ann  |          | successful                     |
| 3           | NPC Han  | Prophet   | NPC Lee  |          | successful                     |
| 3           | NPC Igi  | Reporter  | NPC Han  |          | successful                     |
| 3           | NPC Ken  | Trader    | NPC Ann  | NPC Lee  | failed because not vulnerable  |
| 3           | NPC Mark | Inspector | NPC Ann  |          | successful                     |
| 3           | NPC Norm | Silencer  | NPC Fae  |          | successful                     |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Norm | Silencer    | False      | True      | True       | 1         | True   | 0              | 0                  |
| 3           | NPC Ken  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 3           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ann  | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Igi  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Gia  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Bob  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed   | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Mark | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Lee  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Ann  | Executioner | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Ann  | Executioner | vote      | Demagog has initiated a vote on eliminating Jailer               |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Bob  | Demagog     | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Bob  | Demagog     | vote      | Demagog has initiated a vote on eliminating Jailer               |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Cal  | Psychic     | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Cal  | Psychic     | reveal    | Player: NPC Lee is not possessed                                 |
| 3           | NPC Cal  | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 3           | NPC Cal  | Psychic     | reveal    | Player: NPC Han is not possessed                                 |
| 3           | NPC Cal  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 3           | NPC Cal  | Psychic     | reveal    | Player: NPC Mark is not possessed                                |
| 3           | NPC Cal  | Psychic     | reveal    | Player: NPC Ann is not possessed                                 |
| 3           | NPC Cal  | Psychic     | vote      | Demagog has initiated a vote on eliminating Jailer               |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Dan  | Medic       | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Dan  | Medic       | vote      | Demagog has initiated a vote on eliminating Jailer               |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Ed   | Assassin    | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Ed   | Assassin    | vote      | Demagog has initiated a vote on eliminating Jailer               |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Fae  | Spy         | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Fae  | Spy         | silenced  | You have been silenced                                           |
| 3           | NPC Fae  | Spy         | reveal    | NPC Norm is targeting NPC Fae                                    |
| 3           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Fae                                     |
| 3           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Fae                                     |
| 3           | NPC Fae  | Spy         | reveal    | NPC Igi is targeting NPC Han                                     |
| 3           | NPC Fae  | Spy         | reveal    | NPC Gia is targeting NPC Ann                                     |
| 3           | NPC Fae  | Spy         | reveal    | NPC Bob is targeting NPC Ann                                     |
| 3           | NPC Fae  | Spy         | reveal    | NPC Han is targeting NPC Jeff                                    |
| 3           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Ken                                     |
| 3           | NPC Fae  | Spy         | reveal    | NPC Ed is targeting NPC Jeff                                     |
| 3           | NPC Fae  | Spy         | reveal    | NPC Mark is targeting NPC Ann                                    |
| 3           | NPC Fae  | Spy         | vote      | Demagog has initiated a vote on eliminating Jailer               |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Gia  | Thief       | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Gia  | Thief       | vote      | Demagog has initiated a vote on eliminating Jailer               |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Han  | Prophet     | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Han  | Prophet     | vote      | Demagog has initiated a vote on eliminating Jailer               |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Igi  | Reporter    | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Igi  | Reporter    | reveal    | NPC Han is Prophet                                               |
| 3           | NPC Igi  | Reporter    | vote      | Demagog has initiated a vote on eliminating Jailer               |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Jeff | Priest      | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Jeff | Priest      | vote      | Demagog has initiated a vote on eliminating Jailer               |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Ken  | Trader      | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Ken  | Trader      | vote      | Demagog has initiated a vote on eliminating Jailer               |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Lee  | Jailer      | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Lee  | Jailer      | vote      | Demagog has initiated a vote on eliminating Jailer               |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Mark | Inspector   | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Mark | Inspector   | reveal    | Executioner is Innocent                                          |
| 3           | NPC Mark | Inspector   | vote      | Demagog has initiated a vote on eliminating Jailer               |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Reporter is not possessed     |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Bob         |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Fae          |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Norm         |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Norm         |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Ann          |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Jeff         |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ken          |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Jeff          |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Igi         |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Gia) am the Thief and I have made NPC Ann vulnerable      |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Igi) am the Reporter and NPC Han is the Prophet           |
| 3           | NPC Norm | Silencer    | broadcast | I (NPC Mark) inspected NPC Ann and they are not possessed        |
| 3           | NPC Norm | Silencer    | vote      | Demagog has initiated a vote on eliminating Jailer               |

#### Actions Round 4
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 4           | NPC Cal  | Psychic  |          |          | successful  |
| 4           | NPC Dan  | Medic    | NPC Ann  |          | successful  |
| 4           | NPC Fae  | Spy      |          |          | successful  |
| 4           | NPC Han  | Prophet  | NPC Fae  |          | successful  |
| 4           | NPC Norm | Silencer | NPC Lee  |          | successful  |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Norm | Silencer    | False      | True      | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Ken  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 4           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ann  | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Igi  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Gia  | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Bob  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed   | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Mark | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Lee  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 4           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Cal  | Psychic     | reveal    | Player: NPC Ann is not possessed                                 |
| 4           | NPC Cal  | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 4           | NPC Cal  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 4           | NPC Cal  | Psychic     | reveal    | Player: NPC Han is not possessed                                 |
| 4           | NPC Cal  | Psychic     | reveal    | Player: NPC Gia is not possessed                                 |
| 4           | NPC Cal  | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Fae  | Spy         | reveal    | NPC Norm is targeting NPC Lee                                    |
| 4           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Ann                                     |
| 4           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Ann                                     |
| 4           | NPC Fae  | Spy         | reveal    | NPC Igi is targeting NPC Han                                     |
| 4           | NPC Fae  | Spy         | reveal    | NPC Gia is targeting NPC Ann                                     |
| 4           | NPC Fae  | Spy         | reveal    | NPC Bob is targeting NPC Lee                                     |
| 4           | NPC Fae  | Spy         | reveal    | NPC Han is targeting NPC Lee                                     |
| 4           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Fae                                     |
| 4           | NPC Fae  | Spy         | reveal    | NPC Ed is targeting NPC Cal                                      |
| 4           | NPC Fae  | Spy         | reveal    | NPC Mark is targeting NPC Ann                                    |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Lee  | Jailer      | silenced  | You have been silenced                                           |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Inspector is not possessed    |
| 4           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |

#### Actions Round 5
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 5           | NPC Bob  | Demagog   | Silencer |          | voting in progress  |
| 5           | NPC Cal  | Psychic   |          |          | successful          |
| 5           | NPC Dan  | Medic     | NPC Igi  |          | successful          |
| 5           | NPC Ed   | Assassin  | Psychic  |          | successful          |
| 5           | NPC Fae  | Spy       |          |          | successful          |
| 5           | NPC Gia  | Thief     | NPC Bob  |          | successful          |
| 5           | NPC Han  | Prophet   | NPC Fae  |          | successful          |
| 5           | NPC Igi  | Reporter  | NPC Bob  |          | successful          |
| 5           | NPC Mark | Inspector | NPC Ed   |          | successful          |
| 5           | NPC Norm | Silencer  | NPC Mark |          | successful          |

#### States Round 5
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Norm | Silencer    | False      | True      | True       | 1         | True   | 0              | 0                  |
| 5           | NPC Ken  | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Fae  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ann  | Executioner | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Igi  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Gia  | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Bob  | Demagog     | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Jeff | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Han  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Dan  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ed   | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Mark | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Lee  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Ann  | Executioner | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Ann  | Executioner | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Bob  | Demagog     | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Bob  | Demagog     | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Cal  | Psychic     | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Cal  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 5           | NPC Cal  | Psychic     | reveal    | Player: NPC Lee is not possessed                                 |
| 5           | NPC Cal  | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 5           | NPC Cal  | Psychic     | reveal    | Player: NPC Dan is not possessed                                 |
| 5           | NPC Cal  | Psychic     | reveal    | Player: NPC Ken is not possessed                                 |
| 5           | NPC Cal  | Psychic     | reveal    | Player: NPC Bob is not possessed                                 |
| 5           | NPC Cal  | Psychic     | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Dan  | Medic       | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Dan  | Medic       | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Ed   | Assassin    | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Ed   | Assassin    | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Fae  | Spy         | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Fae  | Spy         | reveal    | NPC Norm is targeting NPC Mark                                   |
| 5           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Ann                                     |
| 5           | NPC Fae  | Spy         | reveal    | NPC Ken is targeting NPC Ann                                     |
| 5           | NPC Fae  | Spy         | reveal    | NPC Igi is targeting NPC Bob                                     |
| 5           | NPC Fae  | Spy         | reveal    | NPC Gia is targeting NPC Bob                                     |
| 5           | NPC Fae  | Spy         | reveal    | NPC Bob is targeting NPC Lee                                     |
| 5           | NPC Fae  | Spy         | reveal    | NPC Han is targeting NPC Fae                                     |
| 5           | NPC Fae  | Spy         | reveal    | NPC Dan is targeting NPC Ann                                     |
| 5           | NPC Fae  | Spy         | reveal    | NPC Ed is targeting NPC Cal                                      |
| 5           | NPC Fae  | Spy         | reveal    | NPC Mark is targeting NPC Ed                                     |
| 5           | NPC Fae  | Spy         | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Gia  | Thief       | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Gia  | Thief       | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Han  | Prophet     | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Han  | Prophet     | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Igi  | Reporter    | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Igi  | Reporter    | reveal    | NPC Bob is Demagog                                               |
| 5           | NPC Igi  | Reporter    | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Jeff | Priest      | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Jeff | Priest      | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Ken  | Trader      | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Ken  | Trader      | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Lee  | Jailer      | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Lee  | Jailer      | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Mark | Inspector   | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Mark | Inspector   | reveal    | Assassin is Innocent                                             |
| 5           | NPC Mark | Inspector   | silenced  | You have been silenced                                           |
| 5           | NPC Mark | Inspector   | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Executioner is not possessed  |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Medic is not possessed        |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Prophet is not possessed      |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Thief is not possessed        |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Jailer is not possessed       |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Priest is not possessed       |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Cal) am the Psychic and the Demagog is not possessed      |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Norm is targeting NPC Lee         |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ken is targeting NPC Ann          |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Igi is targeting NPC Han          |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Gia is targeting NPC Ann          |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Bob is targeting NPC Lee          |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Han is targeting NPC Fae          |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Dan is targeting NPC Ann          |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Ed is targeting NPC Cal           |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Fae) am the Spy and NPC Mark is targeting NPC Ann         |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Gia) am the Thief and I have made NPC Bob vulnerable      |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Igi) am the Reporter and NPC Bob is the Demagog           |
| 5           | NPC Norm | Silencer    | broadcast | I (NPC Mark) inspected NPC Ed and they are not possessed         |
| 5           | NPC Norm | Silencer    | vote      | Demagog has initiated a vote on eliminating Silencer             |