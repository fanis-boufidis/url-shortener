from django.test import TestCase
from .models import Link
# Create your tests here.
class LinkTest(TestCase):
    def test_create_link_valid(self):
        response = self.client.post( # self.client: "fake" browser 
            "/api/links/", 
            data={"url": "https://example.com"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201) # status response = 201 or test fails
        
    def test_create_link_invalid(self):
        response = self.client.post(
            "/api/links/",
            data={"url": "abc"},
            content_type="application/json", #sends JSON
        )
        self.assertEqual(response.status_code, 400)
    def test_redirect_counts_clicks(self):
        link = Link.objects.create(original_url="https://example.com")
        response = self.client.get(f"/{link.code}")
        self.assertEqual(response.status_code, 302)
        link.refresh_from_db()
        self.assertEqual(link.clicks, 1)