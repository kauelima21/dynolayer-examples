from models.address import Address
from models.user import User
from dotenv import load_dotenv


load_dotenv()

user = User()
users = user.find().fetch(True)

# for item in users:
#     item.destroy()

address = Address()
addresses = address.find().fetch(True)

# for item in addresses:
#     item.destroy()
