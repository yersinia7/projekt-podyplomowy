# Generated by Django 4.2.11 on 2024-05-28 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bilety', '0012_seat_is_booked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='is_booked',
        ),
    ]
