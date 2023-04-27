from django.db import models

# Create your models here.

OSZTALY_CHOICES = (
    ("0", "SZF1A"),
    ("1", "SZF1B"),
    ("2", "SZF2"),
    ("3", "nSZF1A"),
    ("4", "nSZF1B")
)

STATUS_CHOICES = (
    ("Jóvahagyásra vár", "Jóvahagyásra vár"),
    ("Jóváhagyott", "Jóváhagyott")
)



class Tevekenyseg(models.Model):
    tevekenyseg_id = models.AutoField(primary_key= True, editable= False)
    tevekenyseg_nev = models.CharField(max_length=100, unique= True, verbose_name="Tevékenység neve")
    pontszam = models.IntegerField(verbose_name="Pontszám")

    def __str__(self):
        return self.tevekenyseg_nev
    


class Bejegyzes(models.Model):
    tevekenyseg_id = models.ForeignKey(Tevekenyseg, on_delete= models.CASCADE, verbose_name="Tevékenység")
    osztaly_id = models.CharField(max_length=10, choices=OSZTALY_CHOICES, verbose_name="Osztály")
    allapot = models.CharField(max_length=30, choices=STATUS_CHOICES, default="Jóváhagyásra vár", verbose_name="Állapot")

    def __str__(self) -> str:
        return f"{self.tevekenyseg_id} | {self.osztaly_id} | {self.allapot}"