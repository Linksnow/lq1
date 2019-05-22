from django.urls import path
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetView

from . import views

app_name='account'
urlpatterns=[
    path('',views.user_login,name="user_login"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="user_logout"),
    path('register/',views.register,name="register"),
    path('myself/',views.myself,name="myself"),
    path('myself_edit/',views.myself_edit,name="myself_edit"),
    path('my_image/',views.my_image,name='my_image'),
    # path('password-change/',  ,{"post_change_redirect":"account/password-change-done"}, name='password_change'),
    # path('password-change-done/', password_change_done, name='password_change_done'),
    # path('password-reset/', PasswordResetView, {"template_name":"account/password_reset_form.html", "email_template_name":"account/password_reset_email.html",  "post_reset_redirect":"/account/password-reset-done"}, name="password_reset"),
    # path('password-reset-done/', PasswordResetDoneView, {"template_name":"account/password_reset_done.html"}, name="password_reset_done"),
    # path('password-reset-confirm/', PasswordResetConfirmView,name="password_reset_confirm"),
    # path('password-reset-complete/', PasswordResetCompleteView, {"template_name":"account/password_reset_complete.html"}, name="password_reset_complete"),
    # # path('',auth_views.login,{"template_name":"account/login.html"}),
    # # path('logout/',logout,{"template_name":"account/logout.html"},name='user_logout'),
]