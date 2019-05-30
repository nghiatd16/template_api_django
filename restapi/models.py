from django.db import models
from django.conf import settings
from uuid import uuid4
# Create your models here.

class Video(models.Model):
    url = models.URLField()
    status = models.IntegerField(default=0)
    # note status
    # -1: download video failed
    # -2: processing video failed
    # 0: new object
    # 1: downloading video
    # 2: processing video
    # 3: done
    filename = models.CharField(max_length=36, default=uuid4().__str__())
