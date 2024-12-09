# Generated by Django 5.1.3 on 2024-12-04 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bancas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('direcccion', models.CharField(max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('presupuesto', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('premios', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('ganancias', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('activa', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
