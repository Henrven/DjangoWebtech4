from datetime import datetime
from django.db import models

class End(models.Model):
    date_now = models.DateTimeField(default=datetime.now())
    date_exit = models.DateTimeField(default = datetime(2019,3,29,11,0,0))

    def __str__(self):
        return self.date_now
# Create your models here.
