# Generated by Django 4.0.6 on 2022-08-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/', verbose_name='imagen')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
            ],
        ),
    ]