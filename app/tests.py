from django.test import TestCase
from .models import YourModel

class YourModelTests(TestCase):

    def setUp(self):
        # Set up any initial data for the tests here
        YourModel.objects.create(field_name='value')

    def test_model_str(self):
        # Test the string representation of the model
        instance = YourModel.objects.get(field_name='value')
        self.assertEqual(str(instance), 'Expected String Representation')

    def test_model_field(self):
        # Test a specific field of the model
        instance = YourModel.objects.get(field_name='value')
        self.assertEqual(instance.field_name, 'value')