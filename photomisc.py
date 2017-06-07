from PIL import Image
from io import BytesIO
from models import Photo
import os
import requests
import PIL


url_origin_photos = "http://54.152.221.29/images.json"
size_dim = { 'small': (320, 240), 'medium': (384, 288), 'large': (640, 480)}


#create directory to save photos if not exist yet
dir_photos = os.path.join(os.getcwd(), "photos")
if not os.path.exists(dir_photos):
    os.makedirs(dir_photos)

    
def get_urls_photos_origin():
    """Send request in api of server with photos and take the urls of the images
       Return:      urls: list of strings
    """
    urls_json = requests.get(url_origin_photos).json()['images']
    return [ url['url'] for url in urls_json ]
    

def get_photo_by_url(url):
    """Get photo stored in the url
       Params:      url:String
       Return:      photo: PIL.Image 
    """
    response = requests.get(url)
    return PIL.Image.open(BytesIO(response.content))
    
    
def resize_photo(photo, size):
    return photo.resize(size_dim[size], PIL.Image.LANCZOS)
    

def create_resized_photo(photo, url, size):
    """Resize the photo and save it. Return your path name
       Params:      photo: PIL.Image
                    url: String
                    size: String
       Return:      path: String
    """
    photo_resized = resize_photo(photo, size)
    
    name_photo = generate_name_photo(url, size)
    dir = os.path.join(dir_photos, name_photo)
    photo_resized.save(dir)
    return dir
    
    
def generate_name_photo(url, size):
    name_photo = url.split('/')[-1]
    return size+'-'+name_photo
    
    
def generate_resized_photos():
    """ Get all photos from server, rezise them and save your paths in database"""
    urls = get_urls_photos_origin()
    Photo.objects.delete()
    for url in urls:
        photo_db = Photo(url=url)
        photo = get_photo_by_url(url)
        photo_db.path_small = create_resized_photo(photo, url, 'small')
        photo_db.path_medium = create_resized_photo(photo, url, 'medium')
        photo_db.path_large = create_resized_photo(photo, url, 'large')
        photo_db.save()
        
        
        