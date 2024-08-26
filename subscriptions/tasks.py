from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from subscriptions.models import CourseSubscription
from courses.models import Course
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from users.models import User


@shared_task
def deactivate_inactive_users():
    one_month_ago = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_active=True)

    for user in inactive_users:
        user.is_active = False
        user.save()


@shared_task
def send_course_update_emails(course_id):
    course = Course.objects.get(id=course_id)
    subscriptions = CourseSubscription.objects.filter(course=course).select_related('user')

    recipient_list = [sub.user.email for sub in subscriptions]

    if recipient_list:
        send_mail(
            subject='Обновление курса',
            message=f'Курс "{course.name}" был обновлен. Проверьте новые материалы.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
            fail_silently=False,
        )
