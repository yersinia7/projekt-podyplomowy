from django.db import transaction
from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from . models import Movie, Room, Seat, Booking

# Create your views here.

def index(request):
    return render(request, "bilety/index.html")

def price_page(request):
    return render(request, "bilety/price.html")

class allMoviesView(ListView):
    template_name = "bilety/all-movies.html"
    model = Movie
    context_object_name = "movies"

def moviePage(request, slug):
    movie = Movie.objects.get(slug=slug)
    movie_id = movie.id     # id obiektu Movie, żeby go wykorzystać do znalezienia obiektu Room
    room = Room.objects.get(movie_name=movie_id)

    return render(request, "bilety/movie.html", {
        "movie": movie,
        "room": room
    })

def reservationPage(request):

    if request.method == "POST":
        room_id = request.POST["room-id"]
        room = Room.objects.get(pk=room_id)
        all_seats = Seat.objects.filter(screening_room=room, booking=None)  # tylko obiekty z tej sali i tylko te, które nie mają rezerwacji

        return render(request, "bilety/reservation.html", {
        "room": room,
        "seats": all_seats
        })

    return HttpResponseRedirect("/repertuar")

@transaction.atomic
def thankYouPage(request):
    if request.method == "POST":
        ticket = request.POST["ticket"]    # normalny/ulgowy
        seat_id = request.POST["selected_seat_id"]
        seat = Seat.objects.get(id=seat_id)

        if not seat.is_booked:
            booked = Booking(chosen_seat=seat, ticket=ticket)
            booked.save()

    return render(request, "bilety/thank-you.html")
