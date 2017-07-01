from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from blog.views import post_list

# Create your tests here.

# Test Smoke Tests
class SmokeTest(TestCase):

    def test_bad_math(self):
        self.assertEqual(1+1, 2)

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<title>Girls blog</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

    def test_uses_list_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')
