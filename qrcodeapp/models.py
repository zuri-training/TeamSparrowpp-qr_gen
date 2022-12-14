from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

class QRModel(models.Model):
    # id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    url = models.URLField(max_length=200, default="https://google.com")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.url