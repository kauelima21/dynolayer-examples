from dynolayer import DynoLayer


class Address(DynoLayer):
    def __init__(self):
        super().__init__('addresses', ['user_id'])

    def add(self, user, street: str, number: str):
        self.user_id = user.id
        self.street = street
        self.number = number

        return self
