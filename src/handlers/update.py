from models.user import User
from dotenv import load_dotenv


load_dotenv()

user = User().find_by_id('a3834206-ec64-4cd0-84ed-668c8ccbbd1d')
user.genre = 'F'
user.save()
