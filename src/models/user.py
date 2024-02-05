from dynolayer import DynoLayer
from models.address import Address


class User(DynoLayer):
    def __init__(self):
        super().__init__('users', ['first_name', 'last_name'])

    def addresses(self):
        return Address().query_by('user_id', self.id, 'user_id-index').fetch(True)
