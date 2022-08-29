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
            template_name='HWStoreChangePass.html',
            success_url='/'
        ),
        name='change_password'
    ),
    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='HWStoreResetPass.html',
             subject_template_name='HWStoreResetSubject.txt',
             email_template_name='HWStoreResetEmail.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='HWStoreResetDone.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='HWStoreResetConfirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='HWStoreResetSuccess.html'
         ),
         name='password_reset_complete'),
    path('profile/', user_views.profile, name='profile'),
    
    path("home", views.home, name="home")
]
