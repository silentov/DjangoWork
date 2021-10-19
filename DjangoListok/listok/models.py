from django.db import models


class Status(models.Model):
    st = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.st}'


class Source(models.Model):
    sr = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.sr}'


class ClassFormat(models.Model):
    cf = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.cf}'


class Contraindications(models.Model):
    cd = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.cd}'


class User(models.Model):

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ['ab_status']

    gender_choise = (
        ('М', 'Мужской'),
        ('Ж', 'Женский')
    )

    blacklist_choise = (
        ('Н', 'Нет'),
        ('Д', 'Да')
    )

    sms_choise = (
        ('Е', 'Есть разрешение'),
        ('Н', 'Нет разрешения')
    )

    FIO = models.CharField(max_length=255, verbose_name='ФИО')
    gender = models.CharField(max_length=1, choices=gender_choise, verbose_name='Пол')
    number = models.CharField(max_length=30, verbose_name='Телефон')
    number2 = models.CharField(max_length=30, verbose_name='Телефон (альтернативный)', blank=True)
    birthday_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата рождения')
    adres = models.CharField(max_length=255, verbose_name='Адрес', blank=True)
    code = models.CharField(max_length=255, verbose_name='Штрих-код')
    family_field = models.CharField(max_length=255, verbose_name='Карточка родителя', blank=True)
    FIO_family = models.CharField(max_length=255, verbose_name='ФИО роидтеля', blank=True)
    number_family = models.CharField(max_length=255, verbose_name='Телефон родителя', blank=True)
    email = models.CharField(max_length=255, verbose_name='Email', blank=True)
    status = models.ForeignKey('Status', verbose_name='Статус', on_delete=models.PROTECT, blank=True, null=True)
    ab_status = models.CharField(max_length=255, verbose_name='Статус абонемента')      # придумать метод и формат поля
    blacklist = models.CharField(max_length=1, verbose_name='Черный список', choices=blacklist_choise)
    source = models.ForeignKey('Source', verbose_name='Источник', on_delete=models.PROTECT, blank=True, null=True)
    class_format = models.ForeignKey('ClassFormat', verbose_name='Формат занятий', on_delete=models.PROTECT, blank=True, null=True)
    personal_disc = models.PositiveSmallIntegerField(verbose_name='Персональная скидка', blank=True, null=True)
    Vk_id = models.CharField(max_length=255, verbose_name='Вконтакте ID', blank=True)
    Fb_id = models.CharField(max_length=255, verbose_name='Facebook ID', blank=True)
    Ig_id = models.CharField(max_length=255, verbose_name='Instagramm ID', blank=True)
    contraindications = models.ForeignKey('Contraindications', verbose_name='Противопоказания', on_delete=models.PROTECT,
                                          blank=True, null=True)
    sms = models.CharField(max_length=1, verbose_name='Отправка сообщений', choices=sms_choise)
    email_choise = models.CharField(max_length=1, verbose_name='Отправка Email', choices=sms_choise)
    notes_unvi = models.TextField(max_length=1000, verbose_name='Заметки', blank=True)
    notes_visible = models.TextField(max_length=500, verbose_name='Заметки (видимые)', blank=True)
    passport = models.PositiveIntegerField(verbose_name='Номер и серия паспорта')
    passport_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата выдачи паспорта')
    passport_org = models.CharField(max_length=255, verbose_name='Кем выдан')
    org_code = models.CharField(max_length=20, verbose_name='Дата выдачи')

    def __str__(self):
        return self.ab_status
