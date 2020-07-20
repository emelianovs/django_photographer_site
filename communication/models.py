from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class MainInfo(models.Model):
    name = models.CharField(max_length=30, verbose_name=_("Your name"))
    email = models.EmailField(default='your@email.com', verbose_name=_("Your email"))
    message_body = models.TextField(verbose_name=_("Text"))
    date_posted = models.DateTimeField('%Y-%m-%d %H:%M', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Review(MainInfo):
    pass

    class Meta:
        db_table = 'portfolio_review'


class Contact(MainInfo):
    phone = models.CharField(default='+1-234-5678', max_length=30, verbose_name=_("Phone"))

    class Meta:
        db_table = 'portfolio_contact'
