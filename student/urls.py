from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),  # نمونه URL برای لیست دانشجویان
    path('students/<int:id>/', views.student_detail, name='student_detail'),  # نمونه URL برای جزییات دانشجو
    # دیگر URLها را نیز اضافه کنید
]
