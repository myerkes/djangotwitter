from django.db import models

# Create your models here.
class Post(models.Model):
    pub_datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    post_text = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.post_text


