# Generated by Django 3.2.8 on 2021-10-19 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listok', '0003_auto_20211018_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cf', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contraindications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=255, verbose_name='ФИО')),
                ('gender', models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], max_length=1, verbose_name='Пол')),
                ('number', models.CharField(max_length=30, verbose_name='Телефон')),
                ('number2', models.CharField(blank=True, max_length=30, verbose_name='Телефон (альтернативный)')),
                ('birthday_date', models.DateTimeField(verbose_name='Год рождения')),
                ('adres', models.CharField(max_length=255, verbose_name='Адрес')),
                ('code', models.CharField(max_length=255, verbose_name='Штрих-код')),
                ('family_field', models.CharField(blank=True, max_length=255, verbose_name='Карточка родителя')),
                ('FIO_family', models.CharField(blank=True, max_length=255, verbose_name='ФИО роидтеля')),
                ('number_family', models.CharField(max_length=255, verbose_name='Телефон родителя')),
                ('email', models.CharField(blank=True, max_length=255, verbose_name='Email')),
                ('ab_status', models.CharField(max_length=255, verbose_name='Статус абонемента')),
                ('blacklist', models.CharField(choices=[('Н', 'Нет'), ('Д', 'Да')], max_length=1, verbose_name='Черный список')),
                ('personal_disc', models.PositiveSmallIntegerField(blank=True)),
                ('Vk_id', models.CharField(blank=True, max_length=255, verbose_name='Вконтакте ID')),
                ('Fb_id', models.CharField(blank=True, max_length=255, verbose_name='Facebook ID')),
                ('Ig_id', models.CharField(blank=True, max_length=255, verbose_name='Instagramm ID')),
                ('sms', models.CharField(choices=[('Е', 'Есть разрешение'), ('Н', 'Нет разрешения')], max_length=1, verbose_name='Отправка сообщений')),
                ('email_choise', models.CharField(choices=[('Е', 'Есть разрешение'), ('Н', 'Нет разрешения')], max_length=1, verbose_name='Отправка Email')),
                ('notes_unvi', models.TextField(blank=True, max_length=1000, verbose_name='Заметки')),
                ('notes_visible', models.TextField(blank=True, max_length=500, verbose_name='Заметки (видимые)')),
                ('passport', models.PositiveIntegerField(verbose_name='Номер и серия паспорта')),
                ('passport_date', models.DateTimeField(verbose_name='Дата выдачи паспорта')),
                ('passport_org', models.CharField(max_length=255, verbose_name='Кем выдан')),
                ('org_code', models.CharField(max_length=20, verbose_name='Дата выдачи')),
                ('class_format', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='listok.classformat', verbose_name='Формат занятий')),
                ('contraindications', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='listok.contraindications', verbose_name='Противопоказания')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='listok.source', verbose_name='Источник')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='listok.status', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.DeleteModel(
            name='Abonements',
        ),
    ]
