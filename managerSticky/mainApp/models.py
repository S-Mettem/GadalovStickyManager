from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Sticky(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    # Choices field
    CHOICES_FIELD = (('link', 'link'), ('note', 'note'),
                     ('memo', 'memo'), ('TODO', 'TODO'))
    category = models.CharField(max_length=20, choices=CHOICES_FIELD)
    # -----------

    favorite = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    uuidu = models.UUIDField(
        default=uuid.uuid4, editable=False, verbose_name='uuid')

    is_public = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)
