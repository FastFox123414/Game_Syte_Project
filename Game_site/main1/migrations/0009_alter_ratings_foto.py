# Generated by Django 5.1.3 on 2024-12-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main1', '0008_alter_ratings_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='foto',
            field=models.ImageField(null=True, upload_to='main1/static/main1/imags', verbose_name='Картинка'),
        ),
    ]