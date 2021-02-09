voting_data = []
voting_data.append({"county" : "Araphoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
voting_data.insert(1,{"county": "El Paso", "registered_voters" : 461149})
voting_data.pop(0)
voting_data.insert(3,{"county":"Denver", "registered_voters": 463353})
voting_data.pop(1)
voting_data.append({"county" : "Araphoe", "registered_voters": 422829})






print(voting_data)