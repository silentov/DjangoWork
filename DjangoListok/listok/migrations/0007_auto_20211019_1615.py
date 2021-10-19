# Generated by Django 3.2.8 on 2021-10-19 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listok', '0006_auto_20211019_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='class_format',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='listok.classformat', verbose_name='Формат занятий'),
        ),
        migrations.AlterField(
            model_name='user',
            name='contraindications',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='listok.contraindications', verbose_name='Противопоказания'),
        ),
        migrations.AlterField(
            model_name='user',
            name='personal_disc',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Персональная скидка'),
        ),
        migrations.AlterField(
            model_name='user',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='listok.source', verbose_name='Источник'),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='listok.status', verbose_name='Статус'),
        ),
    ]
