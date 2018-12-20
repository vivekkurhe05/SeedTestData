from __future__ import print_function
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gfgp_db.settings")
django.setup()
import sys
from users.models import User, Organisation
from faker import Faker
import random
import time

fake = Faker()
fake.seed_instance(1)


def seed_organisations(num_entries=10, overwrite=True):

    if overwrite:
        print("Overwriting fake organisations")
        Organisation.objects.all().delete()

    count = 0
    for _ in range(num_entries):
        legalname = fake.company()
        address = fake.address()
        city = fake.city()
        size_index = fake.random_int(min=0, max=3)
        expenditure_index = fake.random_int(min=0, max=3)

        org = Organisation.objects.create(
            legal_name=legalname,
            address_1=address,
            city=city,
            size=Organisation.SIZE[size_index][0],
            annual_expenditure=Organisation.ANNUAL_EXPENDITURE[expenditure_index][0]
        )
        org.save()
        count += 1
        percentage_complete = count / num_entries * 100

        print("Adding {} new organisations: {:.2f}%".format(num_entries, percentage_complete), end='\r')
        sys.stdout.flush()

    print()


def seed_users(num_entries=10, overwrite=True):

    if overwrite:
        print("Overwriting fake users")
        User.objects.all().delete()

    count = 0
    for _ in range(num_entries):
        name = fake.name()
        usermobile = fake.phone_number()
        jobrole = fake.company_suffix()
        org = list(Organisation.objects.all())

        u = User.objects.create(
            name=name,
            user_mobile=usermobile,
            job_role=jobrole,
            organisation=random.choice(org)
        )
        u.save()
        count += 1
        percentage_complete = count / num_entries * 100

        print("Adding {} new Users: {:.2f}%".format(num_entries, percentage_complete), end='\r')
        sys.stdout.flush()

    print()


def seed_all():

    start_time = time.time()
    seed_organisations(num_entries=10, overwrite=True)
    seed_users(num_entries=20, overwrite=False)

    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Script Execution took: {} minutes {} seconds".format(minutes, seconds))


seed_all()
print('Data populated successfully')
