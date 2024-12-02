from datetime import timedelta

from django.core.mail import send_mail
from celery import shared_task
from django.utils.timezone import now
from django.contrib.auth import get_user_model

@shared_task
def send_course_update_email(email, course_name):
    send_mail(
        subject=f'Обновление курса: {course_name}',
        message=f'Материалы курса "{course_name}" были обновлены!',
        from_email='noreply@example.com',
        recipient_list=[email],
    )



@shared_task
def deactivate_inactive_users():
    User = get_user_model()
    threshold_date = now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=threshold_date, is_active=True)
    inactive_users.update(is_active=False)