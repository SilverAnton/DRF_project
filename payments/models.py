from django.db import models

from courses.models import Course
from users.models import User
from lessons.models import Lesson


class Payment(models.Model):
    PAYMENT_METHODS = (
        ("cash", "Cash"),
        ("bank_transfer", "Bank Transfer"),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь"
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name="дата оплаты")
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="оплаченный курс",
        null=True,
        blank=True,
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name="оплаченный урок",
        null=True,
        blank=True,
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="сумма оплаты"
    )
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHODS, verbose_name="способ оплаты"
    )

    def __str__(self):
        return f"{self.user.email} - {self.amount} - {self.payment_method}"

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
