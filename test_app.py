"""
This module contains unit tests for the Netflix-inspired frontend project.
It tests the Flask app's routes and their responses.
"""

import unittest
from app import app

class AppTestCase(unittest.TestCase):
    """Test case for the Flask app."""

    def setUp(self):
        """Set up the test client for the Flask app."""
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        """Test the homepage route."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Inflix', response.data)

    def test_play_trailer(self):
        """Test the play trailer route."""
        response = self.app.get('/play-trailer')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'https://www.youtube.com/watch?v=b9EkMc79ZSU', response.data)

    def test_show_info(self):
        """Test the show info route."""
        response = self.app.get('/show-info')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'https://en.wikipedia.org/wiki/Stranger_Things', response.data)

    def test_get_url_valid(self):
        """Test the get-url route with a valid movie ID."""
        response = self.app.get('/get-url/T1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'https://example.com/trending1', response.data)

    def test_get_url_invalid(self):
        """Test the get-url route with an invalid movie ID."""
        response = self.app.get('/get-url/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'URL not found', response.data)

    def test_get_title_valid(self):
        """Test the get-title route with a valid movie ID."""
        response = self.app.get('/get-title/T1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Pushpa 2', response.data)

    def test_get_title_invalid(self):
        """Test the get-title route with an invalid movie ID."""
        response = self.app.get('/get-title/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Title not found', response.data)

if __name__ == '__main__':
    unittest.main()
