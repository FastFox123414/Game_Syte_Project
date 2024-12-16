from django.db import models

class New(models.Model):
    title = models.CharField("Название", max_length=40)
    anons = models.CharField("Анонс", max_length=250)
    foto = models.ImageField("Картинка", null= True, upload_to="main1/static/imags")
    full_text  = models.TextField("Основной текст")
    date = models.DateTimeField("Дата публикайии")
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Новость"
        verbose_name_plural="Новости"