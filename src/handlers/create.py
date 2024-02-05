from models.address import Address
from models.user import User
from dotenv import load_dotenv


load_dotenv()

user = User()
# user.find_by_id('1829b284-0c27-49ae-ae46-396dd9d312fd')
user.first_name = 'Kaue'
user.last_name = 'Leal'
user.genre = 'M'
user.save()

print(user.id)

addr = Address()
addr.add(user, 'Rua dos Bobos', '70b')
addr.save()

if user.error:
    print('user', user.error)
if addr.error:
    print('addr', addr.error)
