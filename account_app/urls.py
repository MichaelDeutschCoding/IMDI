from django.urls import path, include
from account_app import views


accounts_patterns = ([
    path('signup', views.signup, name='signup'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile'),
], 'accounts')

urlpatterns = [
    path('', include(accounts_patterns)),
]