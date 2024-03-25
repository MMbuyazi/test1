def register_party(parties, new_party):

    
    min_member_count = 0
    max_member_count = 1000

    if min_member_count <= new_party['member_count'] <= max_member_count:
        parties.append(new_party)
        return True
    else:
        return False


