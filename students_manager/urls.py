from django.urls import path
from students_manager import views as students_manager_views

urlpatterns = [
    path('signup', students_manager_views.signup, name='students_signup'),
    path('identification/<str:username>/<str:type>/<str:id>', students_manager_views.register_id, name='identification')
]