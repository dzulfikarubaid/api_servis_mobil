from django.db import models

class Servis(models.Model):
    nama = models.CharField(max_length=50)
    tanggal = models.DateField()
    keluhan = models.TextField()
    def __str__(self):
        return self.nama + ' | ' + str(self.tanggal)
