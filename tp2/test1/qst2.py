
# 2.2 Execution of register_party function for MK party

last_reg_number = 10003318
new_party = [{'party_name': 'MK Party', 'reg_number': last_reg_number + 1, 'member_count': 5300}]
register_party(new_party)



# 2.4 Filtering parties with less than 1000 members using list comprehension and filter function

parties = ['ANC', 'DA', 'EFF', 'IFP', 'VF+', 'GOOD', 'ACDP', 'COPE']
filtered_parties = [party for party in parties if len(party) >= 1000]
print(filtered_parties)

# 2.5 Rewrite list comprehension into a normal list data structure

filtered_parties = list(filter(lambda party: len(party) >= 1000, parties))
print(filtered_parties)

# 2.6 Extracting records of registered voters using lambda function and filter

voters = [
    {'id': 1, 'name': 'John', 'registered': True},
    {'id': 2, 'name': 'Jane', 'registered': False},
    {'id': 3, 'name': 'Bob', 'registered': True},
]

registered_voters = list(filter(lambda voter: voter['registered'], voters))
print(registered_voters)


