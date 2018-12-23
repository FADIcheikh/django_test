# Create your models here.
from __future__ import unicode_literals

from audioop import reverse

from django.db import models


class Utilisateur(models.Model):
    nom = models.CharField(max_length=200)
    pre = models.CharField(max_length=200)
    email = models.EmailField()
    login = models.CharField(max_length=20)
    psw = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title

    def get_post_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})