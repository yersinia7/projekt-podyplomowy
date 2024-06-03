from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Movie(models.Model):
    GENRE_CHOICES = [("familijny", "familijny"), ("horror", "horror"), ("thriller","thriller"), ("komedia","komedia"), ("romans","romans")]
    AGE_CHOICES = [("b/o","b/o"), ("od 13 lat", "od 13 lat"), ("od 18 lat", "od 18 lat")]
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    age_restrictions = models.CharField(max_length=50, choices=AGE_CHOICES)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default="komedia")
    duration = models.PositiveSmallIntegerField()
    production_country = models.CharField(max_length=50)
    trailer = models.CharField(max_length=200)
    slug = models.SlugField(default="", null=True)

    def __str__(self):
        return f"{self.title}"


class Room(models.Model):
    movie_name = models.OneToOneField(Movie, on_delete=models.CASCADE)
    screening_date = models.DateField(null=True)
    screening_time = models.TimeField(null=True)

    def __str__(self):
        return f"{self.movie_name}, {self.screening_date}, {self.screening_time}"


class Seat(models.Model):
    row_number = models.PositiveSmallIntegerField(validators=(MaxValueValidator(2), MinValueValidator(1)))
    seat_number = models.PositiveSmallIntegerField(validators=(MaxValueValidator(5), MinValueValidator(1)))
    screening_room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)

    @property
    def is_booked(self):
        try:
            booked = self.booking
        except Booking.DoesNotExist:
            return False
        else: return True

    def __str__(self):
        return f"Rząd {self.row_number}, miejsce {self.seat_number}, {self.screening_room.screening_date}, {self.screening_room.screening_time}"
class Booking(models.Model):
    TICKET_CHOICES = [("normalny", "normalny"), ("ulgowy", "ulgowy")]
    ticket = models.CharField(max_length=15, choices=TICKET_CHOICES, default="normalny")
    chosen_seat = models.OneToOneField(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.chosen_seat}"


