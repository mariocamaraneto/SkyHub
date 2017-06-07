from flask import Flask, request, render_template, jsonify, send_from_directory, url_for
from db import db
from models import Photo
import photomisc
import os

app = Flask("SkyHub")
app.config.from_pyfile('config.cfg')
db.init_app(app)


@app.route("/")
def index():
    return "<h1>SkyHub</h1>EndPoints:<br>/photo/<br>/photo/&#60;name&#62;<br><br><br>Info: https://github.com/mariocamaraneto/SkyHub"

@app.route("/photo/")
def photo():
    photos_db = Photo.objects.fields(url=1)
    photos = []
    for photo_db in photos_db:
        photo_dict = {}
        photo_dict['url'] = photo_db['url']
        photo_dict['small'] = request.url+photomisc.generate_name_photo(photo_db['url'], "small")
        photo_dict['medium'] = request.url+photomisc.generate_name_photo(photo_db['url'], "medium")
        photo_dict['large'] = request.url+photomisc.generate_name_photo(photo_db['url'], "large")
        photos.append(photo_dict)
    return jsonify(photos=photos)
    
@app.route("/photo/<name>")
def get_photo(name):
    dir_photos = os.path.join(os.getcwd(), "photos")
    return send_from_directory(dir_photos, name)

    
if __name__ == '__main__':
    #load photos from server
    photomisc.generate_resized_photos()
    app.run(debug=False, use_reloader=True)