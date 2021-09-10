from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone

from constants import DEPARTMENTS, SEMESTERS, METHODS


class Payment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    roll = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255)
    department = models.CharField(max_length=127, choices=DEPARTMENTS)
    semester = models.CharField(max_length=127, choices=SEMESTERS)
    method = models.CharField(max_length=127, choices=METHODS)
    account = models.CharField(max_length=127)
    amount = models.FloatField()
    transaction_id = models.CharField(max_length=255, unique=True)
    extra_transactions = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    verified = models.BooleanField(default=None, blank=True, null=True)
    pay_code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = [['roll', 'registration_number', 'department', 'semester']]
        ordering = ('created_at', 'department')

    def __str__(self):
        return f'{self.name} {self.roll} {self.department} {self.semester}'
