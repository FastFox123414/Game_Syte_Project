# Generated by Django 5.1.3 on 2024-12-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main1', '0006_alter_new_foto_alter_new_game_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='foto',
            field=models.ImageField(null=True, upload_to='static/main1/imags', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='new_game',
            name='foto',
            field=models.ImageField(null=True, upload_to='static/main1/imags', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='foto',
            field=models.ImageField(null=True, upload_to='static/main1/imags', verbose_name='Картинка'),
        ),
    ]
