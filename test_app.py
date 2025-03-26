import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Inflix', response.data)

    def test_play_trailer(self):
        response = self.app.get('/play-trailer')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'https://www.youtube.com/watch?v=b9EkMc79ZSU', response.data)

    def test_show_info(self):
        response = self.app.get('/show-info')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'https://en.wikipedia.org/wiki/Stranger_Things', response.data)

    def test_get_url_valid(self):
        response = self.app.get('/get-url/T1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'https://example.com/trending1', response.data)

    def test_get_url_invalid(self):
        response = self.app.get('/get-url/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'URL not found', response.data)

    def test_get_title_valid(self):
        response = self.app.get('/get-title/T1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Pushpa 2', response.data)

    def test_get_title_invalid(self):
        response = self.app.get('/get-title/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Title not found', response.data)

if __name__ == '__main__':
    unittest.main()
