from django.contrib.auth.models import AbstractUser
from django.db import models
from courses.models import Course
from lessons.models import Lesson



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=100, verbose_name='phone', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', null=True, blank=True)
    country = models.CharField(max_length=150, verbose_name='country', null=True, blank=True)
    token = models.CharField(max_length=100, verbose_name='token', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='is_active status',null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"




class Payment(models.Model):
    PAYMENT_METHODS = (
        ('cash', 'Cash'),
        ('bank_transfer', 'Bank Transfer'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='оплаченный курс', null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='оплаченный урок', null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, verbose_name='способ оплаты')

    def __str__(self):
        return f"{self.user.email} - {self.amount} - {self.payment_method}"

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

