from django.db import models

# Реєстрація замовлення на розробку проекта
class OrderProject(models.Model):
    author = models.ForeignKey('auth.User')
