# Generated by Django 2.2.7 on 2019-11-13 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('corre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]
