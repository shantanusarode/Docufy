from database import Database

class User:
    
    def __init__(self, username, password, name=None, DOB=None, address=None, state=None, constituency=None, mobile=None, email=None, aadhaar=None, profilePic=None, status=None):
        self.username = username
        self.password = password
        self.name = name
        self.DOB = DOB
        self.address = address
        self.state = state
        self.constituency = constituency
        self.mobile = mobile
        self.email = email
        self.aadhaar = aadhaar
        self.profilePic = profilePic
        self.status = status
    
    def json(self):
        return {
            'username': self.username,
            'password': self.password,
            'name': self.name,
            'DOB': self.DOB,
            'address': self.address,
            'state': self.state,
            'constituency': self.constituency,
            'mobile': self.mobile,
            'email': self.email,
            'aadhaar': self.aadhaar,
            'profilePic': self.profilePic,
            'status': self.status
        }

    def addUser(self):
        Database.insert(collection='users', data=self.json())

    @staticmethod
    def getUser(query={}):
        return Database.find_one(collection='users', query=query)

    @staticmethod
    def getUsers(query={}):
        return [user for user in Database.find(collection='users', query=query)]

    @staticmethod
    def updateUser(query={}, newval={}):
        return Database.update_one(collection='users', query=query, newval=newval)