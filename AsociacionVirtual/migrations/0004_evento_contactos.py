# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AsociacionVirtual', '0003_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='contactos',
            field=models.ManyToManyField(to='AsociacionVirtual.Contacto'),
        ),
    ]