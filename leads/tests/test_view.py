from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class LandingPageTest(TestCase):
    def test_get(self):
        response = self.client.get(reverse("lead-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "leads_list.html")
