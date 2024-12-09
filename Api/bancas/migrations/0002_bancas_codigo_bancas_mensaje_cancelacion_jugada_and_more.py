# Generated by Django 5.1.3 on 2024-12-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bancas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bancas',
            name='codigo',
            field=models.CharField(default=1, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bancas',
            name='mensaje_cancelacion_jugada',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bancas',
            name='mensaje_creacion_jugada',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bancas',
            name='mensaje_jugada_premiada',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bancas',
            name='nombre_ticket',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bancas',
            name='tipo_de_bancas',
            field=models.CharField(choices=[('clasica', 'Clasica'), ('moderna', 'Moderna')], default='clasica', max_length=20),
        ),
        migrations.AddField(
            model_name='bancas',
            name='usar_presupuesto_propio',
            field=models.BooleanField(default=False),
        ),
    ]