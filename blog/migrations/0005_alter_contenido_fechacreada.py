# Generated by Django 5.0.2 on 2024-03-03 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_contenido_fechacreada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='fechaCreada',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
