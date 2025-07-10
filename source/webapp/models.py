from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")


class Type(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название типа:", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Types"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Status(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Название статуса:", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Statuses"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Issue(BaseModel):
    summary = models.CharField(max_length=50, null=False, blank=False, verbose_name="Краткое Описание")
    description = models.TextField(null=True, blank=True, verbose_name="Подробное описание")
    statuses = models.ForeignKey('webapp.Status', related_name='issues', on_delete=models.PROTECT)
    types = models.ForeignKey('webapp.Type', related_name='issues', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.summary} {self.description} {self.statuses} {self.types}"

    class Meta:
        db_table = 'Issues'
        verbose_name = "Трекер задач"
        verbose_name_plural = "Трекеры задач"