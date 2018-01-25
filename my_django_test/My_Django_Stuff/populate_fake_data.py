import os
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'My_Django_Stuff.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, Topic, Webpage, UserInfo
fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def add_user():
    fake_name = fakegen.name()
    fake_phone_number = fakegen.phone_number()
    user  = UserInfo.objects.get_or_create(name=fake_name, phone_number=fake_phone_number)[0]
    user.save()
    return user;


def populate(n=5):
    for entry in range(n):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]


def populate_users(n=10):
    for _ in range(n):
        fake_name = fakegen.name()
        fake_email = fakegen.email()
        user = UserInfo.objects.get_or_create(name=fake_name, email=fake_email)[0]
        user.save()


if __name__ == '__main__':
    """
    print('populating fake data')
    populate(20)
    print('populating complete')
    """

    populate_users()
