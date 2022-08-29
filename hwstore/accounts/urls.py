from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('ClienteRegistro/', views.ClienteRegistro.as_view(), name='ClienteRegistro'),
    path('EmpleadoRegistro/', views.EmpleadoRegistro.as_view(), name='EmpleadoRegistro')
]