
from django.test import TestCase
from django.urls import reverse


class HelloAPITests(TestCase):

    def test_hello_api_returns_correct_data(self):
        response = self.client.get(reverse('hello_api'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()['message'],
            'Welcome to my CSC325 API'
        )
        self.assertEqual(
            response.json()['course'],
            'CSC325'
        )

    def test_hello_api_rejects_post_requests(self):
        response = self.client.post(reverse('hello_api'))

        self.assertEqual(response.status_code, 405)
        self.assertIn('GET', response.headers['Allow'])
