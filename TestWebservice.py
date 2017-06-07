from flask import json
import os
import app
import unittest
import tempfile
import photomisc

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        photomisc.generate_resized_photos()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])
    
    def test_index(self):
        response = self.app.get('/')
        assert b'SkyHub' in response.data
        
    def test_photo(self):
        response = self.app.get('/photo/')
        response_json = json.loads(response.data)
        assert 'photos' in response_json
        self.assertEqual(len(response_json['photos']), 10)
        

if __name__ == '__main__':
    unittest.main()