from django.db import models

# Create your models here.

class projects(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class instruments(models.Model):
    n_instrument=models.CharField(max_length=200)
    project=models.ForeignKey(projects,on_delete=models.CASCADE)

    def __str__(self):
        return self.n_instrument

class study(models.Model):
    
    SEASON_CHOICES=[
        ('humeda','húmeda'),
        ('seca','seca'),
        ('fria','fría'),
        ('calida','cálida'),
        ('transicion','transición')
    ]

    TAXON_CHOICES=[
        ('plantas','Plantas'),
        ('mamiferos','Mamíferos'),
        ('aves','Aves'),
        ('anfibios','Anfibios'),
        ('reptiles','Reptiles')
    ]
    
    COUNTRY_CHOICES=[
        ('Peru', 'Perú'),
    ]
    instrument=models.OneToOneField(instruments,on_delete=models.CASCADE)
    n_study=models.CharField(max_length=50)
    t_study=models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    season=models.CharField(max_length=20,choices=SEASON_CHOICES)
    n_specialist=models.CharField(max_length=100)
    country=models.CharField(max_length=10,choices=COUNTRY_CHOICES)
    taxon=models.CharField(max_length=20,choices=TAXON_CHOICES)
    field = models.FileField(upload_to='studies/', blank=True, null=True)

    def __str__(self):
        return self.n_study