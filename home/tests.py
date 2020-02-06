from django.test import TestCase


class HomeViewTest(TestCase):

    def test_home_sucesso(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)