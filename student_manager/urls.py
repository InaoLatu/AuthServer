from django.urls import path
from student_manager import views as students_manager_views

urlpatterns = [
    path('identification_telegram/<str:username>/<str:id>', students_manager_views.identification_telegram, name='identification_telegram'),
    path('identification_alexa/<str:name>/<str:last_name>/<str:birth_date>/<str:id>', students_manager_views.identification_alexa, name='identification_alexa'),
    path('check_user/<str:type>/<str:id>', students_manager_views.check_user_exists, name='check_user'),
]