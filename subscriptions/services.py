from django.core.mail import send_mail
from django.conf import settings
from subscriptions.models import CourseSubscription
from courses.models import Course
import logging
logging.basicConfig(level=logging.DEBUG)


def send_mails():
    """
    Функция отправки рассылок
    """
    courses = Course.objects.all()  # Предполагаем, что у курса есть флаг is_subscribe

    for course in courses:
        if course.is_subscribe:  # Проверьте, что у курса включена подписка
            users = CourseSubscription.objects.filter(course=course).select_related('user')
            try:
                recipient_list = [sub.user.email for sub in users]
                send_mail(
                    subject='Новое обновление курса',
                    message="У вас новая подписка на курс: {}".format(course.name),
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Ошибка при отправке писем: {e}")
