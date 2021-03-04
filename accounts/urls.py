from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('guidelines/', views.guidelines_view, name='guidelines'),
    path('java/', views.java_view),
    path('python/', views.python_view),
    path('aptitude/', views.aptitude_view),
    path('register/', views.register_view, name='register_url'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
