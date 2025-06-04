
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='courses'),
    path('students/', views.student_list, name='students'),
    # оптимизированный маршрут
    path('info/<str:type>/', views.general_info, name='general_info'),
]
