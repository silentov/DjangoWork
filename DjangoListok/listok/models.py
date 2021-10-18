from django.db import models


class Abonements(models.Model):

    class Meta:
        verbose_name = "Абонементы"

    ident = models.PositiveSmallIntegerField(verbose_name='ID', default=0)
    title = models.CharField(max_length=255, verbose_name='Название', default=0)
    num = models.PositiveSmallIntegerField(verbose_name='Занятий', default=0)
    month = models.PositiveSmallIntegerField(default=0)
    days = models.PositiveSmallIntegerField(default=0)
    price = models.CharField(max_length=255, verbose_name='Цена', default=0)


    def __str__(self):
        return f'{self.ident} | {self.title} | {self.num} | {self.month} мес.{self.days} дн. | {self.price}'



class User(models.Model):

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

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
    birthday_date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Год рождения')
    adres = models.CharField(max_length=255, verbose_name='Адрес')
    code = models.CharField(max_length=255, verbose_name='Штрих-код')
    family_field = models.CharField(max_length=255, verbose_name='Карточка родителя', blank=True)
    FIO_family = models.CharField(max_length=255, verbose_name='ФИО роидтеля', blank=True)
    number_family = models.CharField(max_length=255, verbose_name='Телефон родителя')
    email = models.CharField(max_length=255, verbose_name='Email', blank=True)
    status = models.ForeignKey()
    blacklist = models.CharField(max_length=1, verbose_name='Черный список', choices=blacklist_choise)
    source = models.ForeignKey()
    class_format = models.ForeignKey()
    personal_disc = models.PositiveSmallIntegerField(blank=True)
    Vk_id = models.CharField(max_length=255, verbose_name='Вконтакте ID', blank=True)
    Fb_id = models.CharField(max_length=255, verbose_name='Facebook ID', blank=True)
    Ig_id = models.CharField(max_length=255, verbose_name='Instagramm ID', blank=True)
    contraindications = models.ForeignKey()
    sms = models.CharField(max_length=1, verbose_name='Отправка сообщений', choices=sms_choise)
    email_choise = models.CharField(max_length=1, verbose_name='Отправка Email', choices=sms_choise)
    notes_unvi = models.TextField(max_length=1000, verbose_name='Заметки', blank=True)
    notes_visible = models.TextField(max_length=500, verbose_name='Заметки (видимые)', blank=True)
    passport = models.PositiveIntegerField(verbose_name='Номер и серия паспорта')
    passport_date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Дата выдачи паспорта')
    passport_org = models.CharField(max_length=255, verbose_name='Кем выдан')
    org_code = models.CharField(max_length=20, verbose_name='Дата выдачи')