from django.contrib import admin
from . import models


@admin.register(models.ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "displayUser",
    )
    raw_id_fields = ("author",)
