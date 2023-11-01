from django.urls import path
from .views import home,login,validate

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('validate/', validate, name='validate'),
]