from django.urls import path
from . import views

urlpatterns = [
    path('', views.PacientList.as_view(), name='pacient_list'),
    path('create', views.PacientAdd.as_view(), name='pacient_create'),
    path('update/<int:id>', views.PacientUpdate.as_view(), name='pacient_update'),
]