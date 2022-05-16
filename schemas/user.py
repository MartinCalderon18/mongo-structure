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
    [userEntity() for item in usersEntity]