from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)  # تاریخ تولد
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد
    updated_at = models.DateTimeField(auto_now=True)  # تاریخ به‌روزرسانی

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
