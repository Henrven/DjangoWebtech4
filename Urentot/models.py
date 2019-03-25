from datetime import datetime
from django.db import models

class End(models.Model):
    date_exit = models.DateTimeField(default=lambda: datetime(2019,3,29,11,0,0).__add__(-datetime.now()))

    def __str__(self):
        return self.date_exit
# Create your models here.
