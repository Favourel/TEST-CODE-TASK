from django.urls import path
from . import views as service_view

urlpatterns = [
    # path("", service_view.home_view, name="home"),
    path("", service_view.add_rental_view, name="add_rental"),
    path("recent/", service_view.recent_reservation_view, name="recent_reservation"),

]