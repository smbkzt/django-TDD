from django.test import TestCase


class SmokeTest(TestCase):
    def test_bad_math(self):
        self.assertEquals(4, 4)
