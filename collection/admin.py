from django.contrib import admin
from trix.admin import TrixAdmin
from collection import models

@admin.register(models.Collection)
class CollectionAdmin(TrixAdmin, admin.ModelAdmin):
    trix_fields = ('content',)

@admin.register(models.Citation)
class CitationAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Modality)
class ModalityAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Upload)
class UploadAdmin(admin.ModelAdmin):
    pass
