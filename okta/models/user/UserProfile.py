class UserProfile:

    types = {
        'login': str,
        'email': str,
        'secondEmail': str,
        'firstName': str,
        'lastName': str,
        'mobilePhone': str,
        'karma_points': int,
        'associations': list 
    }

    def __init__(self):

        self.login = None  # str

        self.email = None  # str

        self.secondEmail = None  # str

        self.firstName = None  # str

        self.lastName = None  # str

        self.mobilePhone = None  # str

        self.karma_points = 0  #int

        self.associations = []
        
