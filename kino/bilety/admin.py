from django.contrib import admin
from . models import Movie, Room, Seat, Booking

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ("movie_name", "screening_date", "screening_time",)
    list_filter = ("movie_name",)

class SeatAdmin(admin.ModelAdmin):
    list_display = ("screening_room", "row_number", "seat_number",)
    list_filter = ("screening_room",)

class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "chosen_seat", "ticket",)


admin.site.register(Movie)
admin.site.register(Room, RoomAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Booking, BookingAdmin)

