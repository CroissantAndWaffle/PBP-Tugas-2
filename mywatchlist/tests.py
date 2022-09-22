from django.test import TestCase
from django.test import Client
# From https://docs.djangoproject.com/en/4.1/topics/testing/tools/#the-test-client


class SimpleTest(TestCase):

    def test_html(self):
        response = Client().get('/mywatchlist/html/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_xml(self):
        response = Client().get('/mywatchlist/xml/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
    
    def test_json(self):
        response = Client().get('/mywatchlist/json/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

