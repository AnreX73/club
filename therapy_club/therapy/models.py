from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class User(AbstractUser):
    phone_number = models.CharField(max_length=30, blank=True, verbose_name='телефон для связи')

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_id': self.pk})

    def __str__(self):
        return self.username


class Graphics(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='изображение')
    title = models.CharField(max_length=55, verbose_name='описание изображения')
    note = RichTextField(blank=True, verbose_name='примечание')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'графический объект'
        verbose_name_plural = 'Графика и т.п.'
        ordering = ['id']


class ServiceCategory(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Категория услуг')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True,
                              verbose_name='основное изображение для категории')
    content = RichTextField(blank=True, default='', verbose_name='Краткое  описание')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_service', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'
        ordering = ['id']


class Services(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, max_length=255, db_index=True, verbose_name='URL')
    cat = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, verbose_name='Категория услуг',
                            related_name='serv_category')
    duration = models.CharField(max_length=255, blank=True, default=' - ', verbose_name='продолжительность')
    price = models.PositiveIntegerField(null=True, default=0, verbose_name='Цена')
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True,
                              verbose_name='основное изображение для услуги')
    video = models.FileField(upload_to='images/%Y/%m/%d', blank=True, null=True, verbose_name='видео (если есть)')
    content = RichTextField(blank=True, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def nice_price(self):
        price = self.price
        nice_price = '{0:,}'.format(price).replace(',', '`')
        return nice_price

    def get_absolute_url(self):
        return reverse('show_service', kwargs={'service_slug': self.slug})

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
        ordering = ['time_create', 'title']


class Coaches(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя')
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True, verbose_name='портрет')
    slug = models.SlugField(unique=True, max_length=255, db_index=True, verbose_name='URL')
    coach_services = models.ManyToManyField(ServiceCategory, verbose_name='Чему тренирует')
    working_time = RichTextField(blank=True, verbose_name='График работы')
    content = RichTextField(blank=True, verbose_name='Кто по жизни')
    is_published = models.BooleanField(default=True, verbose_name='Работает или нет')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_coach', kwargs={'coach_slug': self.slug})

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренера'
        ordering = ['id', 'title']


# Статьи
class Post(models.Model):
    title = models.CharField(max_length=55, verbose_name='Заголовок статьи')
    slug = models.SlugField(unique=True, max_length=255, db_index=True, verbose_name='URL')
    content = RichTextField(blank=True, verbose_name='текст статьи')
    post_cat = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='О какой услуге статья',
                                 related_name='service_post')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_coach', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
        ordering = ['id']


class ServicesGallery(models.Model):
    gallery_service_link = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name=' к какой услуге фото')
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True, verbose_name='Фото')
    note = models.CharField(blank=True, max_length=100, verbose_name='примечание')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.note

    class Meta:
        verbose_name = 'фотографию к услуге'
        verbose_name_plural = 'фото к услуге'
        ordering = ['gallery_service_link']


class PostGallery(models.Model):
    gallery_post_link = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=' к какой статье фото')
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True, verbose_name='Фото')
    note = models.CharField(blank=True, max_length=100, verbose_name='примечание')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.note

    class Meta:
        verbose_name = 'фотографию к статье'
        verbose_name_plural = 'фото к статье'
        ordering = ['gallery_post_link']


class Gallery(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True, verbose_name='Фото')
    video = models.FileField(upload_to='images/%Y/%m/%d', blank=True, null=True, verbose_name='видео (если есть)')
    gallery_link = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, default=6, verbose_name='к какой '
                                                                                                        'категории '
                                                                                                        'фото',
                                     related_name='cat_photo')
    note = models.CharField(blank=True, max_length=100, verbose_name='примечание')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.note

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фото'
        ordering = ['id']


class Contacts(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='заголовок')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to="images", blank=True, null=True, verbose_name='Изображение')
    annotations1 = RichTextField(blank=True, verbose_name='информация')
    annotations2 = models.TextField(blank=True, verbose_name='ссылка,если есть')
    is_header_published = models.BooleanField(default=False, verbose_name='Публикация в шапке сайта')
    is_published = models.BooleanField(default=False, verbose_name='Публикация в контактах, карты-не отмечать!!!')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_service', kwargs={'service_slug': self.slug})

    class Meta:
        verbose_name = 'контакты '
        verbose_name_plural = 'Контакты'
        ordering = ['id']


class Commercial(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Кричащий заголовок')
    sub_title = models.CharField(max_length=255, blank=True, verbose_name='Подзаголовок, если нужен')
    about = models.CharField(max_length=100, blank=True, verbose_name='Слоган для ссылки на кнопке')
    slug = models.SlugField(unique=True, max_length=100, db_index=True, verbose_name='URL')
    icon = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True,
                             verbose_name='рекламная иконка ')
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True,
                              verbose_name='изображение к рекламной статье, если есть')
    content = RichTextField(blank=True, verbose_name='текст рекламы')
    is_published = models.BooleanField(default=False, verbose_name='Публикация')
    end_action = models.DateField(default=date.today, verbose_name='конец акции')

    class Meta:
        verbose_name = 'Акции и реклама'
        verbose_name_plural = 'Акции'
        ordering = ['id']


class Abonements(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Заголовок')
    sub_title = models.CharField(max_length=255, db_index=True, verbose_name='подзаголовок')
    service_link = models.ForeignKey(Services, on_delete=models.CASCADE,
                                     verbose_name='к какой  услуге относится')
    abonement_duration = models.CharField(max_length=255, blank=True, default=' - ', verbose_name='кол-во занятий или '
                                                                                                  'сеансов')
    abonement_price = models.PositiveIntegerField(null=True, default=0, verbose_name='Цена абонемента')
    validity = models.CharField(max_length=100, verbose_name='срок действия')
    is_published = models.BooleanField(default=False, verbose_name='Публикация')

    def nice_price(self):
        abonement_price = self.abonement_price
        nice_price = '{0:,}'.format(abonement_price).replace(',', '`')
        return nice_price

    class Meta:
        verbose_name = 'Абонемет'
        verbose_name_plural = 'Абонементы'
        ordering = ['id']
