from faker import Faker


class RegistrationData:
    def __init__(self):
        fake = Faker("pl_PL")
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.date_of_birth = '01.12.2001'
        self.address = 'ul. Polna 11'
        self.country = 'PL'
        self.postal_code = '00-084'
        self.city = 'Kraków'
        self.state = 'mazowieckie'
        self.phone_number = '545555123'
        self.email = 'test@test.pl'
        self.passwd = 'testHaslo%123'

class get_csv_data:
    def get_data(self):
        pass

# Adam = RegistrationData()
# print(Adam.first_name)
