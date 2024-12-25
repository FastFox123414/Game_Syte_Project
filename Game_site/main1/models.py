from django.db import models

class New(models.Model):
    title = models.CharField("Название", max_length=40)
    anons = models.CharField("Анонс", max_length=250)
    foto = models.ImageField("Картинка", null= True, upload_to="static/main1/imags")
    full_text  = models.TextField("Основной текст")
    date = models.DateTimeField("Дата публикайии")
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Новость"
        verbose_name_plural="Новости"
        
class New_Game(models.Model):
    title = models.CharField("Название игры", max_length=20)
    foto = models.ImageField("Картинка", null= True, upload_to="static/main1/imags")
    full_text  = models.CharField("Небольшое описание",max_length=40)
    date = models.DateTimeField("Дата анонса")
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Новинки"
        verbose_name_plural="Новинки"
        
class Reviews(models.Model):
    title = models.CharField("Название игры", max_length=30)
    foto = models.ImageField("Картинка", null= True, upload_to="static/main1/imags")
    full_text  = models.TextField("Описание")
    link = models.TextField("Ссылка на видео")
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Обзор"
        verbose_name_plural="Обзоры"
        
class Ratings(models.Model):
    title = models.CharField("Название игры",max_length=40)
    foto = models.ImageField("Картинка", null= True, upload_to="main1/static/main1/imags")
    full_text  = models.CharField("Небольшое описание",max_length=40)
    rating= models.FloatField("Оценка до 2 знаков после запятой")
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Рейтинги"
        verbose_name_plural="Рейтинги"
        


        
        