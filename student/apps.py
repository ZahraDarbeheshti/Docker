from django.apps import AppConfig

class StudentConfig(AppConfig):  # نام کلاس باید StudentConfig باشد
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student'  # نام اپلیکیشن باید با نام پوشه مطابقت داشته باشد
