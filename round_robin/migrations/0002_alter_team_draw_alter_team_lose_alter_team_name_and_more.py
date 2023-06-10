# Generated by Django 4.2.2 on 2023-06-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('round_robin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='draw',
            field=models.IntegerField(default=0, verbose_name='Ничья'),
        ),
        migrations.AlterField(
            model_name='team',
            name='lose',
            field=models.IntegerField(default=0, verbose_name='Поражения'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='team',
            name='win',
            field=models.IntegerField(default=0, verbose_name='Победа'),
        ),
    ]
