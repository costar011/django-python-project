from django.contrib import admin
from . import models


@admin.register(models.SkillModel)
class SkillModel(admin.ModelAdmin):
    pass
