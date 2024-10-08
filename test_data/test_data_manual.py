import csv


class RegistrationDataManual:
    def __init__(self):
        self.first_name = 'Monika'
        self.last_name = 'Testowa'
        self.date_of_birth = '01.12.2001'
        self.address = 'ul. Polna 11'
        self.country = 'PL'
        self.postal_code = '00-084'
        self.city = 'Kraków'
        self.state = 'mazowieckie'
        self.phone_number = '545555123'
        self.email = 'test@test.pl'
        self.passwd = 'testHaslo%123'


# Adam = RegistrationData()
# print(Adam.first_name)


def get_csv_data(filename):
    rows = []
    data_file = open(filename, "r")
    reader = csv.reader(data_file)
    # skipping row with headers
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows
