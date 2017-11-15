from django.db import models
from django.utils.translation import ugettext_lazy as _

# якщо особа юридична,
# то в поля first_name, last_name, sur_name
# вводимо імя, прізвище і по батькові контактної особи
class Client(models.Model):
    TYPE_CLIENT = (
        ('Ф', 'Фізична особа'),
        ('Ю', 'Юридична особа')
    )
    author = models.ForeignKey('auth.User')
    type_client = models.CharField(max_length=1,
                                   default='Ф',
                                   choices=TYPE_CLIENT,
                                   verbose_name=_("Тип клієнта"))
    first_name = models.CharField(max_length=50,
                                  blank=True,
                                  verbose_name=_("Ім'я"))
    last_name = models.CharField(max_length=50,
                                 blank=True,
                                 verbose_name=_("Прізвище"))
    sur_name = models.CharField(max_length=50,
                                blank=True,
                                verbose_name=_("По батькові"))
    full_name = models.CharField(max_length=200,
                                 blank=True,
                                 verbose_name=_("Повна назва")) # назва для юридичної особи. для фізичної = first_name + name + sur_name
    phone_mobile = models.CharField(max_length=15,
                                    verbose_name=_("Телефон"))
    email = models.EmailField(verbose_name=_("Електронна адреса"))
    url_site = models.URLField(verbose_name=_("Сайт"), blank=True)
    address = models.CharField(max_length=300, verbose_name=_("Адреса"))

    def publish(self):
        if self.full_name.isspace():
            self.full_name = '%s  %s %s' % (self.last_name, self.first_name, self.sur_name)
        self.save()

    def __str__(self):
        return self.full_name

#! контактна особа клієнта
class ContactPeople(models.Model):
    author = models.ForeignKey('auth.User')
    client = models.ForeignKey('Client')
    first_name = models.CharField(max_length=50, verbose_name=_("Ім'я"))
    last_name = models.CharField(max_length=50, verbose_name=_("Прізвище"))
    sur_name = models.CharField(max_length=50, verbose_name=_("По батькові"))
    mobile = models.CharField(max_length=15, verbose_name=_("Телефон"))
    email = models.EmailField(verbose_name=_("Електронна адреса"))



