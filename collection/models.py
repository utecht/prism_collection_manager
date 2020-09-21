from django.db import models
from trix.fields import TrixField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20, unique=True)
    content = TrixField('Content')
    citations = models.ManyToManyField('Citation', blank=True)
    uploads = models.ManyToManyField('Upload', blank=True)
    modalities = models.ManyToManyField('Modality', blank=True)
    participant_count = models.IntegerField(blank=True, null=True)
    study_count = models.IntegerField(blank=True, null=True)
    series_count = models.IntegerField(blank=True, null=True)
    image_count = models.IntegerField(blank=True, null=True)
    image_size = models.FloatField(blank=True, null=True)
    def modality_list(self):
        return ', '.join([m.short for m in self.modalities.all()])
    def __str__(self):
        return self.name

class Modality(models.Model):
    short = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.short

class Citation(models.Model):
    line = models.TextField()
    link = models.CharField(max_length=2000)
    class CitationType(models.TextChoices):
        DATAC = 'DC', _('Data Citation')
        PUBC = 'PC', _('Publication Citation')
        TCIAC = 'TC', _('TCIA Citation')
    citation_type = models.CharField(
        max_length=2,
        choices=CitationType.choices,
        default=CitationType.PUBC
    )
    def __str__(self):
        return self.line[:30]

class Upload(models.Model):
    file = models.FileField(upload_to='uploads/')
    description = models.TextField(blank=True)
    updated = models.TimeField(auto_now=True)
    def __str__(self):
        return self.file.name
