# Generated by Django 5.0.6 on 2024-06-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bilety', '0014_remove_seat_ticket_booking_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='movie_title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
