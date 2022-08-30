from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from Accounts import views as user_views

urlpatterns = [
    
    # Registro
    path("register", views.register, name="register"),
    # Iniciar sesión
    path("login_user", views.login_user, name="login_user"),
    # Cerrar sesión
    path("logout_user", views.logout_user, name="logout_user"),
    # Cambiar contraseña
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='Account_Change_Password.html',
            success_url='/'
        ),
        name='change_password'
    ),
    # Olvide la contraseña
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='Account_Reset_Password.html',
             subject_template_name='Account_Reset_Subject.txt',
             email_template_name='Account_Reset_Email.html',
             success_url='login_user'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='Account_Reset_Done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='Account_Reset_Confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='Account_Reset_Success.html'
         ),
         name='password_reset_complete'),
    path('profile/', user_views.profile, name='profile'),
    # Home que renderiza el home de la tienda
    path("home", views.home, name="home")
]
