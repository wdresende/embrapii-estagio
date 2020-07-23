from django.db import models

class Pacient(models.Model):
    TEST_TYPES_CHOICES = (
        ("RT-PCR", "RT-PCR"),
        ("Sorologia", "Sorologia"),
        ("Teste Rápido - Antígenos", "Teste Rápido - Antígenos"),
        ("Teste Rápido - Anticorpos", "Teste Rápido - Anticorpos"),
    )

    TEST_RESULT_CHOICES = (
        ("P", "Positivo"),
        ("N", "Negativo"),
    )

    name = models.CharField('Nome', max_length=100)
    date_birth = models.DateField('Data de Nascimento')
    test_type = models.CharField('Tipo de Teste', max_length=26, choices=TEST_TYPES_CHOICES)
    result = models.CharField('Resultado', max_length=25, choices=TEST_RESULT_CHOICES)

    def __str__(self):
        return self.name