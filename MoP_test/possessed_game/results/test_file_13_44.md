#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 44   | 13      | 4       |

#### Roles
| Role         |
| :----------- |
| Executioner  |
| Psychic      |
| Demagog      |
| Assassin     |
| Prophet      |
| Reporter     |
| Priest       |
| Jailer       |
| Judge        |
| Medic        |
| Trader       |
| Silencer     |
| Spy          |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Assassin    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Mark | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Ann  | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Bob  | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Bob  | Assassin    | possessed   | You are Possessed         |
| 0           | NPC Cal  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Cal  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Trader      | role change | Your Role is Trader       |
| 0           | NPC Dan  | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Ed   | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Fae  | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Gia  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Han  | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Igi  | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Jeff | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Ken  | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Priest      | role change | Your Role is Priest       |
| 0           | NPC Lee  | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Mark | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Mark | Reporter    | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player   | action   | Target 1 | Target 2 | status                         |
| :-----------| :--------| :--------| :--------| :--------| :----------------------------- |
| 1           | NPC Ann  | Demagog  | Silencer |          | voting in progress             |
| 1           | NPC Bob  | Assassin | Judge    |          | successful                     |
| 1           | NPC Dan  | Trader   | NPC Cal  | NPC Jeff | failed because not vulnerable  |
| 1           | NPC Fae  | Silencer | NPC Han  |          | successful                     |
| 1           | NPC Gia  | Judge    | Silencer |          | successful                     |
| 1           | NPC Han  | Psychic  |          |          | successful                     |
| 1           | NPC Igi  | Spy      |          |          | successful                     |
| 1           | NPC Jeff | Prophet  | NPC Fae  |          | successful                     |
| 1           | NPC Ken  | Medic    | NPC Han  |          | successful                     |
| 1           | NPC Mark | Reporter | NPC Lee  |          | successful                     |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob  | Assassin    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Jeff | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Mark | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Lee  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ken  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Fae  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Igi  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Ann  | Demagog     | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Priest        |
| 1           | NPC Ann  | Demagog     | vote      | Demagog has initiated a vote on eliminating Silencer          |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Bob  | Assassin    | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Priest        |
| 1           | NPC Bob  | Assassin    | vote      | Demagog has initiated a vote on eliminating Silencer          |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Cal  | Executioner | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Priest        |
| 1           | NPC Cal  | Executioner | vote      | Demagog has initiated a vote on eliminating Silencer          |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Dan  | Trader      | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Priest        |
| 1           | NPC Dan  | Trader      | vote      | Demagog has initiated a vote on eliminating Silencer          |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Priest        |
| 1           | NPC Ed   | Jailer      | vote      | Demagog has initiated a vote on eliminating Silencer          |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Priest        |
| 1           | NPC Fae  | Silencer    | vote      | Demagog has initiated a vote on eliminating Silencer          |
| 1           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 1           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Gia  | Judge       | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Priest        |
| 1           | NPC Gia  | Judge       | vote      | Demagog has initiated a vote on eliminating Silencer          |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Han  | Psychic     | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Priest        |
| 1           | NPC Han  | Psychic     | silenced  | You have been silenced                                        |
| 1           | NPC Han  | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 1           | NPC Han  | Psychic     | reveal    | Player: NPC Ed is not possessed                               |
| 1           | NPC Han  | Psychic     | reveal    | Player: NPC Cal is not possessed                              |
| 1           | NPC Han  | Psychic     | reveal    | Player: NPC Lee is not possessed                              |
| 1           | NPC Han  | Psychic     | reveal    | Player: NPC Mark is not possessed                             |
| 1           | NPC Han  | Psychic     | reveal    | Player: NPC Jeff is not possessed                             |
| 1           | NPC Han  | Psychic     | vote      | Demagog has initiated a vote on eliminating Silencer          |
| 1           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 1           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Igi  | Spy         | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Priest        |
| 1           | NPC Igi  | Spy         | reveal    | NPC Mark is targeting NPC Lee                                 |
| 1           | NPC Igi  | Spy         | reveal    | NPC Gia is targeting NPC Fae                                  |
| 1           | NPC Igi  | Spy         | reveal    | NPC Fae is targeting NPC Han                                  |
| 1           | NPC Igi  | Spy         | vote      | Demagog has initiated a vote on eliminating Silencer          |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Jeff | Prophet     | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Priest        |
| 1           | NPC Jeff | Prophet     | vote      | Demagog has initiated a vote on eliminating Silencer          |
| 1           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 1           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Ken  | Medic       | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Priest        |
| 1           | NPC Ken  | Medic       | vote      | Demagog has initiated a vote on eliminating Silencer          |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Lee  | Priest      | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Priest        |
| 1           | NPC Lee  | Priest      | vote      | Demagog has initiated a vote on eliminating Silencer          |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Trader is not possessed    |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed  |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed     |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed       |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed    |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Priest        |
| 1           | NPC Mark | Reporter    | reveal    | NPC Lee is Priest                                             |
| 1           | NPC Mark | Reporter    | vote      | Demagog has initiated a vote on eliminating Silencer          |

#### Actions Round 2
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 2           | NPC Fae  | Silencer | NPC Lee  |          | successful  |
| 2           | NPC Gia  | Judge    | Assassin |          | successful  |
| 2           | NPC Han  | Psychic  |          |          | successful  |
| 2           | NPC Igi  | Spy      |          |          | successful  |
| 2           | NPC Jeff | Prophet  | NPC Ann  |          | successful  |
| 2           | NPC Ken  | Medic    | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ann  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob  | Assassin    | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Jeff | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Mark | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Lee  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ken  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Fae  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Igi  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                   |
| :-----------| :--------| :-----------| :---------| :-------------------------------------------------------- |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae   |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia   |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Fae  |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee  |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Fae   |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Han   |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Han   |
| 2           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae   |
| 2           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia   |
| 2           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Fae  |
| 2           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee  |
| 2           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Fae   |
| 2           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Han   |
| 2           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Han   |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae   |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia   |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Fae  |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee  |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Fae   |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Han   |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Han   |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae   |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia   |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Fae  |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee  |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Fae   |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Han   |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Han   |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae   |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia   |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Fae  |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee  |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Fae   |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Han   |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Han   |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae   |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia   |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Fae  |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee  |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Fae   |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Han   |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Han   |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae   |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia   |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Fae  |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee  |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Fae   |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Han   |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Han   |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae   |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia   |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Fae  |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee  |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Fae   |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Han   |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Han   |
| 2           | NPC Han  | Psychic     | reveal    | Player: NPC Gia is not possessed                          |
| 2           | NPC Han  | Psychic     | reveal    | Player: NPC Jeff is not possessed                         |
| 2           | NPC Han  | Psychic     | reveal    | Player: NPC Ann is not possessed                          |
| 2           | NPC Han  | Psychic     | reveal    | Player: NPC Ken is not possessed                          |
| 2           | NPC Han  | Psychic     | reveal    | Player: NPC Lee is not possessed                          |
| 2           | NPC Han  | Psychic     | reveal    | Player: NPC Mark is not possessed                         |
| 2           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae   |
| 2           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia   |
| 2           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Fae  |
| 2           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee  |
| 2           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Fae   |
| 2           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Han   |
| 2           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Han   |
| 2           | NPC Igi  | Spy         | reveal    | NPC Ann is targeting NPC Fae                              |
| 2           | NPC Igi  | Spy         | reveal    | NPC Bob is targeting NPC Gia                              |
| 2           | NPC Igi  | Spy         | reveal    | NPC Jeff is targeting NPC Fae                             |
| 2           | NPC Igi  | Spy         | reveal    | NPC Mark is targeting NPC Lee                             |
| 2           | NPC Igi  | Spy         | reveal    | NPC Gia is targeting NPC Bob                              |
| 2           | NPC Igi  | Spy         | reveal    | NPC Ken is targeting NPC Han                              |
| 2           | NPC Igi  | Spy         | reveal    | NPC Dan is targeting NPC Cal                              |
| 2           | NPC Igi  | Spy         | reveal    | NPC Dan is targeting NPC Cal                              |
| 2           | NPC Igi  | Spy         | reveal    | NPC Fae is targeting NPC Lee                              |
| 2           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae   |
| 2           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia   |
| 2           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Fae  |
| 2           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee  |
| 2           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Fae   |
| 2           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Han   |
| 2           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Han   |
| 2           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae   |
| 2           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia   |
| 2           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Fae  |
| 2           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee  |
| 2           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Fae   |
| 2           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Han   |
| 2           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Han   |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae   |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia   |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Fae  |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee  |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Fae   |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Han   |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Han   |
| 2           | NPC Lee  | Priest      | silenced  | You have been silenced                                    |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae   |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia   |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Fae  |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee  |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Fae   |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Han   |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal   |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Han   |

#### Actions Round 3
| round_index | Player   | action   | Target 1 | Target 2 | status              |
| :-----------| :--------| :--------| :--------| :--------| :------------------ |
| 3           | NPC Ann  | Demagog  | Assassin |          | voting in progress  |
| 3           | NPC Bob  | Assassin | Silencer |          | successful          |
| 3           | NPC Fae  | Silencer | NPC Jeff |          | successful          |
| 3           | NPC Gia  | Judge    | Medic    |          | successful          |
| 3           | NPC Han  | Psychic  |          |          | successful          |
| 3           | NPC Igi  | Spy      |          |          | successful          |
| 3           | NPC Jeff | Prophet  | NPC Ed   |          | successful          |
| 3           | NPC Ken  | Medic    | NPC Bob  |          | successful          |
| 3           | NPC Mark | Reporter | NPC Gia  |          | successful          |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Han  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ann  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Bob  | Assassin    | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Jeff | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Mark | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Lee  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ken  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Dan  | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Fae  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Igi  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message   | details                                                      |
| :-----------| :--------| :-----------| :---------| :----------------------------------------------------------- |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed      |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed    |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Medic is not possessed    |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia      |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ann     |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee     |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Ann      |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Lee      |
| 3           | NPC Ann  | Demagog     | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed      |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed    |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Medic is not possessed    |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia      |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ann     |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee     |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Ann      |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Lee      |
| 3           | NPC Bob  | Assassin    | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed      |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed    |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Medic is not possessed    |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia      |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ann     |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee     |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Ann      |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Lee      |
| 3           | NPC Cal  | Executioner | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed    |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Medic is not possessed    |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ann     |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee     |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Ann      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Lee      |
| 3           | NPC Dan  | Trader      | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed      |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed    |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Medic is not possessed    |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia      |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ann     |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee     |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Ann      |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Lee      |
| 3           | NPC Ed   | Jailer      | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed      |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed    |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Medic is not possessed    |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia      |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ann     |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee     |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Ann      |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Lee      |
| 3           | NPC Fae  | Silencer    | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed    |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Medic is not possessed    |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ann     |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee     |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Ann      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Lee      |
| 3           | NPC Gia  | Judge       | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed      |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed    |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Medic is not possessed    |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia      |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ann     |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee     |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Ann      |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Lee      |
| 3           | NPC Han  | Psychic     | reveal    | Player: NPC Dan is not possessed                             |
| 3           | NPC Han  | Psychic     | reveal    | Player: NPC Jeff is not possessed                            |
| 3           | NPC Han  | Psychic     | reveal    | Player: NPC Mark is not possessed                            |
| 3           | NPC Han  | Psychic     | reveal    | Player: NPC Gia is not possessed                             |
| 3           | NPC Han  | Psychic     | reveal    | Player: NPC Lee is not possessed                             |
| 3           | NPC Han  | Psychic     | reveal    | Player: NPC Ann is not possessed                             |
| 3           | NPC Han  | Psychic     | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed      |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed    |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Medic is not possessed    |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia      |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ann     |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee     |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Ann      |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Lee      |
| 3           | NPC Igi  | Spy         | reveal    | NPC Ann is targeting NPC Fae                                 |
| 3           | NPC Igi  | Spy         | reveal    | NPC Bob is targeting NPC Gia                                 |
| 3           | NPC Igi  | Spy         | reveal    | NPC Jeff is targeting NPC Ann                                |
| 3           | NPC Igi  | Spy         | reveal    | NPC Mark is targeting NPC Gia                                |
| 3           | NPC Igi  | Spy         | reveal    | NPC Gia is targeting NPC Ken                                 |
| 3           | NPC Igi  | Spy         | reveal    | NPC Ken is targeting NPC Ann                                 |
| 3           | NPC Igi  | Spy         | reveal    | NPC Dan is targeting NPC Cal                                 |
| 3           | NPC Igi  | Spy         | reveal    | NPC Dan is targeting NPC Cal                                 |
| 3           | NPC Igi  | Spy         | reveal    | NPC Fae is targeting NPC Jeff                                |
| 3           | NPC Igi  | Spy         | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed      |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed    |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Medic is not possessed    |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia      |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ann     |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee     |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Ann      |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Lee      |
| 3           | NPC Jeff | Prophet     | silenced  | You have been silenced                                       |
| 3           | NPC Jeff | Prophet     | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed      |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed    |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Medic is not possessed    |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia      |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ann     |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee     |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Ann      |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Lee      |
| 3           | NPC Ken  | Medic       | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed      |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed    |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Medic is not possessed    |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia      |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ann     |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee     |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Ann      |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Lee      |
| 3           | NPC Lee  | Priest      | vote      | Demagog has initiated a vote on eliminating Assassin         |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Spy is not possessed      |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed    |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Medic is not possessed    |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed  |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed   |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Fae      |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Gia      |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ann     |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Lee     |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Bob      |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Ann      |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal      |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Lee      |
| 3           | NPC Mark | Reporter    | reveal    | NPC Gia is Judge                                             |
| 3           | NPC Mark | Reporter    | vote      | Demagog has initiated a vote on eliminating Assassin         |

#### Actions Round 4
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 4           | NPC Bob  | Assassin | Psychic  |          | successful  |
| 4           | NPC Fae  | Silencer | NPC Bob  |          | successful  |
| 4           | NPC Gia  | Judge    | Assassin |          | successful  |
| 4           | NPC Han  | Psychic  |          |          | successful  |
| 4           | NPC Igi  | Spy      |          |          | successful  |
| 4           | NPC Jeff | Prophet  | NPC Lee  |          | successful  |
| 4           | NPC Ken  | Medic    | NPC Jeff |          | successful  |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Han  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ann  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Bob  | Assassin    | False      | True      | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Jeff | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Mark | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Lee  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Gia  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ken  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Dan  | Trader      | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Fae  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Igi  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed       |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Bob          |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Fae          |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ed          |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Gia         |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ken          |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Bob          |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Ann  | Demagog     | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Jeff         |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed       |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Bob          |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Fae          |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ed          |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Gia         |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ken          |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Bob          |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Bob  | Assassin    | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Jeff         |
| 4           | NPC Bob  | Assassin    | silenced  | You have been silenced                                           |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed       |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Bob          |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Fae          |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ed          |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Gia         |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ken          |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Bob          |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Cal  | Executioner | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Jeff         |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed       |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Bob          |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Fae          |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ed          |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Gia         |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ken          |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Bob          |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Dan  | Trader      | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Jeff         |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed       |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Bob          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Fae          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ed          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Gia         |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ken          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Bob          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Ed   | Jailer      | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Jeff         |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed       |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Bob          |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Fae          |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ed          |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Gia         |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ken          |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Bob          |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Jeff         |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed       |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Bob          |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Fae          |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ed          |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Gia         |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ken          |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Bob          |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Gia  | Judge       | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Jeff         |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed       |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Bob          |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Fae          |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ed          |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Gia         |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ken          |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Bob          |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Han  | Psychic     | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Jeff         |
| 4           | NPC Han  | Psychic     | reveal    | Player: NPC Lee is not possessed                                 |
| 4           | NPC Han  | Psychic     | reveal    | Player: NPC Mark is not possessed                                |
| 4           | NPC Han  | Psychic     | reveal    | Player: NPC Gia is not possessed                                 |
| 4           | NPC Han  | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 4           | NPC Han  | Psychic     | reveal    | Player: NPC Ann is not possessed                                 |
| 4           | NPC Han  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed       |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Bob          |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Fae          |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ed          |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Gia         |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ken          |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Bob          |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Igi  | Spy         | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Jeff         |
| 4           | NPC Igi  | Spy         | reveal    | NPC Ann is targeting NPC Bob                                     |
| 4           | NPC Igi  | Spy         | reveal    | NPC Bob is targeting NPC Fae                                     |
| 4           | NPC Igi  | Spy         | reveal    | NPC Jeff is targeting NPC Ed                                     |
| 4           | NPC Igi  | Spy         | reveal    | NPC Mark is targeting NPC Gia                                    |
| 4           | NPC Igi  | Spy         | reveal    | NPC Gia is targeting NPC Bob                                     |
| 4           | NPC Igi  | Spy         | reveal    | NPC Ken is targeting NPC Bob                                     |
| 4           | NPC Igi  | Spy         | reveal    | NPC Dan is targeting NPC Cal                                     |
| 4           | NPC Igi  | Spy         | reveal    | NPC Dan is targeting NPC Cal                                     |
| 4           | NPC Igi  | Spy         | reveal    | NPC Fae is targeting NPC Bob                                     |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed       |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Bob          |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Fae          |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ed          |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Gia         |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ken          |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Bob          |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Jeff | Prophet     | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Jeff         |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed       |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Bob          |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Fae          |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ed          |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Gia         |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ken          |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Bob          |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Ken  | Medic       | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Jeff         |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed       |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Bob          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Fae          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ed          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Gia         |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ken          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Bob          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Lee  | Priest      | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Jeff         |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Executioner is not possessed  |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Jailer is not possessed       |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Priest is not possessed       |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Silencer is not possessed     |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Demagog is not possessed      |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Han) am the Psychic and the Judge is not possessed        |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Ann is targeting NPC Bob          |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Bob is targeting NPC Fae          |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Jeff is targeting NPC Ed          |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Mark is targeting NPC Gia         |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Gia is targeting NPC Ken          |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Ken is targeting NPC Bob          |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Dan is targeting NPC Cal          |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Igi) am the Spy and NPC Fae is targeting NPC Jeff         |