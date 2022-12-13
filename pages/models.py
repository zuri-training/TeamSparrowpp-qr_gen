from django.db import models

class QRModel(models.Model):
    url = models.URLField(max_length=200)
    