from django import views
from django.urls import path
from . import veiws

urlpatterns = [
    path('',views.post_list,name='post_list'),
]