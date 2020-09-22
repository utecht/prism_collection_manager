from django.db import models
from trix.fields import TrixField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200, unique=True)
    content = TrixField('Content')
    citations = models.ManyToManyField('Citation', blank=True)
    def image_collections(self):
        return ImageCollection.objects.filter(collection=self)
    def modality_list(self):
        modalities = []
        for ic in self.image_collections():
            for mod in ic.modalities.all():
                if mod not in modalities:
                    modalities.append(mod.short)
        return ', '.join(modalities)
    def participant_count(self):
        return max([ic.participant_count for ic in self.image_collections()])
    def study_count(self):
        return sum([ic.study_count for ic in self.image_collections()])
    def image_count(self):
        return sum([ic.image_count for ic in self.image_collections()])
    def image_size(self):
        return sum([ic.image_size for ic in self.image_collections()])
    def versions(self):
        return DownloadVersion.objects.filter(collection=self).order_by('-version')
    def __str__(self):
        return self.name

class ImageCollection(models.Model):
    name = models.CharField(max_length=200)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    modalities = models.ManyToManyField('Modality', blank=True)
    participant_count = models.IntegerField(blank=True, null=True)
    study_count = models.IntegerField(blank=True, null=True)
    series_count = models.IntegerField(blank=True, null=True)
    image_count = models.IntegerField(blank=True, null=True)
    image_size = models.FloatField(blank=True, null=True)
    def modality_list(self):
        return ', '.join([m.short for m in self.modalities.all()])
    def __str__(self):
        return '{} {}'.format(self.collection, self.name)

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
        return self.line[:200]

class DownloadVersion(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    version = models.IntegerField()
    updated = models.TimeField(auto_now=True)
    def downloads(self):
        return Download.objects.filter(version=self)
    def __str__(self):
        return "{} v{}".format(self.collection, self.version)
    class Meta:
        unique_together = ['collection', 'version']

class Download(models.Model):
    file = models.FileField(upload_to='uploads/', blank=True)
    version = models.ForeignKey(DownloadVersion, on_delete=models.CASCADE)
    download_link = models.CharField(max_length=200, blank=True)
    nbia_search = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    updated = models.TimeField(auto_now=True)
    def __str__(self):
        return "{} {}".format(self.file.name, self.download_link)
