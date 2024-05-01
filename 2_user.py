

#User Class
#Attributes: email, username, password
#method: user_contact (this user can be contacted at this email)

class User():

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        self.friends = []
        self.posts = {'caption': 'img_url'}
        self.best_friend = None
        self.is_admin = False

    #methods
    def user_contact(self):
        print(f'{self.username} can be contacted at {self.email}!')

    def add_friend(self, friend):
        if isinstance(friend, User):
            print(f'Adding {friend.username} to my friends list!')
            self.friends.append(friend)
        else:
            print('Invalid User')

    def friends_list(self):
        print(f'{self.username}\'s Friends List')
        print('---------------------------------')
        for friend in self.friends:
            print(friend.username)


WforWumbo = User(email='wumbo@email.com', username='wumbology', password='wstandsforwumbology')
isaias = User(email='iep@email.com', username='ipalma', password='abcdefg')
steve = User(email = "crungus@gmail.com", username = "crung", password = "us")
joshua = User('jm@mail.com', 'jmartinez', '*****')
reggie = User(email='myemail@email.com', username='rme', password='canesugar')
iryna = User('ip@gmail.com', 'IP24', "aaaaaaa")


dylan = User('dk@email.com', 'Dizzy:D', '12345')

WforWumbo.user_contact()


dylan.add_friend(WforWumbo)
dylan.add_friend(isaias)
dylan.add_friend(steve)
dylan.add_friend(joshua)
dylan.add_friend(reggie)
dylan.add_friend(iryna)
dylan.add_friend('Craig')

dylan.friends_list()

