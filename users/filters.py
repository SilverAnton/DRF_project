import django_filters
from users.models import Payment
from courses.models import Course
from lessons.models import Lesson


class PaymentFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(field_name='date')
    course = django_filters.ModelChoiceFilter(queryset=Course.objects.all(), field_name='course')
    lesson = django_filters.ModelChoiceFilter(queryset=Lesson.objects.all(), field_name='lesson')
    payment_method = django_filters.ChoiceFilter(choices=Payment.PAYMENT_METHODS)

    class Meta:
        model = Payment
        fields = ['date', 'course', 'lesson', 'payment_method']
