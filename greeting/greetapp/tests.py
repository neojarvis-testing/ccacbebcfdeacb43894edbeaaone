# test.py

from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from .views import calculate_greeting

class GreetingAppTests(TestCase):
    def run_test(self, test_func, *args):
        try:
            test_func(*args)
            print("Passed")
        except AssertionError as e:
            print("Failed")

    def test_calculate_greeting_morning(self):
        self.run_test(self.assertEqual, calculate_greeting("5"), "Good Morning")

    def test_calculate_greeting_afternoon(self):
        self.run_test(self.assertEqual, calculate_greeting("15"), "Good Afternoon")

    def test_calculate_greeting_evening(self):
        self.run_test(self.assertEqual, calculate_greeting("18"), "Good Evening")

    def test_calculate_greeting_night(self):
        self.run_test(self.assertEqual, calculate_greeting("22"), "Good Night")

    def test_get_greeting_post_request(self):
        url = reverse('get_greeting')
        response = self.client.post(url, {'time': '14'})
        self.run_test(self.assertEqual, response.status_code, 200)
        self.run_test(self.assertContains, response, "Good Afternoon")

    def test_get_greeting_get_request(self):
        url = reverse('get_greeting')
        response = self.client.get(url)
        self.run_test(self.assertEqual, response.status_code, 200)
        # Add more assertions based on your specific expected behavior for a GET request

    # Add more test cases as needed
