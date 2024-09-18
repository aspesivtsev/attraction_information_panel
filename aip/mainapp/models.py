from django.db import models

class Attraction(models.Model):
    name = models.CharField(max_length = 255, verbose_name = "Название аттракциона")
    height = models.IntegerField(verbose_name = "Рост", blank = True, null= True)
    age = models.IntegerField(verbose_name = "Возраст", blank = True, null= True)
    info = models.CharField(verbose_name = "Доп инфа", max_length=255, blank = True, null= True)
    picture = models.ImageField(verbose_name = "Фото", blank = True, null= True)
    active = models.BooleanField(verbose_name = "Работает", default=True, blank = False, null= False)
    order = models.IntegerField(verbose_name = "Сортировка", blank = False, default=50)

    class Meta:
        verbose_name = "Аттракцион"
        verbose_name_plural = "Аттракционы"

    def __str__(self):
        return self.name