from django.test import TestCase
from django.urls import reverse

from accounts.models import HiveUser
from apiary_app.models import ApiaryModel
from product_app.models import ProductModel


class ShopPageViewTest(TestCase):

    VALID_APIARY_DATA = {
        'apiary_name': 'Testgarden',
        'location': 'Testtown',
        'hives_count': 5,
        'apiary_photo': None,
        'description': None,
        'owner': None
    }

    VALID_PRODUCT_DATA = {

        'product_name': None,
        'product_type': 'Honey',
        'product_image': None,
        'description': None,
        'price': 22,
        'grams': 22,
        'quantity': 22,
        'apiary': None,
        'owner': None
    }

    VALID_USER_CREATION_DATA = {
        'username': 'testuser',
        'email': 'test@mail.com',
        'password': 'testpass123'
    }

    def setUp(self):

        user = HiveUser.objects.create_user(**self.VALID_USER_CREATION_DATA)

        full_apiary_data = {**self.VALID_APIARY_DATA, 'owner': user}
        apiary = ApiaryModel.objects.create(**full_apiary_data)

        product_data = {**self.VALID_PRODUCT_DATA, 'apiary': apiary, 'owner': user, 'product_name': ''}

        for x in range(3):
            product_data['product_name'] = f'Product{x}'
            ProductModel.objects.create(**product_data)

    def test_shop_view(self):

        url = reverse('shop')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/shop.html')
        self.assertContains(response, 'Product0')
        self.assertContains(response, 'Product1')
        self.assertContains(response, 'Product2')

    def test_shop_search(self):

        url = reverse('shop')
        response = self.client.get(url, {'Search': 'Product1'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/shop.html')
        self.assertContains(response, 'Product1')
        self.assertNotContains(response, 'Product0')
        self.assertNotContains(response, 'Product2')

    def test_shop_search_invalid_product(self):
        url = reverse('shop')
        response = self.client.get(url, {'Search': 'Product3'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Not any products yet . . .')
















