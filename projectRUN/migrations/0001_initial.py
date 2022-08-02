# Generated by Django 4.0.6 on 2022-08-02 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id_permiso', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_permiso', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id_roles', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=100)),
            ],
        ),
    ]