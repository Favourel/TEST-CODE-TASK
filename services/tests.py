from django.shortcuts import reverse
from django.test import TestCase
from .models import Reservation, Rental

# Create your tests here.


class RentalTestCase(TestCase):

    def setUp(self):
        create_rental = Rental(name='Rental Services 1')
        create_rental.save()
        self.reservation = Reservation.objects.create(
            rental_name=create_rental,
            rental_id="156655.7777",
            checkIn='2022-05-31',
            checkOut='2022-06-20',)

    def test_name_content(self):
        self.rental = Rental.objects.get(id=1)
        expected_object_count = f'{self.rental.name}'
        self.assertEqual(expected_object_count, 'Rental Services 1')

    def test_reservation_listing(self):
        self.assertEqual(f'{self.reservation.rental_name}', 'Rental Services 1')
        self.assertEqual(f'{self.reservation.rental_id}', '156655.7777')
        self.assertEqual(f'{self.reservation.checkIn}', '2022-05-31')
        self.assertEqual(f'{self.reservation.checkOut}', '2022-06-20')

    def test_reservation_view(self):
        create_rental = Rental(name='Rental Services 2')
        create_rental.save()
        self.reservation = Reservation.objects.create(
            rental_name=create_rental,
            rental_id="1564535.7777",
            checkIn="2022-05-31",
            checkOut="2022-05-13", )
        response = self.client.get(reverse('recent_reservation'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rental Services 2')
        self.assertContains(response, '1564535.7777')
        self.assertContains(response, 'May 31, 2022')
        self.assertTemplateUsed(response, 'services/recent_reservation.html')

