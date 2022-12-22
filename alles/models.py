from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Turi(models.Model):
    nomi = models.CharField(max_length=30)

    def __str__(self):
        return self.nomi

class Maxsulot(models.Model):
    turi = models.ForeignKey(Turi, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=50)
    malumoti = models.TextField()
    soni = models.PositiveIntegerField(default=0)
    narxi = models.PositiveIntegerField(default=0)
    aksiya = models.BooleanField(default=False)
    aksiya_n = models.PositiveIntegerField(default=0, blank=True, null=True)
    sana = models.DateField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    img = models.ImageField(upload_to='alle_images/')

    def __str__(self):
        return self.nomi

    # def get_absolute_url(self):
    #     return reverse('profil', args=[str(self.id)])