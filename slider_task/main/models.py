from django.db import models
from filer.fields.image import FilerImageField


class Slide(models.Model):
    name = models.CharField(max_length=255)
    image = FilerImageField(null=True, blank=True, related_name="image", on_delete=models.CASCADE)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['my_order']