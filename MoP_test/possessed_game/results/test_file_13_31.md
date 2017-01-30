#### Setup
| Seed | Players | Rounds  |
| :----| :-------| :------ |
| 31   | 13      | 4       |

#### Roles
| Role       |
| :--------- |
| Thief      |
| Priest     |
| Reporter   |
| Assassin   |
| Prophet    |
| Demagog    |
| Silencer   |
| Inspector  |
| Judge      |
| Jailer     |
| Medic      |
| Trader     |
| Psychic    |

#### States Round 0
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 0           | NPC Cal  | Thief     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Han  | Priest    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ann  | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Bob  | Assassin  | False      | True      | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Jeff | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Mark | Demagog   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Lee  | Silencer  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ed   | Inspector | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Gia  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Ken  | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Dan  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Fae  | Trader    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 0           | NPC Igi  | Psychic   | False      | False     | False      | 0         | True   | 0              | 0                  |

#### Notifications Round 0
| round_index | Player   | Role      | message     | details                 |
| :-----------| :--------| :---------| :-----------| :---------------------- |
| 0           | NPC Ann  | Reporter  | role change | Your Role is Reporter   |
| 0           | NPC Ann  | Reporter  | possessed   | You are Not Possessed   |
| 0           | NPC Bob  | Assassin  | role change | Your Role is Assassin   |
| 0           | NPC Bob  | Assassin  | possessed   | You are Possessed       |
| 0           | NPC Cal  | Thief     | role change | Your Role is Thief      |
| 0           | NPC Cal  | Thief     | possessed   | You are Not Possessed   |
| 0           | NPC Dan  | Medic     | role change | Your Role is Medic      |
| 0           | NPC Dan  | Medic     | possessed   | You are Not Possessed   |
| 0           | NPC Ed   | Inspector | role change | Your Role is Inspector  |
| 0           | NPC Ed   | Inspector | possessed   | You are Not Possessed   |
| 0           | NPC Fae  | Trader    | role change | Your Role is Trader     |
| 0           | NPC Fae  | Trader    | possessed   | You are Not Possessed   |
| 0           | NPC Gia  | Judge     | role change | Your Role is Judge      |
| 0           | NPC Gia  | Judge     | possessed   | You are Not Possessed   |
| 0           | NPC Han  | Priest    | role change | Your Role is Priest     |
| 0           | NPC Han  | Priest    | possessed   | You are Not Possessed   |
| 0           | NPC Igi  | Psychic   | role change | Your Role is Psychic    |
| 0           | NPC Igi  | Psychic   | possessed   | You are Not Possessed   |
| 0           | NPC Jeff | Prophet   | role change | Your Role is Prophet    |
| 0           | NPC Jeff | Prophet   | possessed   | You are Not Possessed   |
| 0           | NPC Ken  | Jailer    | role change | Your Role is Jailer     |
| 0           | NPC Ken  | Jailer    | possessed   | You are Not Possessed   |
| 0           | NPC Lee  | Silencer  | role change | Your Role is Silencer   |
| 0           | NPC Lee  | Silencer  | possessed   | You are Not Possessed   |
| 0           | NPC Mark | Demagog   | role change | Your Role is Demagog    |
| 0           | NPC Mark | Demagog   | possessed   | You are Not Possessed   |

#### Actions Round 1
| round_index | Player   | action    | Target 1  | Target 2 | status                         |
| :-----------| :--------| :---------| :---------| :--------| :----------------------------- |
| 1           | NPC Ann  | Reporter  | NPC Fae   |          | successful                     |
| 1           | NPC Bob  | Assassin  | Judge     |          | successful                     |
| 1           | NPC Cal  | Thief     | NPC Han   |          | successful                     |
| 1           | NPC Dan  | Medic     | NPC Han   |          | successful                     |
| 1           | NPC Ed   | Inspector | NPC Bob   |          | successful                     |
| 1           | NPC Fae  | Trader    | NPC Han   | NPC Dan  | failed because not vulnerable  |
| 1           | NPC Gia  | Judge     | Medic     |          | successful                     |
| 1           | NPC Igi  | Psychic   |           |          | successful                     |
| 1           | NPC Jeff | Prophet   | NPC Lee   |          | successful                     |
| 1           | NPC Lee  | Silencer  | NPC Ken   |          | successful                     |
| 1           | NPC Mark | Demagog   | Inspector |          | voting in progress             |

#### States Round 1
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 1           | NPC Cal  | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Han  | Priest    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 1           | NPC Ann  | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Bob  | Assassin  | False      | True      | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Jeff | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Mark | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Lee  | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 1           | NPC Ed   | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 1           | NPC Gia  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Ken  | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Dan  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 1           | NPC Fae  | Trader    | False      | False     | False      | 4         | True   | 0              | 0                  |
| 1           | NPC Igi  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 1
| round_index | Player   | Role      | message   | details                                                        |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------- |
| 1           | NPC Ann  | Reporter  | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Trader          |
| 1           | NPC Ann  | Reporter  | broadcast | I (NPC Cal) am the Thief and I have made NPC Han vulnerable    |
| 1           | NPC Ann  | Reporter  | broadcast | I (NPC Ed) inspected NPC Bob and they are possessed            |
| 1           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 1           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 1           | NPC Ann  | Reporter  | reveal    | NPC Fae is Trader                                              |
| 1           | NPC Ann  | Reporter  | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Bob  | Assassin  | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Trader          |
| 1           | NPC Bob  | Assassin  | broadcast | I (NPC Cal) am the Thief and I have made NPC Han vulnerable    |
| 1           | NPC Bob  | Assassin  | broadcast | I (NPC Ed) inspected NPC Bob and they are possessed            |
| 1           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 1           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 1           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 1           | NPC Bob  | Assassin  | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Cal  | Thief     | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Trader          |
| 1           | NPC Cal  | Thief     | broadcast | I (NPC Cal) am the Thief and I have made NPC Han vulnerable    |
| 1           | NPC Cal  | Thief     | broadcast | I (NPC Ed) inspected NPC Bob and they are possessed            |
| 1           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 1           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 1           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 1           | NPC Cal  | Thief     | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Dan  | Medic     | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Trader          |
| 1           | NPC Dan  | Medic     | broadcast | I (NPC Cal) am the Thief and I have made NPC Han vulnerable    |
| 1           | NPC Dan  | Medic     | broadcast | I (NPC Ed) inspected NPC Bob and they are possessed            |
| 1           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 1           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 1           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 1           | NPC Dan  | Medic     | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Ed   | Inspector | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Trader          |
| 1           | NPC Ed   | Inspector | broadcast | I (NPC Cal) am the Thief and I have made NPC Han vulnerable    |
| 1           | NPC Ed   | Inspector | broadcast | I (NPC Ed) inspected NPC Bob and they are possessed            |
| 1           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 1           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 1           | NPC Ed   | Inspector | reveal    | Assassin is Possessed                                          |
| 1           | NPC Ed   | Inspector | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Fae  | Trader    | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Trader          |
| 1           | NPC Fae  | Trader    | broadcast | I (NPC Cal) am the Thief and I have made NPC Han vulnerable    |
| 1           | NPC Fae  | Trader    | broadcast | I (NPC Ed) inspected NPC Bob and they are possessed            |
| 1           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 1           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 1           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 1           | NPC Fae  | Trader    | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Gia  | Judge     | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Trader          |
| 1           | NPC Gia  | Judge     | broadcast | I (NPC Cal) am the Thief and I have made NPC Han vulnerable    |
| 1           | NPC Gia  | Judge     | broadcast | I (NPC Ed) inspected NPC Bob and they are possessed            |
| 1           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 1           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 1           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 1           | NPC Gia  | Judge     | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Han  | Priest    | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Trader          |
| 1           | NPC Han  | Priest    | broadcast | I (NPC Cal) am the Thief and I have made NPC Han vulnerable    |
| 1           | NPC Han  | Priest    | broadcast | I (NPC Ed) inspected NPC Bob and they are possessed            |
| 1           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 1           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 1           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 1           | NPC Han  | Priest    | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Trader          |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Cal) am the Thief and I have made NPC Han vulnerable    |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Ed) inspected NPC Bob and they are possessed            |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 1           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 1           | NPC Igi  | Psychic   | reveal    | Player: NPC Fae is not possessed                               |
| 1           | NPC Igi  | Psychic   | reveal    | Player: NPC Ann is not possessed                               |
| 1           | NPC Igi  | Psychic   | reveal    | Player: NPC Jeff is not possessed                              |
| 1           | NPC Igi  | Psychic   | reveal    | Player: NPC Han is not possessed                               |
| 1           | NPC Igi  | Psychic   | reveal    | Player: NPC Ken is not possessed                               |
| 1           | NPC Igi  | Psychic   | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Jeff | Prophet   | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Trader          |
| 1           | NPC Jeff | Prophet   | broadcast | I (NPC Cal) am the Thief and I have made NPC Han vulnerable    |
| 1           | NPC Jeff | Prophet   | broadcast | I (NPC Ed) inspected NPC Bob and they are possessed            |
| 1           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 1           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 1           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 1           | NPC Jeff | Prophet   | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Ken  | Jailer    | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Trader          |
| 1           | NPC Ken  | Jailer    | broadcast | I (NPC Cal) am the Thief and I have made NPC Han vulnerable    |
| 1           | NPC Ken  | Jailer    | broadcast | I (NPC Ed) inspected NPC Bob and they are possessed            |
| 1           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 1           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 1           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 1           | NPC Ken  | Jailer    | silenced  | You have been silenced                                         |
| 1           | NPC Ken  | Jailer    | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Lee  | Silencer  | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Trader          |
| 1           | NPC Lee  | Silencer  | broadcast | I (NPC Cal) am the Thief and I have made NPC Han vulnerable    |
| 1           | NPC Lee  | Silencer  | broadcast | I (NPC Ed) inspected NPC Bob and they are possessed            |
| 1           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 1           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 1           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 1           | NPC Lee  | Silencer  | vote      | Demagog has initiated a vote on eliminating Inspector          |
| 1           | NPC Mark | Demagog   | broadcast | I (NPC Ann) am the Reporter and NPC Fae is the Trader          |
| 1           | NPC Mark | Demagog   | broadcast | I (NPC Cal) am the Thief and I have made NPC Han vulnerable    |
| 1           | NPC Mark | Demagog   | broadcast | I (NPC Ed) inspected NPC Bob and they are possessed            |
| 1           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 1           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 1           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Trader is not possessed     |
| 1           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 1           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 1           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 1           | NPC Mark | Demagog   | vote      | Demagog has initiated a vote on eliminating Inspector          |

#### Actions Round 2
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 2           | NPC Dan  | Medic    | NPC Ann  |          | successful  |
| 2           | NPC Gia  | Judge    | Assassin |          | successful  |
| 2           | NPC Igi  | Psychic  |          |          | successful  |
| 2           | NPC Jeff | Prophet  | NPC Ann  |          | successful  |
| 2           | NPC Lee  | Silencer | NPC Ann  |          | successful  |

#### States Round 2
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 2           | NPC Cal  | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Han  | Priest    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 2           | NPC Ann  | Reporter  | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Bob  | Assassin  | False      | True      | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Jeff | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Mark | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Lee  | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Ed   | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 2           | NPC Gia  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Ken  | Jailer    | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Dan  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 2           | NPC Fae  | Trader    | False      | False     | False      | 3         | True   | 0              | 0                  |
| 2           | NPC Igi  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 2
| round_index | Player   | Role      | message   | details                                                        |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------- |
| 2           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Ann  | Reporter  | silenced  | You have been silenced                                         |
| 2           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 2           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 2           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 2           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 2           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 2           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 2           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Igi  | Psychic   | reveal    | Player: NPC Han is not possessed                               |
| 2           | NPC Igi  | Psychic   | reveal    | Player: NPC Ann is not possessed                               |
| 2           | NPC Igi  | Psychic   | reveal    | Player: NPC Ed is not possessed                                |
| 2           | NPC Igi  | Psychic   | reveal    | Player: NPC Jeff is not possessed                              |
| 2           | NPC Igi  | Psychic   | reveal    | Player: NPC Dan is not possessed                               |
| 2           | NPC Igi  | Psychic   | reveal    | Player: NPC Ken is not possessed                               |
| 2           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 2           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 2           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 2           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 2           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 2           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 2           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Priest is not possessed     |
| 2           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 2           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |

#### Actions Round 3
| round_index | Player   | action    | Target 1 | Target 2 | status              |
| :-----------| :--------| :---------| :--------| :--------| :------------------ |
| 3           | NPC Ann  | Reporter  | NPC Dan  |          | successful          |
| 3           | NPC Bob  | Assassin  | Demagog  |          | successful          |
| 3           | NPC Cal  | Thief     | NPC Ken  |          | successful          |
| 3           | NPC Dan  | Medic     | NPC Bob  |          | successful          |
| 3           | NPC Ed   | Inspector | NPC Han  |          | successful          |
| 3           | NPC Gia  | Judge     | Psychic  |          | successful          |
| 3           | NPC Igi  | Psychic   |          |          | successful          |
| 3           | NPC Jeff | Prophet   | NPC Ken  |          | successful          |
| 3           | NPC Lee  | Silencer  | NPC Jeff |          | successful          |
| 3           | NPC Mark | Demagog   | Assassin |          | voting in progress  |

#### States Round 3
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 3           | NPC Cal  | Thief     | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Han  | Priest    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Ann  | Reporter  | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Bob  | Assassin  | False      | True      | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Jeff | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Mark | Demagog   | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Lee  | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 3           | NPC Ed   | Inspector | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Gia  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Ken  | Jailer    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 3           | NPC Dan  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 3           | NPC Fae  | Trader    | False      | False     | False      | 2         | True   | 0              | 0                  |
| 3           | NPC Igi  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 3
| round_index | Player   | Role      | message   | details                                                        |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------- |
| 3           | NPC Ann  | Reporter  | broadcast | I (NPC Cal) am the Thief and I have made NPC Ken vulnerable    |
| 3           | NPC Ann  | Reporter  | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed        |
| 3           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 3           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Ann  | Reporter  | reveal    | NPC Dan is Medic                                               |
| 3           | NPC Ann  | Reporter  | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Bob  | Assassin  | broadcast | I (NPC Cal) am the Thief and I have made NPC Ken vulnerable    |
| 3           | NPC Bob  | Assassin  | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed        |
| 3           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 3           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Bob  | Assassin  | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Cal  | Thief     | broadcast | I (NPC Cal) am the Thief and I have made NPC Ken vulnerable    |
| 3           | NPC Cal  | Thief     | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed        |
| 3           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 3           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Cal  | Thief     | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Dan  | Medic     | broadcast | I (NPC Cal) am the Thief and I have made NPC Ken vulnerable    |
| 3           | NPC Dan  | Medic     | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed        |
| 3           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 3           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Dan  | Medic     | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Ed   | Inspector | broadcast | I (NPC Cal) am the Thief and I have made NPC Ken vulnerable    |
| 3           | NPC Ed   | Inspector | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed        |
| 3           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 3           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Ed   | Inspector | reveal    | Priest is Innocent                                             |
| 3           | NPC Ed   | Inspector | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Fae  | Trader    | broadcast | I (NPC Cal) am the Thief and I have made NPC Ken vulnerable    |
| 3           | NPC Fae  | Trader    | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed        |
| 3           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 3           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Fae  | Trader    | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Gia  | Judge     | broadcast | I (NPC Cal) am the Thief and I have made NPC Ken vulnerable    |
| 3           | NPC Gia  | Judge     | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed        |
| 3           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 3           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Gia  | Judge     | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Han  | Priest    | broadcast | I (NPC Cal) am the Thief and I have made NPC Ken vulnerable    |
| 3           | NPC Han  | Priest    | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed        |
| 3           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 3           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Han  | Priest    | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Cal) am the Thief and I have made NPC Ken vulnerable    |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed        |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Igi  | Psychic   | reveal    | Player: NPC Ken is not possessed                               |
| 3           | NPC Igi  | Psychic   | reveal    | Player: NPC Han is not possessed                               |
| 3           | NPC Igi  | Psychic   | reveal    | Player: NPC Ann is not possessed                               |
| 3           | NPC Igi  | Psychic   | reveal    | Player: NPC Jeff is not possessed                              |
| 3           | NPC Igi  | Psychic   | reveal    | Player: NPC Cal is not possessed                               |
| 3           | NPC Igi  | Psychic   | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Jeff | Prophet   | broadcast | I (NPC Cal) am the Thief and I have made NPC Ken vulnerable    |
| 3           | NPC Jeff | Prophet   | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed        |
| 3           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 3           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Jeff | Prophet   | silenced  | You have been silenced                                         |
| 3           | NPC Jeff | Prophet   | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Ken  | Jailer    | broadcast | I (NPC Cal) am the Thief and I have made NPC Ken vulnerable    |
| 3           | NPC Ken  | Jailer    | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed        |
| 3           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 3           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Ken  | Jailer    | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Lee  | Silencer  | broadcast | I (NPC Cal) am the Thief and I have made NPC Ken vulnerable    |
| 3           | NPC Lee  | Silencer  | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed        |
| 3           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 3           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Lee  | Silencer  | vote      | Demagog has initiated a vote on eliminating Assassin           |
| 3           | NPC Mark | Demagog   | broadcast | I (NPC Cal) am the Thief and I have made NPC Ken vulnerable    |
| 3           | NPC Mark | Demagog   | broadcast | I (NPC Ed) inspected NPC Han and they are not possessed        |
| 3           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Judge is not possessed      |
| 3           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Reporter is not possessed   |
| 3           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 3           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Silencer is not possessed   |
| 3           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Jailer is not possessed     |
| 3           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 3           | NPC Mark | Demagog   | vote      | Demagog has initiated a vote on eliminating Assassin           |

#### Actions Round 4
| round_index | Player   | action   | Target 1 | Target 2 | status      |
| :-----------| :--------| :--------| :--------| :--------| :---------- |
| 4           | NPC Bob  | Assassin | Judge    |          | successful  |
| 4           | NPC Dan  | Medic    | NPC Jeff |          | successful  |
| 4           | NPC Gia  | Judge    | Thief    |          | successful  |
| 4           | NPC Igi  | Psychic  |          |          | successful  |
| 4           | NPC Jeff | Prophet  | NPC Igi  |          | successful  |
| 4           | NPC Lee  | Silencer | NPC Lee  |          | successful  |

#### States Round 4
| round_index | Player   | Role      | eliminated | possessed | vulnerable | cool_down | active | cleansed_index | last_action_index  |
| :-----------| :--------| :---------| :----------| :---------| :----------| :---------| :------| :--------------| :----------------- |
| 4           | NPC Cal  | Thief     | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Han  | Priest    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Ann  | Reporter  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Bob  | Assassin  | False      | True      | False      | 2         | True   | 0              | 0                  |
| 4           | NPC Jeff | Prophet   | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Mark | Demagog   | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Lee  | Silencer  | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Ed   | Inspector | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Gia  | Judge     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Ken  | Jailer    | False      | False     | True       | 0         | True   | 0              | 0                  |
| 4           | NPC Dan  | Medic     | False      | False     | False      | 0         | True   | 0              | 0                  |
| 4           | NPC Fae  | Trader    | False      | False     | False      | 1         | True   | 0              | 0                  |
| 4           | NPC Igi  | Psychic   | False      | False     | False      | 1         | True   | 0              | 0                  |

#### Notifications Round 4
| round_index | Player   | Role      | message   | details                                                        |
| :-----------| :--------| :---------| :---------| :------------------------------------------------------------- |
| 4           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Thief is not possessed      |
| 4           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Ann  | Reporter  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Thief is not possessed      |
| 4           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Bob  | Assassin  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Thief is not possessed      |
| 4           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Cal  | Thief     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Thief is not possessed      |
| 4           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Dan  | Medic     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Thief is not possessed      |
| 4           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Ed   | Inspector | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Thief is not possessed      |
| 4           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Fae  | Trader    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Thief is not possessed      |
| 4           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Gia  | Judge     | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Thief is not possessed      |
| 4           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Han  | Priest    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Thief is not possessed      |
| 4           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Igi  | Psychic   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Igi  | Psychic   | reveal    | Player: NPC Ann is not possessed                               |
| 4           | NPC Igi  | Psychic   | reveal    | Player: NPC Fae is not possessed                               |
| 4           | NPC Igi  | Psychic   | reveal    | Player: NPC Cal is not possessed                               |
| 4           | NPC Igi  | Psychic   | reveal    | Player: NPC Gia is not possessed                               |
| 4           | NPC Igi  | Psychic   | reveal    | Player: NPC Han is not possessed                               |
| 4           | NPC Igi  | Psychic   | reveal    | Player: NPC Jeff is not possessed                              |
| 4           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Thief is not possessed      |
| 4           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Jeff | Prophet   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Thief is not possessed      |
| 4           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Ken  | Jailer    | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Thief is not possessed      |
| 4           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Lee  | Silencer  | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |
| 4           | NPC Lee  | Silencer  | silenced  | You have been silenced                                         |
| 4           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Demagog is not possessed    |
| 4           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Medic is not possessed      |
| 4           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Thief is not possessed      |
| 4           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Prophet is not possessed    |
| 4           | NPC Mark | Demagog   | broadcast | I (NPC Igi) am the Psychic and the Inspector is not possessed  |