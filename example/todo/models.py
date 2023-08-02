from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField('Название', max_length=50, blank=True, null=True)
    task=models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.task}"

    class Meta:
        verbose_name='Задача'
        verbose_name_plural='Задачи'