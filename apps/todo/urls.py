from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Todo.as_view(), name='users-index'),
    url(r'^contacted_patient$', views.PatientContact.as_view(), name="contacted_patient"),
]
