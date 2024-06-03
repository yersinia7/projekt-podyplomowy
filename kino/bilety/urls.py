from django.urls import path
from . views import index, moviePage, reservationPage, thankYouPage, allMoviesView, price_page

urlpatterns = [
    path("", index, name="index"),
    path("repertuar", allMoviesView.as_view(), name="all-movies"),
    path("cennik", price_page, name="price-page"),
    path("rezerwacja", reservationPage, name="reservation"),
    path("repertuar/<slug:slug>", moviePage, name="movie-name"),
    path("thank-you", thankYouPage, name="thanks"),
]
