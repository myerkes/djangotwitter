from djangotwitter.settings import INSTALLED_APPS
from django.db import models
from django.contrib.auth.models import User
from crum import get_current_user

# Create your models here.
class Post(models.Model):
    post_text = models.CharField(max_length=255)
    pub_datetime = models.DateTimeField(
        auto_now=False, 
        auto_now_add=True
    )
    poster = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="user"
    )
    # If Post is reply to another post, the other post is the Origin
    origin = models.ForeignKey(
        'self',
        default = None,
        null = True, 
        blank = True,
        on_delete=models.CASCADE,
        related_name="reply"
    )
    # Reference to post that is being re-posted
    repost = models.ForeignKey(
        'self', 
        default = None,
        null = True, 
        blank = True,
        on_delete=models.CASCADE,
        related_name="post"
    )

    def __str__(self) -> str:
        return self.post_text

    def get_absolute_url(self):
        return ''

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.poster = user
        super(Post, self).save(*args, **kwargs)