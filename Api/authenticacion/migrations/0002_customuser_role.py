# Generated by Django 5.1.3 on 2024-12-09 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Administrador'), ('GERENTE', 'Gerente'), ('EMPLEADO', 'Empleado')], default='EMPLEADO', max_length=10),
        ),
    ]
