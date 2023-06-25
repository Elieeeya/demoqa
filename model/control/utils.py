from faker import Faker
import random


class FakeUser:
    fake = Faker("en_US")
    fake_login = fake.name()
    fake_email = fake.email()
    fake_address = fake.address()
