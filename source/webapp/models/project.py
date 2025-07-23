from django.db import models
from django.urls import reverse


class Project(models.Model):
    start_date = models.DateField(null=False, blank=False, verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    title = models.CharField(null=False, blank=False, verbose_name='Название', max_length=65)
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Описание")

    def get_absolute_url(self):
        return reverse("detail_project", kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        db_table = 'Projects'
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"