# Generated by Django 4.2.11 on 2024-05-28 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilety', '0011_remove_room_seat_seat_screening_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
