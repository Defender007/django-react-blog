from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from blog.settings.base import AUTH_USER_MODEL
from apps.common.models import TImeStampedModel
from autoslug import AutoSlugField


class PostPublishedManager(models.Model):
    def get_queryset(self):
        return (
            super(PostPublishedManager, self)
            .get_deferred_fields()
            .filter(published_status=True)
        )

class Post(TImeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True,
                          blank=False, editable=False)
    author= models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=255)
    slug= AutoSlugField(populate_from="title", always_update=True, unique=True)
    content = models.TextField(_("Post Content"))
    published_status = models.BooleanField(_("Published Status"), default=False)
    
    objects=models.Manager()
    published = PostPublishedManager()
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    def save(self):
        """The title method returns a string where the first 
        character in every word is uppercase
        """
        self.title =str.title(self.title)
        self.content= str.capitalize(self.content)
        super(Post, self).save(*args, **kwargs)
        
