# Generated by Django 3.2.13 on 2022-04-18 17:49

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sveden', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childitemprop',
            name='header',
            field=models.CharField(help_text='Подпись к единице информации', max_length=255),
        ),
        migrations.AlterField(
            model_name='childitemprop',
            name='item_prop',
            field=models.CharField(help_text='Дочерний тег', max_length=255),
        ),
        migrations.AlterField(
            model_name='childitemprop',
            name='parent',
            field=models.ForeignKey(help_text='Главный тег', on_delete=django.db.models.deletion.CASCADE, to='sveden.itemprop'),
        ),
        migrations.AlterField(
            model_name='childitemprop',
            name='show_position',
            field=models.PositiveIntegerField(help_text='Позиция дочернего тега при выводе'),
        ),
        migrations.AlterField(
            model_name='childitemprop',
            name='value_position',
            field=models.PositiveIntegerField(help_text='Индекс под которым хранится данные с тегом'),
        ),
        migrations.AlterField(
            model_name='itemprop',
            name='container',
            field=models.OneToOneField(help_text='Контейнер с данными', on_delete=django.db.models.deletion.CASCADE, to='sveden.itempropcontainer'),
        ),
        migrations.AlterField(
            model_name='itemprop',
            name='item_prop',
            field=models.CharField(help_text='Главный тег', max_length=255),
        ),
        migrations.AlterField(
            model_name='itempropcontainer',
            name='header',
            field=models.CharField(help_text='Подпись к данным', max_length=255),
        ),
        migrations.AlterField(
            model_name='itempropcontainer',
            name='is_generated',
            field=models.BooleanField(default=False, help_text='Флаг, что данные заполняются автоматически'),
        ),
        migrations.AlterField(
            model_name='itempropcontainer',
            name='subsection',
            field=models.ForeignKey(help_text='Подраздел', null=True, on_delete=django.db.models.deletion.CASCADE, to='sveden.subsection'),
        ),
        migrations.AlterField(
            model_name='itempropcontainer',
            name='values',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None), default=list, help_text='Данные', size=None),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='header',
            field=models.CharField(help_text='Название подраздела', max_length=255),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='url',
            field=models.CharField(help_text='Адрес подраздела', max_length=255, unique=True),
        ),
    ]
