from django.urls import path
from . import views

urlpatterns = [
    path('pacients/', views.PacientList.as_view(), name='pacient_list'),
    path('pacients/create', views.PacientAdd.as_view(), name='pacient_create'),
    path('pacients/update/<int:id>', views.PacientUpdate.as_view(), name='pacient_update'),
]