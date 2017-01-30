#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 63   | 13      | 7       |

#### Roles
| Role         |
| :----------- |
| Assassin     |
| Demagog      |
| Priest       |
| Jailer       |
| Spy          |
| Thief        |
| Psychic      |
| Reporter     |
| Trader       |
| Medic        |
| Silencer     |
| Inspector    |
| Executioner  |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Jailer      | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Mark | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Priest      | role change | Your Role is Priest       |
| 0           | NPC Ann  | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Bob  | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Bob  | Jailer      | possessed   | You are Possessed         |
| 0           | NPC Cal  | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Cal  | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Dan  | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Ed   | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Fae  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Trader      | role change | Your Role is Trader       |
| 0           | NPC Gia  | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Han  | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Igi  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Spy         | role change | Your Role is Spy          |
| 0           | NPC Jeff | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Ken  | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Lee  | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Mark | Thief       | role change | Your Role is Thief        |
| 0           | NPC Mark | Thief       | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 1           | NPC Bob  | Jailer    | NPC Igi  |          | successful          |
| 1           | NPC Cal  | Assassin  | Trader   |          | successful          |
| 1           | NPC Dan  | Silencer  | NPC Cal  |          | successful          |
| 1           | NPC Ed   | Reporter  | NPC Bob  |          | successful          |
| 1           | NPC Fae  | Inspector | NPC Han  |          | successful          |
| 1           | NPC Gia  | Trader    | NPC Fae  | NPC Ken  | successful          |
| 1           | NPC Han  | Demagog   | Silencer |          | voting in progress  |
| 1           | NPC Jeff | Spy       |          |          | successful          |
| 1           | NPC Ken  | Medic     | NPC Han  |          | successful          |
| 1           | NPC Lee  | Psychic   |          |          | successful          |
| 1           | NPC Mark | Thief     | NPC Dan  |          | successful          |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Han  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob  | Jailer      | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Jeff | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Mark | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Lee  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ed   | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Gia  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Ken  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Silencer    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 1           | NPC Fae  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Igi  | Executioner | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 1           | NPC Ann  | Priest      | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Jailer             |
| 1           | NPC Ann  | Priest      | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed         |
| 1           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 1           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ann  | Priest      | broadcast | I (NPC Mark) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Ann  | Priest      | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Jailer             |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed         |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed        |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed       |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 1           | NPC Bob  | Jailer      | broadcast | I (NPC Mark) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Bob  | Jailer      | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Jailer             |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed         |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed        |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed       |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 1           | NPC Cal  | Assassin    | broadcast | I (NPC Mark) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Cal  | Assassin    | silenced  | You have been silenced                                           |
| 1           | NPC Cal  | Assassin    | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Jailer             |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed         |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed        |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed       |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 1           | NPC Dan  | Silencer    | broadcast | I (NPC Mark) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Dan  | Silencer    | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Jailer             |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed         |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Ed   | Reporter    | reveal    | NPC Bob is Jailer                                                |
| 1           | NPC Ed   | Reporter    | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 1           | NPC Fae  | Medic       | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Jailer             |
| 1           | NPC Fae  | Medic       | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed         |
| 1           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed        |
| 1           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed       |
| 1           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 1           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 1           | NPC Fae  | Medic       | broadcast | I (NPC Mark) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Fae  | Medic       | reveal    | Demagog is Innocent                                              |
| 1           | NPC Fae  | Medic       | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 1           | NPC Gia  | Trader      | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Jailer             |
| 1           | NPC Gia  | Trader      | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed         |
| 1           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed        |
| 1           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed       |
| 1           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 1           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 1           | NPC Gia  | Trader      | broadcast | I (NPC Mark) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Gia  | Trader      | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 1           | NPC Han  | Demagog     | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Jailer             |
| 1           | NPC Han  | Demagog     | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed         |
| 1           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed        |
| 1           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed       |
| 1           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 1           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 1           | NPC Han  | Demagog     | broadcast | I (NPC Mark) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Han  | Demagog     | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Jailer             |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed         |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed        |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed       |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Mark) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Igi  | Executioner | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 1           | NPC Jeff | Spy         | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Jailer             |
| 1           | NPC Jeff | Spy         | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed         |
| 1           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed        |
| 1           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed       |
| 1           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 1           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 1           | NPC Jeff | Spy         | broadcast | I (NPC Mark) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Jeff | Spy         | reveal    | NPC Mark is targeting NPC Dan                                    |
| 1           | NPC Jeff | Spy         | reveal    | NPC Ed is targeting NPC Bob                                      |
| 1           | NPC Jeff | Spy         | reveal    | NPC Dan is targeting NPC Cal                                     |
| 1           | NPC Jeff | Spy         | reveal    | NPC Fae is targeting NPC Han                                     |
| 1           | NPC Jeff | Spy         | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Jailer             |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed         |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ken  | Inspector   | broadcast | I (NPC Mark) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Ken  | Inspector   | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Jailer             |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed         |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed        |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed       |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 1           | NPC Lee  | Psychic     | broadcast | I (NPC Mark) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Lee  | Psychic     | reveal    | Player: NPC Mark is not possessed                                |
| 1           | NPC Lee  | Psychic     | reveal    | Player: NPC Fae is not possessed                                 |
| 1           | NPC Lee  | Psychic     | reveal    | Player: NPC Jeff is not possessed                                |
| 1           | NPC Lee  | Psychic     | reveal    | Player: NPC Ann is not possessed                                 |
| 1           | NPC Lee  | Psychic     | reveal    | Player: NPC Han is not possessed                                 |
| 1           | NPC Lee  | Psychic     | reveal    | Player: NPC Ken is not possessed                                 |
| 1           | NPC Lee  | Psychic     | vote      | Demagog has initiated a vote on eliminating Silencer             |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Ed) am the Reporter and NPC Bob is the Jailer             |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Fae) inspected NPC Han and they are not possessed         |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed        |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed       |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed       |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed          |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Mark) am the Thief and I have made NPC Dan vulnerable     |
| 1           | NPC Mark | Thief       | vote      | Demagog has initiated a vote on eliminating Silencer             |

#### Actions Round 2
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 2           | NPC Dan  | Silencer  | NPC Bob  |          | successful          |
| 2           | NPC Fae  | Medic     | NPC Ann  |          | successful          |
| 2           | NPC Han  | Demagog   | Psychic  |          | voting in progress  |
| 2           | NPC Jeff | Spy       |          |          | successful          |
| 2           | NPC Ken  | Inspector | NPC Ed   |          | successful          |
| 2           | NPC Lee  | Psychic   |          |          | successful          |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Han  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Ann  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob  | Jailer      | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Jeff | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Mark | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Lee  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed   | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Ken  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Dan  | Silencer    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Fae  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Igi  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia      |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Dan      |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan     |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob       |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Han      |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Cal      |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Ken) inspected NPC Ed and they are not possessed       |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 2           | NPC Ann  | Priest      | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia      |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Dan      |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan     |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob       |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Han      |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Cal      |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Ken) inspected NPC Ed and they are not possessed       |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 2           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 2           | NPC Bob  | Jailer      | silenced  | You have been silenced                                        |
| 2           | NPC Bob  | Jailer      | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia      |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Dan      |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan     |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob       |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Han      |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Cal      |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Ken) inspected NPC Ed and they are not possessed       |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 2           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 2           | NPC Cal  | Assassin    | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia      |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Dan      |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan     |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob       |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Han      |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Cal      |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Ken) inspected NPC Ed and they are not possessed       |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 2           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 2           | NPC Dan  | Silencer    | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia      |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Dan      |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan     |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob       |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Han      |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Cal      |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) inspected NPC Ed and they are not possessed       |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 2           | NPC Ed   | Reporter    | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia      |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Dan      |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan     |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob       |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Han      |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Cal      |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Ken) inspected NPC Ed and they are not possessed       |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 2           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 2           | NPC Fae  | Medic       | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia      |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Dan      |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan     |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob       |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Han      |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Cal      |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Ken) inspected NPC Ed and they are not possessed       |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 2           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 2           | NPC Gia  | Trader      | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia      |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Dan      |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan     |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob       |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Han      |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Cal      |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Ken) inspected NPC Ed and they are not possessed       |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 2           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 2           | NPC Han  | Demagog     | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia      |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Dan      |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan     |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob       |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Han      |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Cal      |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Ken) inspected NPC Ed and they are not possessed       |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 2           | NPC Igi  | Executioner | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia      |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Dan      |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan     |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob       |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Han      |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Cal      |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Ken) inspected NPC Ed and they are not possessed       |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 2           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 2           | NPC Jeff | Spy         | reveal    | NPC Cal is targeting NPC Gia                                  |
| 2           | NPC Jeff | Spy         | reveal    | NPC Han is targeting NPC Dan                                  |
| 2           | NPC Jeff | Spy         | reveal    | NPC Bob is targeting NPC Igi                                  |
| 2           | NPC Jeff | Spy         | reveal    | NPC Mark is targeting NPC Dan                                 |
| 2           | NPC Jeff | Spy         | reveal    | NPC Ed is targeting NPC Bob                                   |
| 2           | NPC Jeff | Spy         | reveal    | NPC Gia is targeting NPC Fae                                  |
| 2           | NPC Jeff | Spy         | reveal    | NPC Gia is targeting NPC Fae                                  |
| 2           | NPC Jeff | Spy         | reveal    | NPC Ken is targeting NPC Ed                                   |
| 2           | NPC Jeff | Spy         | reveal    | NPC Dan is targeting NPC Bob                                  |
| 2           | NPC Jeff | Spy         | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia      |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Dan      |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan     |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob       |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Han      |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Cal      |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Ken) inspected NPC Ed and they are not possessed       |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 2           | NPC Ken  | Inspector   | reveal    | Reporter is Innocent                                          |
| 2           | NPC Ken  | Inspector   | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia      |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Dan      |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan     |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob       |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Han      |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Cal      |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Ken) inspected NPC Ed and they are not possessed       |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 2           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 2           | NPC Lee  | Psychic     | reveal    | Player: NPC Han is not possessed                              |
| 2           | NPC Lee  | Psychic     | reveal    | Player: NPC Ann is not possessed                              |
| 2           | NPC Lee  | Psychic     | reveal    | Player: NPC Gia is not possessed                              |
| 2           | NPC Lee  | Psychic     | reveal    | Player: NPC Jeff is not possessed                             |
| 2           | NPC Lee  | Psychic     | reveal    | Player: NPC Fae is not possessed                              |
| 2           | NPC Lee  | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 2           | NPC Lee  | Psychic     | vote      | Demagog has initiated a vote on eliminating Psychic           |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia      |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Dan      |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan     |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob       |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Han      |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Cal      |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Ken) inspected NPC Ed and they are not possessed       |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 2           | NPC Mark | Thief       | vote      | Demagog has initiated a vote on eliminating Psychic           |

#### Actions Round 3
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 3           | NPC Bob  | Jailer   | NPC Igi  |          | successful  |
| 3           | NPC Cal  | Assassin | Thief    |          | successful  |
| 3           | NPC Dan  | Silencer | NPC Ken  |          | successful  |
| 3           | NPC Ed   | Reporter | NPC Han  |          | successful  |
| 3           | NPC Fae  | Medic    | NPC Bob  |          | successful  |
| 3           | NPC Jeff | Spy      |          |          | successful  |
| 3           | NPC Lee  | Psychic  |          |          | successful  |
| 3           | NPC Mark | Thief    | NPC Bob  |          | successful  |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Han  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ann  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob  | Jailer      | False      | True      | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Jeff | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Mark | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Lee  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ed   | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Gia  | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Ken  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Dan  | Silencer    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 3           | NPC Fae  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Igi  | Executioner | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Ed) am the Reporter and NPC Han is the Demagog          |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia       |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee       |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi       |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan      |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob        |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Ann       |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed      |
| 3           | NPC Ann  | Priest      | broadcast | I (NPC Mark) am the Thief and I have made NPC Bob vulnerable   |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Ed) am the Reporter and NPC Han is the Demagog          |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia       |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee       |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi       |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan      |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob        |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Ann       |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed      |
| 3           | NPC Bob  | Jailer      | broadcast | I (NPC Mark) am the Thief and I have made NPC Bob vulnerable   |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Ed) am the Reporter and NPC Han is the Demagog          |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia       |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee       |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi       |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan      |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob        |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Ann       |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed      |
| 3           | NPC Cal  | Assassin    | broadcast | I (NPC Mark) am the Thief and I have made NPC Bob vulnerable   |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Reporter and NPC Han is the Demagog          |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia       |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee       |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi       |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan      |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob        |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Ann       |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed      |
| 3           | NPC Dan  | Silencer    | broadcast | I (NPC Mark) am the Thief and I have made NPC Bob vulnerable   |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Ed) am the Reporter and NPC Han is the Demagog          |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia       |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee       |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi       |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan      |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob        |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Ann       |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed      |
| 3           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Thief and I have made NPC Bob vulnerable   |
| 3           | NPC Ed   | Reporter    | reveal    | NPC Han is Demagog                                             |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Ed) am the Reporter and NPC Han is the Demagog          |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia       |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee       |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi       |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan      |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob        |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Ann       |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed      |
| 3           | NPC Fae  | Medic       | broadcast | I (NPC Mark) am the Thief and I have made NPC Bob vulnerable   |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Ed) am the Reporter and NPC Han is the Demagog          |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia       |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee       |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi       |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan      |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob        |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Ann       |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed      |
| 3           | NPC Gia  | Trader      | broadcast | I (NPC Mark) am the Thief and I have made NPC Bob vulnerable   |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Ed) am the Reporter and NPC Han is the Demagog          |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia       |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee       |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi       |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan      |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob        |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Ann       |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed      |
| 3           | NPC Han  | Demagog     | broadcast | I (NPC Mark) am the Thief and I have made NPC Bob vulnerable   |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Ed) am the Reporter and NPC Han is the Demagog          |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia       |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee       |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi       |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan      |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob        |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Ann       |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed      |
| 3           | NPC Igi  | Executioner | broadcast | I (NPC Mark) am the Thief and I have made NPC Bob vulnerable   |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Ed) am the Reporter and NPC Han is the Demagog          |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia       |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee       |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi       |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan      |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob        |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Ann       |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed      |
| 3           | NPC Jeff | Spy         | broadcast | I (NPC Mark) am the Thief and I have made NPC Bob vulnerable   |
| 3           | NPC Jeff | Spy         | reveal    | NPC Cal is targeting NPC Gia                                   |
| 3           | NPC Jeff | Spy         | reveal    | NPC Han is targeting NPC Lee                                   |
| 3           | NPC Jeff | Spy         | reveal    | NPC Bob is targeting NPC Igi                                   |
| 3           | NPC Jeff | Spy         | reveal    | NPC Mark is targeting NPC Bob                                  |
| 3           | NPC Jeff | Spy         | reveal    | NPC Ed is targeting NPC Han                                    |
| 3           | NPC Jeff | Spy         | reveal    | NPC Gia is targeting NPC Fae                                   |
| 3           | NPC Jeff | Spy         | reveal    | NPC Gia is targeting NPC Fae                                   |
| 3           | NPC Jeff | Spy         | reveal    | NPC Ken is targeting NPC Ed                                    |
| 3           | NPC Jeff | Spy         | reveal    | NPC Dan is targeting NPC Ken                                   |
| 3           | NPC Jeff | Spy         | reveal    | NPC Fae is targeting NPC Ann                                   |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Reporter and NPC Han is the Demagog          |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia       |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee       |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi       |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan      |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob        |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Ann       |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed      |
| 3           | NPC Ken  | Inspector   | broadcast | I (NPC Mark) am the Thief and I have made NPC Bob vulnerable   |
| 3           | NPC Ken  | Inspector   | silenced  | You have been silenced                                         |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Reporter and NPC Han is the Demagog          |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia       |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee       |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi       |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan      |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob        |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Ann       |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed      |
| 3           | NPC Lee  | Psychic     | broadcast | I (NPC Mark) am the Thief and I have made NPC Bob vulnerable   |
| 3           | NPC Lee  | Psychic     | reveal    | Player: NPC Ann is not possessed                               |
| 3           | NPC Lee  | Psychic     | reveal    | Player: NPC Gia is not possessed                               |
| 3           | NPC Lee  | Psychic     | reveal    | Player: NPC Ken is not possessed                               |
| 3           | NPC Lee  | Psychic     | reveal    | Player: NPC Ed is not possessed                                |
| 3           | NPC Lee  | Psychic     | reveal    | Player: NPC Cal is not possessed                               |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Ed) am the Reporter and NPC Han is the Demagog          |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Gia       |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee       |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi       |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Dan      |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Bob        |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Ann       |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed    |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed      |
| 3           | NPC Mark | Thief       | broadcast | I (NPC Mark) am the Thief and I have made NPC Bob vulnerable   |

#### Actions Round 4
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 4           | NPC Bob  | Jailer    | NPC Cal  |          | successful          |
| 4           | NPC Dan  | Silencer  | NPC Bob  |          | successful          |
| 4           | NPC Fae  | Medic     | NPC Jeff |          | successful          |
| 4           | NPC Han  | Demagog   | Spy      |          | voting in progress  |
| 4           | NPC Jeff | Spy       |          |          | successful          |
| 4           | NPC Ken  | Inspector | NPC Ed   |          | successful          |
| 4           | NPC Lee  | Psychic   |          |          | successful          |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Han  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Ann  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob  | Jailer      | False      | True      | True       | 2         | True   | 0              | 0                  |
| 4           | NPC Jeff | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Mark | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Lee  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed   | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Gia  | Trader      | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ken  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Dan  | Silencer    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Fae  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Igi  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark     |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee      |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob     |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han       |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed       |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Ken      |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Bob      |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 4           | NPC Ann  | Priest      | vote      | Demagog has initiated a vote on eliminating Spy               |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark     |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee      |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob     |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han       |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed       |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Ken      |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Bob      |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 4           | NPC Bob  | Jailer      | silenced  | You have been silenced                                        |
| 4           | NPC Bob  | Jailer      | vote      | Demagog has initiated a vote on eliminating Spy               |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark     |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee      |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob     |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han       |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed       |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Ken      |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Bob      |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 4           | NPC Cal  | Assassin    | vote      | Demagog has initiated a vote on eliminating Spy               |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark     |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee      |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob     |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han       |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed       |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Ken      |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Bob      |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 4           | NPC Dan  | Silencer    | vote      | Demagog has initiated a vote on eliminating Spy               |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark     |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee      |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob     |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han       |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed       |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Ken      |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Bob      |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 4           | NPC Ed   | Reporter    | vote      | Demagog has initiated a vote on eliminating Spy               |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark     |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee      |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob     |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han       |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed       |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Ken      |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Bob      |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 4           | NPC Fae  | Medic       | vote      | Demagog has initiated a vote on eliminating Spy               |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark     |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee      |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob     |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han       |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed       |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Ken      |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Bob      |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 4           | NPC Gia  | Trader      | vote      | Demagog has initiated a vote on eliminating Spy               |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark     |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee      |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob     |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han       |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed       |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Ken      |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Bob      |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 4           | NPC Han  | Demagog     | vote      | Demagog has initiated a vote on eliminating Spy               |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark     |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee      |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob     |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han       |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed       |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Ken      |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Bob      |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 4           | NPC Igi  | Executioner | vote      | Demagog has initiated a vote on eliminating Spy               |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark     |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee      |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob     |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han       |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed       |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Ken      |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Bob      |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 4           | NPC Jeff | Spy         | reveal    | NPC Cal is targeting NPC Mark                                 |
| 4           | NPC Jeff | Spy         | reveal    | NPC Han is targeting NPC Lee                                  |
| 4           | NPC Jeff | Spy         | reveal    | NPC Bob is targeting NPC Igi                                  |
| 4           | NPC Jeff | Spy         | reveal    | NPC Mark is targeting NPC Bob                                 |
| 4           | NPC Jeff | Spy         | reveal    | NPC Ed is targeting NPC Han                                   |
| 4           | NPC Jeff | Spy         | reveal    | NPC Gia is targeting NPC Fae                                  |
| 4           | NPC Jeff | Spy         | reveal    | NPC Gia is targeting NPC Fae                                  |
| 4           | NPC Jeff | Spy         | reveal    | NPC Ken is targeting NPC Ed                                   |
| 4           | NPC Jeff | Spy         | reveal    | NPC Dan is targeting NPC Bob                                  |
| 4           | NPC Jeff | Spy         | reveal    | NPC Fae is targeting NPC Bob                                  |
| 4           | NPC Jeff | Spy         | vote      | Demagog has initiated a vote on eliminating Spy               |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark     |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee      |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob     |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han       |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed       |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Ken      |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Bob      |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 4           | NPC Ken  | Inspector   | reveal    | Reporter is Innocent                                          |
| 4           | NPC Ken  | Inspector   | vote      | Demagog has initiated a vote on eliminating Spy               |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark     |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee      |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob     |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han       |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed       |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Ken      |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Bob      |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 4           | NPC Lee  | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 4           | NPC Lee  | Psychic     | reveal    | Player: NPC Ed is not possessed                               |
| 4           | NPC Lee  | Psychic     | reveal    | Player: NPC Ann is not possessed                              |
| 4           | NPC Lee  | Psychic     | reveal    | Player: NPC Jeff is not possessed                             |
| 4           | NPC Lee  | Psychic     | reveal    | Player: NPC Igi is not possessed                              |
| 4           | NPC Lee  | Psychic     | reveal    | Player: NPC Cal is not possessed                              |
| 4           | NPC Lee  | Psychic     | vote      | Demagog has initiated a vote on eliminating Spy               |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark     |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Lee      |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Igi      |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob     |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han       |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae      |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed       |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Ken      |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Bob      |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 4           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 4           | NPC Mark | Thief       | vote      | Demagog has initiated a vote on eliminating Spy               |

#### Actions Round 5
| round_index | Player   | action   | Target 1 | Target 2 | status                         |
| :-----------| :--------| :--------| :--------| :--------| :----------------------------- |
| 5           | NPC Cal  | Assassin | Jailer   |          | successful                     |
| 5           | NPC Dan  | Silencer | NPC Jeff |          | successful                     |
| 5           | NPC Ed   | Reporter | NPC Cal  |          | successful                     |
| 5           | NPC Fae  | Medic    | NPC Mark |          | successful                     |
| 5           | NPC Gia  | Trader   | NPC Jeff | NPC Cal  | failed because not vulnerable  |
| 5           | NPC Jeff | Spy      |          |          | successful                     |
| 5           | NPC Lee  | Psychic  |          |          | successful                     |
| 5           | NPC Mark | Thief    | NPC Jeff |          | successful                     |

#### States Round 5
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Cal  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Han  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Ann  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob  | Jailer      | False      | True      | True       | 1         | True   | 0              | 0                  |
| 5           | NPC Jeff | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Mark | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Lee  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Ed   | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Gia  | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 5           | NPC Ken  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Dan  | Silencer    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 5           | NPC Fae  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Igi  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Assassin         |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark      |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff      |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal       |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob      |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han        |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Jeff      |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed     |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ann  | Priest      | broadcast | I (NPC Mark) am the Thief and I have made NPC Jeff vulnerable  |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Assassin         |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark      |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff      |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal       |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob      |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han        |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Jeff      |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed     |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Bob  | Jailer      | broadcast | I (NPC Mark) am the Thief and I have made NPC Jeff vulnerable  |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Assassin         |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark      |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff      |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal       |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob      |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han        |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Jeff      |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed     |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Cal  | Assassin    | broadcast | I (NPC Mark) am the Thief and I have made NPC Jeff vulnerable  |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Assassin         |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark      |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff      |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal       |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob      |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han        |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Jeff      |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed     |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Dan  | Silencer    | broadcast | I (NPC Mark) am the Thief and I have made NPC Jeff vulnerable  |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Assassin         |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark      |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff      |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal       |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob      |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han        |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Jeff      |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed     |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Thief and I have made NPC Jeff vulnerable  |
| 5           | NPC Ed   | Reporter    | reveal    | NPC Cal is Assassin                                            |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Assassin         |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark      |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff      |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal       |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob      |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han        |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Jeff      |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed     |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Fae  | Medic       | broadcast | I (NPC Mark) am the Thief and I have made NPC Jeff vulnerable  |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Assassin         |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark      |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff      |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal       |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob      |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han        |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Jeff      |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed     |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Gia  | Trader      | broadcast | I (NPC Mark) am the Thief and I have made NPC Jeff vulnerable  |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Assassin         |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark      |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff      |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal       |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob      |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han        |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Jeff      |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed     |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Han  | Demagog     | broadcast | I (NPC Mark) am the Thief and I have made NPC Jeff vulnerable  |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Assassin         |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark      |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff      |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal       |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob      |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han        |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Jeff      |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed     |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Igi  | Executioner | broadcast | I (NPC Mark) am the Thief and I have made NPC Jeff vulnerable  |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Assassin         |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark      |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff      |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal       |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob      |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han        |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Jeff      |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed     |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Jeff | Spy         | broadcast | I (NPC Mark) am the Thief and I have made NPC Jeff vulnerable  |
| 5           | NPC Jeff | Spy         | silenced  | You have been silenced                                         |
| 5           | NPC Jeff | Spy         | reveal    | NPC Cal is targeting NPC Mark                                  |
| 5           | NPC Jeff | Spy         | reveal    | NPC Han is targeting NPC Jeff                                  |
| 5           | NPC Jeff | Spy         | reveal    | NPC Bob is targeting NPC Cal                                   |
| 5           | NPC Jeff | Spy         | reveal    | NPC Mark is targeting NPC Jeff                                 |
| 5           | NPC Jeff | Spy         | reveal    | NPC Ed is targeting NPC Cal                                    |
| 5           | NPC Jeff | Spy         | reveal    | NPC Gia is targeting NPC Fae                                   |
| 5           | NPC Jeff | Spy         | reveal    | NPC Gia is targeting NPC Fae                                   |
| 5           | NPC Jeff | Spy         | reveal    | NPC Ken is targeting NPC Ed                                    |
| 5           | NPC Jeff | Spy         | reveal    | NPC Dan is targeting NPC Jeff                                  |
| 5           | NPC Jeff | Spy         | reveal    | NPC Fae is targeting NPC Jeff                                  |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Assassin         |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark      |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff      |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal       |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob      |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han        |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Jeff      |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed     |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ken  | Inspector   | broadcast | I (NPC Mark) am the Thief and I have made NPC Jeff vulnerable  |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Assassin         |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark      |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff      |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal       |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob      |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han        |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Jeff      |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed     |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Lee  | Psychic     | broadcast | I (NPC Mark) am the Thief and I have made NPC Jeff vulnerable  |
| 5           | NPC Lee  | Psychic     | reveal    | Player: NPC Gia is not possessed                               |
| 5           | NPC Lee  | Psychic     | reveal    | Player: NPC Ed is not possessed                                |
| 5           | NPC Lee  | Psychic     | reveal    | Player: NPC Jeff is not possessed                              |
| 5           | NPC Lee  | Psychic     | reveal    | Player: NPC Fae is not possessed                               |
| 5           | NPC Lee  | Psychic     | reveal    | Player: NPC Cal is not possessed                               |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Ed) am the Reporter and NPC Cal is the Assassin         |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Mark      |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff      |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal       |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Bob      |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Han        |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Fae       |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Ed        |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Bob       |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Jeff      |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed     |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed   |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed     |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Reporter is not possessed   |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Mark | Thief       | broadcast | I (NPC Mark) am the Thief and I have made NPC Jeff vulnerable  |

#### Actions Round 6
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 6           | NPC Bob  | Jailer    | NPC Cal  |          | successful          |
| 6           | NPC Dan  | Silencer  | NPC Dan  |          | successful          |
| 6           | NPC Fae  | Medic     | NPC Lee  |          | successful          |
| 6           | NPC Han  | Demagog   | Spy      |          | voting in progress  |
| 6           | NPC Jeff | Spy       |          |          | successful          |
| 6           | NPC Ken  | Inspector | NPC Fae  |          | successful          |
| 6           | NPC Lee  | Psychic   |          |          | successful          |
| 6           | NPC Mark | Thief     | NPC Lee  |          | successful          |

#### States Round 6
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Cal  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Han  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Ann  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob  | Jailer      | False      | True      | True       | 2         | True   | 0              | 0                  |
| 6           | NPC Jeff | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Mark | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Lee  | Psychic     | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Ed   | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Gia  | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 6           | NPC Ken  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 6           | NPC Dan  | Silencer    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Fae  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Igi  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 6           | NPC Ann  | Priest      | broadcast | I (NPC Ken) inspected NPC Fae and they are not possessed      |
| 6           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 6           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 6           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 6           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed    |
| 6           | NPC Ann  | Priest      | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 6           | NPC Ann  | Priest      | vote      | Demagog has initiated a vote on eliminating Spy               |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Ken) inspected NPC Fae and they are not possessed      |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed    |
| 6           | NPC Bob  | Jailer      | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 6           | NPC Bob  | Jailer      | vote      | Demagog has initiated a vote on eliminating Spy               |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Ken) inspected NPC Fae and they are not possessed      |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed    |
| 6           | NPC Cal  | Assassin    | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 6           | NPC Cal  | Assassin    | vote      | Demagog has initiated a vote on eliminating Spy               |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Ken) inspected NPC Fae and they are not possessed      |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed    |
| 6           | NPC Dan  | Silencer    | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 6           | NPC Dan  | Silencer    | silenced  | You have been silenced                                        |
| 6           | NPC Dan  | Silencer    | vote      | Demagog has initiated a vote on eliminating Spy               |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Ken) inspected NPC Fae and they are not possessed      |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed    |
| 6           | NPC Ed   | Reporter    | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 6           | NPC Ed   | Reporter    | vote      | Demagog has initiated a vote on eliminating Spy               |
| 6           | NPC Fae  | Medic       | broadcast | I (NPC Ken) inspected NPC Fae and they are not possessed      |
| 6           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 6           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 6           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 6           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed    |
| 6           | NPC Fae  | Medic       | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 6           | NPC Fae  | Medic       | vote      | Demagog has initiated a vote on eliminating Spy               |
| 6           | NPC Gia  | Trader      | broadcast | I (NPC Ken) inspected NPC Fae and they are not possessed      |
| 6           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 6           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 6           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 6           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed    |
| 6           | NPC Gia  | Trader      | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 6           | NPC Gia  | Trader      | vote      | Demagog has initiated a vote on eliminating Spy               |
| 6           | NPC Han  | Demagog     | broadcast | I (NPC Ken) inspected NPC Fae and they are not possessed      |
| 6           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 6           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 6           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 6           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed    |
| 6           | NPC Han  | Demagog     | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 6           | NPC Han  | Demagog     | vote      | Demagog has initiated a vote on eliminating Spy               |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Ken) inspected NPC Fae and they are not possessed      |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed    |
| 6           | NPC Igi  | Executioner | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 6           | NPC Igi  | Executioner | vote      | Demagog has initiated a vote on eliminating Spy               |
| 6           | NPC Jeff | Spy         | broadcast | I (NPC Ken) inspected NPC Fae and they are not possessed      |
| 6           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 6           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 6           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 6           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed    |
| 6           | NPC Jeff | Spy         | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 6           | NPC Jeff | Spy         | reveal    | NPC Cal is targeting NPC Bob                                  |
| 6           | NPC Jeff | Spy         | reveal    | NPC Han is targeting NPC Jeff                                 |
| 6           | NPC Jeff | Spy         | reveal    | NPC Bob is targeting NPC Cal                                  |
| 6           | NPC Jeff | Spy         | reveal    | NPC Mark is targeting NPC Lee                                 |
| 6           | NPC Jeff | Spy         | reveal    | NPC Ed is targeting NPC Cal                                   |
| 6           | NPC Jeff | Spy         | reveal    | NPC Gia is targeting NPC Jeff                                 |
| 6           | NPC Jeff | Spy         | reveal    | NPC Gia is targeting NPC Jeff                                 |
| 6           | NPC Jeff | Spy         | reveal    | NPC Ken is targeting NPC Fae                                  |
| 6           | NPC Jeff | Spy         | reveal    | NPC Dan is targeting NPC Dan                                  |
| 6           | NPC Jeff | Spy         | reveal    | NPC Fae is targeting NPC Mark                                 |
| 6           | NPC Jeff | Spy         | vote      | Demagog has initiated a vote on eliminating Spy               |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Ken) inspected NPC Fae and they are not possessed      |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed    |
| 6           | NPC Ken  | Inspector   | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 6           | NPC Ken  | Inspector   | reveal    | Medic is Innocent                                             |
| 6           | NPC Ken  | Inspector   | vote      | Demagog has initiated a vote on eliminating Spy               |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Ken) inspected NPC Fae and they are not possessed      |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed    |
| 6           | NPC Lee  | Psychic     | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 6           | NPC Lee  | Psychic     | reveal    | Player: NPC Ken is not possessed                              |
| 6           | NPC Lee  | Psychic     | reveal    | Player: NPC Cal is not possessed                              |
| 6           | NPC Lee  | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 6           | NPC Lee  | Psychic     | reveal    | Player: NPC Mark is not possessed                             |
| 6           | NPC Lee  | Psychic     | reveal    | Player: NPC Han is not possessed                              |
| 6           | NPC Lee  | Psychic     | reveal    | Player: NPC Igi is not possessed                              |
| 6           | NPC Lee  | Psychic     | vote      | Demagog has initiated a vote on eliminating Spy               |
| 6           | NPC Mark | Thief       | broadcast | I (NPC Ken) inspected NPC Fae and they are not possessed      |
| 6           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 6           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 6           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Thief is not possessed     |
| 6           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Medic is not possessed     |
| 6           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 6           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Trader is not possessed    |
| 6           | NPC Mark | Thief       | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 6           | NPC Mark | Thief       | vote      | Demagog has initiated a vote on eliminating Spy               |

#### Actions Round 7
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 7           | NPC Dan  | Silencer | NPC Bob  |          | successful  |
| 7           | NPC Ed   | Reporter | NPC Igi  |          | successful  |
| 7           | NPC Fae  | Medic    | NPC Ed   |          | successful  |
| 7           | NPC Jeff | Spy      |          |          | successful  |
| 7           | NPC Lee  | Psychic  |          |          | successful  |

#### States Round 7
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Cal  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Han  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Ann  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Bob  | Jailer      | False      | True      | True       | 1         | True   | 0              | 0                  |
| 7           | NPC Jeff | Spy         | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Mark | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Lee  | Psychic     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 7           | NPC Ed   | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Gia  | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Ken  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Dan  | Silencer    | False      | False     | True       | 1         | True   | 0              | 0                  |
| 7           | NPC Fae  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Igi  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Bob      |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff     |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal      |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Lee     |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Fae      |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Dan      |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Lee      |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Ann  | Priest      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Bob      |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff     |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal      |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Lee     |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Fae      |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Dan      |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Lee      |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Bob  | Jailer      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 7           | NPC Bob  | Jailer      | silenced  | You have been silenced                                        |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Bob      |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff     |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal      |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Lee     |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Fae      |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Dan      |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Lee      |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Cal  | Assassin    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Bob      |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff     |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal      |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Lee     |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Fae      |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Dan      |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Lee      |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Dan  | Silencer    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Bob      |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff     |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal      |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Lee     |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Fae      |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Dan      |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Lee      |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Ed   | Reporter    | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 7           | NPC Ed   | Reporter    | reveal    | NPC Igi is Executioner                                        |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Bob      |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff     |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal      |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Lee     |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Fae      |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Dan      |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Lee      |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Fae  | Medic       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Bob      |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff     |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal      |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Lee     |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Fae      |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Dan      |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Lee      |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Gia  | Trader      | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Bob      |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff     |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal      |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Lee     |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Fae      |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Dan      |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Lee      |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Han  | Demagog     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Bob      |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff     |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal      |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Lee     |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Fae      |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Dan      |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Lee      |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Igi  | Executioner | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Bob      |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff     |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal      |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Lee     |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Fae      |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Dan      |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Lee      |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Jeff | Spy         | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 7           | NPC Jeff | Spy         | reveal    | NPC Cal is targeting NPC Bob                                  |
| 7           | NPC Jeff | Spy         | reveal    | NPC Han is targeting NPC Jeff                                 |
| 7           | NPC Jeff | Spy         | reveal    | NPC Bob is targeting NPC Cal                                  |
| 7           | NPC Jeff | Spy         | reveal    | NPC Mark is targeting NPC Lee                                 |
| 7           | NPC Jeff | Spy         | reveal    | NPC Ed is targeting NPC Igi                                   |
| 7           | NPC Jeff | Spy         | reveal    | NPC Gia is targeting NPC Jeff                                 |
| 7           | NPC Jeff | Spy         | reveal    | NPC Gia is targeting NPC Jeff                                 |
| 7           | NPC Jeff | Spy         | reveal    | NPC Ken is targeting NPC Fae                                  |
| 7           | NPC Jeff | Spy         | reveal    | NPC Dan is targeting NPC Bob                                  |
| 7           | NPC Jeff | Spy         | reveal    | NPC Fae is targeting NPC Lee                                  |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Bob      |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff     |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal      |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Lee     |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Fae      |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Dan      |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Lee      |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Ken  | Inspector   | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Bob      |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff     |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal      |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Lee     |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Fae      |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Dan      |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Lee      |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Lee  | Psychic     | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |
| 7           | NPC Lee  | Psychic     | reveal    | Player: NPC Ann is not possessed                              |
| 7           | NPC Lee  | Psychic     | reveal    | Player: NPC Ken is not possessed                              |
| 7           | NPC Lee  | Psychic     | reveal    | Player: NPC Mark is not possessed                             |
| 7           | NPC Lee  | Psychic     | reveal    | Player: NPC Gia is not possessed                              |
| 7           | NPC Lee  | Psychic     | reveal    | Player: NPC Cal is not possessed                              |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Cal is targeting NPC Bob      |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Han is targeting NPC Jeff     |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Bob is targeting NPC Cal      |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Mark is targeting NPC Lee     |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Ed is targeting NPC Cal       |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Gia is targeting NPC Jeff     |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Ken is targeting NPC Fae      |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Dan is targeting NPC Dan      |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Jeff) am the Spy and NPC Fae is targeting NPC Lee      |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Assassin is not possessed  |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Demagog is not possessed   |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Priest is not possessed    |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Silencer is not possessed  |
| 7           | NPC Mark | Thief       | broadcast | I (NPC Lee) am the Psychic and the Spy is not possessed       |