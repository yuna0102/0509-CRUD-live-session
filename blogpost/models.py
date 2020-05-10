from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    #내가 정한 이름으로 제목 표시하기