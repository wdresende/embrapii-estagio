from rest_framework import generics
from .models import Pacient
from .serializers import PacientSerializer


class PacientList(generics.ListCreateAPIView):

    queryset = Pacient.objects.all()
    serializer_class = PacientSerializer

class PacientAdd(generics.CreateAPIView):

    queryset = Pacient.objects.all()
    serializer_class = PacientSerializer

class PacientUpdate(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pacient.objects.all()
    serializer_class = PacientSerializer
    lookup_field = 'id'
