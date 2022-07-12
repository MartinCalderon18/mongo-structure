# This function will accept a user and return a dictionary with its values
def userEntity(item) -> dict:
    return {
        'id' : item['id'],
        'name': item['name'],
        'email': item['email'],
        'password' : item['password']
    }

# This function will take a list of users and then pass each one to userEntity to generate the schema
def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]