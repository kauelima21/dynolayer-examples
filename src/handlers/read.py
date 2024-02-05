from models.user import User
from dotenv import load_dotenv


load_dotenv()

user = User()
users_list = user.find().fetch(True)

for user_item in users_list:
    print(user_item.first_name, user_item.genre)
    addresses = user_item.addresses()
    for address in addresses:
        print(address.street)
        # print(address.data())
