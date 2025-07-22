from django.db import models

from webapp.models.base_model import BaseModel


class Issue(BaseModel):
    summary = models.CharField(max_length=50, null=False, blank=False, verbose_name="Краткое Описание")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Подробное описание")
    statuses = models.ForeignKey('webapp.Status', related_name='issues', verbose_name='Статусы',
                                 on_delete=models.PROTECT)
    types = models.ManyToManyField('webapp.Type', related_name='issues', verbose_name='Типы', blank=True)

    def __str__(self):
        return f"{self.summary} {self.description} {self.statuses}"

    class Meta:
        db_table = 'Issues'
        verbose_name = "Трекер задач"
        verbose_name_plural = "Трекеры задач"