from django.db import models

# Las 8 artes clásicas/contemporáneas para el perfil del usuario
# Campo de tipo CHOICE para que el usuario seleccione una opción.
ARTES_CHOICES = [
    ('arquitectura',    'Arquitectura'),
    ('escultura',       'Escultura'),
    ('pintura',         'Pintura'),
    ('musica',          'Música'),
    ('literatura',      'Literatura / Poesía'),
    ('danza',           'Danza'),
    ('teatro',          'Teatro'),
    ('cine',            'Cine / Audiovisual'),
]

class normalUser(models.Model):
    name = models.CharField(max_length=120, verbose_name="Nombre completo")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    phone_number = models.CharField(blank=True, null=True, max_length=20, verbose_name="Teléfono")
    password = models.CharField(max_length=128, default="", verbose_name="Contraseña")
    fav_art = models.CharField(max_length=30, choices=ARTES_CHOICES, verbose_name="Arte favirito")
    city = models.CharField(blank=True, null=True, max_length=50, verbose_name="Ciudad residencia")