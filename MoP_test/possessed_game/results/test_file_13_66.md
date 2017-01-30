#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 66   | 13      | 9       |

#### Roles
| Role         |
| :----------- |
| Priest       |
| Inspector    |
| Reporter     |
| Spy          |
| Trader       |
| Thief        |
| Medic        |
| Jailer       |
| Prophet      |
| Assassin     |
| Psychic      |
| Demagog      |
| Executioner  |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Mark | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Ann  | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Bob  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Bob  | Spy         | possessed   | You are Possessed         |
| 0           | NPC Cal  | Priest      | role change | Your Role is Priest       |
| 0           | NPC Cal  | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Dan  | Psychic     | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Ed   | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Fae  | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Gia  | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Han  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Igi  | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Trader      | role change | Your Role is Trader       |
| 0           | NPC Jeff | Trader      | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Ken  | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Lee  | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Mark | Thief       | role change | Your Role is Thief        |
| 0           | NPC Mark | Thief       | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 1           | NPC Ann  | Reporter  | NPC Fae  |          | successful          |
| 1           | NPC Bob  | Spy       |          |          | successful          |
| 1           | NPC Dan  | Psychic   |          |          | successful          |
| 1           | NPC Fae  | Demagog   | Assassin |          | voting in progress  |
| 1           | NPC Gia  | Prophet   | NPC Ken  |          | successful          |
| 1           | NPC Han  | Inspector | NPC Igi  |          | successful          |
| 1           | NPC Jeff | Trader    | NPC Dan  | NPC Ann  | successful          |
| 1           | NPC Ken  | Assassin  | Demagog  |          | successful          |
| 1           | NPC Lee  | Medic     | NPC Han  |          | successful          |
| 1           | NPC Mark | Thief     | NPC Lee  |          | successful          |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Han  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ann  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob  | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Jeff | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Mark | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Lee  | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ken  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan  | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Fae  | Demagog     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Igi  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Demagog        |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed    |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Dan) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed      |
| 1           | NPC Ann  | Psychic     | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 1           | NPC Ann  | Psychic     | reveal    | NPC Fae is Demagog                                            |
| 1           | NPC Ann  | Psychic     | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 1           | NPC Bob  | Spy         | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Demagog        |
| 1           | NPC Bob  | Spy         | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed    |
| 1           | NPC Bob  | Spy         | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 1           | NPC Bob  | Spy         | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Bob  | Spy         | broadcast | I (NPC Dan) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Bob  | Spy         | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Bob  | Spy         | broadcast | I (NPC Dan) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Bob  | Spy         | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed      |
| 1           | NPC Bob  | Spy         | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 1           | NPC Bob  | Spy         | reveal    | NPC Han is targeting NPC Igi                                  |
| 1           | NPC Bob  | Spy         | reveal    | NPC Ann is targeting NPC Fae                                  |
| 1           | NPC Bob  | Spy         | reveal    | NPC Mark is targeting NPC Lee                                 |
| 1           | NPC Bob  | Spy         | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 1           | NPC Cal  | Priest      | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Demagog        |
| 1           | NPC Cal  | Priest      | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed    |
| 1           | NPC Cal  | Priest      | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 1           | NPC Cal  | Priest      | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Cal  | Priest      | broadcast | I (NPC Dan) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Cal  | Priest      | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Cal  | Priest      | broadcast | I (NPC Dan) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Cal  | Priest      | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed      |
| 1           | NPC Cal  | Priest      | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 1           | NPC Cal  | Priest      | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 1           | NPC Dan  | Reporter    | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Demagog        |
| 1           | NPC Dan  | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed    |
| 1           | NPC Dan  | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 1           | NPC Dan  | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Dan  | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Dan  | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Dan  | Reporter    | broadcast | I (NPC Dan) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Dan  | Reporter    | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed      |
| 1           | NPC Dan  | Reporter    | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 1           | NPC Dan  | Reporter    | reveal    | Player: NPC Ken is not possessed                              |
| 1           | NPC Dan  | Reporter    | reveal    | Player: NPC Lee is not possessed                              |
| 1           | NPC Dan  | Reporter    | reveal    | Player: NPC Cal is not possessed                              |
| 1           | NPC Dan  | Reporter    | reveal    | Player: NPC Mark is not possessed                             |
| 1           | NPC Dan  | Reporter    | reveal    | Player: NPC Jeff is not possessed                             |
| 1           | NPC Dan  | Reporter    | reveal    | Player: NPC Ann is not possessed                              |
| 1           | NPC Dan  | Reporter    | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Demagog        |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed    |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed      |
| 1           | NPC Ed   | Jailer      | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 1           | NPC Ed   | Jailer      | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 1           | NPC Fae  | Demagog     | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Demagog        |
| 1           | NPC Fae  | Demagog     | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed    |
| 1           | NPC Fae  | Demagog     | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 1           | NPC Fae  | Demagog     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Fae  | Demagog     | broadcast | I (NPC Dan) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Fae  | Demagog     | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Fae  | Demagog     | broadcast | I (NPC Dan) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Fae  | Demagog     | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed      |
| 1           | NPC Fae  | Demagog     | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 1           | NPC Fae  | Demagog     | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 1           | NPC Gia  | Prophet     | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Demagog        |
| 1           | NPC Gia  | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed    |
| 1           | NPC Gia  | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 1           | NPC Gia  | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Gia  | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Gia  | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Gia  | Prophet     | broadcast | I (NPC Dan) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Gia  | Prophet     | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed      |
| 1           | NPC Gia  | Prophet     | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 1           | NPC Gia  | Prophet     | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 1           | NPC Han  | Inspector   | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Demagog        |
| 1           | NPC Han  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed    |
| 1           | NPC Han  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 1           | NPC Han  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Han  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Han  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Han  | Inspector   | broadcast | I (NPC Dan) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Han  | Inspector   | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed      |
| 1           | NPC Han  | Inspector   | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 1           | NPC Han  | Inspector   | reveal    | Executioner is Innocent                                       |
| 1           | NPC Han  | Inspector   | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Demagog        |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed    |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Dan) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Dan) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed      |
| 1           | NPC Igi  | Executioner | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 1           | NPC Igi  | Executioner | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 1           | NPC Jeff | Trader      | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Demagog        |
| 1           | NPC Jeff | Trader      | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed    |
| 1           | NPC Jeff | Trader      | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 1           | NPC Jeff | Trader      | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Jeff | Trader      | broadcast | I (NPC Dan) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Jeff | Trader      | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Jeff | Trader      | broadcast | I (NPC Dan) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Jeff | Trader      | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed      |
| 1           | NPC Jeff | Trader      | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 1           | NPC Jeff | Trader      | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Demagog        |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed    |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Dan) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed      |
| 1           | NPC Ken  | Assassin    | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 1           | NPC Ken  | Assassin    | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 1           | NPC Lee  | Medic       | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Demagog        |
| 1           | NPC Lee  | Medic       | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed    |
| 1           | NPC Lee  | Medic       | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 1           | NPC Lee  | Medic       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Lee  | Medic       | broadcast | I (NPC Dan) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Lee  | Medic       | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Lee  | Medic       | broadcast | I (NPC Dan) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Lee  | Medic       | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed      |
| 1           | NPC Lee  | Medic       | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 1           | NPC Lee  | Medic       | vote      | Demagog has initiated a vote on eliminating Assassin          |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Demagog        |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Dan) am the Psychic and the Priest is not possessed    |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Dan) am the Psychic and the Trader is not possessed    |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Dan) am the Psychic and the Reporter is not possessed  |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Dan) am the Psychic and the Demagog is not possessed   |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Dan) am the Psychic and the Assassin is not possessed  |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Dan) am the Psychic and the Prophet is not possessed   |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Han) inspected NPC Igi and they are not possessed      |
| 1           | NPC Mark | Thief       | broadcast | I (NPC Mark) am the Thief and I have made NPC Lee vulnerable  |
| 1           | NPC Mark | Thief       | vote      | Demagog has initiated a vote on eliminating Assassin          |

#### Actions Round 2
| round_index | Player  | action    | Target 1 | Target 2 | status      |
| :-----------| :-------| :---------| :--------| :--------| :---------- |
| 2           | NPC Ann | Psychic   |          |          | successful  |
| 2           | NPC Bob | Spy       |          |          | successful  |
| 2           | NPC Dan | Reporter  | NPC Ann  |          | successful  |
| 2           | NPC Gia | Prophet   | NPC Ann  |          | successful  |
| 2           | NPC Han | Inspector | NPC Bob  |          | successful  |
| 2           | NPC Lee | Medic     | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Ann  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob  | Spy         | False      | True      | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Jeff | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Mark | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Lee  | Medic       | False      | False     | True       | 0         | True   | 0              | 0                  |
| 2           | NPC Ed   | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Gia  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ken  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan  | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 2           | NPC Fae  | Demagog     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Igi  | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Bob) am the Spy and NPC Han is targeting NPC Igi       |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Bob) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Bob) am the Spy and NPC Lee is targeting NPC Han       |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ken       |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Bob) am the Spy and NPC Ken is targeting NPC Fae       |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ken       |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Psychic        |
| 2           | NPC Ann  | Psychic     | broadcast | I (NPC Han) inspected NPC Bob and they are possessed          |
| 2           | NPC Ann  | Psychic     | reveal    | Player: NPC Han is not possessed                              |
| 2           | NPC Ann  | Psychic     | reveal    | Player: NPC Jeff is not possessed                             |
| 2           | NPC Ann  | Psychic     | reveal    | Player: NPC Gia is not possessed                              |
| 2           | NPC Ann  | Psychic     | reveal    | Player: NPC Mark is not possessed                             |
| 2           | NPC Ann  | Psychic     | reveal    | Player: NPC Fae is not possessed                              |
| 2           | NPC Ann  | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed    |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Han is targeting NPC Igi       |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Lee is targeting NPC Han       |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ken       |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Ken is targeting NPC Fae       |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ken       |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Psychic        |
| 2           | NPC Bob  | Spy         | broadcast | I (NPC Han) inspected NPC Bob and they are possessed          |
| 2           | NPC Bob  | Spy         | reveal    | NPC Han is targeting NPC Bob                                  |
| 2           | NPC Bob  | Spy         | reveal    | NPC Jeff is targeting NPC Dan                                 |
| 2           | NPC Bob  | Spy         | reveal    | NPC Jeff is targeting NPC Dan                                 |
| 2           | NPC Bob  | Spy         | reveal    | NPC Mark is targeting NPC Lee                                 |
| 2           | NPC Bob  | Spy         | reveal    | NPC Lee is targeting NPC Han                                  |
| 2           | NPC Bob  | Spy         | reveal    | NPC Gia is targeting NPC Ken                                  |
| 2           | NPC Bob  | Spy         | reveal    | NPC Ken is targeting NPC Fae                                  |
| 2           | NPC Bob  | Spy         | reveal    | NPC Dan is targeting NPC Ann                                  |
| 2           | NPC Bob  | Spy         | reveal    | NPC Fae is targeting NPC Ken                                  |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed    |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Bob) am the Spy and NPC Han is targeting NPC Igi       |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Bob) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Bob) am the Spy and NPC Lee is targeting NPC Han       |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ken       |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Bob) am the Spy and NPC Ken is targeting NPC Fae       |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ken       |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Psychic        |
| 2           | NPC Cal  | Priest      | broadcast | I (NPC Han) inspected NPC Bob and they are possessed          |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed    |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Han is targeting NPC Igi       |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Lee is targeting NPC Han       |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ken       |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Ken is targeting NPC Fae       |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ken       |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Psychic        |
| 2           | NPC Dan  | Reporter    | broadcast | I (NPC Han) inspected NPC Bob and they are possessed          |
| 2           | NPC Dan  | Reporter    | reveal    | NPC Ann is Psychic                                            |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Bob) am the Spy and NPC Han is targeting NPC Igi       |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Bob) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Bob) am the Spy and NPC Lee is targeting NPC Han       |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ken       |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Bob) am the Spy and NPC Ken is targeting NPC Fae       |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ken       |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Psychic        |
| 2           | NPC Ed   | Jailer      | broadcast | I (NPC Han) inspected NPC Bob and they are possessed          |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed    |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Han is targeting NPC Igi       |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Lee is targeting NPC Han       |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ken       |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Ken is targeting NPC Fae       |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ken       |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Psychic        |
| 2           | NPC Fae  | Demagog     | broadcast | I (NPC Han) inspected NPC Bob and they are possessed          |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed    |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Han is targeting NPC Igi       |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Lee is targeting NPC Han       |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ken       |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Ken is targeting NPC Fae       |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ken       |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Psychic        |
| 2           | NPC Gia  | Prophet     | broadcast | I (NPC Han) inspected NPC Bob and they are possessed          |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed    |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Bob) am the Spy and NPC Han is targeting NPC Igi       |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Bob) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Bob) am the Spy and NPC Lee is targeting NPC Han       |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ken       |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Bob) am the Spy and NPC Ken is targeting NPC Fae       |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ken       |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Psychic        |
| 2           | NPC Han  | Inspector   | broadcast | I (NPC Han) inspected NPC Bob and they are possessed          |
| 2           | NPC Han  | Inspector   | reveal    | Spy is Possessed                                              |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed    |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Han is targeting NPC Igi       |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Lee is targeting NPC Han       |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ken       |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Ken is targeting NPC Fae       |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ken       |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Psychic        |
| 2           | NPC Igi  | Executioner | broadcast | I (NPC Han) inspected NPC Bob and they are possessed          |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed    |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Han is targeting NPC Igi       |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Lee is targeting NPC Han       |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ken       |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Ken is targeting NPC Fae       |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ken       |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Psychic        |
| 2           | NPC Jeff | Trader      | broadcast | I (NPC Han) inspected NPC Bob and they are possessed          |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Bob) am the Spy and NPC Han is targeting NPC Igi       |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Bob) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Bob) am the Spy and NPC Lee is targeting NPC Han       |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ken       |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Bob) am the Spy and NPC Ken is targeting NPC Fae       |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ken       |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Psychic        |
| 2           | NPC Ken  | Assassin    | broadcast | I (NPC Han) inspected NPC Bob and they are possessed          |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed    |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Han is targeting NPC Igi       |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Lee is targeting NPC Han       |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ken       |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Ken is targeting NPC Fae       |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ken       |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Psychic        |
| 2           | NPC Lee  | Medic       | broadcast | I (NPC Han) inspected NPC Bob and they are possessed          |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Ann) am the Psychic and the Trader is not possessed    |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Ann) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Ann) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed     |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed    |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed   |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Bob) am the Spy and NPC Han is targeting NPC Igi       |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Bob) am the Spy and NPC Jeff is targeting NPC Dan      |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Bob) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Bob) am the Spy and NPC Lee is targeting NPC Han       |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Bob) am the Spy and NPC Gia is targeting NPC Ken       |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Bob) am the Spy and NPC Ken is targeting NPC Fae       |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Bob) am the Spy and NPC Fae is targeting NPC Ken       |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Dan) am the Reporter and NPC Ann is the Psychic        |
| 2           | NPC Mark | Thief       | broadcast | I (NPC Han) inspected NPC Bob and they are possessed          |