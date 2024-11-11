from django.core.management.base import BaseCommand
from users.models import Payment
from django.contrib.auth import get_user_model
from lms.models import Course, Lesson
from decimal import Decimal
from datetime import date

User = get_user_model()

class Command(BaseCommand):
    help = 'Создает пользователей и добавляет записи в таблицу Payment'

    def handle(self, *args, **kwargs):
        # Создаем пользователей и добавляем им оплату
        user1, created1 = User.objects.get_or_create(
            email="user1@example.com",
            defaults={
                "password": "password123",
                "phone": "1234567890",
                "city": "City1"
            }
        )
        user2, created2 = User.objects.get_or_create(
            email="user2@example.com",
            defaults={
                "password": "password123",
                "phone": "0987654321",
                "city": "City2"
            }
        )


        course1 = Course.objects.get(pk=1)
        lesson1 = Lesson.objects.get(pk=1)

        # Добавляем платежи
        payments = [
            Payment(user=user1, payment_date=date(2024, 1, 1), course=course1, amount=Decimal('500.00'), payment_method='cash'),
            Payment(user=user2, payment_date=date(2024, 1, 2), lesson=lesson1, amount=Decimal('200.00'), payment_method='transfer'),
        ]

        Payment.objects.bulk_create(payments)
        self.stdout.write(self.style.SUCCESS('Пользователи и записи успешно добавлены'))
