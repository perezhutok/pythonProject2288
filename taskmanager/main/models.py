from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=200)
    task = models.TextField('Описание')
    image_url = models.URLField(default="https://images.nplod.ru/gen_images_3/pbL0X0WmoV99X8lL7MSp2ZoZ0E3DEnaH_sm.jpg")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'