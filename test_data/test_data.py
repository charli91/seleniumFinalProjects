from faker import Faker


class RegistrationData:
    def __init__(self):
        fake = Faker("pl_PL")
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.day_of_birth = '11'
        self.month_of_birth = '02'
        self.year_of_birth = '1990'


# Adam = RegistrationData()
# print(Adam.first_name)
