# Generated by Django 5.1.3 on 2024-12-04 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bancas', '0003_bancas_daily_revenue_bancas_monthly_revenue_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bancas',
            name='daily_revenue',
        ),
        migrations.RemoveField(
            model_name='bancas',
            name='monthly_revenue',
        ),
    ]