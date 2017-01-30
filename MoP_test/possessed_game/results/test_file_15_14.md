#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 14   | 15      | 7       |

#### Roles
| Role         |
| :----------- |
| Assassin     |
| Judge        |
| Silencer     |
| Medic        |
| Priest       |
| Spy          |
| Prophet      |
| Jailer       |
| Reporter     |
| Thief        |
| Executioner  |
| Trader       |
| Inspector    |
| Demagog      |
| Psychic      |

#### States Round 0
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Igi  | Assassin    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Prophet     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Mark | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Norm | Thief       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ozie | Trader      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Cal  | Inspector   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Demagog     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Psychic     | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role        | message     | details                   |
| :-----------| :--------| :-----------| :-----------| :------------------------ |
| 0           | NPC Ann  | Psychic     | role change | Your Role is Psychic      |
| 0           | NPC Ann  | Psychic     | possessed   | You are Possessed         |
| 0           | NPC Bob  | Priest      | role change | Your Role is Priest       |
| 0           | NPC Bob  | Priest      | possessed   | You are Not Possessed     |
| 0           | NPC Cal  | Inspector   | role change | Your Role is Inspector    |
| 0           | NPC Cal  | Inspector   | possessed   | You are Not Possessed     |
| 0           | NPC Dan  | Judge       | role change | Your Role is Judge        |
| 0           | NPC Dan  | Judge       | possessed   | You are Not Possessed     |
| 0           | NPC Ed   | Demagog     | role change | Your Role is Demagog      |
| 0           | NPC Ed   | Demagog     | possessed   | You are Not Possessed     |
| 0           | NPC Fae  | Silencer    | role change | Your Role is Silencer     |
| 0           | NPC Fae  | Silencer    | possessed   | You are Not Possessed     |
| 0           | NPC Gia  | Prophet     | role change | Your Role is Prophet      |
| 0           | NPC Gia  | Prophet     | possessed   | You are Not Possessed     |
| 0           | NPC Han  | Medic       | role change | Your Role is Medic        |
| 0           | NPC Han  | Medic       | possessed   | You are Not Possessed     |
| 0           | NPC Igi  | Assassin    | role change | Your Role is Assassin     |
| 0           | NPC Igi  | Assassin    | possessed   | You are Not Possessed     |
| 0           | NPC Jeff | Executioner | role change | Your Role is Executioner  |
| 0           | NPC Jeff | Executioner | possessed   | You are Not Possessed     |
| 0           | NPC Ken  | Jailer      | role change | Your Role is Jailer       |
| 0           | NPC Ken  | Jailer      | possessed   | You are Not Possessed     |
| 0           | NPC Lee  | Spy         | role change | Your Role is Spy          |
| 0           | NPC Lee  | Spy         | possessed   | You are Not Possessed     |
| 0           | NPC Mark | Reporter    | role change | Your Role is Reporter     |
| 0           | NPC Mark | Reporter    | possessed   | You are Not Possessed     |
| 0           | NPC Norm | Thief       | role change | Your Role is Thief        |
| 0           | NPC Norm | Thief       | possessed   | You are Not Possessed     |
| 0           | NPC Ozie | Trader      | role change | Your Role is Trader       |
| 0           | NPC Ozie | Trader      | possessed   | You are Not Possessed     |

#### Actions Round 1
| round_index | Player   | action    | Target 1    | Target 2 | status              |
| :-----------| :--------| :---------| :-----------| :--------| :------------------ |
| 1           | NPC Ann  | Psychic   |             |          | successful          |
| 1           | NPC Cal  | Inspector | NPC Dan     |          | successful          |
| 1           | NPC Dan  | Judge     | Reporter    |          | successful          |
| 1           | NPC Ed   | Demagog   | Spy         |          | voting in progress  |
| 1           | NPC Fae  | Silencer  | NPC Mark    |          | successful          |
| 1           | NPC Gia  | Prophet   | NPC Ann     |          | successful          |
| 1           | NPC Han  | Medic     | NPC Dan     |          | successful          |
| 1           | NPC Igi  | Assassin  | Executioner |          | successful          |
| 1           | NPC Lee  | Spy       |             |          | successful          |
| 1           | NPC Mark | Reporter  | NPC Lee     |          | successful          |
| 1           | NPC Norm | Thief     | NPC Ed      |          | successful          |
| 1           | NPC Ozie | Trader    | NPC Ann     | NPC Gia  | successful          |

#### States Round 1
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Igi  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Dan  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Han  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Bob  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Lee  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Gia  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ken  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Mark | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Norm | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Jeff | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ozie | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Cal  | Inspector   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Ed   | Demagog     | False      | False     | True       | 2         | True   | 0              | 0                  |
| 1           | NPC Ann  | Prophet     | False      | True      | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role        | message   | details                                                          |
| :-----------| :--------| :-----------| :---------| :--------------------------------------------------------------- |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Ann  | Prophet     | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Ann  | Prophet     | reveal    | Player: NPC Ed is not possessed                                  |
| 1           | NPC Ann  | Prophet     | reveal    | Player: NPC Han is not possessed                                 |
| 1           | NPC Ann  | Prophet     | reveal    | Player: NPC Mark is not possessed                                |
| 1           | NPC Ann  | Prophet     | reveal    | Player: NPC Cal is not possessed                                 |
| 1           | NPC Ann  | Prophet     | reveal    | Player: NPC Igi is not possessed                                 |
| 1           | NPC Ann  | Prophet     | reveal    | Player: NPC Fae is not possessed                                 |
| 1           | NPC Ann  | Prophet     | reveal    | Player: NPC Jeff is not possessed                                |
| 1           | NPC Ann  | Prophet     | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Bob  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Bob  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Bob  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Bob  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Bob  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Bob  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Bob  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Bob  | Priest      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Bob  | Priest      | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Bob  | Priest      | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Bob  | Priest      | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Bob  | Priest      | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Cal  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Cal  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Cal  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Cal  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Cal  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Cal  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Cal  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Cal  | Inspector   | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Cal  | Inspector   | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Cal  | Inspector   | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Cal  | Inspector   | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Cal  | Inspector   | reveal    | Judge is Innocent                                                |
| 1           | NPC Cal  | Inspector   | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Dan  | Judge       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Dan  | Judge       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Dan  | Judge       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Dan  | Judge       | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Dan  | Judge       | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Dan  | Judge       | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Dan  | Judge       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Dan  | Judge       | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Dan  | Judge       | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Dan  | Judge       | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Dan  | Judge       | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Dan  | Judge       | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Ed   | Demagog     | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Ed   | Demagog     | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Fae  | Silencer    | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Fae  | Silencer    | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Gia  | Psychic     | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Gia  | Psychic     | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Han  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Han  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Han  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Han  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Han  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Han  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Han  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Han  | Medic       | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Han  | Medic       | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Han  | Medic       | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Han  | Medic       | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Han  | Medic       | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Igi  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Igi  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Igi  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Igi  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Igi  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Igi  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Igi  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Igi  | Assassin    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Igi  | Assassin    | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Igi  | Assassin    | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Igi  | Assassin    | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Igi  | Assassin    | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Jeff | Executioner | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Jeff | Executioner | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Jeff | Executioner | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Jeff | Executioner | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Jeff | Executioner | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Jeff | Executioner | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Jeff | Executioner | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Jeff | Executioner | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Jeff | Executioner | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Jeff | Executioner | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Jeff | Executioner | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Jeff | Executioner | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Ken  | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Ken  | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ken  | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ken  | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ken  | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Ken  | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ken  | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ken  | Jailer      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ken  | Jailer      | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Ken  | Jailer      | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Ken  | Jailer      | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Ken  | Jailer      | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Lee  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Lee  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Lee  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Lee  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Lee  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Lee  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Lee  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Lee  | Spy         | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Lee  | Spy         | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Lee  | Spy         | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Lee  | Spy         | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Lee  | Spy         | reveal    | NPC Dan is targeting NPC Mark                                    |
| 1           | NPC Lee  | Spy         | reveal    | NPC Fae is targeting NPC Mark                                    |
| 1           | NPC Lee  | Spy         | reveal    | NPC Mark is targeting NPC Lee                                    |
| 1           | NPC Lee  | Spy         | reveal    | NPC Norm is targeting NPC Ed                                     |
| 1           | NPC Lee  | Spy         | reveal    | NPC Cal is targeting NPC Dan                                     |
| 1           | NPC Lee  | Spy         | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Mark | Reporter    | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Mark | Reporter    | silenced  | You have been silenced                                           |
| 1           | NPC Mark | Reporter    | reveal    | NPC Lee is Spy                                                   |
| 1           | NPC Mark | Reporter    | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Norm | Thief       | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Norm | Thief       | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Norm | Thief       | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Norm | Thief       | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Norm | Thief       | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Norm | Thief       | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Norm | Thief       | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Norm | Thief       | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Norm | Thief       | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Norm | Thief       | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Norm | Thief       | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Norm | Thief       | vote      | Demagog has initiated a vote on eliminating Spy                  |
| 1           | NPC Ozie | Trader      | broadcast | I (NPC Ann) am the Psychic and the Inspector is not possessed    |
| 1           | NPC Ozie | Trader      | broadcast | I (NPC Ann) am the Psychic and the Executioner is not possessed  |
| 1           | NPC Ozie | Trader      | broadcast | I (NPC Ann) am the Psychic and the Silencer is not possessed     |
| 1           | NPC Ozie | Trader      | broadcast | I (NPC Ann) am the Psychic and the Demagog is not possessed      |
| 1           | NPC Ozie | Trader      | broadcast | I (NPC Ann) am the Psychic and the Prophet is not possessed      |
| 1           | NPC Ozie | Trader      | broadcast | I (NPC Ann) am the Psychic and the Medic is not possessed        |
| 1           | NPC Ozie | Trader      | broadcast | I (NPC Ann) am the Psychic and the Spy is not possessed          |
| 1           | NPC Ozie | Trader      | broadcast | I (NPC Ann) am the Psychic and the Priest is not possessed       |
| 1           | NPC Ozie | Trader      | broadcast | I (NPC Cal) inspected NPC Dan and they are not possessed         |
| 1           | NPC Ozie | Trader      | broadcast | I (NPC Mark) am the Reporter and NPC Lee is the Spy              |
| 1           | NPC Ozie | Trader      | broadcast | I (NPC Norm) am the Thief and I have made NPC Ed vulnerable      |
| 1           | NPC Ozie | Trader      | vote      | Demagog has initiated a vote on eliminating Spy                  |

#### Actions Round 2
| round_index | Player  | action   | Target 1  | Target 2 | status      |
| :-----------| :-------| :--------| :---------| :--------| :---------- |
| 2           | NPC Ann | Prophet  | NPC Bob   |          | successful  |
| 2           | NPC Dan | Judge    | Inspector |          | successful  |
| 2           | NPC Fae | Silencer | NPC Bob   |          | successful  |
| 2           | NPC Gia | Psychic  |           |          | successful  |
| 2           | NPC Han | Medic    | NPC Fae   |          | successful  |
| 2           | NPC Lee | Spy      |           |          | successful  |

#### States Round 2
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Igi  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Dan  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae  | Silencer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Han  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Lee  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Gia  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ken  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Mark | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Norm | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Jeff | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ozie | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Cal  | Inspector   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed   | Demagog     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 2           | NPC Ann  | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Bob  | Priest      | silenced  | You have been silenced                                        |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Gia  | Psychic     | reveal    | Player: NPC Ken is not possessed                              |
| 2           | NPC Gia  | Psychic     | reveal    | Player: NPC Norm is not possessed                             |
| 2           | NPC Gia  | Psychic     | reveal    | Player: NPC Bob is not possessed                              |
| 2           | NPC Gia  | Psychic     | reveal    | Player: NPC Igi is not possessed                              |
| 2           | NPC Gia  | Psychic     | reveal    | Player: NPC Mark is not possessed                             |
| 2           | NPC Gia  | Psychic     | reveal    | Player: NPC Ozie is not possessed                             |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Lee  | Spy         | reveal    | NPC Igi is targeting NPC Jeff                                 |
| 2           | NPC Lee  | Spy         | reveal    | NPC Dan is targeting NPC Cal                                  |
| 2           | NPC Lee  | Spy         | reveal    | NPC Fae is targeting NPC Bob                                  |
| 2           | NPC Lee  | Spy         | reveal    | NPC Han is targeting NPC Dan                                  |
| 2           | NPC Lee  | Spy         | reveal    | NPC Mark is targeting NPC Lee                                 |
| 2           | NPC Lee  | Spy         | reveal    | NPC Norm is targeting NPC Ed                                  |
| 2           | NPC Lee  | Spy         | reveal    | NPC Ozie is targeting NPC Ann                                 |
| 2           | NPC Lee  | Spy         | reveal    | NPC Ozie is targeting NPC Ann                                 |
| 2           | NPC Lee  | Spy         | reveal    | NPC Cal is targeting NPC Dan                                  |
| 2           | NPC Lee  | Spy         | reveal    | NPC Ed is targeting NPC Lee                                   |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed    |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed  |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff      |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Mark      |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Mark      |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Dan       |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee      |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed       |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan       |
| 2           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee        |

#### Actions Round 3
| round_index | Player   | action    | Target 1  | Target 2 | status              |
| :-----------| :--------| :---------| :---------| :--------| :------------------ |
| 3           | NPC Ann  | Prophet   | NPC Norm  |          | successful          |
| 3           | NPC Cal  | Inspector | NPC Han   |          | successful          |
| 3           | NPC Dan  | Judge     | Silencer  |          | successful          |
| 3           | NPC Ed   | Demagog   | Assassin  |          | voting in progress  |
| 3           | NPC Fae  | Silencer  | NPC Bob   |          | successful          |
| 3           | NPC Gia  | Psychic   |           |          | successful          |
| 3           | NPC Han  | Medic     | NPC Bob   |          | successful          |
| 3           | NPC Igi  | Assassin  | Inspector |          | successful          |
| 3           | NPC Lee  | Spy       |           |          | successful          |
| 3           | NPC Mark | Reporter  | NPC Ed    |          | successful          |
| 3           | NPC Norm | Thief     | NPC Cal   |          | successful          |

#### States Round 3
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Igi  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Dan  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Fae  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Han  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Bob  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Lee  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Gia  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ken  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Mark | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Norm | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Jeff | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ozie | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Cal  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Ed   | Demagog     | False      | False     | True       | 2         | True   | 0              | 0                  |
| 3           | NPC Ann  | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Ann  | Prophet     | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Ann  | Prophet     | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Bob  | Priest      | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Bob  | Priest      | silenced  | You have been silenced                                         |
| 3           | NPC Bob  | Priest      | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Cal  | Inspector   | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Cal  | Inspector   | reveal    | Medic is Innocent                                              |
| 3           | NPC Cal  | Inspector   | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Dan  | Judge       | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Dan  | Judge       | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Ed   | Demagog     | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Ed   | Demagog     | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Fae  | Silencer    | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Fae  | Silencer    | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Gia  | Psychic     | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Gia  | Psychic     | reveal    | Player: NPC Dan is not possessed                               |
| 3           | NPC Gia  | Psychic     | reveal    | Player: NPC Ed is not possessed                                |
| 3           | NPC Gia  | Psychic     | reveal    | Player: NPC Igi is not possessed                               |
| 3           | NPC Gia  | Psychic     | reveal    | Player: NPC Ken is not possessed                               |
| 3           | NPC Gia  | Psychic     | reveal    | Player: NPC Jeff is not possessed                              |
| 3           | NPC Gia  | Psychic     | reveal    | Player: NPC Bob is not possessed                               |
| 3           | NPC Gia  | Psychic     | reveal    | Player: NPC Lee is not possessed                               |
| 3           | NPC Gia  | Psychic     | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Han  | Medic       | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Han  | Medic       | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Igi  | Assassin    | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Igi  | Assassin    | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Jeff | Executioner | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Jeff | Executioner | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Ken  | Jailer      | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Ken  | Jailer      | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Lee  | Spy         | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Lee  | Spy         | reveal    | NPC Igi is targeting NPC Jeff                                  |
| 3           | NPC Lee  | Spy         | reveal    | NPC Dan is targeting NPC Fae                                   |
| 3           | NPC Lee  | Spy         | reveal    | NPC Fae is targeting NPC Bob                                   |
| 3           | NPC Lee  | Spy         | reveal    | NPC Han is targeting NPC Fae                                   |
| 3           | NPC Lee  | Spy         | reveal    | NPC Mark is targeting NPC Ed                                   |
| 3           | NPC Lee  | Spy         | reveal    | NPC Norm is targeting NPC Cal                                  |
| 3           | NPC Lee  | Spy         | reveal    | NPC Ozie is targeting NPC Ann                                  |
| 3           | NPC Lee  | Spy         | reveal    | NPC Ozie is targeting NPC Ann                                  |
| 3           | NPC Lee  | Spy         | reveal    | NPC Cal is targeting NPC Han                                   |
| 3           | NPC Lee  | Spy         | reveal    | NPC Ed is targeting NPC Lee                                    |
| 3           | NPC Lee  | Spy         | reveal    | NPC Ann is targeting NPC Bob                                   |
| 3           | NPC Lee  | Spy         | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Mark | Reporter    | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Mark | Reporter    | reveal    | NPC Ed is Demagog                                              |
| 3           | NPC Mark | Reporter    | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Norm | Thief       | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Norm | Thief       | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Cal) inspected NPC Han and they are not possessed       |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Jeff       |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Cal        |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob        |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Fae        |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Lee       |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ed        |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann       |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Dan        |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Lee         |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob        |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Mark) am the Reporter and NPC Ed is the Demagog         |
| 3           | NPC Ozie | Trader      | broadcast | I (NPC Norm) am the Thief and I have made NPC Cal vulnerable   |
| 3           | NPC Ozie | Trader      | vote      | Demagog has initiated a vote on eliminating Assassin           |

#### Actions Round 4
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 4           | NPC Ann | Prophet  | NPC Ozie |          | successful  |
| 4           | NPC Dan | Judge    | Reporter |          | successful  |
| 4           | NPC Fae | Silencer | NPC Lee  |          | successful  |
| 4           | NPC Gia | Psychic  |          |          | successful  |
| 4           | NPC Han | Medic    | NPC Lee  |          | successful  |
| 4           | NPC Lee | Spy      |          |          | successful  |

#### States Round 4
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Igi  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Dan  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Han  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Bob  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Lee  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Gia  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ken  | Jailer      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Mark | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Norm | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Jeff | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ozie | Trader      | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Cal  | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Ed   | Demagog     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 4           | NPC Ann  | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role        | message   | details                                                       |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------ |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Gia  | Psychic     | reveal    | Player: NPC Norm is not possessed                             |
| 4           | NPC Gia  | Psychic     | reveal    | Player: NPC Bob is not possessed                              |
| 4           | NPC Gia  | Psychic     | reveal    | Player: NPC Lee is not possessed                              |
| 4           | NPC Gia  | Psychic     | reveal    | Player: NPC Jeff is not possessed                             |
| 4           | NPC Gia  | Psychic     | reveal    | Player: NPC Ed is not possessed                               |
| 4           | NPC Gia  | Psychic     | reveal    | Player: NPC Han is not possessed                              |
| 4           | NPC Gia  | Psychic     | reveal    | Player: NPC Dan is not possessed                              |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Lee  | Spy         | silenced  | You have been silenced                                        |
| 4           | NPC Lee  | Spy         | reveal    | NPC Igi is targeting NPC Cal                                  |
| 4           | NPC Lee  | Spy         | reveal    | NPC Dan is targeting NPC Mark                                 |
| 4           | NPC Lee  | Spy         | reveal    | NPC Fae is targeting NPC Lee                                  |
| 4           | NPC Lee  | Spy         | reveal    | NPC Han is targeting NPC Bob                                  |
| 4           | NPC Lee  | Spy         | reveal    | NPC Mark is targeting NPC Ed                                  |
| 4           | NPC Lee  | Spy         | reveal    | NPC Norm is targeting NPC Cal                                 |
| 4           | NPC Lee  | Spy         | reveal    | NPC Ozie is targeting NPC Ann                                 |
| 4           | NPC Lee  | Spy         | reveal    | NPC Ozie is targeting NPC Ann                                 |
| 4           | NPC Lee  | Spy         | reveal    | NPC Cal is targeting NPC Han                                  |
| 4           | NPC Lee  | Spy         | reveal    | NPC Ed is targeting NPC Igi                                   |
| 4           | NPC Lee  | Spy         | reveal    | NPC Ann is targeting NPC Norm                                 |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed     |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Silencer is not possessed  |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Spy is not possessed       |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Trader is not possessed    |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Reporter is not possessed  |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Jailer is not possessed    |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed   |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Cal       |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Fae       |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Bob       |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Bob       |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Ed       |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Cal      |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Ann      |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Han       |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Igi        |
| 4           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Norm      |

#### Actions Round 5
| round_index | Player   | action    | Target 1 | Target 2 | status                         |
| :-----------| :--------| :---------| :--------| :--------| :----------------------------- |
| 5           | NPC Ann  | Prophet   | NPC Bob  |          | successful                     |
| 5           | NPC Cal  | Inspector | NPC Ed   |          | successful                     |
| 5           | NPC Dan  | Judge     | Prophet  |          | successful                     |
| 5           | NPC Ed   | Demagog   | Thief    |          | voting in progress             |
| 5           | NPC Fae  | Silencer  | NPC Gia  |          | successful                     |
| 5           | NPC Gia  | Psychic   |          |          | successful                     |
| 5           | NPC Han  | Medic     | NPC Gia  |          | successful                     |
| 5           | NPC Igi  | Assassin  | Trader   |          | successful                     |
| 5           | NPC Lee  | Spy       |          |          | successful                     |
| 5           | NPC Mark | Reporter  | NPC Dan  |          | successful                     |
| 5           | NPC Norm | Thief     | NPC Ken  |          | successful                     |
| 5           | NPC Ozie | Trader    | NPC Fae  | NPC Norm | failed because not vulnerable  |

#### States Round 5
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 5           | NPC Igi  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Dan  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Fae  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 5           | NPC Han  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Bob  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Lee  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Gia  | Psychic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ken  | Jailer      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 5           | NPC Mark | Reporter    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Norm | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 5           | NPC Jeff | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 5           | NPC Ozie | Trader      | False      | False     | False      | 4         | True   | 0              | 0                  |
| 5           | NPC Cal  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Ed   | Demagog     | False      | False     | True       | 2         | True   | 0              | 0                  |
| 5           | NPC Ann  | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 5
| round_index | Player   | Role        | message   | details                                                        |
| :-----------| :--------| :-----------| :---------| :------------------------------------------------------------- |
| 5           | NPC Ann  | Prophet     | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ann  | Prophet     | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Ann  | Prophet     | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Ann  | Prophet     | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Bob  | Priest      | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Bob  | Priest      | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Bob  | Priest      | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Bob  | Priest      | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Cal  | Inspector   | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Cal  | Inspector   | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Cal  | Inspector   | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Cal  | Inspector   | reveal    | Demagog is Innocent                                            |
| 5           | NPC Cal  | Inspector   | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Dan  | Judge       | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Dan  | Judge       | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Dan  | Judge       | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Dan  | Judge       | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Ed   | Demagog     | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ed   | Demagog     | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Ed   | Demagog     | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Ed   | Demagog     | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Fae  | Silencer    | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Fae  | Silencer    | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Fae  | Silencer    | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Fae  | Silencer    | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Gia  | Psychic     | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Gia  | Psychic     | silenced  | You have been silenced                                         |
| 5           | NPC Gia  | Psychic     | reveal    | Player: NPC Fae is not possessed                               |
| 5           | NPC Gia  | Psychic     | reveal    | Player: NPC Jeff is not possessed                              |
| 5           | NPC Gia  | Psychic     | reveal    | Player: NPC Ed is not possessed                                |
| 5           | NPC Gia  | Psychic     | reveal    | Player: NPC Dan is not possessed                               |
| 5           | NPC Gia  | Psychic     | reveal    | Player: NPC Cal is not possessed                               |
| 5           | NPC Gia  | Psychic     | reveal    | Player: NPC Norm is not possessed                              |
| 5           | NPC Gia  | Psychic     | reveal    | Player: NPC Han is not possessed                               |
| 5           | NPC Gia  | Psychic     | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Han  | Medic       | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Han  | Medic       | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Han  | Medic       | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Han  | Medic       | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Igi  | Assassin    | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Igi  | Assassin    | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Igi  | Assassin    | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Igi  | Assassin    | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Jeff | Executioner | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Jeff | Executioner | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Jeff | Executioner | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Jeff | Executioner | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Ken  | Jailer      | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ken  | Jailer      | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Ken  | Jailer      | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Ken  | Jailer      | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Lee  | Spy         | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Lee  | Spy         | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Lee  | Spy         | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Lee  | Spy         | reveal    | NPC Igi is targeting NPC Cal                                   |
| 5           | NPC Lee  | Spy         | reveal    | NPC Dan is targeting NPC Ann                                   |
| 5           | NPC Lee  | Spy         | reveal    | NPC Fae is targeting NPC Gia                                   |
| 5           | NPC Lee  | Spy         | reveal    | NPC Han is targeting NPC Lee                                   |
| 5           | NPC Lee  | Spy         | reveal    | NPC Mark is targeting NPC Dan                                  |
| 5           | NPC Lee  | Spy         | reveal    | NPC Norm is targeting NPC Ken                                  |
| 5           | NPC Lee  | Spy         | reveal    | NPC Ozie is targeting NPC Ann                                  |
| 5           | NPC Lee  | Spy         | reveal    | NPC Ozie is targeting NPC Ann                                  |
| 5           | NPC Lee  | Spy         | reveal    | NPC Cal is targeting NPC Ed                                    |
| 5           | NPC Lee  | Spy         | reveal    | NPC Ed is targeting NPC Igi                                    |
| 5           | NPC Lee  | Spy         | reveal    | NPC Ann is targeting NPC Ozie                                  |
| 5           | NPC Lee  | Spy         | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Mark | Reporter    | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Mark | Reporter    | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Mark | Reporter    | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Mark | Reporter    | reveal    | NPC Dan is Judge                                               |
| 5           | NPC Mark | Reporter    | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Norm | Thief       | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Norm | Thief       | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Norm | Thief       | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Norm | Thief       | vote      | Demagog has initiated a vote on eliminating Thief              |
| 5           | NPC Ozie | Trader      | broadcast | I (NPC Cal) inspected NPC Ed and they are not possessed        |
| 5           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 5           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Priest is not possessed     |
| 5           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 5           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Assassin is not possessed   |
| 5           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 5           | NPC Ozie | Trader      | broadcast | I (NPC Gia) am the Psychic and the Thief is not possessed      |
| 5           | NPC Ozie | Trader      | broadcast | I (NPC Norm) am the Thief and I have made NPC Ken vulnerable   |
| 5           | NPC Ozie | Trader      | vote      | Demagog has initiated a vote on eliminating Thief              |

#### Actions Round 6
| round_index | Player  | action   | Target 1 | Target 2 | status      |
| :-----------| :-------| :--------| :--------| :--------| :---------- |
| 6           | NPC Ann | Prophet  | NPC Ed   |          | successful  |
| 6           | NPC Dan | Judge    | Priest   |          | successful  |
| 6           | NPC Fae | Silencer | NPC Ann  |          | successful  |
| 6           | NPC Gia | Psychic  |          |          | successful  |
| 6           | NPC Han | Medic    | NPC Ken  |          | successful  |
| 6           | NPC Lee | Spy      |          |          | successful  |

#### States Round 6
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 6           | NPC Igi  | Assassin    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Dan  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Fae  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Han  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Bob  | Priest      | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Lee  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Gia  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Ken  | Jailer      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 6           | NPC Mark | Reporter    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Norm | Thief       | False      | False     | False      | 1         | True   | 0              | 0                  |
| 6           | NPC Jeff | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 6           | NPC Ozie | Trader      | False      | False     | False      | 3         | True   | 0              | 0                  |
| 6           | NPC Cal  | Inspector   | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Ed   | Demagog     | False      | False     | True       | 1         | True   | 0              | 0                  |
| 6           | NPC Ann  | Prophet     | False      | True      | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 6
| round_index | Player   | Role        | message   | details                                                   |
| :-----------| :--------| :-----------| :---------| :-------------------------------------------------------- |
| 6           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Ann  | Prophet     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Ann  | Prophet     | silenced  | You have been silenced                                    |
| 6           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Bob  | Priest      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Cal  | Inspector   | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Dan  | Judge       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Ed   | Demagog     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Fae  | Silencer    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Gia  | Psychic     | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Gia  | Psychic     | reveal    | Player: NPC Cal is not possessed                          |
| 6           | NPC Gia  | Psychic     | reveal    | Player: NPC Igi is not possessed                          |
| 6           | NPC Gia  | Psychic     | reveal    | Player: NPC Fae is not possessed                          |
| 6           | NPC Gia  | Psychic     | reveal    | Player: NPC Lee is not possessed                          |
| 6           | NPC Gia  | Psychic     | reveal    | Player: NPC Ozie is not possessed                         |
| 6           | NPC Gia  | Psychic     | reveal    | Player: NPC Bob is not possessed                          |
| 6           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Han  | Medic       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Igi  | Assassin    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Jeff | Executioner | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Ken  | Jailer      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Lee  | Spy         | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Lee  | Spy         | reveal    | NPC Igi is targeting NPC Ozie                             |
| 6           | NPC Lee  | Spy         | reveal    | NPC Dan is targeting NPC Bob                              |
| 6           | NPC Lee  | Spy         | reveal    | NPC Fae is targeting NPC Ann                              |
| 6           | NPC Lee  | Spy         | reveal    | NPC Han is targeting NPC Gia                              |
| 6           | NPC Lee  | Spy         | reveal    | NPC Mark is targeting NPC Dan                             |
| 6           | NPC Lee  | Spy         | reveal    | NPC Norm is targeting NPC Ken                             |
| 6           | NPC Lee  | Spy         | reveal    | NPC Ozie is targeting NPC Fae                             |
| 6           | NPC Lee  | Spy         | reveal    | NPC Ozie is targeting NPC Fae                             |
| 6           | NPC Lee  | Spy         | reveal    | NPC Cal is targeting NPC Ed                               |
| 6           | NPC Lee  | Spy         | reveal    | NPC Ed is targeting NPC Norm                              |
| 6           | NPC Lee  | Spy         | reveal    | NPC Ann is targeting NPC Bob                              |
| 6           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Mark | Reporter    | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Norm | Thief       | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |
| 6           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie  |
| 6           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Ann   |
| 6           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Gia   |
| 6           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Han is targeting NPC Gia   |
| 6           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan  |
| 6           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken  |
| 6           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae  |
| 6           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed    |
| 6           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm   |
| 6           | NPC Ozie | Trader      | broadcast | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Bob   |

#### Actions Round 7
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 7           | NPC Ann  | Prophet   | NPC Ken  |          | successful          |
| 7           | NPC Cal  | Inspector | NPC Mark |          | successful          |
| 7           | NPC Dan  | Judge     | Trader   |          | successful          |
| 7           | NPC Ed   | Demagog   | Thief    |          | voting in progress  |
| 7           | NPC Fae  | Silencer  | NPC Bob  |          | successful          |
| 7           | NPC Gia  | Psychic   |          |          | successful          |
| 7           | NPC Han  | Medic     | NPC Mark |          | successful          |
| 7           | NPC Igi  | Assassin  | Priest   |          | successful          |
| 7           | NPC Lee  | Spy       |          |          | successful          |
| 7           | NPC Mark | Reporter  | NPC Norm |          | successful          |
| 7           | NPC Norm | Thief     | NPC Ann  |          | successful          |

#### States Round 7
| round_index | Player   | Role        | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :-----------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 7           | NPC Igi  | Assassin    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Dan  | Judge       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Fae  | Silencer    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Han  | Medic       | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Bob  | Priest      | True       | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Lee  | Spy         | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Gia  | Psychic     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 7           | NPC Ken  | Jailer      | False      | False     | True       | 0         | True   | 0              | 0                  |
| 7           | NPC Mark | Reporter    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Norm | Thief       | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Jeff | Executioner | False      | False     | False      | 0         | True   | 0              | 0                  |
| 7           | NPC Ozie | Trader      | False      | False     | False      | 2         | True   | 0              | 0                  |
| 7           | NPC Cal  | Inspector   | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Ed   | Demagog     | False      | False     | True       | 2         | True   | 0              | 0                  |
| 7           | NPC Ann  | Prophet     | False      | True      | True       | 0         | True   | 0              | 0                  |

#### Notifications Round 7
| round_index | Player   | Role        | message     | details                                                        |
| :-----------| :--------| :-----------| :-----------| :------------------------------------------------------------- |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Ann  | Prophet     | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Ann  | Prophet     | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Ann  | Prophet     | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Bob  | Priest      | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Bob  | Priest      | silenced    | You have been silenced                                         |
| 7           | NPC Bob  | Priest      | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Bob  | Priest      | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Cal  | Inspector   | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Cal  | Inspector   | reveal      | Reporter is Innocent                                           |
| 7           | NPC Cal  | Inspector   | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Cal  | Inspector   | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Dan  | Judge       | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Dan  | Judge       | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Dan  | Judge       | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Ed   | Demagog     | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Ed   | Demagog     | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Ed   | Demagog     | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Fae  | Silencer    | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Fae  | Silencer    | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Fae  | Silencer    | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Gia  | Psychic     | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Gia  | Psychic     | reveal      | Player: NPC Ed is not possessed                                |
| 7           | NPC Gia  | Psychic     | reveal      | Player: NPC Jeff is not possessed                              |
| 7           | NPC Gia  | Psychic     | reveal      | Player: NPC Cal is not possessed                               |
| 7           | NPC Gia  | Psychic     | reveal      | Player: NPC Bob is not possessed                               |
| 7           | NPC Gia  | Psychic     | reveal      | Player: NPC Dan is not possessed                               |
| 7           | NPC Gia  | Psychic     | reveal      | Player: NPC Fae is not possessed                               |
| 7           | NPC Gia  | Psychic     | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Gia  | Psychic     | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Han  | Medic       | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Han  | Medic       | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Han  | Medic       | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Igi  | Assassin    | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Igi  | Assassin    | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Igi  | Assassin    | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Jeff | Executioner | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Jeff | Executioner | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Jeff | Executioner | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Ken  | Jailer      | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Ken  | Jailer      | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Ken  | Jailer      | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Lee  | Spy         | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Lee  | Spy         | reveal      | NPC Igi is targeting NPC Ozie                                  |
| 7           | NPC Lee  | Spy         | reveal      | NPC Dan is targeting NPC Ozie                                  |
| 7           | NPC Lee  | Spy         | reveal      | NPC Fae is targeting NPC Bob                                   |
| 7           | NPC Lee  | Spy         | reveal      | NPC Han is targeting NPC Ken                                   |
| 7           | NPC Lee  | Spy         | reveal      | NPC Mark is targeting NPC Norm                                 |
| 7           | NPC Lee  | Spy         | reveal      | NPC Norm is targeting NPC Ann                                  |
| 7           | NPC Lee  | Spy         | reveal      | NPC Ozie is targeting NPC Fae                                  |
| 7           | NPC Lee  | Spy         | reveal      | NPC Ozie is targeting NPC Fae                                  |
| 7           | NPC Lee  | Spy         | reveal      | NPC Cal is targeting NPC Mark                                  |
| 7           | NPC Lee  | Spy         | reveal      | NPC Ed is targeting NPC Norm                                   |
| 7           | NPC Lee  | Spy         | reveal      | NPC Ann is targeting NPC Ed                                    |
| 7           | NPC Lee  | Spy         | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Lee  | Spy         | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Mark | Reporter    | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Mark | Reporter    | reveal      | NPC Norm is Thief                                              |
| 7           | NPC Mark | Reporter    | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Mark | Reporter    | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Norm | Thief       | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Norm | Thief       | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Norm | Thief       | vote        | Demagog has initiated a vote on eliminating Thief              |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Cal) inspected NPC Mark and they are not possessed      |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Gia) am the Psychic and the Spy is not possessed        |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Gia) am the Psychic and the Silencer is not possessed   |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Gia) am the Psychic and the Inspector is not possessed  |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Gia) am the Psychic and the Demagog is not possessed    |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Gia) am the Psychic and the Judge is not possessed      |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Gia) am the Psychic and the Trader is not possessed     |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Gia) am the Psychic and the Reporter is not possessed   |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Lee) am the Spy and NPC Igi is targeting NPC Ozie       |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Lee) am the Spy and NPC Dan is targeting NPC Bob        |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Lee) am the Spy and NPC Fae is targeting NPC Ann        |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Lee) am the Spy and NPC Han is targeting NPC Ken        |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Lee) am the Spy and NPC Mark is targeting NPC Dan       |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Lee) am the Spy and NPC Norm is targeting NPC Ken       |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Lee) am the Spy and NPC Ozie is targeting NPC Fae       |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Lee) am the Spy and NPC Cal is targeting NPC Ed         |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Lee) am the Spy and NPC Ed is targeting NPC Norm        |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Lee) am the Spy and NPC Ann is targeting NPC Ed         |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Mark) am the Reporter and NPC Norm is the Thief         |
| 7           | NPC Ozie | Trader      | broadcast   | I (NPC Norm) am the Thief and I have made NPC Ann vulnerable   |
| 7           | NPC Ozie | Trader      | elimination | NPC Bob has been eliminated                                    |
| 7           | NPC Ozie | Trader      | vote        | Demagog has initiated a vote on eliminating Thief              |