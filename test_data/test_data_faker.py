from faker import Faker
import random


class RegistrationDataFaker:
    def __init__(self):
        fake = Faker("pl_PL")
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.address = fake.street_name()
        self.country = 'PL'
        self.postal_code = fake.postalcode()
        self.city = fake.city()
        self.state = fake.administrative_unit()
        self.phone_number = random.randrange(100000000,999999999)
        # self.phone_number = phone_number
        self.email = fake.email()
        self.passwd = fake.password(8, 1, 1, 1, 1)
        data = fake.date_of_birth()
        day_birth = str(data.day)
        month_birth = str(data.month)
        year_birth = str(data.year)
        self.date_of_birth = (day_birth+month_birth+year_birth)
    #
Adam = RegistrationDataFaker()
# print(Adam.first_name)
# print(Adam.last_name)
# print(Adam.postal_code)
# print(Adam.date_of_birth)
# print(Adam.address)
# print(Adam.country)
# print(Adam.city)
print(Adam.phone_number)
# print(Adam.email)
# print(Adam.passwd)
