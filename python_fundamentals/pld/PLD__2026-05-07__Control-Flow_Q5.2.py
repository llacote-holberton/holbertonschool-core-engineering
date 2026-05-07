#!/usr/bin/env python3
# Creating invitations list to a wine tastery
# Consider users is a dictionary with strings "id" as key, plain objects as values with "name", "age", "email"
# WARNING: avoid putting mutable objects as fallback parameter value
def getList_AdultUsers(users=None):
    # DO NOT USE 'list' as it is a reserved keyword (for the related data type)
    adult_users = {}
    # Equivalent short-hand: if not(users): return {}
    if (users == None or len(users) == 0):
        return adult_users
    # Don't forget to use the .items() to get a list!!
    # WARNING: same with 'id', reserved keyword
    for user_id, user_infos in users.items():
        # Syntax var.member is ONLY for OBJECTS! -> user_infos.active CANNOT WORK.
        if not (user_infos['active']):
            continue
        if not (user_infos['email'] or user_infos['email'] == ""):
            continue
        if (user_infos['age'] < 18):
            continue
        adult_users[user_id] = user_infos['email']
    return adult_users

users = {
   1: {"name": "Alice", "active": True, "age": 15, "email": "alice@mail.com"},
   2: {"name": "Bob", "active": False, "age": 23, "email": "bob@mail.com"},
   3: {"name": "Charlie", "active": True, "age": 13, "email": ""},
   4: {"name": "Pauch Tron", "active": True, "age": 65, "email": "alwaysreadytodrink@picole.com"},
}

print(getList_AdultUsers(users))
