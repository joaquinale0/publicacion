# Generated by Django 5.0.2 on 2024-03-03 13:03

import django.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contenido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30, null=True)),
                ('tituloImg', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes')),
                ('descripcion', models.CharField(max_length=1000, null=True, verbose_name=django.db.models.fields.TextField)),
            ],
        ),
    ]