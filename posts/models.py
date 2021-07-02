from django.db import models

# Create your models here.
class Post(models.Model):
    post_text = models.CharField(max_length=255)
    pub_datetime = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.post_text

    def get_absolute_url(self):
        return ''


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=255)
    pub_datetime = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.reply_text