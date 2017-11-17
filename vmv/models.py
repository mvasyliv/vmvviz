from django.db import models
from django.utils.translation import ugettext_lazy as _

class GroupTehnology(models.Model):
    author = models.ForeignKey('auth.User', verbose_name=_("Автор"))
    name = models.CharField(max_length=100, verbose_name=_("Назва"))

    def __str__(self):
        return self.name

class Tehnology(models.Model):
    author = models.ForeignKey('auth.User', verbose_name=_("Автор"))
    group_tehnology = models.ForeignKey('GroupTehnology', verbose_name=_("Група"))
    name = models.CharField(max_length=50, verbose_name=_("Назва технології"))

    def __str__(self):
        return self.name

class Author(models.Model):
    author = models.ForeignKey('auth.User', verbose_name=_("Автор"))
    first_name = models.CharField(max_length=50, verbose_name=_("Ім'я"))
    last_name = models.CharField(max_length=50, verbose_name=_("Прізвище"))
    sur_name = models.CharField(max_length=50, verbose_name=_("По батькові"))
    email = models.EmailField(verbose_name=_("Електронна адреса"))
    mobile = models.CharField(max_length=15, verbose_name=_("Контактний телефон"))

    def __str__(self):
        return "Автор {} {} {}".format(self.last_name, self.first_name, self.sur_name)

class Article(models.Model):
    author = models.ForeignKey('auth.User', verbose_name=_("Автор"))
    authors_article = models.ManyToManyField('Author', verbose_name=_("Автор(и) статті"))
    title = models.CharField(max_length=100, verbose_name=_("Назва стітті"))
    text_article = models.TextField(verbose_name=_("Стаття"))
    published_date = models.DateTimeField(blank=True, null=True, verbose_name=_("Дата публікації"))

    def __str__(self):
        return _("Назва статті: {}. Дата публікації: {}").format(self.title, self.published_date)

