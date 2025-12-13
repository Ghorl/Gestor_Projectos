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