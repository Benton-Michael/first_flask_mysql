# import function to return an instance of a connection
from mysqlconnection import connectToMySQL

# the class Friend is modeled after the friends Table 
# from the database schema first_flask

class Friend:
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # using class methods to query the database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"

        # call the connectToMySQL function with the
        # schema that is being targeted
        results = connectToMySQL('first_flask').query_db(query)

        # creating an empty list to append the instances of friends
        friends = []

        # iterate over the db results and create instances of friends
        # with cls
        
        # each row in the db is a dictionary and this will return a list
        # of dictionaries
        for friend in results:
            friends.append( cls(friend))
        return friends
