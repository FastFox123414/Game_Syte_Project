# Generated by Django 5.1.3 on 2024-12-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='new',
            name='foto',
            field=models.ImageField(null=True, upload_to='', verbose_name='Картинка'),
        ),
    ]