from __future__ import print_function
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gfgp_db.settings")
django.setup()
import sys
from survey.models import Survey, SurveyArea, SurveyQuestion, SurveySection
from faker import Faker
import random
import time


fake = Faker()
fake.seed()


def seed_survey(num_entries=10, overwrite=False):

    if overwrite:
        print("Overwriting Fake Surveys")
        try:
            Survey.objects.all().delete()
            print("Surveys overwrited successfully")
        except:
            print("Problem in overwriting survey")

    count = 0
    for _ in range(num_entries):
        fake_survey_name = fake.name()
        is_selected = fake.boolean()
        s = Survey.objects.create(
            name=fake_survey_name,
            is_active=is_selected
        )
        s.save()
        count += 1
        percentage_complete = count / num_entries * 100
        print("Adding {} new surveys: {:.2f}%".format(num_entries, percentage_complete), end='\r')
        sys.stdout.flush()

    print()


def seed_survey_area(num_entries=10, overwrite=False):

    if overwrite:
        print("Overwriting Fake Survey Area")
        try:
            SurveyArea.objects.all().delete()
            print("Survey areas overwrited successfully")
        except:
            print("Problem in overwriting survey areas")

    count = 0
    for _ in range(num_entries):
        fake_survey_area_name = fake.street_name()
        fake_survey_area_number = fake.random_int(min=0, max=99)
        s = SurveyArea.objects.create(
            name=fake_survey_area_name,
            number=fake_survey_area_number
        )
        s.save()
        count += 1
        percentage_complete = count / num_entries * 100
        print("Adding {} new survey areas: {:.2f}".format(num_entries, percentage_complete), end='\r')
        sys.stdout.flush()

    print()


def seed_survey_section(num_entries=10, overwrite=False):

    if overwrite:
        print("Overwriting survey sections")
        try:
            SurveySection.objects.all().delete()
            print("Overwrited survey sections")
        except:
            print("Problem in overwriting survey sections")

    count = 0
    for _ in range(num_entries):
        pass


def seed_survey_question(num_entries=10, overwrite=False):

    if overwrite:
        print("Overwriting survey sections")
        try:
            SurveyQuestion.objects.all().delete()
            print("Overwrited survey questions")
        except:
            print("Problem in overwriting survey questions")

    count = 0
    for _ in range(num_entries):
        pass
