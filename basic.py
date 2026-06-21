# login

# class
class Signup_or_Signin:
    def __init__(self, user_name, password):
        # variables
        self.user_name = user_name
        self.password = password

    def login(self):
        if self.user_name == 'Alif' and self.password == 1234:
            print('Yes, are logged in')
        else:
            print("Sorry the username or password is wrong")
        
    def signup(self):
        if self.user_name != None and self.password != None:
            print('You account is created successfully.')
        else:
            print("Sorry, give a valid username or password")

def demo():
    print('This is a demo.')
    
signup = Signup_or_Signin('Alif', 1234)
user2 = Signup_or_Signin('Bob', 12345)
user3 = Signup_or_Signin('Chris', 'abc123')

print(user2.password)
print(user3.password)
print(user2.user_name)
