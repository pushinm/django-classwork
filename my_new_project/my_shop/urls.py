from django.urls import path
from .views import Mainpage_view

app_name = 'my_shop'

urlpatterns = [
  path('', Mainpage_view.as_view(), name='mainpage')
]