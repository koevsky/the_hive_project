from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):

    def test_get_index_page(self):
        url = reverse('index')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'common/index.html')
        self.assertEqual(response.status_code, 200)

