from django.test import TestCase
from billing_payment.utils.phone import normalize_phone_number


class PhoneNormalizationTest(TestCase):
    def test_kenyan_local_format(self):
        self.assertEqual(normalize_phone_number('0712345678'), '254712345678')

    def test_kenyan_local_01_format(self):
        self.assertEqual(normalize_phone_number('0112345678'), '254112345678')

    def test_international_plus_format(self):
        self.assertEqual(normalize_phone_number('+254712345678'), '254712345678')

    def test_already_normalized(self):
        self.assertEqual(normalize_phone_number('254712345678'), '254712345678')

    def test_whitespace_stripped(self):
        self.assertEqual(normalize_phone_number('  0712345678  '), '254712345678')

    def test_invalid_non_numeric_raises(self):
        with self.assertRaises(ValueError):
            normalize_phone_number('07ABCD5678')

    def test_too_short_raises(self):
        with self.assertRaises(ValueError):
            normalize_phone_number('07123')
