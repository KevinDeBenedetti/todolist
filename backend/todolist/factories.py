import factory
from todolist.models import Task
from django.contrib.auth.models import User
from faker import Faker
import random

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda x: fake.user_name())
    email = factory.LazyAttribute(lambda x: fake.email())
    password = factory.PostGenerationMethodCall('set_password', 'password123')

class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = factory.LazyAttribute(lambda x: fake.sentence(nb_words=5))
    description = factory.LazyAttribute(lambda x: fake.paragraph(nb_sentences=3))
    completed = factory.LazyAttribute(lambda x: random.choice([True, False]))
    due_date = factory.LazyAttribute(lambda x: fake.future_date(end_date='+30d'))
    assigned_to = factory.SubFactory(UserFactory)