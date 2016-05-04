# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 12:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alquila',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_alquiler', models.DateTimeField(default=datetime.datetime.now)),
                ('fecha_devolucion', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Asociacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('nif', models.CharField(max_length=11)),
                ('direccion', models.CharField(max_length=255)),
                ('mail', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=30)),
                ('fecha_alta', models.DateTimeField(default=datetime.datetime.now)),
                ('telefono', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateTimeField(default=datetime.datetime.now)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_alta', models.DateTimeField(blank=True)),
                ('fecha_baja', models.DateTimeField(blank=True)),
                ('coste', models.DecimalField(decimal_places=2, max_digits=10)),
                ('beneficio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contactos', models.ManyToManyField(to='AsociacionVirtual.Contacto')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('J', 'Juego'), ('U', 'Utensilio'), ('C', 'Comida')], max_length=1)),
                ('nombre', models.CharField(max_length=255)),
                ('foto', models.ImageField(upload_to='media/materiales/')),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=30)),
                ('fecha_alta', models.DateTimeField(default=datetime.datetime.now)),
                ('fecha_baja', models.DateTimeField(blank=True, null=True)),
                ('mail', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=12)),
                ('foto', models.ImageField(upload_to='media/socios/')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('N', 'Nuevo'), ('R', 'Roto'), ('S', 'Semi nuevo')], max_length=1)),
                ('fecha_alta', models.DateTimeField(default=datetime.datetime.now)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foto', models.ImageField(upload_to='media/stock/')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsociacionVirtual.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='AsociacionVirtual.Socio')),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('A', 'Alta'), ('B', 'Baja'), ('AY', 'Ayudas')], max_length=2)),
                ('fecha_alta', models.DateTimeField(default=datetime.datetime.now)),
                ('link', models.FilePathField()),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='participantes',
            field=models.ManyToManyField(to='AsociacionVirtual.Socio'),
        ),
        migrations.AddField(
            model_name='cuota',
            name='socio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsociacionVirtual.Socio'),
        ),
        migrations.AddField(
            model_name='alquila',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsociacionVirtual.Stock'),
        ),
        migrations.AddField(
            model_name='alquila',
            name='socio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AsociacionVirtual.Socio'),
        ),
        migrations.AlterUniqueTogether(
            name='alquila',
            unique_together=set([('socio', 'material', 'fecha_alquiler')]),
        ),
    ]
