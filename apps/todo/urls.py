from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Todo.as_view(), name='users-index'),
]
