from django.core.management import BaseCommand
from django.contrib.auth.models import Group

from users.models import User


class Command(BaseCommand):
    """Creating moderator group with moderator"""
    def handle(self, *args, **options):
        moderator_group, created = Group.objects.get_or_create(name="Moderator")
        user = User.objects.create(email='moderator@yandex.ru')
        user.is_active = True
        user.is_staff = True
        user.groups.add(moderator_group)
        user.set_password('1234')
        user.save()
        self.stdout.write(self.style.SUCCESS('Successfully created user with email: moderator@yandex.ru; password 1234'))

