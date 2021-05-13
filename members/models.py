from os import name
from django.db import models
from django.db.models.base import Model


class SkillModel(models.Model):
    """Skill Model Definition"""

    skill_name = models.CharField(max_length=40)

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name_plural = "SKILLS"
