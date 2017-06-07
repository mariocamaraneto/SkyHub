import unittest
import os
import photomisc

from io import BytesIO
import requests
import PIL


class TestPhotoMisc(unittest.TestCase):

    def setUp(self):
        self.URL_IMAGE_TEST = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png'
        response = requests.get(self.URL_IMAGE_TEST)
        self.image_test = PIL.Image.open(BytesIO(response.content))

        
    def test_get_photo_by_url(self):
        response = photomisc.get_photo_by_url(self.URL_IMAGE_TEST)
        self.assertEqual(response, self.image_test)

        
    def test_resized_photo(self):
        responseS = photomisc.resize_photo(self.image_test, 'small')
        self.assertEqual(responseS.size, photomisc.size_dim['small'])
        
        responseM = photomisc.resize_photo(self.image_test, 'medium')
        self.assertEqual(responseM.size, photomisc.size_dim['medium'])
        
        responseL = photomisc.resize_photo(self.image_test, 'large')
        self.assertEqual(responseL.size, photomisc.size_dim['large'])

    
    def test_generate_name_photo(self):
        response = photomisc.generate_name_photo(self.URL_IMAGE_TEST, 'small')
        self.assertEqual(response, 'small-googlelogo_color_150x54dp.png')
        
        
        
if __name__ == '__main__':
    unittest.main()