from django.test import TestCase

from .models import Pacient

class PacientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Pacient.objects.create(name="Diego", date_birth="1996-10-01", test_type="RT-PCR", result="P")
    
    def testName(self):
        pacient = Pacient.objects.get(id=1)
        name = pacient.name
        self.assertEquals(name, 'Diego')

    def testNameMaxLength(self):
        pacient = Pacient.objects.get(id=1)
        name_max_lenght = pacient._meta.get_field('name').max_length
        self.assertEquals(name_max_lenght, 100)